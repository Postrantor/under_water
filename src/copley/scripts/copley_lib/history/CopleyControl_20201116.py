#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''md
# 20201112:
    [Task]:
    1. 当前调试在位置模式下使用速度移动的方式，即：
        self.DesiredState = 21 # 0x24: Desired State(0x24). Bits: 0~42(P19)
        self.ProfileType = 2 # 0xc8: Give trajectory profile mode(0xc8). Bits: 0\1\256\257\2
    后面加入速度模式进行调用；
    2. 需要解决端口占用的问题，避免陷入死循环；加入更多的判断，比如有个端口处于不可读的状态，强行写入则会陷入死循环卡住
    [Issue]:
    √: 位置模式下的速度移动有个问题，读取速度时候使用的ASCII读取的是最大速度，应该使用0x18；
        同样的，设置速度值的时候也是设置的最大速度，这个不太合理，至少应该在速度模式下设置速度更合理，在位置模式下还是设置位置吧
    √: 使用0x18读取编码器的实际速度时候，本身带有正负号；
    修改该函数`def WriteRead(self, argin):`，当端口不可用的时候强行调用会引发错误，陷入死循环
    
# 20201111:
    [Task]:
    之前在写3个专利、苏老师的论文、开题、硬件接线；
    今天开始联调6个电机（实际上是5个，有一个推拉电机是坏的，正在购买新的）
    1. 首先两个驱动电机可以正常运转，在ROS上位机上显示轨迹信息
    2. 其他4个电机可以分别控制，主要需要解决的问题就是分别控制6个电机
    3. 对于端口号需要固定下来，或者不能固定的话，就是对称分布的方式，比如：USB0和USB4分别对应主驱动电机的左右
        但是这里还是有一个问题，这个对应的电机可以确定，但是左右哪个电机不能确定，后面思考一下，左右是不是不需要固定
    [Issue]:
    1. 两个USB转RS232的端口号不能固定，两个同时供电需要确定以及明确的指定端口的顺序；
        这个可能是不用担心的，他们同时供电应该是固定的顺序，后面测试一下；
    2. 这8个端口有时候不能正常通讯很头疼，  庆幸的是有时候是可以同时进行通讯的，所以估计多半是硬件的问题；
        后面需要排除一下这个问题；
    [Solve]:
    1. 解决速度、加速度、减速度的单位换算问题，在该类内将单位转换好，直接给其他函数调用，即不用考虑单位转换问题；

# 20201001:
    已经可以接入ROS进行调试，但是当前只是第一个电机，需要将`NodeId`替换成`defaultPortID`进行调用
    在此声明，之后要是从串口改成CAN的时候，继续使用该版本作为辅助参考
'''

# %%
# 可用于模块导入时限制，只有__all__内指定的属性、方法、类可被导入
__all__ = ['CopleyControlClass', 'main']
# 允许诸如 epydoc之类的python文档生成器工具知道如何正确解析模块文档
__docformat__ = 'restructuredtext'


# %%
# import tango as PyTango
import sys
# Add additional import
# ----- PROTECTED REGION ID(CopleyControl.additionnal_import) ENABLED START -----#
import time
import serial
# ----- PROTECTED REGION END -----#	//	CopleyControl.additionnal_import

# Device States Description
# MOVING : Moving
# ON : Device On
# FAULT : Amp is faulted and must be reset.
# ALARM : There is an alarm raised.
# INIT : The amp is initialising.


# %%
class CopleyControlClass():
    '''
        CopleyControl
    '''
# ------------------------------------------------------------------------------------------------------------------------
#                  CopleyControl Initial Device
# ------------------------------------------------------------------------------------------------------------------------
    # -------- Add you global variables here --------------------------
    # ----- PROTECTED REGION ID(CopleyControl.global_variables) ENABLED START -----#
    defaultPortID = '/dev/ttyUSB0'
    defaultBaud = 9600
    defaultTimeout = None  # .1

    PortIDUSB0 = '/dev/ttyUSB0'  # 主驱动_Left
    PortIDUSB1 = '/dev/ttyUSB1'  # 主驱动_Right
    PortIDUSB2 = '/dev/ttyUSB2'  # 钩刺机构_Left
    PortIDUSB4 = '/dev/ttyUSB4'  # 钩刺机构_Right
    PortIDUSB5 = '/dev/ttyUSB5'  # 推拉机构_Left
    PortIDUSB6 = '/dev/ttyUSB6'  # 推拉机构_Right
    # ----- PROTECTED REGION END -----#	//	CopleyControl.global_variables

    def __init__(self):
        # self.debug_stream('In __init__()')
        # ----- PROTECTED REGION ID(CopleyControl.__init__) ENABLED START -----#
        # self.name = name
        self.init_device()
        # CopleyControlClass.init_device(self)
        # ----- PROTECTED REGION END -----#	//	CopleyControl.__init__

    def delete_device(self):
        # self.debug_stream('In delete_device()')
        # ----- PROTECTED REGION ID(CopleyControl.delete_device) ENABLED START -----#
        print('delete_device')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.delete_device

    def init_device(self):
        # inits the device
        # self.debug_stream('In init_device()') # Sends the given message to the tango debug stream.

        self.NodeId = 0  # 对于单轴的RS-232串行总线控制，请将该轴的CAN节点地址设置为零（0）。
        # 若在加电后将CAN节点地址切换为零，则必须重置驱动器或重启电源，以使新的地址设置生效。
        # self.SerialPortID = self.defaultPortID

        self.attr_Position_read = 0.0  # 0x2d: Limited position. Units: counts. targetPosition = Position + SetPoint
        self.attr_SetPoint_read = 0.0  # 0xca: Trajectory Generator Position Command(0xca). Units: Counts.
        self.attr_DialPosition_read = 0.0  # 0x2d: Limited position. Units: counts.
        self.attr_Conversion_read = 1.0  # The ratio between the position and the dial position. The default value is 1.0
        self.attr_Velocity_read = 0.0  # 0x18: Actual velocity. Units: 0.1 counts/second. 这里将0xcb替换成了0x18
        self.attr_Acceleration_read = 0.0  # 0xcc: Maximum acceleration rate. Units: 10 counts/second2.
        self.attr_Deceleration_read = 0.0  # 0xcd: Maximum deceleration rate. Units: 10 counts/second2.

        self.attr_SoftwareCwLimit_read = 0.0  # 0xb8: Positive Software Limit Units: counts.
        self.attr_SoftwareCcwLimit_read = 0.0  # 0xb9: Negative Software Limit Units: counts.
        self.attr_SoftwareCwDialLimit_read = 0.0
        self.attr_SoftwareCcwDialLimit_read = 0.0
        self.attr_CwLimit_read = False  # Positive limit switche is active
        self.attr_CcwLimit_read = False  # Negative limit switche is active

        self.attr_HomeOffset_read = 0.0  # 0xc6: Home Offset. Units: counts.
        self.attr_HomingMethod_read = 0.0  # 归位方法
        # ----- PROTECTED REGION ID(CopleyControl.init_device) ENABLED START -----#
        self.DesiredState = 21  # 0x24: Desired State(0x24). Bits: 0~42(P19)
        self.ProfileType = 2  # 0xc8: Give trajectory profile mode(0xc8). Bits: 0\1\256\257\2

        self.attr_SetPoint_read = 0  # 0xca: This value gives destination position for absolute moves or move distance for relative moves. Units: Counts.
        self.targetPosition = 0
        self.attr_Velocity_read = 0  # 0xcb: Maximum velocity. Units: 0.1 counts/second.
        self.attr_Acceleration_read = 20000  # 0xcc: Maximum acceleration rate. Units: 10 counts/second2.
        self.attr_Deceleration_read = 20000  # 0xcd: Maximum deceleration rate. Units: 10 counts/second2.

        self.connectSerial()
        self.setInitParameters()
        # ----- PROTECTED REGION END -----#	//	CopleyControl.init_device

    def always_executed_hook(self):
        # self.debug_stream('In always_excuted_hook()')
        # ----- PROTECTED REGION ID(CopleyControl.always_executed_hook) ENABLED START -----#
        pass
        # ----- PROTECTED REGION END -----#	//	CopleyControl.always_executed_hook


# ------------------------------------------------------------------------------------------------------------------------
#    CopleyControl read/write attribute methods
#    attributes: 由设备中的名称标识。它具有可以读取的值。某些属性也可以更改（读写属性）。每个属性都有一个众所周知的固定数据类型。
# ------------------------------------------------------------------------------------------------------------------------
# --------------------------------Position--------------------------------

    def read_Position(self):
        '''
        # Commanded Position(0x2d_R*). Units: counts. / Read Actual Position
        # Actual Position(0x17). Units: Counts. Used to close position loop in drive every servo cycle. # For single feedback systems, this value is same as Actual Motor Position (0x32). For dual feedback systems, this value is same as Load Encoder Position (0x112).
        # 由0x17 -> 0x2d，0x2d是限制位置，主要是位置环下使用，当位置环处于速度模式的时候，也可以用来读取实时位置
        # 换句话说，取消了读取所有的限制值，后面可以考虑再写一些函数专门用来读取限制值
        '''
        # ----- PROTECTED REGION ID(CopleyControl.Position_read) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::read_Position()'
        command = self.getParameterCommand('0x17')
        self.attr_Position_read = self.getValue(command)
        # if self.attr_Position_read != '':
        #     attr.set_value(int(self.attr_Position_read))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.Position_read

    def write_Position(self, data):
        '''
        # Trajectory Generator Position Command(0xca). Units: Counts.
        # This value gives destination position for absolute moves or move distance for relative moves.
        '''
        # ----- PROTECTED REGION ID(CopleyControl.Position_write) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::write_Position()'
        self.targetPosition = int(data)
        # 分为三种模式：相对移动(0xc8=256、257)、绝对移动(0xc8=0、1)、速度移动(0xc8=2)，详见P28；
        # 当为速度模式的时候，不需要设置位置，所以没写这种情况；
        if int(self.ProfileType) == 256 or int(self.ProfileType) == 257:  # 相对位移
            # 在相对移动模式下，需要移动的位移(attr_SetPoint_read) = 目标位置(targetPosition) - 实际位置(attr_Position_read)
            # 256/1 0000 0000 = If set, relative move, trapezoidal profile.
            # 257/1 0000 0001 = If clear, relative move, S-curve profile.
            self.attr_SetPoint_read = self.targetPosition - int(self.attr_Position_read)
        elif int(self.ProfileType) == 0 or int(self.ProfileType) == 1:  # 绝对移动
            # 在绝对移动模式下，需要移动的位移(attr_SetPoint_read) = 目标位置(targetPosition)
            # 0     /0 0000 0000 = Absolute move, trapezoidal profile.
            # 1     /0 0000 0001 = Absolute move, S-curve profile.
            self.attr_SetPoint_read = self.targetPosition
        if int(self.attr_SoftwareCcwLimit_read) == 0 and int(self.attr_SoftwareCcwLimit_read) == 0:
            print('Software Limits are not set.')
            command = self.setParameterCommand('0xca', str(int(self.attr_SetPoint_read)))
            self.write(command)
        elif self.targetPosition in range(int(self.attr_SoftwareCcwLimit_read), int(self.attr_SoftwareCwLimit_read)):
            command = self.setParameterCommand('0xca', str(int(self.attr_SetPoint_read)))
            self.write(command)
        else:
            print('The input is out of the valid range, check the software limits. ')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.Position_write

    def read_SetPoint(self):
        # the set point for the movement. Units: Counts
        # self.debug_stream('In read_SetPoint()')
        # ----- PROTECTED REGION ID(CopleyControl.SetPoint_read) ENABLED START -----#
        print 'In ', self.dev_serial.port, '::read_SetPoint()'
        # attr.set_value(int(self.attr_SetPoint_read))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SetPoint_read

    def write_SetPoint(self, data):
        # command = self.setParameterCommand('0xca', int(data))
        # self.getValue(command)
        '''
        # Commanded Position(0x2d_R*). Units: counts.
        # Trajectory Generator Position Command(0xca). Units: Counts.
        # This value gives destination position for absolute moves or move distance for relative moves.
        '''
        # ----- PROTECTED REGION ID(CopleyControl.SetPoint_write) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::write_SetPoint()'
        self.attr_SetPoint_read = int(data)
        # set targetPosition
        command_current_position = self.getParameterCommand(0x2d)
        current_position = self.getValue(command_current_position)
        if int(self.ProfileType) == 256 or int(self.ProfileType) == 257:
            self.targetPosition = int(current_position) + int(data)
        elif int(self.ProfileType) == 0 or int(self.ProfileType) == 1:
            self.targetPosition = int(data)
        # write command
        if int(self.attr_SoftwareCcwLimit_read) == 0 and int(self.attr_SoftwareCcwLimit_read) == 0:
            # print('Software Limits are not set.')
            command = self.setParameterCommand('0xca', int(self.attr_SetPoint_read))
            self.getValue(command)
            # attr.set_value(self.attr_SetPoint_read)
        elif self.targetPosition in range(int(self.attr_SoftwareCcwLimit_read), int(self.attr_SoftwareCwLimit_read)):
            # print('expected Position is ', self.targetPosition, 'current position is ', self.attr_Position_read, 'input is ', data)/
            # print('SetPoint:', data, 'expected position: ', self.targetPosition, 'Ccwlimit: ', self.attr_SoftwareCcwLimit_read, 'Cwlimit: ', self.attr_SoftwareCwLimit_read)
            command = self.setParameterCommand('0xca', int(self.attr_SetPoint_read))
            self.getValue(command)
            # attr.set_value(self.attr_SetPoint_read)
        else:
            print('The input is out of range of the software limits')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SetPoint_write

    def read_DialPosition(self):
        '''
        # Commanded Position(0x2d_R*). Units: counts. 
        '''
        # ----- PROTECTED REGION ID(CopleyControl.DialPosition_read) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::read_DialPosition()'
        # attr.set_value(self.attr_DialPosition_read)
        command = self.getParameterCommand('0x2d')
        self.attr_Position_read = self.getValue(command)
        self.attr_DialPosition_read = float(self.attr_Position_read) / float(self.attr_Conversion_read)
        # attr.set_value(self.attr_DialPosition_read)
        # ----- PROTECTED REGION END -----#	//	CopleyControl.DialPosition_read

    def write_DialPosition(self, data):
        '''
        # Trajectory Generator Position Command(0xca). Units: Counts.
        # This value gives destination position for absolute moves or move distance for relative moves.
        '''
        # ----- PROTECTED REGION ID(CopleyControl.DialPosition_write) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::write_DialPosition()'
        self.targetPosition = float(self.attr_Conversion_read) * data
        data_new = (data - self.attr_DialPosition_read) * float(self.attr_Conversion_read)
        self.attr_SetPoint_read = (data - self.attr_DialPosition_read) * float(self.attr_Conversion_read)
        if self.targetPosition in range(int(self.attr_SoftwareCcwLimit_read), int(self.attr_SoftwareCwLimit_read)):
            command = self.setParameterCommand('0xca', str(int(data_new)))
            self.write(command)
        else:
            print('DialPosition is out of range.')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.DialPosition_write
# --------------------------------Conversion--------------------------------

    def read_Conversion(self):
        # The ratio between the position and the dial position. The default value is 1.0
        # self.debug_stream('In read_Conversion()')
        # ----- PROTECTED REGION ID(CopleyControl.Conversion_read) ENABLED START -----#
        print 'In ', self.dev_serial.port, '::read_Conversion()'
        # attr.set_value(self.attr_Conversion_read)
        # ----- PROTECTED REGION END -----#	//	CopleyControl.Conversion_read

    def write_Conversion(self, data):
        '''
        # The ratio between the position and the dial position. The default value is 1.0
        # self.debug_stream('In write_Conversion()')
        '''
        # ----- PROTECTED REGION ID(CopleyControl.Conversion_write) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::write_Conversion()'
        self.attr_Conversion_read = data
        # ----- PROTECTED REGION END -----#	//	CopleyControl.Conversion_write
# --------------------------------Velocity--------------------------------

    def read_Velocity(self):
        '''
        # Actual Velocity(0x18). Units: 0.1 encoder counts/s.
            # For estimated velocity. Units: 0.01 RPM.
            # For stepper mode: Units: 0.1 microsteps/s.
        # 这里将0xcb -> 0x18，即读取实际的速度值且有符号，区别于0xcb读取的是设定的最大速度数值（是位置模式下的命令）
        '''
        # ----- PROTECTED REGION ID(CopleyControl.Velocity_read) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::read_Velocity()'
        # if self.Copley.ProfileType == 2:
        command = self.getParameterCommand('0x18')  # 将0xcb替换成0x18，即读取实际的速度，这个数值是有正负号的
        # 将`self.attr_Velocity_read`这个变量更改为`attr_Velocity_read`变量
        # 这样可以避免获取的数据不是数值的时候程序报错，就一直使用前一个可用的数值
        # 另外，所有的指令最好依次发布比较好，也可以避免返回值为空的情况
        attr_Velocity_read = self.getValue(command)
        if attr_Velocity_read != '':
            unit = 0.1
            self.attr_Velocity_read = int(attr_Velocity_read) * unit
        else:  # 这种情况是驱动器没有给响应，如果是发布数据，一直用一定频率进行发送会好一些
            print('attr_Velocity_read is None')

        return self.attr_Velocity_read
        # ----- PROTECTED REGION END -----#	//	CopleyControl.Velocity_read

    def write_Velocity(self, data):
        '''
        # Programmed Position Mode
            # Trajectory Maximum Velocity(0xcb). Units: 0.1 counts/s.
            # Trajectory generator will attempt to reach this velocity during a move.
        # Programmed Speed Mode
            # Programmed Velocity Command(0x2f). Only used in Programmed Velocity Mode (Desired State (0x24) = 11)
            # Units: 0.1 encoder counts/s.
            # For estimated velocity. Units: 0.01 RPM.
            # For stepper mode. Units: 0.1 microsteps/s.
        '''
        # ----- PROTECTED REGION ID(CopleyControl.Velocity_write) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::write_Velocity()'
        # attr.set_value(self.attr_Velocity_read)
        # 根据不同的模式切换不同的ASCII
        if self.DesiredState == 11:  # Programmed Position Mode
            command = self.setParameterCommand('0x2f ', str(int(data)))
            unit = 0.1
        elif self.DesiredState == 21:  # Programmed Speed Mode
            command = self.setParameterCommand('0xcb ', str(int(data)))
            unit = 0.1
        data = int(data) / unit
        self.write(command)
        self.attr_Velocity_read = int(data)
        # print('Set maximum velocity to  ', str(vel), 'counts/second.')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.Velocity_write
# --------------------------------Ac/Deceleration--------------------------------

    def read_Acceleration(self):
        '''
        # Programmed Position Mode
            # Maximum acceleration rate(0xcc). Units: 10 counts/second2.
        # Programmed Speed Mode
            # Velocity Loop Acceleration Limit(0x36). Units: 1000 counts/s2.
            # Used by velocity loop limiter. Not used when velocity
            # loop is controlled by position loop.
        [Note]: 这个设置的也是加速度限制，因为是速度环，能直接控制的是速度，就像位置环能直接控制的是位置，而速度和加速度的说明都是设置最大值；类似于0x18取代0xcb一样，找到可以读取实际加速度的数值
        不过，好像没有，编码器能读取的是位置，做一次差分得到速度值，如果再差一次的话，噪声会比较大；但是既然能设置最大加速度，就应该可以读取实际的加速度值；在CME的上位机中调试电机也是只有位置和速度，没有加速度的数值
        '''
        # ----- PROTECTED REGION ID(CopleyControl.Acceleration_read) ENABLED START -----#
        # attr.set_value(self.attr_Acceleration_read)
        # print 'In ', self.dev_serial.port, '::read_Acceleration()'
        if self.DesiredState == 11:  # Programmed Position Mode
            command = self.getParameterCommand('0xcc')
            unit = 10
        elif self.DesiredState == 21:  # Programmed Speed Mode
            command = self.getParameterCommand('0x36')
            unit = 1000
        self.attr_Acceleration_read = self.getValue(command)
        if self.attr_Acceleration_read != '':
            self.attr_Acceleration_read = int(self.attr_Acceleration_read) * unit
            # print('Read maximum acceleration: ', str(acc), 'counts/(second*second)')
            # conversion = 0.0025
            # realAcceleration = int(self.attr_Acceleration_read) * conversion
            # print('Read motor real maximum acceleration: ', realAcceleration, 'counts/(second*second)')
            # attr.set_value(int(self.attr_Acceleration_read))
        else:
            print('attr_Acceleration_read is None')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.Acceleration_read

    def write_Acceleration(self, data):
        '''
        # Programmed Position Mode
            # Trajectory Maximum Acceleration(0xcc). Units: 10 counts/s2. 
            # Trajectory generator will attempt to reach this acceleration during a move. For s-curve profiles, this value also used to decelerate at end of move.
        # Programmed Speed Mode
            # Velocity Loop Acceleration Limit(0x36). Units: 1000 counts/s2.
            # Used by velocity loop limiter. Not used when velocity
            # loop is controlled by position loop.
        '''
        # ----- PROTECTED REGION ID(CopleyControl.Acceleration_write) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::write_Acceleration()'
        # print 'realAcceleration input is: ', int(data)
        # realAcceleration = int(data)
        # self.attr_Acceleration_read = realAcceleration*400
        if self.DesiredState == 11:  # Programmed Position Mode
            command = self.setParameterCommand('0xcc', str(int(self.attr_Acceleration_read)))
            unit = 10
        elif self.DesiredState == 21:  # Programmed Speed Mode
            command = self.setParameterCommand('0x36', str(int(self.attr_Acceleration_read)))
            unit = 1000
        data = int(data) / unit
        self.write(command)
        self.attr_Acceleration_read = int(data)
        # print('Set maximum acceleration to  ', str(acc), 'counts/(second*second).')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.Acceleration_write

    def read_Deceleration(self):
        '''
        # Programmed Position Mode
            Trajectory Maximum Deceleration(0xcd). Units: 10 counts/s2. 
            In trapezoidal trajectory mode, this value used to decelerate at end of move.
        # Programmed Speed Mode
            Velocity Loop Deceleration Limit(0x37). Units: 1000 counts/s2. 
            Used by velocity loop limiter. Not used when velocity loop is controlled by position loop.
        '''
        # ----- PROTECTED REGION ID(CopleyControl.Deceleration_read) ENABLED START -----#
        # attr.set_value(self.attr_Deceleration_read)
        # print 'In ', self.dev_serial.port, '::read_Deceleration()'
        if self.DesiredState == 11:  # Programmed Position Mode
            command = self.getParameterCommand('0xcd')
            unit = 10
        elif self.DesiredState == 21:  # Programmed Speed Mode
            command = self.getParameterCommand('0x37')
            unit = 1000
        self.attr_Deceleration_read = self.getValue(command)
        if self.attr_Deceleration_read != '':
            self.attr_Deceleration_read = int(self.attr_Deceleration_read) * unit
            # print('Read maximum deceleration: ', str(self.attr_Deceleration_read),  'counts/(second*second)')
            # conversion = 0.0025
            # realDeceleration = int(self.attr_Deceleration_read)*conversion
            # print('Read motor real maximum deceleration: ', realDeceleration, 'counts/(second*second)')
            # attr.set_value(int(realDeceleration))
            # attr.set_value(int(self.attr_Deceleration_read))
        else:
            print('attr_Deceleration_read is None')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.Deceleration_read

    def write_Deceleration(self, data):
        '''
        # Programmed Position Mode
            Trajectory Maximum Deceleration(0xcd). Units: 10 counts/s2. 
            In trapezoidal trajectory mode, this value used to decelerate at end of move.
        # Programmed Speed Mode
            Velocity Loop Deceleration Limit(0x37). Units: 1000 counts/s2. 
            Used by velocity loop limiter. Not used when velocity loop is controlled by position loop.
        '''
        # ----- PROTECTED REGION ID(CopleyControl.Deceleration_write) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::write_Deceleration()'
        # print 'realDeceleration input is: ', int(data)
        # self.attr_Deceleration_read = int(data)*400
        if self.DesiredState == 11:  # Programmed Position Mode
            command = self.setParameterCommand('0xcd', str(int(self.attr_Deceleration_read)))
            unit = 10
        elif self.DesiredState == 21:  # Programmed Speed Mode
            command = self.setParameterCommand('0x37', str(int(self.attr_Deceleration_read)))
            unit = 1000
        self.attr_Deceleration_read = int(data) / unit
        self.write(command)
        # print('Set maximum deceleration to  ', str(dec), 'counts/(second*second).')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.Deceleration_write
# --------------------------------Current--------------------------------

    def read_Current(self):
        pass

    def write_Current(self):
        pass
# --------------------------------SoftwareLimit--------------------------------
# PositiveSoftwareLimit
    # Positive Software Limit value(0xb8_RF). Units: counts.
    # This parameter is only available on drives that support trajectory generation and homing.
    # Software limits are only in effect after drive has been referenced
    # (i.e. homing has been successfully completed).
    # Set to less than negative software limit to disable.

    def read_SoftwareCwLimit(self):
        # self.debug_stream('In read_SoftwareCwLimit()')
        # ----- PROTECTED REGION ID(CopleyControl.SoftwareCwLimit_read) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::read_SoftwareCwLimit()'
        command = self.getParameterCommand('0xb8')
        self.attr_SoftwareCwLimit_read = self.getValue(command)
        # attr.set_value(int(self.attr_SoftwareCwLimit_read))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCwLimit_read

    def write_SoftwareCwLimit(self, data):
        # self.debug_stream('In write_SoftwareCwLimit()')
        '''
        data = attr.get_write_value()
        '''
        # ----- PROTECTED REGION ID(CopleyControl.SoftwareCwLimit_write) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::write_SoftwareCwLimit()'
        # print('SoftwareCwLimit:', data, 'current position: ', self.attr_Position_read, 'Ccwlimit: ', self.attr_SoftwareCcwLimit_read, 'Cwlimit: ', self.attr_SoftwareCwLimit_read)
        self.targetPosition = int(self.attr_Position_read) + int(self.attr_SetPoint_read)
        if self.targetPosition in range(int(self.attr_SoftwareCcwLimit_read), int(data)):
            self.attr_SoftwareCwLimit_read = data
            command = self.setParameterCommand('0xb8', str(int(data)))
            self.write(command)
            # attr.set_value(int(self.attr_SoftwareCwLimit_read))
        else:
            print('SoftwareCwLimit must be higher than current Position plus current SetPoint')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCwLimit_write
# NegativeSoftwareLimit
    # Negative Software Limit(0xb9). Units: counts.
    # Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). Set to greater than positive software limit to disable.

    def read_SoftwareCcwLimit(self):
        # ----- PROTECTED REGION ID(CopleyControl.SoftwareCcwLimit_read) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::read_SoftwareCcwLimit()'
        command = self.getParameterCommand('0xb9')
        self.attr_SoftwareCcwLimit_read = self.getValue(command)
        # attr.set_value(int(self.attr_SoftwareCcwLimit_read))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCcwLimit_read

    def write_SoftwareCcwLimit(self, data):
        '''
        data = attr.get_write_value()
        '''
        # ----- PROTECTED REGION ID(CopleyControl.SoftwareCcwLimit_write) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::write_SoftwareCcwLimit()'
        self.targetPosition = int(self.attr_Position_read) + int(self.attr_SetPoint_read)
        if int(data) < self.targetPosition:
            command = self.setParameterCommand('0xb9', str(int(data)))
            self.write(command)
            # attr.set_value(int(data))
        else:
            print('SoftwareCcwLimit must be smaller than Position plus SetPoint')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCcwLimit_write

# PositiveSoftwareDialLimit
    # Positive Software Limit value(0xb8_RF). Units: counts.
    # This parameter is only available on drives that support trajectory generation and homing.
    # Software limits are only in effect after drive has been referenced
    # (i.e. homing has been successfully completed).
    # Set to less than negative software limit to disable.
    def read_SoftwareCwDialLimit(self):
        # ----- PROTECTED REGION ID(CopleyControl.SoftwareCwDialLimit_read) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::read_SoftwareCwDialLimit()'
        self.attr_SoftwareCwDialLimit_read = float(self.attr_SoftwareCwLimit_read) / float(self.attr_Conversion_read)
        # if self.attr_SoftwareCwDialLimit_read != '':
        #     attr.set_value(int(self.attr_SoftwareCwDialLimit_read))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCwDialLimit_read

    def write_SoftwareCwDialLimit(self, data):
        '''
        data = attr.get_write_value()
        '''
        # ----- PROTECTED REGION ID(CopleyControl.SoftwareCwDialLimit_write) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::write_SoftwareCwDialLimit()'
        data_new = float(self.attr_Conversion_read) * data
        self.attr_SoftwareCwLimit_read = data_new
        self.attr_SoftwareCwDialLimit_read = data
        # attr.set_value(data)
        command = self.setParameterCommand('0xb8', int(self.attr_SoftwareCwLimit_read))
        self.write(command)
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCwDialLimit_write
# NegativeSoftwareDialLimit
    # Negative Software Limit(0xb9). Units: counts.
    # Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). Set to greater than positive software limit to disable.

    def read_SoftwareCcwDialLimit(self):
        # ----- PROTECTED REGION ID(CopleyControl.SoftwareCcwDialLimit_read) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::read_SoftwareCcwDialLimit()'
        self.attr_SoftwareCcwDialLimit_read = float(self.attr_SoftwareCcwLimit_read) / float(self.attr_Conversion_read)
        # if self.attr_SoftwareCcwLimit_read != '':
        #     attr.set_value(int(self.attr_SoftwareCcwDialLimit_read))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCcwDialLimit_read

    def write_SoftwareCcwDialLimit(self, data):
        '''
        data = attr.get_write_value()
        '''
        # ----- PROTECTED REGION ID(CopleyControl.SoftwareCcwDialLimit_write) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::write_SoftwareCcwDialLimit()'
        # attr.set_value(data)
        data_new = float(self.attr_Conversion_read) * data
        self.attr_SoftwareCcwLimit_read = int(data_new)
        self.attr_SoftwareCcwDialLimit_read = data
        command = self.setParameterCommand('0xb9', int(self.attr_SoftwareCcwLimit_read))
        self.write(command)
        # attr.set_value(self.attr_SoftwareCcwDialLimit_read)
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCcwDialLimit_write

# --------------------------------HardwareLimit--------------------------------
    # 9 = 512 正限位开关有效(Positive limit switch active)[电机轴已经接触到正限位开关。]
    # 10 = 1024 负限位开关有效(Negative limit switch active)[电机轴已经接触到负限位开关。]
    def read_CwLimit(self):
        '''
        # Positive hardware limit
        '''
        # ----- PROTECTED REGION ID(CopleyControl.CwLimit_read) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::read_CwLimit()'
        self.clearLatchedStatus()
        value = self.readLatchedEventStatus()
        self.attr_CwLimit_read = (int(value) & 512) != 0  # 若也是512则返回`True`，可能是运行指令`g r0xc2 \n`
        # attr.set_value(self.attr_CwLimit_read)
        if self.attr_CwLimit_read:
            print('Positive limit switche is active')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.CwLimit_read

    def read_CcwLimit(self):
        '''
        # Negative hardware limit
        '''
        # ----- PROTECTED REGION ID(CopleyControl.CcwLimit_read) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::read_CcwLimit()'
        self.clearLatchedStatus()
        value = self.readLatchedEventStatus()
        self.attr_CcwLimit_read = (int(value) & 1024) != 0
        # attr.set_value(self.attr_CcwLimit_read)
        if self.attr_CcwLimit_read:
            print('Negative limit switche is active')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.CcwLimit_read
# --------------------------------Homing--------------------------------

    def read_HomeOffset(self):
        '''
        # Home Offset(0xc6_RF). Units: counts.
        # Home offset is difference between zero position for application and machine home position (found during homing). Once homing is completed, new zero position determined by homing state machine will be located sensor position plus this offset. All subsequent absolute moves shall be taken relative to this new zero position.
        '''
        # ----- PROTECTED REGION ID(CopleyControl.HomeOffset_read) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::read_HomeOffset()'
        command = self.getParameterCommand('0xc6')
        self.attr_HomeOffset_read = self.getValue(command)
        # if self.attr_HomeOffset_read != '':
        #     attr.set_value(int(self.attr_HomeOffset_read))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.HomeOffset_read

    def write_HomeOffset(self, data):
        '''
        data = attr.get_write_value()
        '''
        # ----- PROTECTED REGION ID(CopleyControl.HomeOffset_write) ENABLED START -----#
        # print 'In ', self.dev_serial.port, '::write_HomeOffset()'
        self.attr_HomeOffset_read = int(data)
        command = self.setParameterCommand('0xc6', str(int(self.attr_HomeOffset_read)))
        self.write(command)
        # ----- PROTECTED REGION END -----#	//	CopleyControl.HomeOffset_write

    def read_HomingMethod(self):
        '''
        # Homing Method Configuration.(0xc2_RF)
            # Set Current Position as Home
                # N/A 512
            # Next Index
                # Positive 544
                # Negative 560
            # Limit Switch
                # Positive 513
                # Negative 529
            # Limit Switch Out to Index
                # Positive 545
                # Negative 561
            # Home Switch
                # Positive 514
                # Negative 530
            # Home Switch Out to Index
                # Positive 546
                # Negative 562
            # Home Switch In to Index
                # Positive 610
                # Negative 626
            # Hard Stop
                # Positive 516
                # Negative 532
            # Hard Stop Out to Index
                # Positive 548
                # Negative 564
            # Lower Home
                # Positive 771
                # Negative 787
            # Upper Home
                # Positive 515
                # Negative 531
            # Lower Home Outside Index
                # Positive 803
                # Negative 819
            # Lower Home Inside Index
                # Positive 867
                # Negative 883
            # Upper Home Outside Index
                # Positive 547
                # Negative 563
            # Upper Home Inside Index
                # Positive 611
                # Negative 627
            # Immediate Home
                # N/A 15
        '''
        # ----- PROTECTED REGION ID(CopleyControl.HomingMethod_read) ENABLED START -----#
        # attr.set_value(self.attr_HomingMethod_read)
        command = self.getParameterCommand('0xc2')
        self.attr_HomingMethod_read = self.getValue(command)
        # if self.attr_HomingMethod_read != '':
        #     attr.set_value(int(self.attr_HomingMethod_read))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.HomingMethod_read

    def write_HomingMethod(self, data):
        '''
        data = attr.get_write_value()
        '''
        # ----- PROTECTED REGION ID(CopleyControl.HomingMethod_write) ENABLED START -----#
        HomeReferenceNrList = [512, 544, 560, 513, 529, 545, 561, 516, 532, 548, 564, 514, 530, 546, 562, 610, 626, 771, 787, 515, 531, 803, 819, 867, 883, 547, 563, 611, 627]
        if int(data) in HomeReferenceNrList:
            self.attr_HomingMethod_read = int(data)
            self.setHomeMethod(int(self.attr_HomingMethod_read))
        else:
            print('Input HomeReferenceNr: {} is not valid.'.format(data))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.HomingMethod_write
# --------------------------------AttrHardware--------------------------------

    def read_attr_hardware(self, data):
        # ----- PROTECTED REGION ID(CopleyControl.read_attr_hardware) ENABLED START -----#
        print('read_attr_hardware')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.read_attr_hardware


# ------------------------------------------------------------------------------------------------------------------------
#                     CopleyControl command methods
# properties: 由设备中的名称标识。通常，设备属性用于提供一种配置设备的方法。
# commands: 也由名称标识。命令执行时可能接收或不接收参数，并且可能会返回值。
# ------------------------------------------------------------------------------------------------------------------------
# $ --------------------------------dev_state/status--------------------------------

    def dev_status(self):
        '''
        Event Status Register(0xA0). Bits: 0~31
            This command gets the device status (stored in its device_status data member) and returns it to the caller.
            :return: Device status
            :rtype: PyTango.ConstDevString
            if the motor is in motion, the Status is 'Status is MOVING';
            if the motor is stationary, the Status is 'Status is ON';
            if the motor is out of power, the Status is 'Status is OFF';
            if the motor reaches the positive hardware limit, the Status is 'Positive limit switch Active';
            if the motor reaches the negative hardware limit, the Status is 'Negative limit switch Active';
        Bit-mapped as follows:
            0  检测到短路(Short circuit detected)
            1  驱动温度(Drive over temperature)
            2  过电压(Over voltage)
            3  欠压(Under voltage)
            4  电机温度传感器激活(Motor temperature sensor active)
            5  编码器电源错误(Encoder power error)
            6  电机定相误差(Motor phasing error)
            7  电流输出限制(Current output limited)[输出电流被I2T Algorithm公式所限制或者一个锁定的电流错误发生。]
            8  电压输出限制(Voltage output limited)[电流环正试图使用全部的母线电压去控制电流，一般发生在电机正占用全部的母线电压高速运行。]
            9  正限位开关有效(Positive limit switch active)[电机轴已经接触到正限位开关。]
            10  负限位开关有效(Negative limit switch active)[电机轴已经接触到负限位开关。]
            11  启用输入无效(Enable input not active)
            12  驱动器已被软件禁用(Drive is disabled by software)]
            13  试图停止电机(Trying to stop motor)[驱动器在速度或位置模式下，已经被去使能。在速度模式下，驱动器正使用“ Fast Stop Ramp”(详见Velocity Loop Limits)；在位置模式下，驱动器正使用"Abort Deceleration rate‘(详见Trajectory Limits)。输出保持有效直到驱动器重新使能。]
            14  电机制动器已激活(Motor brake activated)
            15  PWM输出禁用(PWM outputs disabled)
            16  正软件极限条件(Positive software limit condition)[实际位置已经超出正的软限位设置。请参考Homing.]
            17  负软件限制条件(Negative software limit condition)[实际位置已经超出负的软限位设置。请参考Homing]
            18  跟随错误故障。 发生跟随错误，驱动器处于跟随错误模式。(Following Error Fault. A following error has occurred, and drive is in following error mode.)[跟随误差已经达到设定的限制值。请参考Following Error Faults]
            19  以下错误警告。 指示位置误差大于警告后的位置。(Following Error Warning. Indicates position error is greater than position following warning.)[跟随误差已经达到设定的报警值。请参考Following Error Faults]
            20  驱动器当前处于重置状态(Drive is currently in reset condition)
            21  位置已封装。 位置变量不能无限增加。 达到一定值后，变量回滚。 这种计数方式称为位置换行或模数计数(Position has wrapped. Position variable cannot increase indefinitely. After reaching a certain value the variable rolls back. This type of counting is called position wrapping or modulo count[位置脉冲计数已超过以下范围。(-2^31 – 2^31-1)且已经设置位置包裹。驱动器其他功能不会受到影响。]
            22  驱动器故障。 发生配置为在故障掩码（0xA7）中锁存的故障。 可以使用锁存故障状态寄存器（0xA4）清除锁存故障。(Drive fault. Fault configured as latching in Fault Mask (0xA7) has occurred. Latched faults may be cleared using Latching Fault Status Register (0xA4).))
            23  已达到速度极限（0x3A）(Velocity limit (0x3A) has been reached)[速度命令 (来自模拟量输入, PWM输入,或位置环) 已经超过了速度限制。请参考Velocity Loop Limits]
            24  达到加速限制（0x36）(Acceleration limit (0x36) has been reached)[在速度模式下，电机已经达到速度环中设置的加速度和减速度限制的设定值。]
            25  位置跟踪。 位置环错误（0x35）超出跟随错误故障限制（0xBA）。(Position Tracking. Position Loop Error (0x35) is outside of Following Error Fault Limit (0xBA).)[跟随误差已经超过了设定值。请参考Position and Velocity Tracking Windows]
            26  归位开关已激活(Home switch is active)[电机轴已经接触到了原点开关。]
            27  运动中。 设置轨迹生成器是否正在运行轮廓或跟随错误故障限制（0xBA）在跟踪窗口之外。 当驱动器固定到位时清除。(In motion. Set if trajectory generator is running profile or Following Error Faul Limit (0xBA) is outside tracking window. Clear when drive is settled in position.)[电机正在运行，或他在一次运动后还没有整定结束。在运动结束时，当电机进入位置跟踪轨迹窗口并且保持设定的跟踪时间表示驱动器完成整定。一旦此项有效，它将保持有效直到一个新的运动开始。]
            28  速度窗口。 当速度误差大于编程的速度窗口时设置(Velocity window. Set when velocity error is larger than programmed velocity window)[目标速度和实际速度之间的误差超过了这个窗口的设定值。请参考Position and Velocity Tracking Windows]
            29  相位尚未初始化。 如果驱动器定相且没有霍尔，则该位置1，直到驱动器初始化其相位。(Phase not yet initialized. If drive is phasing with no Halls, this bit is set until drive has initialized its phase.)[驱动器使用了相位初始化功能，但是相位没能被初始化。]
            30  命令故障。 CANopen或EtherCAT主站不发送命令或不存在PWM命令。注意：如果通过设置数字输入命令配置（0xA8）的位3启用了“允许100％输出”选项，此故障将不会检测到丢失的PWM命令。(Command fault. CANopen or EtherCAT master not sending commands or PWM command not present.)[缺少PWM或其他命令信号 (例如EtherCAT主站)。如果在将“Digital InputCommand Configuration” Bit 3值为激活100%输出选项，驱动器将不会再检测PWM命令丢失，该错误不会出现。]
            31  保留。(Reserved.)
            Note: If Allow 100% Output option is enabled by setting Bit 3 of Digital Input Command Configuration (0xA8) this fault will not detect missing PWM command.
        '''
        argout = ''
        # ----- PROTECTED REGION ID(CopleyControl.Status) ENABLED START -----#
        # EventStatus(0xa1)
        command_DriveEventStatus = self.getParameterCommand('0xa0')
        DriveEventStatus = self.getValue(command_DriveEventStatus)
        # print 'DriveEventStatus=', DriveEventStatus
        if DriveEventStatus == 'No power':
            argout = 'Status is OFF, Power OFF'
        elif str(int(DriveEventStatus)) == '0':
            argout = 'Status is STANDBY'
        elif str(int(DriveEventStatus)) != '0' and str(int(DriveEventStatus)) != 'No power':
            self.clearLatchedStatus()
            value = int(self.readLatchedEventStatus())
            # 0xa1(Latched) = 0xa0
            if int(value) == int(DriveEventStatus):
                # (value&2^DriveEventStatus) != 0
                if (value & 1) != 0:
                    argout = '2^0  检测到短路(Short circuit detected)'
                elif (value & 2) != 0:
                    argout = '2^1  驱动温度(Drive over temperature)'
                elif (value & 4) != 0:
                    argout = '2^2  过电压(Over voltage)'
                elif (value & 8) != 0:
                    argout = '2^3  欠压(Under voltage)'
                elif (value & 16) != 0:
                    argout = '2^4  电机温度传感器激活(Motor temperature sensor active)'
                elif (value & 32) != 0:
                    argout = '2^5  编码器电源错误(Encoder power error)'
                elif (value & 64) != 0:
                    argout = '2^6  电机定相误差(Motor phasing error)'
                elif (value & 128) != 0:
                    argout = '2^7  电流输出限制(Current output limited)[输出电流被I2T Algorithm公式所限制或者一个锁定的电流错误发生。]'
                elif (value & 256) != 0:
                    argout = '2^8  电压输出限制(Voltage output limited)[电流环正试图使用全部的母线电压去控制电流，一般发生在电机正占用全elif (value&1024)!=0:'
                    argout = '部的母线电压高速运行。]'
                elif (value & 512) != 0:
                    argout = '2^9  正限位开关有效(Positive limit switch active)[电机轴已经接触到正限位开关。]'
                elif (value & 1024) != 0:
                    argout = '2^10  负限位开关有效(Negative limit switch active)[电机轴已经接触到负限位开关。]'
                elif (value & 2048) != 0:
                    argout = '2^4096  启用输入无效(Enable input not active)'
                elif (value & 8192) != 0:
                    argout = '2^12  驱动器已被软件禁用(Drive is disabled by software)]'
                elif (value & 16384) != 0:
                    argout = '2^13  试图停止电机(Trying to stop motor)[驱动器在速度或位置模式下，已经被去使能。在速度模式下，驱动器正使用“ Fast Stop Ramp”(详见Velocity Loop Limits)；在位置模式下，驱动器正使用"Abort Deceleration rate‘(详见Trajectory Limits)。输出保持有效直到驱动器重新使能。]'
                elif (value & 32768) != 0:
                    argout = '2^14  电机制动器已激活(Motor brake activated)'
                elif (value & 65536) != 0:
                    argout = '2^15  PWM输出禁用(PWM outputs disabled)'
                elif (value & 131072) != 0:
                    argout = '2^16  正软件极限条件(Positive software limit condition)[实际位置已经超出正的软限位设置。请参考Homing.]'
                elif (value & 262144) != 0:
                    argout = '2^17  负软件限制条件(Negative software limit condition)[实际位置已经超出负的软限位设置。请参考Homing]'
                elif (value & 524288) != 0:
                    argout = '2^18  跟随错误故障。 发生跟随错误，驱动器处于跟随错误模式。(Following Error Fault. A following error has occurred, and drive is in following error mode.)[跟随误差已经达到设定的限制值。请参考Following Error Faults]'
                elif (value & 1048576) != 0:
                    argout = '2^19  以下错误警告。 指示位置误差大于警告后的位置。(Following Error Warning. Indicates position error is greater than position following warning.)[跟随误差已经达到设定的报警值。请参考Following Error Faults]'
                elif (value & 2097152) != 0:
                    argout = '2^20  驱动器当前处于重置状态(Drive is currently in reset condition)'
                elif (value & 4194304) != 0:
                    argout = '2^21  位置已封装。 位置变量不能无限增加。 达到一定值后，变量回滚。 这种计数方式称为位置换行或模数计数(Position has wrapped. Position variable cannot increase indefinitely. After reaching a certain value the variable rolls back. This type of counting is called position wrapping or modulo count[位置脉冲计数已超过以下范围。(-2^31 – 2^31-1)且已经设置位置包裹。驱动器其他功能不会受到影响。]'
                elif (value & 8388608) != 0:
                    argout = '2^22  驱动器故障。 发生配置为在故障掩码（0xA7）中锁存的故障。 可以使用锁存故障状态寄存器（0xA4）清除锁存故障。(Drive fault. Fault configured as latching in Fault Mask (0xA7) has occurred. Latched faults may be cleared using Latching Fault Status Register (0xA4).))'
                elif (value & 16777216) != 0:
                    argout = '2^23  已达到速度极限（0x3A）(Velocity limit (0x3A) has been reached)[速度命令 (来自模拟量输入, PWM输入,或位置环) 已经超过了速度限制。请参考Velocity Loop Limits]'
                elif (value & 33554432) != 0:
                    argout = '2^24  达到加速限制（0x36）(Acceleration limit (0x36) has been reached)[在速度模式下，电机已经达到速度环中设置的加速度和减速度限制的设定值。]'
                elif (value & 67108864) != 0:
                    argout = '2^25  位置跟踪。 位置环错误（0x35）超出跟随错误故障限制（0xBA）。(Position Tracking. Position Loop Error (0x35) is outside of Following Error Fault Limit (0xBA).)[跟随误差已经超过了设定值。请参考Position and Velocity Tracking Windows]'
                elif (value & 134217728) != 0:
                    argout = '2^26  归位开关已激活(Home switch is active)[电机轴已经接触到了原点开关。]'
                elif (value & 268435456) != 0:
                    argout = '2^27  运动中。 设置轨迹生成器是否正在运行轮廓或跟随错误故障限制（0xBA）在跟踪窗口之外。 当驱动器固定到位时清除。(In motion. Set if trajectory generator is running profile or Following Error Faul Limit (0xBA) is outside tracking window. Clear when drive is settled in position.)[电机正在运行，或他在一次运动后还没有整定结束。在运动结束时，当电机进入位置跟踪轨迹窗口并且保持设定的跟踪时间表示驱动器完成整定。一旦此项有效，它将保持有效直到一个新的运动开始。]'
                elif (value & 536870912) != 0:
                    argout = '2^28  速度窗口。 当速度误差大于编程的速度窗口时设置(Velocity window. Set when velocity error is larger than programmed velocity window)[目标速度和实际速度之间的误差超过了这个窗口的设定值。请参考Position and Velocity Tracking Windows]'
                elif (value & 1073741824) != 0:
                    argout = '2^29  相位尚未初始化。 如果驱动器定相且没有霍尔，则该位置1，直到驱动器初始化其相位。(Phase not yet initialized. If drive is phasing with no Halls, this bit is set until drive has initialized its phase.)[驱动器使用了相位初始化功能，但是相位没能被初始化。]'
                elif (value & 2147483648) != 0:
                    argout = '2^30  命令故障。 CANopen或EtherCAT主站不发送命令或不存在PWM命令。注意：如果通过设置数字输入命令配置（0xA8）的位3启用了“允许100％输出”选项，此故障将不会检测到丢失的PWM命令。(Command fault. CANopen or EtherCAT master not sending commands or PWM command not present.)[缺少PWM或其他命令信号 (例如EtherCAT主站)。如果在将“Digital InputCommand Configuration” Bit 3值为激活100%输出选项，驱动器将不会再检测PWM命令丢失，该错误不会出现。]'
                elif (value & 4294967296) != 0:
                    argout = '2^31  保留。(Reserved.)'
            else:
                argout = 'Status is MOVING'
                # print('Status is MOVING')
        else:
            argout = 'Status is FAULT'
        self.argout = argout
        # ----- PROTECTED REGION END -----#	//	CopleyControl.Status
        # self.set_status(self.argout)
        # self.__status = PyTango.Device_4Impl.dev_status(self)
        return self.argout

    def dev_fault(self):
        '''
        Fault Register(0xA4). Bits: 0~18
        '''
        argout = ''
        # ----- PROTECTED REGION ID(CopleyControl.Fault) ENABLED START -----#
        # FaultRegister(0xa4)
        command_DriveFaultRegister = self.getParameterCommand('0xa4')
        DriveFaultRegiater = self.getValue(command_DriveFaultRegister)
        value = int(DriveFaultRegiater)
        if str(int(DriveFaultRegiater)) == '0':
            argout = 'Status is STANDBY'
        elif (value & 1) != 0:
            argout = '0 (Data flash CRC failure. This fault is considered fatal and cannot be cleared. This bit is read-only and will always be set. If drive detects corrupted flash data values on startup it will remain disabled and indicate fault condition. )数据闪存CRC故障。 该故障被认为是致命的，无法清除。 该位是只读的，将始终被设置。 如果驱动器检测到损坏的闪存数据启动时的值将保持禁用状态并指示故障情况。'
        elif (value & 2) != 0:
            argout = '1 (Drive internal error. This bit is read-only and will always be set. If drive fails its power-on self-test, it will remain disabled and indicate fault condition.) 驱动器内部错误。 该位是只读的，将始终被设置。 如果驱动器无法通过开机自检，它将保持禁用状态并指示故障状态。'
        elif (value & 4) != 0:
            argout = '2 (Short circuit. If set: programs drive to latch a fault when short circuit is detected on motor outputs. If clear: programs drive to disable outputs for 100 ms after short circuit and then re-enable.) 短路 如果置位：当在电机输出上检测到短路时，程序将驱动以锁定故障。 如果清除，则在短路后程序会在100毫秒内禁用输出，然后重新启用。'
        elif (value & 8) != 0:
            argout = '3 (Drive over temperature. If set: programs drive to latch a fault when drive over temperature event happens. If clear: programs drive to re-enable as soon as it cools sufficiently from over temperature event.) 驱动温度过高。 如果设置：当发生驱动器超温事件时，程序将驱动器锁存故障。 如果清除，则表明程序在由于过热事件而充分冷却后立即重新启用。'
        elif (value & 16) != 0:
            argout = '4 (Motor over temperature. If set: programs drive to latch a fault when motor temperature sensor input activates. If clear: programs drive to re-enable as soon as over temperature input becomes inactive.) 电机温度过高。 如果置位：当电动机温度传感器输入激活时，程序将驱动以锁定故障。 如果清除，则表明驱动程序在温度输入无效时立即重新启用。'
        elif (value & 32) != 0:
            argout = '5 (Over voltage. If set: programs drive to latch a fault when excessive bus voltage is detected. If clear: programs drive to re-enable as soon as bus voltage is within normal range.) 过电压。 如果设置：当检测到总线电压过高时，程序将驱动程序以锁定故障。 如果清除，则表明程序在总线电压处于正常范围内时立即重新启用。'
        elif (value & 64) != 0:
            argout = '6 (Under voltage. If set: programs drive to latch a fault condition when inadequate bus voltage is detected. If clear: programs drive to re-enable as soon as bus voltage is within normal range.) 欠电压。 如果置位：当检测到总线电压不足时，程序将驱动以锁定故障状态。 如果清除，则表明程序在总线电压处于正常范围内时立即重新启用。'
        elif (value & 128) != 0:
            argout = '7 (Feedback fault. If set: programs drive to latch a fault when feedback faults occur. Feedback faults occur if too much current is drawn from 5 V source on drive, resolver or analog encoder is disconnected, or resolver or analog encoder has levels out of tolerance. )反馈故障。 如果设置：当发生反馈故障时，程序将驱动程序以锁定故障。 如果从驱动器上的5 V电源汲取过多电流，分解器或模拟编码器断开连接，或者分解器或模拟编码器的电平超出容限，则会发生反馈故障。'
        elif (value & 256) != 0:
            argout = '8 (Phasing error. If set: programs drive to latch a fault when phasing errors occur. If clear: programs drive to re-enable when phasing error is removed.) 相位错误。 如果设置：当出现定相错误时，程序将驱动程序以锁定故障。 如果清除，则说明移相错误后程序将重新启用。'
        elif (value & 512) != 0:
            argout = '9 (Following error. If set: programs the drive to latch a fault and disable drive when following error occurs. If clear: programs drive to abort current move and remain enabled when following error occurs.) 跟随错误。 如果设置：对驱动器进行编程以锁定故障并在以下情况下禁用驱动器。 如果清除，则程序将中止当前运动，并在发生以下错误时保持启用状态。'
        elif (value & 1024) != 0:
            argout = '10 (If set: programs drive to latch a fault when output current is limited by I2T algorithm.) 如果置位：当输出电流受I2T算法限制时，程序将驱动程序锁定故障。'
        elif (value & 2048) != 0:
            argout = '11 (FPGA failure. This bit is read-only.) FPGA故障。 该位是只读的。'
        elif (value & 4096) != 0:
            argout = '12 (Command input lost fault. If set: programs drive to latch a fault and disable when command input is lost.) 命令输入丢失故障。 如果设置，则程序将驱动程序以锁定故障并在丢失命令输入时禁用。'
        elif (value & 8192) != 0:
            argout = '13 (Unable to initialize internal drive hardware. This bit is read-only.) 无法初始化内部驱动器硬件。 该位是只读的。'
        elif (value & 16384) != 0:
            argout = '14 (if set, programs drive to latch a fault when there is safety circuit consistency check failure.) 如果设置，当安全电路一致性检查失败时，程序将驱动以锁定故障。'
        elif (value & 32768) != 0:
            argout = '15 (If set, programs drive to latch a fault when drive is unable to control motor current.) 如果置位，程序将在驱动器无法控制电动机电流时锁存故障。'
        elif (value & 65636) != 0:
            argout = '16 (If set, programs drive to latch a fault when motor wiring is disconnected, see Open Motor Wiring Check Current (0x19D).) 如果置位，程序将在断开电动机接线时驱动程序以锁定故障，请参阅断开电动机接线检查电流（0x19D）。'
        elif (value & 131072) != 0:
            argout = '17 (Reserved.) 保留'
        elif (value & 262144) != 0:
            argout = '18 (Safe torque off active) 安全扭矩关闭有效'
        else:
            argout = 'Status is FAULT'
        self.argout = argout
        # ----- PROTECTED REGION END -----#	//	CopleyControl.Fault
        # self.set_fault(self.argout)
        # self.__fault = PyTango.Device_4Impl.dev_fault(self)
        return self.argout
# $ --------------------------------StopMove--------------------------------

    def StopMove(self):
        ''' 
        stops a movement immediately.
        要中止正在进行的移动，请发送t 0命令。
        这将使用中止减速率停止正在进行的移动。 驱动器将保持启用状态。
        '''
        # ----- PROTECTED REGION ID(CopleyControl.StopMove) ENABLED START -----#
        self.write('{} t 0\n'.format(str(self.NodeId)))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.StopMove
# $ --------------------------------ResetMotor--------------------------------

    def ResetMotor(self):
        ''' 
        Reset the amplifier immediately(r\n). 
            The amplifier baud rate is set to 9600 when the amplifier restarts.
            NOTE: if a reset command is issued to an amplifier on a multi-drop network, error code 32, 'CAN Network communications failure,' will be received. This is because the amplifier reset before responding to the gateway amplifier. This error can be safely ignored in this circumstance.
        '''
        # ----- PROTECTED REGION ID(CopleyControl.ResetMotor) ENABLED START -----#
        self.write('{} r\n'.format(str(self.NodeId)))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.ResetMotor
# --------------------------------WriteRead--------------------------------

    def WriteRead(self, argin):
        '''
        writes a command to the serial line and gets the result of this command from the amplifier.
            port_id: Serial Port ID
            argin: Wait To Command(ACSII)
        # 这里还需要完善，当端口不可用的时候，强行调用会出问题
        '''
        argout = ''
        # ----- PROTECTED REGION ID(CopleyControl.WriteRead) ENABLED START -----#
        raw_result = ''
        # print 'In ', self.dev_serial.port, '::WriteRead()', str(argin)
        # self.dev_serial.port = self.SerialPortID
        # start_time = time.clock()
        # time.sleep(0.1)
        # while (time.clock() - start_time) < 1:
        # # 判断驱动器是否上电，则输出结果
        #     raw_result = dev.ReadLine()
        #     if len(raw_result) > 0:
        #         pass
        #     else:
        #         # print('No power')
        #         return 'No power'
        #     break
        self.dev_serial.write(argin)
        raw_result = self.dev_serial.read_until('\r')
        if (raw_result[-1] == '\r' or raw_result[-1] == '\n'):
            argout = raw_result[0:-1]
        # ----- PROTECTED REGION END -----#	//	CopleyControl.WriteRead
        return argout
# --------------------------------MoveHome/Limit--------------------------------

    def MoveToCwLimit(self):
        ''' 
        moves the motor until the CW limit is reached (positive step direction). Software limits are ignored. StopMove works.
        '''
        argout = 0
        # ----- PROTECTED REGION ID(CopleyControl.MoveToCwLimit) ENABLED START -----#
        limitStatus = self.checkLimit()
        if limitStatus != 1:
            self.getValue(str(self.NodeId) + ' s r0xc2 516')  # 设置归位方法：Hard Stop - Positive
            self.getValue(str(self.NodeId) + ' t 2')  # 启动归位序列
        else:
            print('Check Device State please.')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.MoveToCwLimit
        return argout

    def MoveToCcwLimit(self):
        '''
        moves the motor until the CcW limit is reached (negative step direction). Software limits are ignored. StopMove works.
        '''
        argout = 0
        # ----- PROTECTED REGION ID(CopleyControl.MoveToCcwLimit) ENABLED START -----#
        limitStatus = self.checkLimit()
        if limitStatus != 2:
            self.getValue(str(self.NodeId) + ' s r0xc2 532')  # 设置归位方法：Hard Stop - Negative
            self.getValue(str(self.NodeId) + ' t 2')  # 启动归位序列
        else:
            print('Check Device State please.')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.MoveToCcwLimit
        return argout
    # ? 这个方法，没有人调用，所以在此处进行了更改，仿照上面checkLimit进行更改，但是先进行了注释后续调试再说
    # write_HomingMethod()
    # 感觉这个方法应该也是在GUI中设置的，需要调整 # 那么，上面那个需要修改吗
    # 可能需要用到checkHomeStatus、setHomeParameters、setHomeMethod这三个方法

    def MoveHome(self):
        ''' 
        executes the homing procedure.
        '''
        # homeStatus = self.checkHomeStatus()
        # if homeStatus != 1:
        #     # self.debug_stream('In MoveHome()')
        # else:
        #     pass

        # self.debug_stream('In MoveHome()')
        argout = ''
        # ----- PROTECTED REGION ID(CopleyControl.MoveHome) ENABLED START -----#
        argout = self.getValue(str(self.NodeId) + ' t 2')
        # ----- PROTECTED REGION END -----#	//	CopleyControl.MoveHome
        return argout

# $ --------------------------------Move--------------------------------
    def MovePostion(self):
        ''' 
            triggers the motor to move.
            # Trajectory Generator Position Command(0xca). Units: Counts.
            # This value gives destination position for absolute moves or move distance for relative moves.
            # Commanded Position(0x2d_R*). Units: counts. 
            # Note: 
                # 将参数设定放置在调用函数那里，这样，执行`self.Move()`时候，就不会反复调用`( '0x24', int(self.DesiredState))`
                # `0x24`设定会让电机先停止一下，不满足应用情况。同理，其他地方也要取消掉
            这里和`def write_Position():`有重复，考虑合并
        '''
        # ----- PROTECTED REGION ID(CopleyControl.Move) ENABLED START -----#
        # 1.Relative move
        if int(self.ProfileType) == 256 or int(self.ProfileType) == 257:
            if self.attr_SetPoint_read == 0:
                print('The expected position is achieved.')
            elif int(self.attr_SoftwareCwLimit_read) == 0.0 and int(self.attr_SoftwareCcwLimit_read) == 0.0:
                print('NO software limits are set.')
                # self.setMoveParameters() # MovePostion(self)_Note
                command_move = str(self.NodeId) + ' t 1\r'
                self.getValue(str(command_move))
                self.attr_SetPoint_read = 0
            else:
                status = str(self.dev_status())
                current_position = self.getValue(str(self.NodeId) + ' g r0x2d\r')
                # Commanded Position(0x2d_R*). Units: counts.
                self.targetPosition = int(current_position) + int(self.attr_SetPoint_read)
                # 首先判断驱动器的状态是否可用，则设定参数，开始执行
                if status == 'Status is STANDBY' or status == 'Positive limit switch Active' or status == 'Negative limit switch Active':
                    if self.targetPosition >= int(self.attr_SoftwareCcwLimit_read) and self.targetPosition <= int(self.attr_SoftwareCwLimit_read):
                        print('The expected position position ', self.targetPosition, ' is among the range from ', int(self.attr_SoftwareCcwLimit_read), ' to ', int(self.attr_SoftwareCwLimit_read))
                        # self.setMoveParameters() # MovePostion(self)_Note
                        command_move = str(self.NodeId) + ' t 1\r'
                        self.getValue(str(command_move))
                        self.attr_SetPoint_read = 0
                    else:
                        print('The expected position ', self.targetPosition, ' is not among the range from ', int(self.attr_SoftwareCcwLimit_read), ' to ', int(self.attr_SoftwareCwLimit_read))
                else:
                    print('Check Device State please.')
        # 2.Absolute move
        elif int(self.ProfileType) == 0 or int(self.ProfileType) == 1:
            # Software limits are only in effect after drive has been referenced
            if int(self.attr_SoftwareCcwLimit_read) == 0.0 and int(self.attr_SoftwareCwLimit_read) == 0.0:
                print('NO software limits are set.')
                # self.setMoveParameters() # MovePostion(self)_Note
                command_move = str(self.NodeId) + ' t 1\r'
                self.getValue(str(command_move))
                self.attr_SetPoint_read = 0
            else:
                status = str(self.dev_status())
                current_position = self.getValue(str(self.NodeId) + ' g r0x2d\r')
                # Commanded Position(0x2d_R*). Units: counts.
                self.targetPosition = int(current_position) + int(self.attr_SetPoint_read)
                # 首先判断驱动器的状态是否可用，则设定参数，开始执行
                if status == 'Status is STANDBY' or status == 'Positive limit switch Active' or status == 'Negative limit switch Active':
                    if self.targetPosition >= int(self.attr_SoftwareCcwLimit_read) and self.targetPosition <= int(self.attr_SoftwareCwLimit_read):
                        print('The expected position position ', self.targetPosition, ' is among the range from ', int(self.attr_SoftwareCcwLimit_read), ' to ', int(self.attr_SoftwareCwLimit_read))
                        # self.setMoveParameters() # MovePostion(self)_Note
                        command_move = str(self.NodeId) + ' t 1\r'
                        self.getValue(str(command_move))
                        self.attr_SetPoint_read = 0
                    else:
                        print('The expected position ', self.targetPosition, ' is not among the range from ', int(self.attr_SoftwareCcwLimit_read), ' to ', int(self.attr_SoftwareCwLimit_read))
                else:
                    print('Check Device State please.')
        # 3.Velocity move.
        elif int(self.ProfileType) == 2:
            # self.setMoveParameters() # MovePostion(self)_Note
            # command_pos = self.setParameterCommand( '0xca', direction)
            # self.getValue(str(command_pos))
            command_move = str(self.NodeId) + ' t 1\r'
            self.getValue(str(command_move))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.Move
    # ----- PROTECTED REGION ID(CopleyControl.programmer_methods) ENABLED START -----#
# --------------------------------Initial--------------------------------

    def connectSerial(self, serialPort=defaultPortID, baud=defaultBaud, timeout=defaultTimeout):
        # def connectSerial(self,serialPort=defaultPortID,baud=defaultBaud,timeout=defaultTimeout):
        '''
            Connects with the pyserial device and make the pyserial state be open.
        '''
        self.dev_serial = serial.Serial()
        self.dev_serial.port = serialPort  # 获取当前usb端口: `python -m serial.tools.list_ports`
        self.dev_serial.timeout = timeout  # 超时设置，None = 永远等待操作；0 = ；立即返回请求结果；Num(其他数值) = 等待时间(s)
    #     self.dev_serial.baudrate=9600 # 波特率, e.g. 9600,19200,38400,57600,115200
    #     # self.dev_serial.parity=PARITY_EVEN,
    #     # self.dev_serial.stopbits=STOPBITS_ONE,
    #     # self.dev_serial.bytesize=SEVENBITS, # 该处会使编码发生变化，需要注释
    #     # self.dev_serial.xonxoff=0 # 软件流控
    #     self.dev_serial.open()
    #     self.dev_serial.write('r \r')
    #     time.sleep(5)
    #     self.changeSerialSpeed(baud)
    #     # 这个单独写一个方法用来保持端口状态打开的，利用下面的状态方法来判断
    #         # try:
    #         #     dev = PyTango.DeviceProxy(self.ConnectedDeviceName)
    #         #     if dev.State() == PyTango.DevState.OFF:
    #         #         dev.Open()
    #         #         return dev
    #         #     elif dev.State() == PyTango.DevState.ON:
    #         #         return dev
    #         #     else:
    #         #         print('Device State of pyserial Unknown')
    #         # except:
    #         #     print('An exception with connecting the pyserial device occurred.')
    # def changeSerialSpeed(self,baud):
    #     # Serial Port Baud Rate. Units: bits/s.
    #     # 这一类指令也要单独做r0x90
    #     commandString='s r0x90'+' '+str(baud) + '\r'
    #     self.dev_serial.write(commandString)
    #     self.dev_serial.close()
        self.dev_serial.baudrate = baud
    #     time.sleep(2)
        # ? 这里需要设置一下容错，如果串口出现问题，要返回错误
        # 结合def WriteRead(self, argin):方法一起改
        # 在初始化的时候，将所有的口都通讯一遍就好，但是上位机还是需要实时显示一下各个口的通讯状况
        self.dev_serial.open()
        # print('Port is open:    ' + str(self.dev_serial.isOpen()))
        # print('Port is readable:' + str(self.dev_serial.readable()))

    def setInitParameters(self):
        '''
            Initial Parameter
            需要完善，除了位置模式外的参数也要初始化，可以考虑添加条件判断
        '''
        # print 'In ', self.dev_serial.port, '::setInitParameters()'
        # dev = self.dev_serial
        # 考虑采用ROS中的YAML配置文件
        # 这里面少位置初始化，即`s r0xca 1\r`，且该数值和ProfileType相关
        command_DesiredState = self.setParameterCommand('0x24', int(self.DesiredState))
        # Desired State(0x24). Bits: 0~42(P19)
        # 所需的状态参数（0x24）定义了驱动器的操作模式和输入源控制。重新设置该数值，电机停止运行，不用执行`t 1`也会停止
        # Value Description
        # 0 驱动器已禁用。
        # 1 电流环路由编程的电流值驱动。
        # 2 电流环路由模拟命令输入驱动。
        # 3 电流环路由PWM和方向输入引脚驱动。
        # 4 电流环路由内部函数发生器驱动。
        # 5 电流回路由UV命令驱动。
        # 6 保留以备将来使用
        # 7 电流命令从动于其他轴
        # 8-10 保留以备将来使用

        # 11 速度环由编程的速度值驱动。
        # 12 速度环由模拟命令输入驱动。
        # 13 速度环由PWM和方向输入引脚驱动。
        # 14 速度环由内部函数发生器驱动。
        # 15-16 保留以备将来使用
        # 17 速度命令已保存到其他轴
        # 18-20 保留以备将来使用

        # 21 伺服模式下，位置环由轨迹发生器驱动。
        # 22 伺服模式下，位置环由模拟命令输入驱动。
        # 23 伺服模式下，位置环由数字输入（脉冲和方向，主编码器等）驱动。
        # 24 伺服模式下，位置环由内部函数发生器驱动。
        # 25 伺服模式下，位置环由凸轮表驱动。
        # 26 Analog reference commands velocity to position loop
        # 27 位置指令从动于另一轴
        # 28-29 Reserved for future use

        # 30 伺服模式下，驱动器由CANopen或EtherCAT接口控制。
        # 31 在微步进模式下，位置环由轨迹生成器驱动。
        # 32 在微步进模式下，位置环由模拟命令输入驱动。
        # 33 微步进模式，位置环由数字输入（脉冲和方向，主编码器等）驱动。
        # 34 微步进模式，位置环由内部函数发生器驱动。
        # 35 微步进模式下，位置环由凸轮工作台驱动。
        # 36 微步进模式下，速度环由模拟命令输入驱动。
        # 37-39 Reserved for future use

        # 40 微步进模式下，驱动器由CANopen或EtherCAT接口控制。
        # 41 Reserved for future use
        # 42 仅用于诊断。 电流环路由编程的电流值驱动，并且相位角微步进。
        command_ProfileType = self.setParameterCommand('0xc8', int(self.ProfileType))
        # Give trajectory profile mode(0xc8).
        # 0 = Absolute move, trapezoidal profile.
        # Trapezoidal profile mode. Uses position/distance, velocity, acceleration and deceleration. Any parameters may be changed during move. Jerk is not used in this mode.
        # 1 = Absolute move, S-curve profile.
        # S-curve profile mode. Uses position/distance, velocity, acceleration, and jerk. No parameters may be changed while move is in progress (although move may be aborted). Acceleration parameter will be used for deceleration.
        # 2 = Velocity move.
        # Velocity mode. Uses velocity, acceleration, and deceleration. Jerk is not used in this mode, and position is only used to define direction of move (zero or positive to move with a positive velocity, negative to move with a negative velocity). Any parameter may be changed during move. Set velocity to zero to stop.
        # 8 = 2^8
        # 256 = If set, relative move, trapezoidal profile.
        # 257 = If clear, relative move, S-curve profile.
        # eg. 's r0xc8 0': 将轨迹生成器设置为绝对移动，梯形轮廓。
        command_Velocity = self.setParameterCommand('0xcb', int(self.attr_Velocity_read))
        # Trajectory Maximum Velocity. Units: 0.1 counts/s.
        # Trajectory generator will attempt to reach this velocity during a move.
        command_Acceleration = self.setParameterCommand('0xcc', int(self.attr_Acceleration_read))
        # Trajectory Maximum Acceleration. Units: 10 counts/s2.
        # Trajectory generator will attempt to reach this acceleration during a move.
        # For s-curve profiles, this value also used to decelerate at end of move.
        command_Deceleration = self.setParameterCommand('0xcd', int(self.attr_Deceleration_read))
        # Trajectory Maximum Deceleration. Units: 10 counts/s2.
        # In trapezoidal trajectory mode, this value used to decelerate at end of move.
        # command = command_DesiredState + command_ProfileType + command_Velocity + command_Acceleration + command_Deceleration
        answer1 = self.getValue(command_DesiredState)
        answer2 = self.getValue(command_ProfileType)
        answer3 = self.getValue(command_Velocity)
        answer4 = self.getValue(command_Acceleration)
        answer5 = self.getValue(command_Deceleration)
        # 判断初始化状态
        if answer1 == answer2 == answer3 == answer4 == answer5 and answer1 == 'ok':
            print 'In ', self.dev_serial.port, '::setInitParameters() OK'
        else:
            print 'In ', self.dev_serial.port, '::setInitParameters() ERROR'
# --------------------------------setHome/Limit--------------------------------

    def checkLimit(self):
        '''
            Check the Hardware limit switches.
        '''
        self.clearLatchedStatus()
        value = self.readLatchedEventStatus()
        if (int(value) & 1536) != 0:
            print('Positive and Negative limit switches are active')
            return 3
        elif (int(value) & 512) != 0:
            print('Positive limit switch is active')
            return 1
        elif (int(value) & 1024) != 0:
            print('Negative limit switch is active')
            return 2
        elif int(value) == 0 or (int(value) & 131072) != 0 or (int(value) & 65536) != 0 or (int(value) & 67108864) != 0:
            print('NO limit switch is active')
            return 0

    def checkHomeStatus(self):
        '''
            Check the Home Switch status.
        '''
        self.clearLatchedStatus()
        value = self.readLatchedEventStatus()
        print('LatchedEventStatus: {}'.format(value))
        if (int(value) & 67108864) != 0:
            print('Home Switch is active.')
            return 1
        else:
            print('Home Switch is not active.')
            return 0

    def setHomeParameters(self, homingMethod):
        '''
            Set the Homing parameters using the input Homing method value
        '''
        command_DesiredState = self.setParameterCommand('0x24', int(self.DesiredState))
        # Desired State(0x24). Bits: 0~42(P19)
        # 所需的状态参数（0x24）定义了驱动器的操作模式和输入源控制。特定于模式的值在本章的其余部分中提到。
        # Value Description
        # 0 驱动器已禁用。
        # 1 电流环路由编程的电流值驱动。
        # 2 电流环路由模拟命令输入驱动。
        # 3 电流环路由PWM和方向输入引脚驱动。
        # 4 电流环路由内部函数发生器驱动。
        # 5 电流回路由UV命令驱动。
        # 6 保留以备将来使用
        # 7 电流命令从动于其他轴
        # 8-10 保留以备将来使用

        # 11 速度环由编程的速度值驱动。
        # 12 速度环由模拟命令输入驱动。
        # 13 速度环由PWM和方向输入引脚驱动。
        # 14 速度环由内部函数发生器驱动。
        # 15-16 保留以备将来使用
        # 17 速度命令已保存到其他轴
        # 18-20 保留以备将来使用

        # 21 伺服模式下，位置环由轨迹发生器驱动。
        # 22 伺服模式下，位置环由模拟命令输入驱动。
        # 23 伺服模式下，位置环由数字输入（脉冲和方向，主编码器等）驱动。
        # 24 伺服模式下，位置环由内部函数发生器驱动。
        # 25 伺服模式下，位置环由凸轮表驱动。
        # 26 Analog reference commands velocity to position loop
        # 27 位置指令从动于另一轴
        # 28-29 Reserved for future use

        # 30 伺服模式下，驱动器由CANopen或EtherCAT接口控制。
        # 31 在微步进模式下，位置环由轨迹生成器驱动。
        # 32 在微步进模式下，位置环由模拟命令输入驱动。
        # 33 微步进模式，位置环由数字输入（脉冲和方向，主编码器等）驱动。
        # 34 微步进模式，位置环由内部函数发生器驱动。
        # 35 微步进模式下，位置环由凸轮工作台驱动。
        # 36 微步进模式下，速度环由模拟命令输入驱动。
        # 37-39 Reserved for future use

        # 40 微步进模式下，驱动器由CANopen或EtherCAT接口控制。
        # 41 Reserved for future use
        # 42 仅用于诊断。 电流环路由编程的电流值驱动，并且相位角微步进。
        # 所需的状态参数定义了驱动器的操作模式和输入源控制。
        command_homingMethod = self.setParameterCommand('0xc2', homingMethod)
        # Homing Method Configuration. Bits: 0~15
        command_FastVelocity = self.setParameterCommand('0xc3', self.attr_Velocity_read)
        # Homing Velocity (fast moves)(0xc3). Units: 0.1 counts/s.
        # This velocity value is used during segments of homing procedure that may be handled at high speed. Generally, this means moves in which home sensor is being located, but edge of sensor is not being found.
        command_SlowVelocity = self.setParameterCommand('0xc4', 3333)
        # Homing Velocity (slow moves)(0xc4). Units: 0.1 counts/s.
        # This velocity value is used for homing segments that require low speed, such as cases where edge of a homing sensor is being sought.
        command_Acceleration = self.setParameterCommand('0xc5', self.attr_Acceleration_read)
        # Homing Acceleration/Deceleration(0xc5). Units: 10 counts/s2.
        # This value defines acceleration used for all homing moves. Same value is used at beginning and ending of moves (i.e. no separate deceleration value).
        command_homeOffset = self.setParameterCommand('0xc6', int(self.attr_HomeOffset_read))
        # Home Offset(0xc6). Units: counts.
        # Home offset is difference between zero position for application and machine home position (found during homing). Once homing is completed, new zero position determined by homing state machine will be located sensor position plus this offset. All subsequent absolute moves shall be taken relative to this new zero position.
        command_CurrentLimit = self.setParameterCommand('0xc7', 19)
        # Homing Current Limit(0xc7). Units: 0.01 A.
        # Used in Home to Hard Stop mode only, this current is used to determine when drive has reached end of travel (hard stop). Used in conjunction with Home to Hard Stop Delay Time (0xBF).
        command_TrajectoryProfileMode = self.setParameterCommand('0xc8', int(self.ProfileType))
        # Give trajectory profile mode(0xc8).
        # 0 = Absolute move, trapezoidal profile.
        # Trapezoidal profile mode. Uses position/distance, velocity, acceleration and deceleration. Any parameters may be changed during move. Jerk is not used in this mode.
        # 1 = Absolute move, S-curve profile.
        # S-curve profile mode. Uses position/distance, velocity, acceleration, and jerk. No parameters may be changed while move is in progress (although move may be aborted). Acceleration parameter will be used for deceleration.
        # 2 = Velocity move.
        # Velocity mode. Uses velocity, acceleration, and deceleration. Jerk is not used in this mode, and position is only used to define direction of move (zero or positive to move with a positive velocity, negative to move with a negative velocity). Any parameter may be changed during move. Set velocity to zero to stop.
        # 8 = 2^8
        # If set, relative move.
        # If clear, relative move.
        # eg. 's r0xc8 0': 将轨迹生成器设置为绝对移动，梯形轮廓。
        command_PositiveSoftwareLimit = self.setParameterCommand('0xb8', self.attr_SoftwareCwLimit_read)
        # Positive Software Limit value(0xb8). Units: counts.
        # This parameter is only available on drives that support trajectory generation and homing. Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). Set to less than negative software limit to disable.
        command_NegativeSoftwareLimit = self.setParameterCommand('0xb9', self.attr_SoftwareCcwLimit_read)
        # Negative Software Limit(0xb9). Units: counts.
        # Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). Set to greater than positive software limit to disable.
        command_Position = self.setParameterCommand('0xca', 0)
        # Trajectory Generator Position Command(0xca). Units: Counts.
        # This value gives destination position for absolute moves or move distance for relative moves.
        command_homing = str(self.NodeId) + ' t 2 '
        # Execute homing. Assumes all homing parameters have been previously set.
        # 执行归位。假设所有原点设置参数均已预先设置。
        # 这个是仿照前面的写得，因为命令没有执行
        # 最后的t 2返回应该是返回给调用的函数，在参数设置完成后，再执行
        answer1 = self.getValue(command_DesiredState)
        answer2 = self.getValue(command_homingMethod)
        answer3 = self.getValue(command_FastVelocity)
        answer4 = self.getValue(command_SlowVelocity)
        answer5 = self.getValue(command_Acceleration)
        answer6 = self.getValue(command_homeOffset)
        answer7 = self.getValue(command_CurrentLimit)
        answer8 = self.getValue(command_TrajectoryProfileMode)
        answer9 = self.getValue(command_PositiveSoftwareLimit)
        answer10 = self.getValue(command_NegativeSoftwareLimit)
        answer11 = self.getValue(command_Position)
        # 判断初始化状态
        if answer1 == answer2 == answer3 == answer4 == answer5 == answer6 == answer7 == answer8 == answer9 == answer10 == answer11 and answer1 == 'ok':
            print 'In ', self.dev_serial.port, '::setInitParameters() OK'
        else:
            print 'In ', self.dev_serial.port, '::setInitParameters() ERROR'
        return command_homing

    def setHomeMethod(self, argin):
        '''
        Set the homeMethod, return the answer
        Homing Method Configuration. Bits: 0~15
            0 如果未设置位5，则仅将当前位置设置为原点。如果设置了位5，则沿由位4指定的方向移动，并将第一个索引脉冲的位置设置为原点。 在该模式下不使用位6。(If bit 5 is not set, then just set current position as home. If bit 5 is set, then move in direction specified by bit 4 and set location of first index pulse as home. Bit 6 not used in this mode.)
            1 沿位4指定的方向移动，直到遇到限位开关。 然后再朝其他方向移动。 如果第5位清零，则边缘位置为原点。 如果设置了位5，则下一个索引脉冲为原点。 在该模式下不使用位6。(If bit 5 is not set, then just set current position as home. If bit 5 is set, then move in direction specified by bit 4 and set location of first index pulse as home. Bit 6 not used in this mode.)
            2 通过恒定的原点开关返回原点。 初始移动沿位4指定的方向进行。遇到回零开关时，方向相反。 如果清除了位5，则将归位开关的边沿设置为归位。 如果设置了位5，则将索引脉冲用作原始位置。 位6用于定义使用哪个索引脉冲。(Home on constant home switch. Initial move is made in direction specified by bit 4. When home switch is encountered, direction is reversed. If bit 5 is clear, edge of home switch is set as home. If bit 5 is set, then an index pulse is used as home position. Bit 6 is used to define which index pulse is used.)
            3 间歇性回零开关上的回零。 此模式与模式2相同，不同之处在于，如果最初搜索原点时遇到限位开关，则方向相反。 在模式2中，在找到家之前碰到限位开关将被视为错误。 位8标识要搜索的房屋边缘（正数或负数）。(Home on intermittent home switch. This mode works same as mode 2 except that if limit switch is encountered when initially searching for home, then direction is reversed. In mode 2, hitting limit switch before finding home would be considered an error. Bit 8 identifies which edge of home to search for (positive or negative).)
            4 硬停的家。 这将按照位4中指定的方向移动，直到达到起始电流极限。 然后，使用该当前值按下硬停止，直到回零延迟时间到期。 如果设置了位5（索引），则从硬停止处驱动，直到找到索引为止。(Home to a hard stop. This moves in the direction specified in bit 4 until home current limit is reached. It then presses against hard stop using that current value until home delay time expires. If bit 5 (index) is set, drive away from the hard stop until an index is found.)
            5-14 Reserved for future
            15 立即回家。 该值使放大器在上电时立即被参考。 编码器初始化后，会将原点偏移值添加到编码器位置，并将结果设置为当前参考位置。 这对于绝对编码器主要有用。(Immediate home. This value causes the amp to be referenced immediately on power-up. Once encoder is initialized, home offset value is added to encoder position and result is set as current referenced position. This is primarily useful with absolute encoders.)

            4 初始移动方向（0 =正，1 =负）。(Initial move direction (0=positive, 1=negative).)
            5 如果置位，则返回索引脉冲。(Home on index pulse if set.)
            6 选择要使用的索引脉冲。 如果已设置，请在传感器边缘的DIR侧使用脉冲。 DIR是该字的位4指定的方向。(Selects which index pulse to use. If set, use pulse on DIR side of sensor edge. DIR is direction specified by bit 4 of this word.)
            7 如果设置，则捕获索引的下降沿。 如果清除，则捕获上升沿。(If set, capture falling edge of index. If clear, capture rising edge.)
            8 当使用瞬时原位开关时，该位标识参考的原位开关的哪个边沿。 如果设置，请使用负边缘。如果清晰，请使用正边缘。(When using momentary home switch, this bit identifies which edge of home switch to reference on. If set, use negative edge. If clear, use positive edge.)
            9 如果设置了该位，则在归位完成后移至零位置。如果清除，则找到零位置，但未移至零位置。(If set, move to zero position when homing is finished. If clear, zero position is found, but not moved to.)
            10 如果设置，则原点复归序列将正常运行，但是在原点复归结束时不会调整实际位置。 请注意，即使未调整实际位置，也将使用原应进行的调整（以计数为单位）更新归位调整（0xB5）。 同样，如果设置了位10，则无论位9的设置如何，都不会移至零。(If set, homing sequence will run as normal, but actual position will not be adjusted at end of homing. Note that even though actual position is not adjusted, Homing Adjustment (0xB5) is updated with size of adjustment (in counts) that would have been made. Also, if bit 10 is set then no move to zero is made regardless of setting of bit 9.)
            11 如果设置了该位，则在归零例程结束时，将存储在Flash中的归零配置设置为15，并且将存储在Flash中的归零偏移量更新为基于最新归零操作校准绝对编码器所需的正确值。 该位用于自动校准绝对值编码器。(If this bit is set, at end of home routine home configuration stored in flash will be set to 15, and home offset stored in flash will be updated to correct value necessary to calibrate an absolute encoder based on most recent home operation. This bit is used to automate calibration of absolute encoders.)
        '''
        # Homing Method Configuration.(0xc2_RF)
        # Set Current Position as Home
        # N/A 512
        # Next Index
        # Positive 544
        # Negative 560
        # Limit Switch
        # Positive 513
        # Negative 529
        # Limit Switch Out to Index
        # Positive 545
        # Negative 561
        # Home Switch
        # Positive 514
        # Negative 530
        # Home Switch Out to Index
        # Positive 546
        # Negative 562
        # Home Switch In to Index
        # Positive 610
        # Negative 626
        # Hard Stop
        # Positive 516
        # Negative 532
        # Hard Stop Out to Index
        # Positive 548
        # Negative 564
        # Lower Home
        # Positive 771
        # Negative 787
        # Upper Home
        # Positive 515
        # Negative 531
        # Lower Home Outside Index
        # Positive 803
        # Negative 819
        # Lower Home Inside Index
        # Positive 867
        # Negative 883
        # Upper Home Outside Index
        # Positive 547
        # Negative 563
        # Upper Home Inside Index
        # Positive 611
        # Negative 627
        # Immediate Home
        # N/A 15
        ans = self.getValue(str(self.NodeId) + ' s r0xc2 ' + str(int(argin)))
        if int(argin) == 512:  # Set Current Position as Home
            print('The current position is the home position.')
        elif int(argin) in [514, 530]:  # Home Switch
            print('Home Switch method is chosen to be Homing method.')
        elif int(argin) == 513:  # Limit Switch Positive
            print('Positive Limit Switch method is chosen to be Homing method.')
        elif int(argin) == 529:  # Limit Switch Negative
            print('Negative Limit Switch method is chosen to be Homing method.')
        elif int(argin) == 516:  # Hard Stop Positive
            print('Positive Hard Stop method is chosen to be Homing method.')
        elif int(argin) == 532:  # Hard Stop Negative
            print('Negative Hard Stop method is chosen to be Homing method.')
        else:
            print('Homing Method is set with Home Method ', argin)
        return ans
# $ --------------------------------Latched Event Status Register--------------------------------
    # Event Status Register(0xa0_R*). Bits: 0~31
        # This command gets the device status (stored in its device_status data member) and returns it to the caller.
        # if the motor is in motion, the Status is 'Status is MOVING';
        # if the motor is stationary, the Status is 'Status is ON';
        # if the motor is out of power, the Status is 'Status is OFF';
        # if the motor reaches the positive hardware limit, the Status is 'Positive limit switch Active';
        # if the motor reaches the negative hardware limit, the Status is 'Negative limit switch Active';
        # Bit-mapped as follows:
        # 0  检测到短路(Short circuit detected)
        # 1  驱动温度(Drive over temperature)
        # 2  过电压(Over voltage)
        # 3  欠压(Under voltage)
        # 4  电机温度传感器激活(Motor temperature sensor active)
        # 5  编码器电源错误(Encoder power error)
        # 6  电机定相误差(Motor phasing error)
        # 7  电流输出限制(Current output limited)[输出电流被I2T Algorithm公式所限制或者一个锁定的电流错误发生。]
        # 8  电压输出限制(Voltage output limited)[电流环正试图使用全部的母线电压去控制电流，一般发生在电机正占用全部的母线电压高速运行。]
        # 9  正限位开关有效(Positive limit switch active)[电机轴已经接触到正限位开关。]
        # 10  负限位开关有效(Negative limit switch active)[电机轴已经接触到负限位开关。]
        # 11  启用输入无效(Enable input not active)
        # 12  驱动器已被软件禁用(Drive is disabled by software)]
        # 13  试图停止电机(Trying to stop motor)[驱动器在速度或位置模式下，已经被去使能。在速度模式下，驱动器正使用“ Fast Stop Ramp”(详见Velocity Loop Limits)；在位置模式下，驱动器正使用"Abort Deceleration rate‘(详见Trajectory Limits)。输出保持有效直到驱动器重新使能。]
        # 14  电机制动器已激活(Motor brake activated)
        # 15  PWM输出禁用(PWM outputs disabled)
        # 16  正软件极限条件(Positive software limit condition)[实际位置已经超出正的软限位设置。请参考Homing.]
        # 17  负软件限制条件(Negative software limit condition)[实际位置已经超出负的软限位设置。请参考Homing]
        # 18  跟随错误故障。 发生跟随错误，驱动器处于跟随错误模式。(Following Error Fault. A following error has occurred, and drive is in following error mode.)[跟随误差已经达到设定的限制值。请参考Following Error Faults]
        # 19  以下错误警告。 指示位置误差大于警告后的位置。(Following Error Warning. Indicates position error is greater than position following warning.)[跟随误差已经达到设定的报警值。请参考Following Error Faults]
        # 20  驱动器当前处于重置状态(Drive is currently in reset condition)
        # 21  位置已封装。 位置变量不能无限增加。 达到一定值后，变量回滚。 这种计数方式称为位置换行或模数计数(Position has wrapped. Position variable cannot increase indefinitely. After reaching a certain value the variable rolls back. This type of counting is called position wrapping or modulo count[位置脉冲计数已超过以下范围。(-2^31 – 2^31-1)且已经设置位置包裹。驱动器其他功能不会受到影响。]
        # 22  驱动器故障。 发生配置为在故障掩码（0xA7）中锁存的故障。 可以使用锁存故障状态寄存器（0xA4）清除锁存故障。(Drive fault. Fault configured as latching in Fault Mask (0xA7) has occurred. Latched faults may be cleared using Latching Fault Status Register (0xA4).))
        # 23  已达到速度极限（0x3A）(Velocity limit (0x3A) has been reached)[速度命令 (来自模拟量输入, PWM输入,或位置环) 已经超过了速度限制。请参考Velocity Loop Limits]
        # 24  达到加速限制（0x36）(Acceleration limit (0x36) has been reached)[在速度模式下，电机已经达到速度环中设置的加速度和减速度限制的设定值。]
        # 25  位置跟踪。 位置环错误（0x35）超出跟随错误故障限制（0xBA）。(Position Tracking. Position Loop Error (0x35) is outside of Following Error Fault Limit (0xBA).)[跟随误差已经超过了设定值。请参考Position and Velocity Tracking Windows]
        # 26  归位开关已激活(Home switch is active)[电机轴已经接触到了原点开关。]
        # 27  运动中。 设置轨迹生成器是否正在运行轮廓或跟随错误故障限制（0xBA）在跟踪窗口之外。 当驱动器固定到位时清除。(In motion. Set if trajectory generator is running profile or Following Error Faul Limit (0xBA) is outside tracking window. Clear when drive is settled in position.)[电机正在运行，或他在一次运动后还没有整定结束。在运动结束时，当电机进入位置跟踪轨迹窗口并且保持设定的跟踪时间表示驱动器完成整定。一旦此项有效，它将保持有效直到一个新的运动开始。]
        # 28  速度窗口。 当速度误差大于编程的速度窗口时设置(Velocity window. Set when velocity error is larger than programmed velocity window)[目标速度和实际速度之间的误差超过了这个窗口的设定值。请参考Position and Velocity Tracking Windows]
        # 29  相位尚未初始化。 如果驱动器定相且没有霍尔，则该位置1，直到驱动器初始化其相位。(Phase not yet initialized. If drive is phasing with no Halls, this bit is set until drive has initialized its phase.)[驱动器使用了相位初始化功能，但是相位没能被初始化。]
        # 30  命令故障。 CANopen或EtherCAT主站不发送命令或不存在PWM命令。注意：如果通过设置数字输入命令配置（0xA8）的位3启用了“允许100％输出”选项，此故障将不会检测到丢失的PWM命令。(Command fault. CANopen or EtherCAT master not sending commands or PWM command not present.)[缺少PWM或其他命令信号 (例如EtherCAT主站)。如果在将“Digital InputCommand Configuration” Bit 3值为激活100%输出选项，驱动器将不会再检测PWM命令丢失，该错误不会出现。]
        # 31  保留。(Reserved.)
        # Note: If Allow 100% Output option is enabled by setting Bit 3 of Digital Input Command Configuration (0xA8) this fault will not detect missing PWM command.
        # 锁定和非锁定错误：
        # 只有当错误条件被修复后并且以下至少一项被执行时，一个锁定的错误才可被清除。
        #      驱动器重新上电
        #      通过输入点重新使能(去使能然后使能) ，该输入点须被配置为使能并清除错误(Enable with Clear Faults)或重启后使能(Enable with Reset)
        #      打开控制面板并点击清除错误(Clear Faults)或重启(Reset)
        #      通过CANopen网络或者串口总线清除错误。
        # 非锁定错误会在错误条件去掉后自动清除，不需要任何人为介入。
        # 非锁定错误时电机异动的风险：
        # 当一个非锁定错误的原因被纠正后，在不需要人为介入的情况下，驱动器重新使能PWM输出级。在这种情况下，运动可能意外地重新开始。请配置错误为锁定错误类型，除非非锁定行为有对应的具体应对措施。当配置非锁定错误时，确保对未知运动有相应的保护措施。忽视这个警告可能会造成设备损毁，人员伤亡。
        # 举例：
        # 驱动器的温度到达了错误限制范围。驱动器报错并断掉了PWM输出。然后，驱动器的温度又恢复到正常的工作范围。以下是两种不同的配置方式。
        # 非锁定错误操作：
        #     若该错误没有被锁定，驱动器的错误将被自动清除并且PWM输出被恢复。
        # 锁定错误操作：
        #     若该错误被锁定了，错误仍然是有效的并且PWM输出也仍然无效，除非按照上述说明清除错误。
        # Latched Event Status Register(0xa1).
        # This is latched version of Event Status Register (0xA0). Bits are set by drive when events occur. Bits are only cleared by writing to this parameter as explained below: When writing to Latched Event Status Register, any bit set will cause corresponding bit in register to be cleared.
        # For example, to clear over voltage bit, write decimal 4 or 0x4 to register. To clear all bits, write 0xffffffff to register
        # f(15)变成二进制：1111，则 0xffffffff = 1111 1111 1111 1111 1111 1111 1111 1111 (8个F的二进制形式, 一个F占4个字节 ) 
        # 0x代表16进制，后面是数字，十进制是4294967295

    def readLatchedEventStatus(self):
        '''
            return the latched event status
        '''
        command = self.getParameterCommand('0xa1')
        LatchedEventStatus = self.getValue(command)
        return int(LatchedEventStatus)

    def clearLatchedStatus(self):
        '''
            Clear the latched status
        '''
        command_Latched = self.getParameterCommand('0xa1')
        value_Latched = self.getValue(command_Latched)
        command_setLatched = self.setParameterCommand('0xa1', value_Latched)
        value_setLatched = self.getValue(command_setLatched)
        return str('In ' + self.dev_serial.port + '::clearLatchedStatus()' + value_setLatched)

    def readFaultRegisterStatus(self):
        '''
            return the latched fault register status
        '''
        command = self.getParameterCommand('0xa4')
        LatchedFaultStatus = self.getValue(command)
        return int(LatchedFaultStatus)

    def clearFaultRegister(self):
        '''
            Clear Latched Fault Register(0xa4)
        '''
        command_Fault = self.getParameterCommand('0xa4')
        value_Fault = self.getValue(command_Fault)
        command_setFault = self.setParameterCommand('0xa4', value_Fault)
        value_setFault = self.getValue(command_setFault)
        return str('In ' + self.dev_serial.port + '::clearFaultRegister()' + value_setFault)
# $ --------------------------------formatCommand--------------------------------

    def setParameterCommand(self, command, data):
        ''' 
            Return the Set Command with nodeID, command and data for copley control.
        '''
        return '{} s r{} {}\n'.format(str(int(self.NodeId)), command, str(int(data)))

    def getParameterCommand(self, command):
        '''
            Return the Get Command with nodeID, command for copley control.
        '''
        return '{} g r{}\n'.format(str(int(self.NodeId)), command)

    def handshake(self, reply):
        '''
            Check the reply to confirm whether the command is sent successfully or not.
        '''
        if reply == 'No power' or 'ok' or reply[0:1] == 'e' or reply[0:1] == 'v ':
            return True
        else:
            return False

    def getValue(self, command):
        '''
            Get the mathematical value of the answer after sending the command.
        '''
        reply = self.WriteRead(command)
        if self.handshake(reply):
            if reply[0:1] == 'v':
                argout = str(reply[2:])
                return argout
            else:
                return reply
        else:
            print 'In ', self.dev_serial.port, '::handshake() ERROR'

    def write(self, command):
        '''
            Write command to the serial line.
            这个还有点问题
        '''
        # print 'In ', self.dev_serial.port, '::write()'
        self.dev_serial.close()
        self.dev_serial.open()
        self.dev_serial.write(command)
        # 这里想写成一个循环，这样就可以发送组合命令了，但是感觉有点麻烦
        # i = 0
        # if num!=0:
        #     while command[0:i]!='\r':
        #         i = i+1
        #         # dev.write(command[])
        #     else:
        #         print(command[0:i])
# $ --------------------------------setModel--------------------------------

    def setMovePara(self):
        ''' 
            Sets Programmed Position Mode, Trajectory Profile Mode, position, velocity, acceleration, deceleration.
            # 在位置模式下更新轨迹参数
                当驱动器进入位置模式时，轨迹参数（速度，加速度和减速度）将复制到轨迹生成器中。 要在驱动器处于位置模式后更改它们中的任何一个，请将新值发送至适当的参数，然后发送t 1命令以启动轨迹更新。
            # 编程位置模式
                在编程位置模式下，轴移动到通过串行接口发送到驱动器的目标位置。 目标位置可以是相对于当前位置的绝对位置或相对位置。可以将使用的运动曲线设置为梯形或S曲线。要开始移动，请首先设置适当的参数，然后发送轨迹命令t 1以开始移动。使用梯形轮廓时，可以在移动过程中更改移动参数。同样，首先设置适当的参数，然后发送另一个t 1命令。收到t 1命令后，目标位置，绝对/相对，速度，加速度和减速度将被更新。以这种方式，可以改变进行中的移动。无法以这种方式更新S曲线轮廓。要中止正在进行的移动，请发送t 0命令。这将使用中止减速率停止正在进行的移动。 驱动器将保持启用状态。可以使用特殊的速度模式通过梯形轮廓的速度，加速度和减速度来移动轴，但没有特定的目标位置。通过在位置命令参数中输入“ 1”或“ -1”来设置运动方向。一旦开始，移动将继续进行，直到速度参数设置为零并发送t 1命令或发送t 0中止命令。
            # Parameter ID    Bank    Description
                0x24                    R F         所需状态：21 = 编程位置模式，伺服
                                                                                31 = 编程位置模式，步进
                0xc8                    R F         Profile type:0 = 绝对移动，梯形轮廓。 1 = 绝对移动，S曲线轮廓。
                                                                                256 = 相对移动，梯形轮廓. 257 = 相对移动，S曲线轮廓。 2 = 速度移动。
                0xca                    R F         位置命令。 单位：计数。
                                                                                相对移动=移动距离. 绝对移动=移动的目标位置。
                                                                                正向运动速度= 1，负向运动速度-1。
                0xcb                    R F         最大速度。 单位：0.1个计数/秒。
                0xcc                    R F          最大加速度。 单位：10个计数/秒2。
                0xcd                    R F         最大减速度。 单位：10个计数/秒2。
                0xce                    R F         最大跳动率。 单位：100个计数/秒3。
                0xcf                     R F         中止减速率。 单位：10个计数/秒2。
                # 位置环参数
                0x32                    R*          Motor position. Units: counts.
                0x17                    R            Load position. Units: counts.
                0x35                    R*          Following Error. Units: counts.
                # 来自轨迹发生器的位置环输入
                0x3d                    R*          Commanded position. Units: counts.
                0x2d                    R            Limited position. Units: counts.
                0x3B                    R*          Profile velocity. Units: 0.1 counts/second.
                0x3C                    R*          Profile acceleration. Units: 10 counts/second2.
                [注意]：1）梯形轮廓中未使用最大加速度率。
                               2）在S曲线轮廓中，注意最大减速度。最大加速度用于加速和减速。
        '''
        print 'In ', self.dev_serial.port, '::setMoveParameters()'
        command_state = self.setParameterCommand('0x24', int(self.DesiredState))
        # Desired State(0x24). Bits: 0~42(P19)
        # 所需的状态参数（0x24）定义了驱动器的操作模式和输入源控制。特定于模式的值在本章的其余部分中提到。
        # Value Description
        # 0 驱动器已禁用。
        # 1 电流环路由编程的电流值驱动。
        # 2 电流环路由模拟命令输入驱动。
        # 3 电流环路由PWM和方向输入引脚驱动。
        # 4 电流环路由内部函数发生器驱动。
        # 5 电流回路由UV命令驱动。
        # 6 保留以备将来使用
        # 7 电流命令从动于其他轴
        # 8-10 保留以备将来使用

        # 11 速度环由编程的速度值驱动。
        # 12 速度环由模拟命令输入驱动。
        # 13 速度环由PWM和方向输入引脚驱动。
        # 14 速度环由内部函数发生器驱动。
        # 15-16 保留以备将来使用
        # 17 速度命令已保存到其他轴
        # 18-20 保留以备将来使用

        # 21 伺服模式下，位置环由轨迹发生器驱动。
        # 22 伺服模式下，位置环由模拟命令输入驱动。
        # 23 伺服模式下，位置环由数字输入（脉冲和方向，主编码器等）驱动。
        # 24 伺服模式下，位置环由内部函数发生器驱动。
        # 25 伺服模式下，位置环由凸轮表驱动。
        # 26 Analog reference commands velocity to position loop
        # 27 位置指令从动于另一轴
        # 28-29 Reserved for future use

        # 30 伺服模式下，驱动器由CANopen或EtherCAT接口控制。
        # 31 在微步进模式下，位置环由轨迹生成器驱动。
        # 32 在微步进模式下，位置环由模拟命令输入驱动。
        # 33 微步进模式，位置环由数字输入（脉冲和方向，主编码器等）驱动。
        # 34 微步进模式，位置环由内部函数发生器驱动。
        # 35 微步进模式下，位置环由凸轮工作台驱动。
        # 36 微步进模式下，速度环由模拟命令输入驱动。
        # 37-39 Reserved for future use

        # 40 微步进模式下，驱动器由CANopen或EtherCAT接口控制。
        # 41 Reserved for future use
        # 42 仅用于诊断。 电流环路由编程的电流值驱动，并且相位角微步进。
        # 所需的状态参数定义了驱动器的操作模式和输入源控制。
        command_profile = self.setParameterCommand('0xc8', int(self.ProfileType))
        # Give trajectory profile mode(0xc8).
        # 0 / 0 0000 0000 = Absolute move, trapezoidal profile.
        # Trapezoidal profile mode. Uses position/distance, velocity, acceleration and deceleration. Any parameters may be changed during move. Jerk is not used in this mode.
        # 1 / 0 0000 0001 = Absolute move, S-curve profile.
        # S-curve profile mode. Uses position/distance, velocity, acceleration, and jerk. No parameters may be changed while move is in progress (although move may be aborted). Acceleration parameter will be used for deceleration.
        # 2 / 0 0000 0010 = Velocity move.
        # Velocity mode. Uses velocity, acceleration, and deceleration. Jerk is not used in this mode, and position is only used to define direction of move (zero or positive to move with a positive velocity, negative to move with a negative velocity). Any parameter may be changed during move. Set velocity to zero to stop.
        # 8 /1 0000 0000 = 2^8
        # 256 = If set, relative move, trapezoidal profile.
        # 257 = If clear, relative move, S-curve profile.
        command_pos = self.setParameterCommand('0xca', int(self.attr_SetPoint_read))
        # command_pos = self.write_SetPoint(int(self.attr_SetPoint_read))
        # Trajectory Generator Position Command(0xca). Units: Counts.
        # This value gives destination position for absolute moves or move distance for relative moves.
        # Relative = Move distance.
        # Absolute = Target position.
        # Velocity Direction: 1 for positive, -1 for negative.
        command_vel = self.setParameterCommand('0xcb', int(self.attr_Velocity_read))
        # command_vel = self.write_Velocity(int(self.attr_Velocity_read))
        # Trajectory Maximum Velocity. Units: 0.1 counts/s.
        # Trajectory generator will attempt to reach this velocity during a move.
        command_acc = self.setParameterCommand('0xcc', int(self.attr_Acceleration_read))
        # Trajectory Maximum Acceleration. Units: 10 counts/s2.
        # Trajectory generator will attempt to reach this acceleration during a move.
        # For s-curve profiles, this value also used to decelerate at end of move.
        command_dec = self.setParameterCommand('0xcd', int(self.attr_Deceleration_read))
        # Trajectory Maximum Deceleration. Units: 10 counts/s2.
        # In trapezoidal trajectory mode, this value used to decelerate at end of move.
        # command = command_state + command_profile + command_vel + command_acc + command_dec + command_pos
        # self.write(command)
        self.getValue(command_state)
        self.getValue(command_profile)
        self.getValue(command_pos)
        self.getValue(command_vel)
        self.getValue(command_acc)
        self.getValue(command_dec)

    def setSpeedPara(self):
        ''' 
            Sets Programmed Speed Mode
            # 编程速度模式将驱动器的输出设置为编程速度。 在此模式下启用驱动器后，或更改了编程速度时，电动机速度将以编程速度升至新的水平。
            # Parameter ID    Bank    Description
                0x24                   R F       所需状态：编程速度模式（11）
                0x2f                    R F       Programmed velocity command. Units: 0.1 counts/second.
                0x36                   R F       Velocity acceleration limit. Units: 1000 counts/second2
                0x37                   R F       Velocity deceleration limit. Units: 1000 counts/second2
                0x39                   R F       Fast stop ramp. Units: 1000 counts/second2
        '''
        print 'In ', self.dev_serial.port, '::setSpeedParameters()'
        # `self.DesiredState`该参数不直接设置为11，因为除了该参数，还有其余参数，可能有多种模式，比如`self.ProfileType`有几个模式
        # 所以采用在调用方先设置好这几个参数，然后再调用def setSpeedPara()方法，这样也整洁一些。在对应的函数说明里面都说明了需要哪些参数以及作用
        command_state = self.setParameterCommand('0x24', int(self.DesiredState))
        # Desired State(0x24). Bits: 0~42(P19)
        # 所需的状态参数（0x24）定义了驱动器的操作模式和输入源控制。特定于模式的值在本章的其余部分中提到。
        # Value Description
        # 0 驱动器已禁用。
        # 1 电流环路由编程的电流值驱动。
        # 2 电流环路由模拟命令输入驱动。
        # 3 电流环路由PWM和方向输入引脚驱动。
        # 4 电流环路由内部函数发生器驱动。
        # 5 电流回路由UV命令驱动。
        # 6 保留以备将来使用
        # 7 电流命令从动于其他轴
        # 8-10 保留以备将来使用

        # 11 速度环由编程的速度值驱动。
        # 12 速度环由模拟命令输入驱动。
        # 13 速度环由PWM和方向输入引脚驱动。
        # 14 速度环由内部函数发生器驱动。
        # 15-16 保留以备将来使用
        # 17 速度命令已保存到其他轴
        # 18-20 保留以备将来使用

        # 21 伺服模式下，位置环由轨迹发生器驱动。
        # 22 伺服模式下，位置环由模拟命令输入驱动。
        # 23 伺服模式下，位置环由数字输入（脉冲和方向，主编码器等）驱动。
        # 24 伺服模式下，位置环由内部函数发生器驱动。
        # 25 伺服模式下，位置环由凸轮表驱动。
        # 26 Analog reference commands velocity to position loop
        # 27 位置指令从动于另一轴
        # 28-29 Reserved for future use

        # 30 伺服模式下，驱动器由CANopen或EtherCAT接口控制。
        # 31 在微步进模式下，位置环由轨迹生成器驱动。
        # 32 在微步进模式下，位置环由模拟命令输入驱动。
        # 33 微步进模式，位置环由数字输入（脉冲和方向，主编码器等）驱动。
        # 34 微步进模式，位置环由内部函数发生器驱动。
        # 35 微步进模式下，位置环由凸轮工作台驱动。
        # 36 微步进模式下，速度环由模拟命令输入驱动。
        # 37-39 Reserved for future use

        # 40 微步进模式下，驱动器由CANopen或EtherCAT接口控制。
        # 41 Reserved for future use
        # 42 仅用于诊断。 电流环路由编程的电流值驱动，并且相位角微步进。
        # 所需的状态参数定义了驱动器的操作模式和输入源控制。
        command_vel = self.setParameterCommand('0x2f', int(self.attr_Velocity_read))
        # Programmed velocity command. Units: 0.1 counts/second.
        command_acc = self.setParameterCommand('0x36', int(self.attr_Acceleration_read))
        # Velocity acceleration limit. Units: 1000 counts/second2
        command_dec = self.setParameterCommand('0x37', int(self.attr_Deceleration_read))
        # Velocity deceleration limit. Units: 1000 counts/second2
        # command = command_state + command_acc + command_dec + command_pos
        # self.write(command)
        self.getValue(command_state)
        self.getValue(command_vel)
        self.getValue(command_acc)
        self.getValue(command_dec)

    def setTorquePara(self):
        ''' 
            Sets Programmed Torque Mode
        '''
        print 'In ', self.dev_serial.port, '::setTorqueParameters()'
        command_state = self.setParameterCommand('0x24', int(self.DesiredState))
        # Desired State(0x24). Bits: 0~42(P19)
        # 所需的状态参数（0x24）定义了驱动器的操作模式和输入源控制。特定于模式的值在本章的其余部分中提到。
        # Value Description
        # 0 驱动器已禁用。
        # 1 电流环路由编程的电流值驱动。
        # 2 电流环路由模拟命令输入驱动。
        # 3 电流环路由PWM和方向输入引脚驱动。
        # 4 电流环路由内部函数发生器驱动。
        # 5 电流回路由UV命令驱动。
        # 6 保留以备将来使用
        # 7 电流命令从动于其他轴
        # 8-10 保留以备将来使用

        # 11 速度环由编程的速度值驱动。
        # 12 速度环由模拟命令输入驱动。
        # 13 速度环由PWM和方向输入引脚驱动。
        # 14 速度环由内部函数发生器驱动。
        # 15-16 保留以备将来使用
        # 17 速度命令已保存到其他轴
        # 18-20 保留以备将来使用

        # 21 伺服模式下，位置环由轨迹发生器驱动。
        # 22 伺服模式下，位置环由模拟命令输入驱动。
        # 23 伺服模式下，位置环由数字输入（脉冲和方向，主编码器等）驱动。
        # 24 伺服模式下，位置环由内部函数发生器驱动。
        # 25 伺服模式下，位置环由凸轮表驱动。
        # 26 Analog reference commands velocity to position loop
        # 27 位置指令从动于另一轴
        # 28-29 Reserved for future use

        # 30 伺服模式下，驱动器由CANopen或EtherCAT接口控制。
        # 31 在微步进模式下，位置环由轨迹生成器驱动。
        # 32 在微步进模式下，位置环由模拟命令输入驱动。
        # 33 微步进模式，位置环由数字输入（脉冲和方向，主编码器等）驱动。
        # 34 微步进模式，位置环由内部函数发生器驱动。
        # 35 微步进模式下，位置环由凸轮工作台驱动。
        # 36 微步进模式下，速度环由模拟命令输入驱动。
        # 37-39 Reserved for future use

        # 40 微步进模式下，驱动器由CANopen或EtherCAT接口控制。
        # 41 Reserved for future use
        # 42 仅用于诊断。 电流环路由编程的电流值驱动，并且相位角微步进。
        # 所需的状态参数定义了驱动器的操作模式和输入源控制。
        command_profile = self.setParameterCommand('0xc8', int(self.ProfileType))
        # Give trajectory profile mode(0xc8).
        # 0 / 0 0000 0000 = Absolute move, trapezoidal profile.
        # Trapezoidal profile mode. Uses position/distance, velocity, acceleration and deceleration. Any parameters may be changed during move. Jerk is not used in this mode.
        # 1 / 0 0000 0001 = Absolute move, S-curve profile.
        # S-curve profile mode. Uses position/distance, velocity, acceleration, and jerk. No parameters may be changed while move is in progress (although move may be aborted). Acceleration parameter will be used for deceleration.
        # 2 / 0 0000 0010 = Velocity move.
        # Velocity mode. Uses velocity, acceleration, and deceleration. Jerk is not used in this mode, and position is only used to define direction of move (zero or positive to move with a positive velocity, negative to move with a negative velocity). Any parameter may be changed during move. Set velocity to zero to stop.
        # 8 /1 0000 0000 = 2^8
        # 256 = If set, relative move, trapezoidal profile.
        # 257 = If clear, relative move, S-curve profile.
        command_pos = self.setParameterCommand('0xca', int(self.attr_SetPoint_read))
        # command_pos = self.write_SetPoint(int(self.attr_SetPoint_read))
        # Trajectory Generator Position Command(0xca). Units: Counts.
        # This value gives destination position for absolute moves or move distance for relative moves.
        # Relative = Move distance.
        # Absolute = Target position.
        # Velocity Direction: 1 for positive, -1 for negative.
        command_vel = self.setParameterCommand('0xcb', int(self.attr_Velocity_read))
        # command_vel = self.write_Velocity(int(self.attr_Velocity_read))
        # Trajectory Maximum Velocity. Units: 0.1 counts/s.
        # Trajectory generator will attempt to reach this velocity during a move.
        command_acc = self.setParameterCommand('0xcc', int(self.attr_Acceleration_read))
        # Trajectory Maximum Acceleration. Units: 10 counts/s2.
        # Trajectory generator will attempt to reach this acceleration during a move.
        # For s-curve profiles, this value also used to decelerate at end of move.
        command_dec = self.setParameterCommand('0xcd', int(self.attr_Deceleration_read))
        # Trajectory Maximum Deceleration. Units: 10 counts/s2.
        # In trapezoidal trajectory mode, this value used to decelerate at end of move.
        # command = command_state + command_profile + command_vel + command_acc + command_dec + command_pos
        # self.write(command)
        self.getValue(command_state)
        self.getValue(command_profile)
        self.getValue(command_pos)
        self.getValue(command_vel)
        self.getValue(command_acc)
        self.getValue(command_dec)
    # ----- PROTECTED REGION END -----#	//	CopleyControl.programmer_methods


# %% 这个应该不用，需要把整个程序改动
def main():
    # try:
    # py = PyTango.Util(sys.argv) # Utilities(https://pytango.readthedocs.io/en/stable/utilities.html)
    # py.add_class(CopleyControlClass, 'CopleyControl')
    #     #----- PROTECTED REGION ID(CopleyControl.add_classes) ENABLED START -----#

    #     #----- PROTECTED REGION END -----#	//	CopleyControl.add_classes
    #     U = PyTango.Util.instance()
    #     U.server_init()
    #     U.server_run()
    # except PyTango.DevFailed as e:
    #     print ('-------> Received a DevFailed exception:', e)
    # except Exception as e:
    #     print ('-------> An unforeseen exception occured....', e)
    print('==')


# %%
if __name__ == '__main__':
    main()
