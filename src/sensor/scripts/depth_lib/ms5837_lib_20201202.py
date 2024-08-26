#! /usr/bin/env python
# -*- coding:UTF-8 -*-
'''
# 这个传感器暂时就先这个样子了，后面再考虑类似陀螺仪的滤波算法，还是有可能将数据漂移压低要很好的程度的
# 现有的二阶温度补偿算法，貌似不太好用呀，应为补偿了之后，压力和温度还有一定程度的线性关系
'''

# %%
# Lib
import smbus
from time import sleep

# Models
MODEL_02BA = 0
MODEL_30BA = 1

# Oversampling options
OSR_256 = 0
OSR_512 = 1
OSR_1024 = 2
OSR_2048 = 3
OSR_4096 = 4
OSR_8192 = 5

# kg/m^3 convenience
DENSITY_FRESHWATER = 997  # 21°C
DENSITY_SALTWATER = 1029

# Conversion factors (from native unit, mbar)
UNITS_Pa = 100.0
UNITS_hPa = 1.0
UNITS_kPa = 0.1
UNITS_mbar = 1.0
UNITS_bar = 0.001
UNITS_atm = 0.000986923
UNITS_Torr = 0.750062
UNITS_psi = 0.014503773773022

# Valid units
UNITS_Centigrade = 1
UNITS_Farenheit = 2
UNITS_Kelvin = 3


class MS5837(object):

    # Registers
    _MS5837_ADDR = 0x76
    _MS5837_RESET = 0x1E
    _MS5837_ADC_READ = 0x00
    _MS5837_PROM_READ = 0xA0
    _MS5837_CONVERT_D1_256 = 0x40
    _MS5837_CONVERT_D2_256 = 0x50

    def __init__(self, model=MODEL_30BA, bus=1):
        self._model = model

        try:
            self._bus = smbus.SMBus(bus)
        except:
            print("Bus %d is not available.") % bus
            print("Available busses are listed as /dev/i2c*")
            self._bus = None

        self._fluidDensity = DENSITY_FRESHWATER
        self._pressure = 0
        self._temperature = 0
        self._D1 = 0
        self._D2 = 0

        # 这个是自己加的，这样的话，调用这个函数就不用单独初始化了
        self.init()  # Have to read values from sensor to update pressure and temperature
        self.read()  # Must initialize the sensor before reading it
        sleep(2)

    def init(self):
        if self._bus is None:
            "No bus!"
            return False

        self._bus.write_byte(self._MS5837_ADDR, self._MS5837_RESET)

        # Wait for reset to complete
        sleep(0.01)

        self._C = []

        # Read calibration values and CRC
        for i in range(7):
            c = self._bus.read_word_data(self._MS5837_ADDR, self._MS5837_PROM_READ + 2 * i)
            c = ((c & 0xFF) << 8) | (c >> 8)  # SMBus is little-endian for word transfers, we need to swap MSB and LSB
            self._C.append(c)

        crc = (self._C[0] & 0xF000) >> 12
        if crc != self._crc4(self._C):
            print "PROM read error, CRC failed!"
            return False

        return True

    def read(self, oversampling=OSR_8192):
        if self._bus is None:
            print "No bus!"
            return False

        if oversampling < OSR_256 or oversampling > OSR_8192:
            print "Invalid oversampling option!"
            return False

        # Request D1 conversion (temperature)
        self._bus.write_byte(self._MS5837_ADDR, self._MS5837_CONVERT_D1_256 + 2 * oversampling)

        # Maximum conversion time increases linearly with oversampling
        # max time (seconds) ~= 2.2e-6(x) where x = OSR = (2^8, 2^9, ..., 2^13)
        # We use 2.5e-6 for some overhead
        sleep(2.5e-6 * 2**(8 + oversampling))

        d = self._bus.read_i2c_block_data(self._MS5837_ADDR, self._MS5837_ADC_READ, 3)
        self._D1 = d[0] << 16 | d[1] << 8 | d[2]

        # Request D2 conversion (pressure)
        self._bus.write_byte(self._MS5837_ADDR, self._MS5837_CONVERT_D2_256 + 2 * oversampling)

        # As above
        sleep(2.5e-6 * 2**(8 + oversampling))

        d = self._bus.read_i2c_block_data(self._MS5837_ADDR, self._MS5837_ADC_READ, 3)
        self._D2 = d[0] << 16 | d[1] << 8 | d[2]

        # Calculate compensated pressure and temperature
        # using raw ADC values and internal calibration
        self._calculate()

        return True

    def setFluidDensity(self, denisty):
        self._fluidDensity = denisty

    # Pressure in requested units
    # mbar * conversion
    def pressure(self, conversion=UNITS_mbar):
        return self._pressure * conversion

    # Temperature in requested units
    # default degrees C
    def temperature(self, conversion=UNITS_Centigrade):
        degC = self._temperature / 100.0
        if conversion == UNITS_Farenheit:
            return (9.0 / 5.0) * degC + 32
        elif conversion == UNITS_Kelvin:
            return degC + 273
        return degC

    # Depth relative to MSL pressure in given fluid density
    def depth(self, denisty):
        # return (self.pressure(UNITS_Pa)-101300)/(self._fluidDensity*9.80665)
        # 北京的重力加速度是9.8015，将原来的数值做了9.80665做了修正
        # 室内的气压是1027.443991，将原来的数值101300做了修正
        return (self.pressure(UNITS_Pa) - 102744.3991) / (denisty * 9.8015)

    # Altitude relative to MSL pressure
    def altitude(self):
        return (1 - pow((self.pressure() / 1013.25), .190284)) * 145366.45 * .3048

    # Cribbed from datasheet
    def _calculate(self):
        OFFi = 0
        SENSi = 0
        Ti = 0

        dT = self._D2 - self._C[5] * 256
        if self._model == MODEL_02BA:
            SENS = self._C[1] * 65536 + (self._C[3] * dT) / 128
            OFF = self._C[2] * 131072 + (self._C[4] * dT) / 64
            self._pressure = (self._D1 * SENS / (2097152) - OFF) / (32768)
        else:
            SENS = self._C[1] * 32768 + (self._C[3] * dT) / 256
            OFF = self._C[2] * 65536 + (self._C[4] * dT) / 128
            self._pressure = (self._D1 * SENS / (2097152) - OFF) / (8192)

        self._temperature = 2000 + dT * self._C[6] / 8388608

        # Second order compensation
        if self._model == MODEL_02BA:
            if (self._temperature / 100) < 20:  # Low temp
                Ti = (11 * dT * dT) / (34359738368)
                OFFi = (31 * (self._temperature - 2000) * (self._temperature - 2000)) / 8
                SENSi = (63 * (self._temperature - 2000) * (self._temperature - 2000)) / 32

        else:
            if (self._temperature / 100) < 20:  # Low temp
                Ti = (3 * dT * dT) / (8589934592)
                OFFi = (3 * (self._temperature - 2000) * (self._temperature - 2000)) / 2
                SENSi = (5 * (self._temperature - 2000) * (self._temperature - 2000)) / 8
                if (self._temperature / 100) < -15:  # Very low temp
                    OFFi = OFFi + 7 * (self._temperature + 1500l) * (self._temperature + 1500)
                    SENSi = SENSi + 4 * (self._temperature + 1500l) * (self._temperature + 1500)
            elif (self._temperature / 100) >= 20:  # High temp
                Ti = 2 * (dT * dT) / (137438953472)
                OFFi = (1 * (self._temperature - 2000) * (self._temperature - 2000)) / 16
                SENSi = 0

        OFF2 = OFF - OFFi
        SENS2 = SENS - SENSi

        if self._model == MODEL_02BA:
            self._temperature = (self._temperature - Ti)
            self._pressure = (((self._D1 * SENS2) / 2097152 - OFF2) / 32768) / 100.0
        else:
            self._temperature = (self._temperature - Ti)
            self._pressure = (((self._D1 * SENS2) / 2097152 - OFF2) / 8192) / 10.0

    # Cribbed from datasheet
    def _crc4(self, n_prom):
        n_rem = 0

        n_prom[0] = ((n_prom[0]) & 0x0FFF)
        n_prom.append(0)

        for i in range(16):
            if i % 2 == 1:
                n_rem ^= ((n_prom[i >> 1]) & 0x00FF)
            else:
                n_rem ^= (n_prom[i >> 1] >> 8)

            for n_bit in range(8, 0, -1):
                if n_rem & 0x8000:
                    n_rem = (n_rem << 1) ^ 0x3000
                else:
                    n_rem = (n_rem << 1)

        n_rem = ((n_rem >> 12) & 0x000F)

        self.n_prom = n_prom
        self.n_rem = n_rem

        return n_rem ^ 0x00


class MS5837_30BA(MS5837):
    def __init__(self, bus=1):
        MS5837.__init__(self, MODEL_30BA, bus)


class MS5837_02BA(MS5837):
    def __init__(self, bus=1):
        MS5837.__init__(self, MODEL_02BA, bus)


# %%
''' https://github.com/bluerobotics/ms5837-python
    The python SMBus library must be installed.

    sudo apt-get install python-smbus
    Download this repository by clicking on the download button in this webpage, or using git:

    git clone https://github.com/bluerobotics/ms5837-python
    If you would like to try the example, move to the directory where you downloaded the repository, and run python example.py. To use the library, copy the ms5837.py file to your project/program directory and use this import statement in your program: import ms5837.

    Raspberry Pi
    If you are using a Raspberry Pi, the i2c interface must be enabled. Run sudo raspi-config, and choose to enable the i2c interface in the interfacing options.

    Usage
    import ms5837
    ms5837 provides a generic MS5837 class for use with different models

    MS5837(model=ms5837.MODEL_30BA, bus=1)
    These model-specific classes inherit from MS5837 and don't have any unique members

    MS5837_30BA(bus=1)
    MS5837_02BA(bus=1)
    An MS5837 object can be constructed by specifiying the model and the bus

    sensor = ms5837.MS5837() # Use defaults (MS5837-30BA device on I2C bus 1)
    sensor = ms5837.MS5837(ms5837.MODEL_02BA, 0) # Specify MS5837-02BA device on I2C bus 0
    Or by creating a model-specific object

    sensor = ms5837.MS5837_30BA() # Use default I2C bus (1)
    sensor = ms5837.MS5837_30BA(0) # Specify I2C bus 0
    init()
    Initialize the sensor. This needs to be called before using any other methods.

    sensor.init()
    Returns true if the sensor was successfully initialized, false otherwise.

    read(oversampling=OSR_8192)
    Read the sensor and update the pressure and temperature. The sensor will be read with the supplied oversampling setting. Greater oversampling increases resolution, but takes longer and increases current consumption.

    sensor.read(ms5837.OSR_256)
    Valid arguments are:

    ms5837.OSR_256
    ms5837.OSR_512
    ms5837.OSR_1024
    ms5837.OSR_2048
    ms5837.OSR_4096
    ms5837.OSR_8192
    Returns True if read was successful, False otherwise.

    setFluidDensity(density)
    Sets the density in (kg/m^3) of the fluid for depth measurements. The default fluid density is ms5837.DENISTY_FRESHWATER.

    sensor.setFluidDensity(1000) # Set fluid density to 1000 kg/m^3
    sensor.setFluidDensity(ms5837.DENSITY_SALTWATER) # Use predefined saltwater density
    Some convenient constants are:

    ms5837.DENSITY_FRESHWATER = 997
    ms5837.DENSITY_SALTWATER = 1029
    pressure(conversion=UNITS_mbar)
    Get the most recent pressure measurement.

    sensor.pressure() # Get pressure in default units (millibar)
    sensor.pressure(ms5837.UNITS_atm) # Get pressure in atmospheres
    sensor.pressure(ms5837.UNITS_kPa) # Get pressure in kilopascal
    Some convenient constants are:

    ms5837.UNITS_Pa     = 100.0
    ms5837.UNITS_hPa    = 1.0
    ms5837.UNITS_kPa    = 0.1
    ms5837.UNITS_mbar   = 1.0
    ms5837.UNITS_bar    = 0.001
    ms5837.UNITS_atm    = 0.000986923
    ms5837.UNITS_Torr   = 0.750062
    ms5837.UNITS_psi    = 0.014503773773022
    Returns the most recent pressure in millibar * conversion. Call read() to update.

    temperature(conversion=UNITS_Centigrade)
    Get the most recent temperature measurement.

    sensor.temperature() # Get temperature in default units (Centigrade)
    sensor.temperature(ms5837.UNITS_Farenheit) # Get temperature in Farenheit
    Valid arguments are:

    ms5837.UNITS_Centigrade
    ms5837.UNITS_Farenheit
    ms5837.UNITS_Kelvin
    Returns the most recent temperature in the requested units, or temperature in degrees Centigrade if invalid units specified. Call read() to update.

    depth()
    Get the most recent depth measurement in meters.

    sensor.depth()
    Returns the most recent depth in meters using the fluid density (kg/m^3) configured by setFluidDensity(). Call read() to update.

    altitude()
    Get the most recent altitude measurement relative to Mean Sea Level pressure in meters.

    sensor.altitude()
    Returns the most recent altitude in meters relative to MSL pressure using the density of air at MSL. Call read() to update.
'''
