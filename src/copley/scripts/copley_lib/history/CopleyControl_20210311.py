#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    # 20210306
        1. 这里面的状态信息，返回给ros，记录的ros日志中
        2. 除了GUI还要加入键盘控制，不仅仅是手柄
    # 20201119
        [Task]:
        1. 加入IMU
        2. 加入功率计
        3. 使用Location的ROS包
        4. 使用UUV
        5. 添加QT界面
        6. 增强程序的容错性：端口故障
        [Issue]:
    # 20201119
        [Task]:
        1. 推拉机构以及钩刺机构的调试
        2. 加入力矩模式
        [Issue]:
        因为不是绝对编码器，也没有限位开关所以对于机器人启动时候的初始状态不能判断，即硬件上不能进行初始化；
        考虑两种方法：1. 手柄进行微调；2. 使用日志文件进行复位以及初始化，但是这个需要考验电机的精度，担心多次启动后，会出现误差的累计；所以这个是不是需要和手动微调进行结合
        另外，在程序上不能和主驱动电机一样，停止的时候，直接发送0指令就可以了；对于两个辅助机构需要进行复位，即关机的时候进行
        但是有个问题，推拉机构的减速比是23:1，就是说可以直接手动调整；钩刺机构的减速比是128:1，这个不能手动调整的。如果可以手动调整，会对日志文件中保留的定位信息冲突；
        另外一种方法，对于推拉机构来说，可以不进行日志文件的记录，让机构收缩到平行位置，并继续运动，这样会碰触一些零件，此时电流会加大，检测到电流突然变大的时候，就认为是初始位置了；
    # 20201118
        [Task]:
        1. 固定树莓派端口号
        2. 添加算法接口代码
        3. 调试其余4台电机
        [Issue]:
        ！: 端口号的固定，采用默认的接法就可以，至少暂时每次重启后端口号都能对应上；上面的先通电吧
        √: 添加算法接口代码，主要是的逻辑和MotorClass等一样，在主函数中进行初始化，可以使用ROS的动态参数配置进行动态调整参数，将该参数传递至算法类中；并且在算法接口代码中添加了开关量，可以选择关闭或启用该算法，可以方便切换不同的算法；
        √: 在变量的命名方式上，py文件采用首字母大写并添加下划线的方式，且下划线后的字母同样大写；定义的类名，采用首字母大写，没有下划线的方式；在主函数中导入包定义别名的时候，采用首字母大写尽可能使用一个单词的方式进行区分；在调用创建对象所拥有的属性时候采用首字母大写添加下划线的方式；在函数内部进行定义变量的时候，尽可能的采用全部小写字母以及下划线的方式；
            总的原则是，在主函数内部，外部导入的内容需要至少首字母大写，包的别名需要尽可能简洁，所以不使用下划线；创建类的属性时候，为了方便和其他类的属性区分，所以可以使用下划线，因为名字会变长；
    # 20201117
        [Task]:
        1. 初步加入速度模式
            后面考虑加入一个手柄按键用于切换模式，考虑用一个按键循环切换还是用多个按键进行定义
        2. 解决默认端口问题
        3. 固定树莓派的端口号
        [Issue]:
        √: 新增MotorClass用于解决默认端口的问题，之前的默认端口出现问题就是因为没有初始化，所以才会初始化后即使再修改默认端口号也正常驱动两个电机了；这里新增的MotorClass()在ROS中调用的时候，初始化6个，分别对应6个电机就好了，其实不新增这个类也是可以的，只是为了主函数更简洁。
        √: 新增MotorClass()之后，出现了一个问题，在调用实时速度的时候出现了问题，查看返回结果，发现返回值不是数值而是ok，后来发现需要清除一下缓存数据；同时修改了def WriteRead()以及def write()这两个函数，增加`self.dev_serial.flushInput()`，可以丢弃接收缓存中的所有数据；相比在def write()函数中`# self.dev_serial.close()# self.dev_serial.open()`这两句应该更好一些，不知道会不会减少代码运行时间，因为打开再关闭端口，应该比清空缓存更慢一些吧。
            不行，后面又测试了一下，在主函数中延迟一段时间可以获取正常的速度值，但是取消延迟时间就不行了，暂时还不清楚；还是采用关闭再打开端口吧，并且flushInput、flushOutput这两个函数并没有值，打印输出都是None
        √: 增加def is_number(self, s)用于判断读取的是否是数值
        ！: 对def read_Velocity(self):等函数进行改动，修改!=0为.isdigit()检测字符串是否只由数字组成；如果是数字那么更新数值，如果不是，那么只用上次的数值；后面需要测试一下，这个不是数字的有多大的概率；
        ×: 后面考虑将单位转换的拿两句话合并为一个函数进行调用
    # 20201112
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
    # 20201111
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
    # 20201001
        已经可以接入ROS进行调试，但是当前只是第一个电机，需要将`NodeID`替换成`PortID`进行调用
        在此声明，之后要是从串口改成CAN的时候，继续使用该版本作为辅助参考
'''

# %% doc
__all__ = ['CopleyControlClass'] # 可用于模块导入时限制，只有__all__内指定的属性、方法、类可被导入
__docformat__ = 'restructuredtext' # 允许诸如 epydoc之类的python文档生成器工具知道如何正确解析模块文档

# %% import
# import tango as PyTango
import time
import serial
# import sys
# import os
# Add additional import
#----- PROTECTED REGION ID(CopleyControl.additionnal_import) ENABLED START -----#
from copley.scripts.copley_lib.ParamDict_EventStatus import BitsMapped as BitsMapped_ES
from copley.scripts.copley_lib.ParamDict_HomingMethod import HomingMethod as BitsMapped_HM
# [issue]:
# 考虑将下面的类拆分成不同的.py，再通过包的形式导入进来
# 这样的话，每个模式都是拆分出去，这样就不用每次都if了，而且每个模式有什么属性也都分明了
#----- PROTECTED REGION END -----#	//	CopleyControl.additionnal_import

# %% Constant
# -------- Add Global Variables Here ------------
#----- PROTECTED REGION ID(CopleyControl.global_variables) ENABLED START -----#
from copley.scripts.copley_lib.Constant_Unit import *
from copley.scripts.copley_lib.Constant_Serial import *
#----- PROTECTED REGION END -----#	//	CopleyControl.global_variables

# -------- Device States Description ------------
# MOVING : Moving
# ON : Device On
# FAULT : Amp is faulted and must be reset.
# ALARM : There is an alarm raised.
# INIT : The amp is initialising.

# %% Class
class InitialParametersClass(object):
    '''
        initial the devide ports info.\n

        :@param PortID->(str): serial port id.\n
        :@param NodeID->(int): canopen node ID.\n
        :@param Mode->(str): sets programmed mode.\n
    '''
    def __init__(self, PortID='/dev/ttyUSB0', NodeID=0, Mode='Position'):
        #----- PROTECTED REGION ID(CopleyControl.__init__) ENABLED START -----#
        if isinstance(PortID,str):
            self.PortID = PortID
        else:
            print('NodeID is not string: {}'.format(PortID))
        try:
            self.NodeID = str(int(NodeID))
        except Exception:
            print('NodeID is not number: {}'.format(NodeID))

        if isinstance(Mode,str) and (Mode=='Position' or Mode=='Speed' or Mode=='Current'):
            self.Mode = Mode
        else:
            print('NodeID is not defined string(Position, Speed, Current): {}'.format(Mode))
        #----- PROTECTED REGION END -----#	//	CopleyControl.__init__

class InitialDeviceClass(InitialParametersClass):
    '''
        Initial with the pyserial device.\n

        :@def connectSerial: connect the device with the default parameters.\n
        :@def changeSerialSpeed: change the baudrate to specified num.\n
        :@def is_number: confirm the input is number when set attributes.\n
        :@def print_log: debug, output the device info and time.\n
    '''
    def connectSerial(self, baud=defaultBaud, timeout=defaultTimeout):
        '''
            Connects with the pyserial device and make the pyserial state be open.
        '''
        #----- PROTECTED REGION ID(InitialDeviceClass.connectSerial) ENABLED START -----#
        self.dev_serial=serial.Serial()
        self.dev_serial.port=self.PortID # 获取当前usb端口: `python -m serial.tools.list_ports`
        self.dev_serial.baudrate=baud # serial port baud rate: 9600, 115200
        self.dev_serial.timeout=timeout # 超时设置，None = 永远等待操作；0 = ；立即返回请求结果；Num(其他数值) = 等待时间(s)
        # self.dev_serial.parity=PARITY_EVEN,
        # self.dev_serial.stopbits=STOPBITS_ONE,
        # self.dev_serial.bytesize=SEVENBITS, # 该处会使编码发生变化，需要注释
        # self.dev_serial.xonxoff=0 # 软件流控
        self.dev_serial.open()
        # [issue]:
        # 有些参数需要重置，比如编码器位置，如果不是断电重启的话，是不会复位的；
        # 但是如果是在运行途中系统问题，仅仅需要重启系统，而且不方便调整机械机构的话，就不能要这行代码，不然编码器的位置会被清除
        # 可以折中，使用日志文件的方式来记录，最后时刻的位置
        # [issue]:
        # 这个需要，有的时候，长时间不用会无法连接，但是可以发送这个指令
        # self.dev_serial.write('{} r\n'.format(self.NodeID))
        # time.sleep(5)
        if self.dev_serial.isOpen() and self.dev_serial.readable():
            print('Serial Port is OK.{}'.format(self.print_log('full_msg')))
        else:
            print('Serial Port is ERROR.{}'.format(self.print_log('full_msg')))
        #----- PROTECTED REGION END -----#	//	CopleyControl.connectSerial
    def changeSerialSpeed(self, baud=highBaud):
        '''
            change the serial port baud rate
        '''
        #----- PROTECTED REGION ID(InitialDeviceClass.changeSerialSpeed) ENABLED START -----#
        cmd_string='{} s r0x90 {}\n'.format(self.NodeID, baud) # serial port baud rate. Units: bits/s.
        self.dev_serial.write(cmd_string)
        self.dev_serial.close()
        self.dev_serial.baudrate=baud
        time.sleep(2)
        self.dev_serial.open()
        if self.dev_serial.isOpen() and self.dev_serial.readable():
            print('Successful change the port baud rate: {}'.format(self.dev_serial.baudrate))
        else:
            print('Failure change the port baud rate: {}'.format(self.dev_serial.baudrate))
        #----- PROTECTED REGION END -----#	//	CopleyControl.changeSerialSpeed
    def openSerialPort(self):
        '''
            # open serial port and catch exceptions
            # 在这里使用try捕获异常来取代close方法，是因为避免出现两个实例同时调用一个端口，但是有一个实例正在写入，而另一个端口突然将其关闭的情况；\n
            # self.dev_serial.close()\n
            # self.dev_serial.open()\n
        '''
        #----- PROTECTED REGION ID(InitialDeviceClass.openSerialPort) ENABLED START -----#
        try:
            self.dev_serial.open()
        except Exception as result:
            # print('{}{}'.format(result, self.print_log()))
            pass # not need print
        # flushInput = self.dev_serial.flushInput() # 丢弃接收缓存中的所有数据
        # flushOutput = self.dev_serial.flushOutput() # 终止当前写操作，并丢弃发送缓存中的数据。
        #----- PROTECTED REGION END -----#	//	CopleyControl.openSerialPort
    def is_number(self, num):
        '''
            str.isdigit()
        '''
        #----- PROTECTED REGION ID(InitialDeviceClass.is_number) ENABLED START -----#
        try:
            float(num)
            return True
        except ValueError:
            print('Input is not numbers: {}'.format(num))
        return False
        #----- PROTECTED REGION END -----#	//	CopleyControl.is_number
    def print_log(self, log='time_msg'):
        '''
            print('Serial Port is OK{}'.format(self.print_log('time_msg')))
        '''
        #----- PROTECTED REGION ID(InitialDeviceClass.print_log) ENABLED START -----#
        if log=='full_msg':
            msg = '\n\t- PortID: {}\n\t- NodeID: {}\n\t- Buad: {}\n\t- Timeout: {}\n\t- Time: {}'.format(self.dev_serial.port, self.NodeID, self.dev_serial.baudrate, self.dev_serial.timeout, time.asctime())
        elif log=='time_msg':
            msg = '\n\t- PortID: {}\n\t- NodeID: {}\n\t- Time: {}'.format(self.dev_serial.port, self.NodeID, time.asctime())
        else:
            msg = '\n\t- PortID: {}'.format(self.dev_serial.port)            
        return msg
        #----- PROTECTED REGION END -----#	//	CopleyControl.print_log
    def debug_stream(self, *msg):
        '''
            output debug info
            [issue]:
            有待完善
        '''
        #----- PROTECTED REGION ID(InitialDeviceClass.debug_stream) ENABLED START -----#
        strs = ''
        for target_tuple in reversed(msg):
            strs = str(target_tuple) + '\t' + strs
        print(strs+'{}'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	CopleyControl.debug_stream
    def is_int(self, input, output=0):
        """
            若read方法中为attribute值，则在write方法中不能使用is_int直接将返回值给attribute
        """
        try:
            result = int(input)
        except Exception:
            if output=='No Power':
                result = output
            else:
                # 这行可以避免在单位转换的时候出现float小数
                result = int(output)
                print('The value: {} is not number, and return is {}.{}'.format(input, output, self.print_log('time_msg')))
        return result

class FormatCmdClass(InitialDeviceClass,InitialParametersClass):
    '''
        :@def write: write command to the serial line.\n
        :@def WriteRead: writes a command to the serial line and gets the result of this command from the amplifier.\n
        :@def handShake: check the reply to confirm whether the command is sent successfully or not.\n
        :@def setParamCmd: Return the Set Command with NodeID, command and data for copley control.\n
        :@def getParamCmd: Return the Get Command with NodeID, command for copley control.\n
        :@def getValue: Get the mathematical value of the answer after sending the command.\n

        format command: [node ID][<.>axis letter] [command code] [command parameters] <CR>
        [node ID]: 
            # (Optional), the CANopen node ID of a drive on a multi-drop network (See Multi-Drop Network Connections). The node ID is followed by a space, unless an axis letter is specified. The valid range is 1-127.
            # 对于单轴的RS-232串行总线控制，请将该轴的CAN节点地址设置为零(0)。 若在加电后将CAN节点地址切换为零，则必须重置驱动器或重启电源，以使新的地址设置生效。
        [<.>axis letter]:
            # Optional, the axis letter for multi-axis drives (BE2, SP4, etc.). Axes are specified by a single letter and must be preceded by a period. Valid axis letters start at “A” and continue sequentially. For example, the SP4 is a four axis drive with valid axis letters of A, B, C, D.
        [command code]: 
            # The command code is a single-letter code for the command.
        [command specific parameters]:
            # Command specific parameters are used to provide additional data for a command. If more than one parameter is required, they should be separated by spaces. The remaining sections of this chapter describe the parameters for each command code.
        <CR>: 
            # A carriage return is used to indicate the end of the command to the drive.
    '''
    def write(self, cmd):
        '''
            write command to the serial line.\n
        '''
        #----- PROTECTED REGION ID(FormatCmdClass.write) ENABLED START -----#
        #print('In ', self.dev_serial.port, '::write()')
        self.openSerialPort()
        self.dev_serial.write(cmd)
        #----- PROTECTED REGION END -----#	//	FormatCmdClass.write
    def WriteRead(self, argin):
        '''
            writes a command to the serial line and gets the result of this command from the amplifier.\n
            :@param port_id: serial port id\n
            :@param argin: wait to command(acsii)\n
        '''
        argout = ''
        #----- PROTECTED REGION ID(FormatCmdClass.WriteRead) ENABLED START -----#
        raw_result = ''
        # print 'In ', self.dev_serial.port, '::WriteRead()', str(argin)
        self.openSerialPort()
        self.dev_serial.write(argin)
        raw_result = self.dev_serial.read_until('\r')
        # self.debug_stream(argin, raw_result)
        # [issue]: IndexError: string index out of range
        # 如果返回值为空
        if (raw_result[-1]=='\r' or raw_result[-1]=='\n'):
            argout = raw_result[0:-1]
        #----- PROTECTED REGION END -----#	//	FormatCmdClass.WriteRead
        return argout
    def handShake(self, reply):
        '''
            Check the reply to confirm whether the command is sent successfully or not.\n
        '''
        #----- PROTECTED REGION ID(FormatCmdClass.handShake) ENABLED START -----#
        if reply == 'No power' or 'ok' or reply[0:1] == 'e' or reply[0:1] == 'v ':
            return True
        else:
            return False
        #----- PROTECTED REGION END -----#	//	FormatCmdClass.handShake
    def setParamCmd(self, ascii, data=0):
        ''' 
            Return the Set Command with NodeID, command and data for copley control.\n
        '''
        #----- PROTECTED REGION ID(FormatCmdClass.setParamCmd) ENABLED START -----#
        try:
            data = int(data)
            if ascii[:2]=='0x':
                cmd = '{} s r{} {}\n'.format(self.NodeID, ascii, data)
            elif ascii=='t':
                cmd = '{} {} {}\n'.format(self.NodeID, ascii, data)
            elif ascii=='r':
                cmd = '{} {}\n'.format(self.NodeID, ascii)
            else:
                cmd = 'command error.\nformat command: [node ID][<.>axis letter] [cmd code] [cmd parameters] <CR>'
        except Exception:
            print('the input value is not numbers.{}'.format(self.print_log('time_msg')))
        return cmd
        #----- PROTECTED REGION END -----#	//	FormatCmdClass.setParamCmd
    def getParamCmd(self, cmd):
        '''
            Return the Get Command with NodeID, command for copley control.\n
        '''
        #----- PROTECTED REGION ID(FormatCmdClass.getParamCmd) ENABLED START -----#
        return '{} g r{}\n'.format(self.NodeID, cmd)
        #----- PROTECTED REGION END -----#	//	FormatCmdClass.getParamCmd
    def setValue(self, result, new, old):
        '''
            Set the mathematical value of the answer to the attribute after sending the command.\n
            主要针对读取方法为属性类的参数，这样省了一步
        '''
        #----- PROTECTED REGION ID(FormatCmdClass.setValue) ENABLED START -----#
        if result[0:-1]=='ok':
            return new
        else:
            print('The result is ERROR: {} is not number, and return old value: {}.{}'.format(result[0:-1], old, self.print_log('time_msg')))
            return old
        #----- PROTECTED REGION END -----#	//	FormatCmdClass.setValue
    def getValue(self, cmd):
        '''
            Get the mathematical value of the answer after sending the command.\n
        '''
        #----- PROTECTED REGION ID(FormatCmdClass.getValue) ENABLED START -----#
        reply = self.WriteRead(cmd)
        if self.handShake(reply):
            if reply[0:1] == 'v':
                argout = str(reply[2:])
                return argout
            else:
                return reply
        else:
            print('Handshake() ERROR.{}'.format(self.print_log('full_msg')))
        # [issue]:
        # 增加一个前缀的e的判断，这个是错误代码，同时修改setvalue()
        #----- PROTECTED REGION END -----#	//	FormatCmdClass.getValue

class CheckEventStateClass(FormatCmdClass):
    '''
        device state
        latched event status register
    '''
    ## ------------------------EventStatusRegister------------------------
    def readEventStatusRegister(self):
        '''
            return the event status register(0xa0_R*)
        '''
        #----- PROTECTED REGION ID(StateRegisteClass.readEventStatusRegister) ENABLED START -----#
        cmd = self.getParamCmd('0xa0')
        value = self.is_int(self.getValue(cmd), 'No Power')
        self.argout = str(value)
        #----- PROTECTED REGION END -----#	//	StateRegisteClass.readEventStatusRegister
        return self.argout
    def readLatchedEventStatus(self):
        '''
            return the latched event status(0xa1)
            This command gets the device status (stored in its device_status data member) and returns it to the caller.

            This is latched version of Event Status Register (0xA0). 
            Bits are set by drive when events occur. Bits are only cleared by writing to this parameter as explained below: When writing to Latched Event Status Register, any bit set will cause corresponding bit in register to be cleared. 
            For example, to clear over voltage bit, write decimal 4 or 0x4 to register. To clear all bits, write 0xffffffff to register.
            
            [Note]:
                f(15)变成二进制：1111，则 0xffffffff = 1111 1111 1111 1111 1111 1111 1111 1111 (8个F的二进制形式, 一个F占4个字节 ) 
                0x代表16进制，后面是数字，十进制是4294967295
        '''
        #----- PROTECTED REGION ID(StateRegisteClass.readLatchedEventStatus) ENABLED START -----#
        cmd = self.getParamCmd('0xa1')
        value = self.is_int(self.getValue(cmd), 'No Power')
        self.argout = str(value)
        #----- PROTECTED REGION END -----#	//	StateRegisteClass.readLatchedEventStatus
        return self.argout
    def clearLatchedStatus(self):
        '''
            clear the latched status
            0xffffffff = b11111111111111111111111111111111 = o4294967295

            [issue]:
            竟然要先清除这个错误，在清除a1才能全部清除，否则a1的不能清除
            也就是如果a1中的22位有问题，需要先调用这里
        '''
        #----- PROTECTED REGION ID(StateRegisteClass.clearLatchedStatus) ENABLED START -----#
        self.clearFaultRegister()
        cmd_setLatched = self.setParamCmd('0xa1', 4294967295)
        value_setLatched =  self.getValue(cmd_setLatched)
        # [issue]:
        # 在这里需要判断一个返回的数据是什么，是ok还是数字，然后根据返回值，决定是return一个true或者其他；
        # 以此来告诉调用对象，现在的状态，不光是打印一串字符；
        result = 'the latched event status register is {}, and the current status is {}{}'.format(value_setLatched, self.print_log('time_msg'))
        #----- PROTECTED REGION END -----#	//	StateRegisteClass.clearLatchedStatus
        return result
    def readFaultRegisterStatus(self):
        '''
            return the latched fault register status(0xA4)
            
            When latching fault has occurred, the fault bit (bit 22) of Event Status Register (0xA0) is set. 
            Cause of fault can be read from this register. To clear fault condition, write a 1 to associated bit in this register. Events that cause drive to latch fault are programmable. See Fault Mask (0xA7) for details.
        '''
        #----- PROTECTED REGION ID(StateRegisteClass.readFaultRegisterStatus) ENABLED START -----#
        cmd = self.getParamCmd('0xa4')
        value = self.is_int(self.getValue(cmd), 'No Power')
        self.argout = str(value)
        #----- PROTECTED REGION END -----#	//	StateRegisteClass.readFaultRegisterStatus
        return self.argout
    def clearFaultRegister(self):
        '''
            clear latched fault register
            0xffff = b1111111111111111 = o65535
        '''
        #----- PROTECTED REGION ID(StateRegisteClass.clearFaultRegister) ENABLED START -----#
        cmd_setFault = self.setParamCmd('0xa4', 65535)
        value_setFault =  self.getValue(cmd_setFault)
        # [issue]:
        # 在这里需要判断一个返回的数据是什么，是ok还是数字，然后根据返回值，决定是return一个true或者其他；
        # 以此来告诉调用对象，现在的状态，不光是打印一串字符；
        result = 'the latched fault register is {}, and the current status is {}{}'.format(value_setFault, self.print_log('time_msg'))
        #----- PROTECTED REGION END -----#	//	StateRegisteClass.clearFaultRegister
        return result
    ## ------------------------@DevStatus------------------------
    def dev_status(self):
        '''
            This command gets the device status (stored in its device_status data member) and returns it to the caller.
            
            :return: Device status

            if the motor is in motion, the Status is 'Status is MOVING';
            if the motor is stationary, the Status is 'Status is ON';
            if the motor is out of power, the Status is 'Status is OFF';
            if the motor reaches the positive hardware limit, the Status is 'Positive limit switch Active';
            if the motor reaches the negative hardware limit, the Status is 'Negative limit switch Active';

            Event Status Register(0xA0). Bits: 0~31
            obsidian://open?vault=Obsidian&file=UCR%2FCopley%2Fclass%20StateRegisteClass()%2Fclass%20StateRegisteClass()
        '''
        argout = ''
        # self.debug_stream('dev_status()')
        #----- PROTECTED REGION ID(StateRegisteClass.dev_status) ENABLED START -----#
        # write command(0xa0)
        # self.clearLatchedStatus()
        DriveEventStatus = self.readEventStatusRegister() # 0xa0
        if DriveEventStatus=='No Power':
            argout = 'Status is OFF, Power OFF'
        elif DriveEventStatus=='0':
            argout = 'Status is STANDBY'
        elif DriveEventStatus!='0' and str(DriveEventStatus)!='No Power':
            # (value&2^DriveEventStatus) != 0
            argout = BitsMapped_ES('0xA0', DriveEventStatus) # -> list/str
        else:
            argout = 'Status is MOVING'
        self.argout = argout
        #----- PROTECTED REGION END -----#	//	StateRegisteClass.dev_status
        return self.argout
    def dev_fault(self):
        '''
            Fault Register(0xA4). Bits: 0~18
        '''
        argout = ''
        # self.debug_stream('dev_fault()')
        #----- PROTECTED REGION ID(StateRegisteClass.dev_fault) ENABLED START -----#
        DriveFaultRegiater = self.readFaultRegisterStatus()
        if DriveFaultRegiater=='No Power':
            argout = 'Status is OFF, Power OFF'
        elif DriveFaultRegiater=='0':
            argout = 'Status is STANDBY'
        elif DriveFaultRegiater!='0' and str(DriveFaultRegiater)!='No Power':
            # (value&2^DriveEventStatus) != 0
            argout = BitsMapped_ES('0xA4', DriveFaultRegiater) # from copley_lib import
        else:
            argout = 'Status is FAULT'
        self.argout = argout
        #----- PROTECTED REGION END -----#	//	StateRegisteClass.dev_fault
        return self.argout

# %%
class SetModeClass(CheckEventStateClass):
    '''
        set mode, include position, speed, current mode\n
        obsidian://open?vault=Obsidian&file=UCR%2FCopley%2Fclass%20SetModeClass()%2Fclass%20SetModeClass()\n

        CopleyControl read/write attribute methods
        Attributes: 由设备中的名称标识。它具有可以读取的值。某些属性也可以更改（读写属性）。每个属性都有一个众所周知的固定数据类型。

        :def read_Position: 绝对数值，忽略self.ProfileType
        :def write_Position:
        :def read_SetPoint: 相对数值，忽略self.ProfileType
        :def write_SetPoint:
        :def read_DialPosition:
        :def write_DialPosition:
        :def read_Conversion:
        :def write_Conversion:

        :def read_Velocity:
        :def write_Velocity:
        :def read_Acceleration:
        :def write_Acceleration:
        :def read_Deceleration:
        :def write_Deceleration:

        :def read_Current:
        :def write_Current:
        :def read_CurrentRamp:
        :def write_CurrentRamp:
    '''
    ## ------------------------AttrState------------------------
    def read_DesiredState(self): # -> attribute
        '''
            Desired State(0x24). Bits: 0~42(P19).
        '''
        # self.debug_stream('read_DesiredState()')
        #----- PROTECTED REGION ID(RWAttributesClass.read_DesiredState) ENABLED START -----#
        cmd = self.getParamCmd('0x24')
        data =  self.getValue(cmd)
        self.DesiredState = self.is_int(data, self.DesiredState)
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.read_DesiredState
        return self.DesiredState
    def write_DesiredState(self, data): # -> attribute
        '''
            0x24	R F	Desired state:
                                0 = Drive disabled.
                                1 = Programmed current value drives current loop
                             21 = Programmed Position Mode, Servo
                             31 = Programmed Position Mode, Stepper
        '''
        # self.debug_stream('write_DesiredState()')
        #----- PROTECTED REGION ID(RWAttributesClass.write_DesiredState) ENABLED START -----#
        data = self.is_int(data, self.DesiredState)
        cmd = self.setParamCmd('0x24', data)
        result = self.getValue(cmd) # self.write(cmd)

        self.DesiredState = self.setValue(result, data, self.DesiredState)
        return result
        # print('Set Desired State to  ', str(self.DesiredState), 'counts/s.'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.write_DesiredState
    def read_Profile(self): # -> attribute
        '''
            Trajectory Profile Mode. To set profile in CANopen see CAN object 0x6086 in CANopen Programmers Manual.

            0xc8  R F Give trajectory profile mode.
            0 / 0 0000 0000 = Absolute move, trapezoidal profile. 
                Trapezoidal profile mode. Uses position/distance, velocity, acceleration and deceleration. Any parameters may be changed during move. Jerk is not used in this mode.
            1 / 0 0000 0001 = Absolute move, S-curve profile.
                S-curve profile mode. Uses position/distance, velocity, acceleration, and jerk. No parameters may be changed while move is in progress (although move may be aborted). Acceleration parameter will be used for deceleration.
            256 /1 0000 0000 = 2^8
                256 = If set, relative move, trapezoidal profile.
                257 = If clear, relative move, S-curve profile.
            2 / 0 0000 0010 = Velocity move.
                Velocity mode. Uses velocity, acceleration, and deceleration. Jerk is not used in this mode, and position is only used to define direction of move (zero or positive to move with a positive velocity, negative to move with a negative velocity). Any parameter may be changed during move. Set velocity to zero to stop.
        '''
        # self.debug_stream('read_Velocity()')
        #----- PROTECTED REGION ID(RWAttributesClass.read_Profile) ENABLED START -----#
        cmd = self.getParamCmd('0xc8')
        data = self.getValue(cmd)
        self.ProfileType = self.is_int(data, self.ProfileType)
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.read_Profile
        return self.ProfileType
    def write_Profile(self, data): # -> attribute
        '''
            Profile type:
             0 = Absolute move, trapezoidal profile.
             1 = Absolute move, S-curve profile.
             256 = Relative move, trapezoidal profile.
             257 = Relative move, S-curve profile.
             2 = Velocity move.
        '''
        # self.debug_stream('write_Profile()')
        #----- PROTECTED REGION ID(RWAttributesClass.write_Profile) ENABLED START -----#
        data = self.is_int(data, self.ProfileType)
        if self.DesiredState==21: # Programmed Position Mode
            cmd = self.setParamCmd('0xc8', data)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('this is not position mode and the "DesiredState" is {}.{}'.format(self.DesiredState, self.print_log('time_msg')))
            result = 'ERROR'
        self.ProfileType = self.setValue(result, data, self.ProfileType)
        return result
        # print('Set Profile type to  ', str(self.ProfileType), 'counts/s.'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.write_Profile
    ## ------------------------AttrPosition------------------------
    def read_Position(self): # -> actual
        '''
            # read actual position and convert unit to count.

            # 0x17	R	Actual Position. Units: Counts. 
                                # Used to close position loop in drive every servo cycle. 
                                # For single feedback systems, this value is same as Actual Motor Position (0x32). 
                                # For dual feedback systems, this value is same as Load Encoder Position (0x112). 
                                # CANopen objects 0x6064 and 0x6063 hold same value.
            [issue]:
            # 由0x17 -> 0x2d，0x2d在速度模式下是限制位置，位置模式下是实际位置；0x17在速度模式和位置模式下都可以用
            # 换句话说，取消了读取所有的限制值，后面可以考虑再写一些函数专门用来读取限制值
        '''
        # self.debug_stream('read_Position()')
        #----- PROTECTED REGION ID(RWAttributesClass.Position_read) ENABLED START -----#   
        cmd = self.getParamCmd('0x17')
        data = self.getValue(cmd)
        self.attr_Position_read = self.is_int(data, self.attr_Position_read)
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Position_read
        return self.attr_Position_read
    def write_Position(self, data): # -> order
        '''
            # absolute move

            # 0xca	R F	Trajectory Generator Position Command. Units: Counts.
                                # This value gives destination position for absolute moves or move distance for relative moves. 
                                # Relative move = the distance of the move.
                                # Absolute move = the target position of the move.
                                # Velocity move = 1 for positive direction,
                                #                               -1 for negative direction.
            [issue]: 需要设置软限位；这个已经在home中设置了，回头再看看
            0xb8
            0xb9
        '''
        # self.debug_stream('write_Position()')
        #----- PROTECTED REGION ID(RWAttributesClass.Position_write) ENABLED START -----#
        self.targetPosition = self.is_int(data, self.targetPosition)
        # set attr_SetPoint_read
        self.attr_Position_read = self.read_Position()
        if self.ProfileType==256 or self.ProfileType==257: # relative move
            self.attr_SetPoint_read = self.targetPosition - int(self.attr_Position_read)
        elif self.ProfileType==0 or self.ProfileType==1: # absolute move
            self.attr_SetPoint_read = self.targetPosition
        # write attr_SetPoint_read to command
        # [issue]:
        # 在使用这个软件限制之前，是不是应该先读取一下
        if self.attr_SoftwareCwLimit_read==0 and self.attr_SoftwareCcwLimit_read==0:
            print('Software Limits are not set.{}'.format(self.print_log('time_msg')))
            cmd = self.setParamCmd('0xca', self.attr_SetPoint_read)
            result = self.getValue(cmd) # self.write(cmd)
        elif self.targetPosition in range(self.attr_SoftwareCcwLimit_read, self.attr_SoftwareCwLimit_read):
            cmd = self.setParamCmd('0xca', self.attr_SetPoint_read)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('The input is out of the valid range, check the software limits.{}'.format(self.print_log('time_msg')))
            result = 'ERROR'
        return result
        #----- PROTECTED REGION END -----#	//	CopleyControl.Position_write
    def read_SetPoint(self): # -> attribute
        # self.debug_stream('In read_SetPoint()')
        #----- PROTECTED REGION ID(CopleyControl.SetPoint_read) ENABLED START -----#

        #----- PROTECTED REGION END -----#	//	CopleyControl.SetPoint_read
        return self.attr_SetPoint_read
    def write_SetPoint(self, data): # -> order
        '''
            # relative move

            # 0xca	R F	Trajectory Generator Position Command. Units: Counts.
                                # This value gives destination position for absolute moves or move distance for relative moves. 
                                # Relative move = the distance of the move.
                                # Absolute move = the target position of the move.
                                # Velocity move = 1 for positive direction,
                                #                               -1 for negative direction.
            [issue]: 需要设置软限位
            0xb8
            0xb9
        '''
        # self.debug_stream('write_SetPoint()')
        #----- PROTECTED REGION ID(CopleyControl.SetPoint_write) ENABLED START -----#
        data = self.is_int(data, self.attr_SetPoint_read)
        # set targetPosition
        self.attr_Position_read = self.read_Position()
        if self.ProfileType==256 or self.ProfileType==257:
            self.targetPosition = data + self.attr_Position_read
        elif self.ProfileType==0 or self.ProfileType==1:
            self.targetPosition = data
        # write attr_SetPoint_read to command
        if self.attr_SoftwareCwLimit_read==0 and self.attr_SoftwareCcwLimit_read==0:
            print('Software Limits are not set.{}'.format(self.print_log('time_msg')))
            cmd = self.setParamCmd('0xca', data)
            result = self.getValue(cmd) # self.write(cmd)
        elif self.targetPosition in range(self.attr_SoftwareCcwLimit_read, self.attr_SoftwareCwLimit_read):
            # print('SetPoint:', data, 'expected position: ', self.targetPosition, 'Ccwlimit: ', self.attr_SoftwareCcwLimit_read, 'Cwlimit: ', self.attr_SoftwareCwLimit_read)
            cmd = self.setParamCmd('0xca', data)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('The input is out of range of the software limits.{}'.format(self.print_log('time_msg')))
            result = 'ERROR'
        self.attr_SetPoint_read = self.setValue(result, data, self.attr_SetPoint_read)
        return result
        #----- PROTECTED REGION END -----#	//	CopleyControl.SetPoint_write
    def read_DialPosition(self): # -> actual
        '''
        # Limited position. Units: counts.(0x2d_R*).
        # the dial position 
        '''
        # self.debug_stream('read_DialPosition()')
        #----- PROTECTED REGION ID(CopleyControl.DialPosition_read) ENABLED START -----#
        self.attr_Position_read = self.read_Position()
        self.attr_DialPosition_read = float(self.attr_Position_read) / float(self.attr_Conversion_read)
        return self.attr_DialPosition_read
        #----- PROTECTED REGION END -----#	//	CopleyControl.DialPosition_read
    def write_DialPosition(self, data): # -> order
        '''
            # Trajectory Generator Position Command(0xca). Units: Counts.
            # This value gives destination position for absolute moves or move distance for relative moves.
        '''
        # self.debug_stream('write_DialPosition()')
        data = self.is_int(data, self.targetPosition)
        #----- PROTECTED REGION ID(CopleyControl.DialPosition_write) ENABLED START -----#
        # [issue]: is_int
        self.targetPosition = float(self.attr_Conversion_read) * data
        data_new = (data - self.attr_DialPosition_read) * float(self.attr_Conversion_read) 
        self.attr_SetPoint_read = (data - self.attr_DialPosition_read) * float(self.attr_Conversion_read) 
        if self.targetPosition in range(int(self.attr_SoftwareCcwLimit_read), int(self.attr_SoftwareCwLimit_read)):
            cmd = self.setParamCmd('0xca', data_new)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('DialPosition is out of range.{}'.format(self.print_log('time_msg')))
            result = 'ERROR'
        return result
        #----- PROTECTED REGION END -----#	//	CopleyControl.DialPosition_write
    ## ------------------------AttrConversion------------------------
    def read_Conversion(self): # -> attribute
        '''
            The ratio between the position and the dial position. The default value is 1.0
        '''
        # self.debug_stream('In read_Conversion()')
        #----- PROTECTED REGION ID(RWAttributesClass.Conversion_read) ENABLED START -----#
        print('In ', self.dev_serial.port, '::read_Conversion()')
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Conversion_read
    def write_Conversion(self, data): # -> attribute
        '''
            The ratio between the position and the dial position. The default value is 1.0
        '''
        # self.debug_stream('In write_Conversion()')
        #----- PROTECTED REGION ID(RWAttributesClass.Conversion_write) ENABLED START -----#
        # [issue]: 应该有一个ascii
        self.attr_Conversion_read = data
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Conversion_write
    ## ------------------------AttrVelocity------------------------
    def read_Velocity(self): # -> actual
        '''
            # read actual velocity and convert unit to counts/s, so data=data*unit
            # This variable(0x18) differentiates between positive and negative

            # 0x18  R*   Actual Velocity. Units: 0.1 encoder counts/s.
                                # For estimated velocity. Units: 0.01 RPM.
                                # For stepper mode: Units: 0.1 microsteps/s.

            这里将0xcb -> 0x18，即读取实际的速度值且有符号，区别于0xcb读取的是设定的最大速度数值（是位置模式下的命令）
        '''
        # self.debug_stream('read_Velocity()')
        #----- PROTECTED REGION ID(RWAttributesClass.Velocity_read) ENABLED START -----#
        cmd = self.getParamCmd('0x18')
        data = self.is_int(self.getValue(cmd), self.attr_Velocity_read)
        self.attr_Velocity_read = data * unit_0x18
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Velocity_read
        return self.attr_Velocity_read
    def write_Velocity(self, data): # -> order
        '''
            # write the target velocity value to the amplifire. 
            # include position & speed mode.

            # Programmed Position Mode(21)
                0xcb    R F Trajectory Maximum Velocity. Units: 0.1 counts/s.
                                    Trajectory generator will attempt to reach this velocity during a move.
            # Programmed Speed Mode(11)
                0x2f    R F Programmed Velocity Command(0x2f). Units: 0.1 encoder counts/s.
                                    Only used in Programmed Velocity Mode (Desired State (0x24) = 11)
                                    For estimated velocity. Units: 0.01 RPM.
                                    For stepper mode. Units: 0.1 microsteps/s.
        '''
        # [issue]:
        # 有些属性没有电流模式，应该是需要修改的
        # 但是电流模式感觉啥都没法控制
        # self.debug_stream('write_Velocity()')
        data = self.is_int(data, self.attr_Velocity_read)
        #----- PROTECTED REGION ID(RWAttributesClass.Velocity_write) ENABLED START -----#
        if self.DesiredState==21: # Programmed Position Mode
            # [issue]
            # 将单位设置为全局变量
            velocity = data / unit_0xcb
            cmd = self.setParamCmd('0xcb', velocity)
            result = self.getValue(cmd) # self.write(cmd)
            # [issue]:
            # 需要完善，当设置为速度模式时候，速度的方向是由0xca指定的(1/-1)
        elif self.DesiredState==11: # Programmed Speed Mode
            velocity = data / unit_0x2f
            cmd = self.setParamCmd('0x2f', velocity)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('this is not position/speed mode and the "DesiredState" is {}.{}'.format(self.DesiredState, self.print_log('time_msg')))
            result = 'ERROR'
        return result
        # print('Set maximum(command) velocity to  ', str(velocity), 'counts/s.'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Velocity_write
    ## ------------------------AttrAc/Deceleration------------------------
    def read_Acceleration(self): # -> attribute
        '''
            # Programmed Position Mode
                0xcc    R F Trajectory Maximum Acceleration. Units: 10 counts/s2.
                                   Trajectory generator will attempt to reach this acceleration during a move. 
                                   For s-curve profiles, this value also used to decelerate at end of move.
            # Programmed Speed Mode
                0x36    R F Velocity Loop Acceleration Limit. Units: 1000 counts/s2.
                                    Used by velocity loop limiter.
                                    Not used when velocity loop is controlled by position loop.
            [Note]: 这个设置的也是加速度限制，因为是速度环，能直接控制的是速度，就像位置环能直接控制的是位置，而速度和加速度的说明都是设置最大值；类似于0x18取代0xcb一样，找到可以读取实际加速度的数值
            不过，好像没有，编码器能读取的是位置，做一次差分得到速度值，如果再差一次的话，噪声会比较大；但是既然能设置最大加速度，就应该可以读取实际的加速度值；在CME的上位机中调试电机也是只有位置和速度，没有加速度的数值
        '''
        self.debug_stream('read_Acceleration()')
        #----- PROTECTED REGION ID(RWAttributesClass.Acceleration_read) ENABLED START -----#
        if self.DesiredState==21: # Programmed Position Mode
            cmd = self.getParamCmd('0xcc')
            data = self.is_int(self.getValue(cmd), self.attr_Acceleration_read)
            self.attr_Acceleration_read = data * unit_0xcc
        elif self.DesiredState==11: # Programmed Speed Mode
            cmd = self.getParamCmd('0x36')
            data = self.is_int(self.getValue(cmd), self.attr_Acceleration_read)
            self.attr_Acceleration_read = data * unit_0x36
        # print('Read maximum acceleration: ', str(acceleration), 'counts/s2')
        # conversion = 0.0025
        # realAcceleration = self.attr_Acceleration_read * conversion
        # print('Read motor real maximum acceleration: ', str(realAcceleration), 'counts/s2)')
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Acceleration_read
        return self.attr_Acceleration_read
    def write_Acceleration(self, data): # -> order
        '''
        '''
        # self.debug_stream('write_Acceleration()')
        data = self.is_int(data, self.attr_Acceleration_read)
        #----- PROTECTED REGION ID(RWAttributesClass.Acceleration_write) ENABLED START -----#
        # print 'realAcceleration input is: ', int(data)
        # realAcceleration = int(data)
        # Inverse_conversion = 400
        # self.attr_Acceleration_read = realAcceleration * Inverse_conversion
        if self.DesiredState==21: # Programmed Position Mode
            acceleration = data / unit_0xcc
            cmd = self.setParamCmd('0xcc', acceleration)
            result = self.getValue(cmd) # self.write(cmd)
        elif self.DesiredState==11: # Programmed Speed Mode
            acceleration = data / unit_0x36
            cmd = self.setParamCmd('0x36', acceleration)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('this is not position/speed mode and the "DesiredState" is {}.{}'.format(self.DesiredState, self.print_log('time_msg')))
            result = 'ERROR'
        self.attr_Acceleration_read = self.setValue(result, data, self.attr_Acceleration_read)
        return result
        # print('Set maximum acceleration to  ', str(acc), 'counts/s2.')
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Acceleration_write
    def read_Deceleration(self): # -> attribute
        '''
            # Programmed Position Mode
                0xcd    R F Trajectory Maximum Deceleration. Units: 10 counts/s2. 
                                    In trapezoidal trajectory mode, this value used to decelerate at end of move.
            # Programmed Speed Mode
                0x37    R F Velocity Loop Deceleration Limit. Units: 1000 counts/s2.
                                    Used by velocity loop limiter. 
                                    Not used when velocity loop is controlled by position loop.
        '''
        # self.debug_stream('read_Deceleration()')
        #----- PROTECTED REGION ID(RWAttributesClass.Deceleration_read) ENABLED START -----#
        if self.DesiredState==21: # Programmed Position Mode
            cmd = self.getParamCmd('0xcd')
            data = self.is_int(self.getValue(cmd), self.attr_Deceleration_read)
            self.attr_Deceleration_read = data * unit_0xcd
        elif self.DesiredState==11: # Programmed Speed Mode
            cmd = self.getParamCmd('0x37')
            data = self.is_int(self.getValue(cmd), self.attr_Deceleration_read)
            self.attr_Deceleration_read = data * unit_0x37
        # print('Read maximum deceleration: ', str(self.attr_Deceleration_read),  'counts/(second*second)')
        # conversion = 0.0025
        # realDeceleration = int(self.attr_Deceleration_read)*conversion
        # print('Read motor real maximum deceleration: ', realDeceleration, 'counts/(second*second)')
        # attr.set_value(int(realDeceleration))  
        # attr.set_value(int(self.attr_Deceleration_read))
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Deceleration_read
        return self.attr_Deceleration_read
    def write_Deceleration(self, data): # -> order
        '''
        '''
        # self.debug_stream('write_Deceleration()')
        data = self.is_int(data, self.attr_Deceleration_read)
        #----- PROTECTED REGION ID(RWAttributesClass.Deceleration_write) ENABLED START -----#
        #print('realDeceleration input is: ', int(data))
        #self.attr_Deceleration_read = int(data)*400
        if self.DesiredState==21: # Programmed Position Mode
            deceleration = data / unit_0xcd
            cmd = self.setParamCmd('0xcd', deceleration)
            result = self.getValue(cmd) # self.write(cmd)
        elif self.DesiredState==11: # Programmed Speed Mode
            deceleration = data / unit_0x37
            cmd = self.setParamCmd('0x37', deceleration)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('this is not position/speed mode and the "DesiredState" is {}.{}'.format(self.DesiredState, self.print_log('time_msg')))
            result = 'ERROR'
        self.attr_Deceleration_read = self.setValue(result, data, self.attr_Deceleration_read)
        return result
        # print('Set maximum deceleration to  ', str(deceleration), 'counts/s2.')
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Deceleration_write
    ## ------------------------AttrCurrent------------------------
    def read_Current(self): # ->actural
        '''
            # 0x0b  R*  Actual Current, D axis of rotor space. Units: 0.01 A.
            # 0x0c  R*  Actual Current, Q axis of rotor space. Units: 0.01 A.
                                The d axis, also known as the direct axis, is the axis by which flux is produced by the field winding. The q axis, or the quadrature axis is the axis on which torque is produced.
            #* 0x38    R*  Actual Motor Current. Units: 0.01 A. This current is calculated based on both D and Q axis currents.
            
            # A -> mA
        '''
        self.debug_stream('read_Current()')
        #----- PROTECTED REGION ID(RWAttributesClass.read_Current) ENABLED START -----#
        cmd = self.getParamCmd('0x38')
        data = self.is_int(self.getValue(cmd), self.attr_Current_read)
        self.attr_Current_read = data * unit_0x38 # mA
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.read_Current
        return self.attr_Current_read
    def write_Current(self, data): # -> attribute
        '''
            # 0x02  R F Current loop programmed value. Units: 0.01 A.
                                # This current will be used to command drive when Desired State (0x24) is set to 1.
            
            # 将单位转换成mA
        '''
        # self.debug_stream('write_Current()')
        data = self.is_int(data, self.attr_Current_read)
        #----- PROTECTED REGION ID(RWAttributesClass.Current_write) ENABLED START -----#
        if self.DesiredState==1: # Programmed Current Mode
            current = data / unit_0x02 # mA
            cmd = self.setParamCmd('0x02', current)
            result = self.getValue(cmd) # self.write(cmd)
            self.attr_Current_read = self.setValue(result, data, self.attr_Current_read)
        else:
            print('this is not current mode and the "DesiredState" is {}.{}'.format(self.DesiredState, self.print_log('time_msg')))
            result = 'ERROR'
        return result
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Current_write
    def read_CurrentRamp(self): # ->attribute
        '''
            # 0x6a  R F Commanded Current Ramp Limit. Units: mA/s. 
                                # Used when running in Current (Torque) mode. 
                                # Setting this to zero disables slope limiting.
        '''
        # self.debug_stream('read_CurrentRamp')
        #----- PROTECTED REGION ID(RWAttributesClass.CurrentRamp_read) ENABLED START -----#
        cmd = self.getParamCmd('0x6a')
        data = self.is_int(self.getValue(cmd), self.attr_Current_ramp)
        self.attr_Current_ramp = data * unit_0x6a
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.CurrentRamp_read
        return self.attr_Current_ramp
    def write_CurrentRamp(self, data): # -> attribute
        '''
        '''
        # self.debug_stream('write_CurrentRamp')
        data = self.is_int(data, self.attr_Current_ramp)
        #----- PROTECTED REGION ID(RWAttributesClass.CurrentRamp_write) ENABLED START -----#
        if self.DesiredState==1: # Programmed Current Mode
            ramp = data / unit_0x6a
            cmd = self.setParamCmd('0x6a', ramp)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('this is not current mode and the "DesiredState" is {}.{}'.format(self.DesiredState, self.print_log('time_msg')))
            result = 'ERROR'
        self.attr_Current_ramp = self.setValue(result, data, self.attr_Current_ramp)
        return result
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.CurrentRamp_write
    ## ------------------------@SetMode------------------------
    def setInitParameters(self, profile=1, pos=0, vel=0, acc=100, dec=100, cur=0, rap=0):
        '''
            initial parameters and sent to specified mode.
            [issue]:
            这有一个作用，除了统一进行初始化外，还可以进行模式间的切换。
            例如，当前为速度模式运行，机器人暂时停顿一下(模式切换必要停顿0x24)，若此时设置了位置数值，也就暗示要切换成位置模式
            此时，直接在设置位置数值的下方再添加一句话就行，即调用相应的模式。因为调用模式的函数所传入的参数和初始化的参数是分离的，实际传入的是实时指定的数值。

            位置模式下也有速度模式，但是速度模式下能达到的速度值更大。位置模式下过大的速度会出现位置跟随错误，所以虽然位置模式也有速度模式，但是并不能舍弃速度模式。
        '''
        #----- PROTECTED REGION ID(SetModeClass.setInitParameters) ENABLED START -----#
        if self.Mode == 'Position':
            self.DesiredState = 21
            self.ProfileType = profile
            self.attr_SetPoint_read = pos
            self.attr_Velocity_read = vel
            self.attr_Acceleration_read = acc
            self.attr_Deceleration_read = dec
            self.setPositionMode()
        elif self.Mode == 'Speed':
            # [issue]: 这个初始化的参数会让电机直接动起来
            # 除非初始化的速度是0，所以有一点不安全
            self.DesiredState = 11
            self.attr_Velocity_read = vel
            self.attr_Acceleration_read = acc
            self.attr_Deceleration_read = dec
            self.setSpeedMode()
        elif self.Mode == 'Current':
            # [issue]: 这个初始化的参数会让电机直接动起来
            # 是否应该让这个参数1放在Move()方法中
            self.DesiredState = 1 # 应该设置为0合适，这里可以不设置为21，和停止不同，这个是初始化
            self.attr_Current_read = cur
            self.attr_Current_ramp = rap
            self.setCurrentMode()
        else:
            print('SetInitParameters() is ERROR{}'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	SetModeClass.setInitParameters
    def setPositionMode(self):
        ''' 
            Sets Programmed Position Mode, Trajectory Profile Mode, position, velocity, acceleration, deceleration.
            # Parameter ID	Bank	Description
            # 0x24	R F	Desired State(0x24). Bits: 0~42(P19)
                                # Desired state:
                                #*  21 = Programmed Position Mode, Servo
                                #  31 = Programmed Position Mode, Stepper
            # 0xc8	R F	Give trajectory profile mode(0xc8).
                                # Profile type: 
                                #  0 / 0 0000 0000 = Absolute move, trapezoidal profile.
                                #*  1 / 0 0000 0001 = Absolute move, S-curve profile.
                                #     256 /1 0000 0000(2^8) = Relative move, trapezoidal profile.
                                #     257 /1 0000 0001(2^8+1) = Relative move, S-curve profile.
                                #  2 / 0 0000 0010 = Velocity move.
            [issue]: 这个可以考虑使用
            # 0xc9 R* Trajectory Status Register. This parameter gives status information about the trajectory generator.
                                # 0-8 Reserved.
                                # 9 Cam table underflow.
                                # 10 Reserved.
                                # 11 Homing error. If set, an error occurred in last home attempt. Cleared by a home command.
                                # 12 Referenced. Set when homing command has been successfully executed. Cleared by home command.
                                # 13 Homing. If set, drive is running home command.
                                # 14 Set when move is aborted. Cleared at start of next move.
                                # 15 In-Motion Bit. If set, trajectory generator is presently generating profile.
            # 0xca	R F	Trajectory Generator Position Command. Units: Counts.
                                # This value gives destination position for absolute moves or move distance for relative moves. 
                                # Relative move = the distance of the move.
                                # Absolute move = the target position of the move.
                                # Velocity move = 1 for positive direction,
                                #         -1 for negative direction.
            # 0xcb	R F	Trajectory Maximum Velocity. Units: 0.1 counts/s.
                                # Trajectory generator will attempt to reach this velocity during a move.
            # 0xcc	R F	Trajectory Maximum Acceleration. Units: 10 counts/s2. 
                                # Trajectory generator will attempt to reach this acceleration during a move. 
                                # For s-curve profiles, this value also used to decelerate at end of move.
            # 0xcd	R F	Trajectory Maximum Deceleration. Units: 10 counts/s2. 
                                # In trapezoidal trajectory mode, this value used to decelerate at end of move.
            [issue]: 
            # 0xce	R F	Trajectory Maximum Jerk. Units: 100 counts/s3.
                                # Also known as Trajectory Jerk Limit. S-curve profile generator uses this value as jerk (rate of change of acceleration/deceleration) during moves. 
                                # Other profiles types do not use jerk limit.
            [issue]: 
            # 0xcf	R F	Trajectory Abort Deceleration. Units: 10 counts/s2.
                                # If move is aborted, this value will be used by trajectory generator to decelerate to stop.
        '''
        #----- PROTECTED REGION ID(SetModeClass.setPositionMode) ENABLED START -----#
        cmd_state = self.write_DesiredState(self.DesiredState) # 21
        cmd_profile = self.write_Profile(self.ProfileType)
        cmd_pos = self.write_SetPoint(self.attr_SetPoint_read)
        cmd_vel = self.write_Velocity(self.attr_Velocity_read)
        cmd_acc = self.write_Acceleration(self.attr_Acceleration_read)
        cmd_dec = self.write_Deceleration(self.attr_Deceleration_read)

        # [issue]: 使用这个方式发送组合命令，这样就不用连续发送好几条，需要提前实验是否可行，以及判断返回值是什么样子的
        # [command specific parameters]
        # Command specific parameters are used to provide additional data for a command. If more than one parameter is required, they should be separated by spaces. The remaining sections of this chapter describe the parameters for each command code.

        if cmd_state==cmd_profile==cmd_pos==cmd_vel==cmd_acc==cmd_dec and cmd_state== 'ok':
            result = 'ok'
            print('SetPositionMode() is OK{}'.format(self.print_log('time_msg')))
        else:
            result = 'ERROR'
            print('SetPositionMode() is ERROR{}'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	SetModeClass.setPositionMode
        return result
    def setSpeedMode(self):
        ''' 
            Sets Programmed Speed Mode
            # 编程速度模式将驱动器的输出设置为编程速度。 在此模式下启用驱动器后，或更改了编程速度时，电动机速度将以编程速度升至新的水平。
            # Parameter ID	Bank	Description
            # 0x24	R F	Programmed Velocity Mode (11).
            # 0x2f    R F Programmed Velocity Command(0x2f). Units: 0.1 encoder counts/s.
                                # Only used in Programmed Velocity Mode (Desired State (0x24) = 11)
                                # For estimated velocity. Units: 0.01 RPM.
                                # For stepper mode. Units: 0.1 microsteps/s.
            # 0x36	R F	Velocity acceleration limit. Units: 1000 counts/second2
            # 0x37	R F	Velocity deceleration limit. Units: 1000 counts/second2
            [issue]:
            # 0x38	R*	Actual Motor Current. Units: 0.01 A. 
                                # This current is calculated based on both D and Q axis currents.
            # 0x39	R F	Fast stop ramp. Units: 1000 counts/second2
        '''
        #----- PROTECTED REGION ID(SetModeClass.setSpeedMode) ENABLED START -----#
        cmd_state = self.write_DesiredState(self.DesiredState) # 11
        cmd_vel = self.write_Velocity(self.attr_Velocity_read)
        cmd_acc = self.write_Acceleration(self.attr_Acceleration_read)
        cmd_dec = self.write_Deceleration(self.attr_Deceleration_read)

        if cmd_state==cmd_vel==cmd_acc==cmd_dec and cmd_state=='ok':
            result = 'ok'
            print('SetSpeedMode() is OK{}'.format(self.print_log('time_msg')))
        else:
            result = 'ERROR'
            print('SetSpeedMode() is ERROR{}'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	SetModeClass.setSpeedMode
        return result
    def setCurrentMode(self):
        ''' 
            Sets Programmed Current Mode
            编程电流模式将驱动器的输出设置为编程电流水平。 在此模式下启用驱动器时，或更改了编程的电流水平时，输出电流将以编程的速率上升到新的水平。

            # Parameter ID	Bank	Description
            # 0x24	R F	Desired state: Programmed Current mode (1)
            # 0x02	R F	Current loop programmed value. Units: 0.01 A.
                                # This current will be used to command drive when Desired State (0x24) is set to 1.
            # 0x6a	R F	Current ramp limit. Units: mA/second. 
                                # Used when running in Current (Torque) mode. Setting this to zero disables slope limiting.
            注意：在启用驱动器的同时更改电平和斜坡参数时，请先更改斜坡率。
        '''
        #----- PROTECTED REGION ID(SetModeClass.setCurrentMode) ENABLED START -----#
        cmd_state = self.write_DesiredState(self.DesiredState) # 1
        cmd_cur = self.write_Current(self.attr_Current_read)
        cmd_rap = self.write_CurrentRamp(self.attr_Current_ramp)

        if cmd_state==cmd_cur==cmd_rap and cmd_state=='ok':
            result = 'ok'
            print('SetCurrentMode() is OK{}'.format(self.print_log('time_msg')))
        else:
            result = 'ERROR'
            print('SetCurrentMode() is ERROR{}'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	SetModeClass.setCurrentMode
        return result

class MoveMotorClass(SetModeClass):
    '''
        Stop/Move
    '''
    def Move(self):
        ''' 
            triggers the motor to move.

            Trajectory Generator Position Command(0xca). Units: Counts.
            This value gives destination position for absolute moves or move distance for relative moves.
            Commanded Position(0x2d_R*). Units: counts. 
            
            [issue]:
            是否考虑要加入其它模式，相对stopMove()函数而言
        '''
        #----- PROTECTED REGION ID(CopleyControl.Move) ENABLED START -----#
        # 这个函数应该是其余的数据都准备好了，然后再来调用的，因为只有一条指令，前面的都是验证是否满足执行的要求
        if self.Mode=='Position': # 这里不用DesiredState参数，是因为在电流模式初始化的时候，可能设置为0(防止突然启动)
            # 1.Relative move
            if self.ProfileType==256 or self.ProfileType==257:
                if self.attr_SetPoint_read==0: # 位置差已经消除变为零，但是这个差要从哪里获取，一直读参数吗？
                    print('The expected position is achieved.{}'.format(self.print_log('time_msg')))
                elif self.attr_SoftwareCwLimit_read==0 and self.attr_SoftwareCcwLimit_read==0:
                    # print('NO software limits are set.')
                    # self.setMoveParameters() # MovePostion(self)_Note
                    self.getValue('{} t 1\r'.format(self.NodeID))
                    self.attr_SetPoint_read = 0 # 是否检测判断一下更好呢
                else:
                    status = str(self.dev_status())
                    current_position = self.getValue('{} g r0x2d\n'.format(self.NodeID)) # Commanded Position(0x2d_R*).
                    self.targetPosition = int(current_position) + int(self.attr_SetPoint_read)
                    # 首先判断驱动器的状态是否可用，则设定参数，开始执行
                    if status=='Status is STANDBY' or status=='Positive limit switch Active' or status=='Negative limit switch Active':
                        if self.targetPosition in range(self.attr_SoftwareCcwLimit_read, self.attr_SoftwareCwLimit_read):
                            # print('The expected position ', self.targetPosition, ' is among the range from ', int(self.attr_SoftwareCcwLimit_read), ' to ', int(self.attr_SoftwareCwLimit_read))
                            # self.setMoveParameters() # MovePostion(self)_Note
                            self.getValue(str('{} t 1\r'.format(self.NodeID)))
                            self.attr_SetPoint_read = 0
                        else:
                            print('The expected position ', self.targetPosition, ' is not among the range from ', int(self.attr_SoftwareCcwLimit_read), ' to ', int(self.attr_SoftwareCwLimit_read))
                    else:
                        print('Check Device State please.{}'.format(self.print_log('time_msg')))
            # 2.Absolute move
            elif self.ProfileType==0 or self.ProfileType==1:
                if self.attr_SoftwareCcwLimit_read==0 and self.attr_SoftwareCwLimit_read==0:
                    # print('NO software limits are set.')
                    # self.setMoveParameters() # MovePostion(self)_Note
                    self.getValue(str('{} t 1\n'.format(self.NodeID)))
                    self.attr_SetPoint_read = 0
                else:
                    status = str(self.dev_status())
                    current_position = self.getValue('{} g r0x17\n'.format(self.NodeID)) # 0x2d
                    self.targetPosition = int(current_position) + int(self.attr_SetPoint_read)

                    if status == 'Status is STANDBY' or status == 'Positive limit switch Active' or status == 'Negative limit switch Active':
                        if self.targetPosition >=self.attr_SoftwareCcwLimit_read and self.targetPosition <= self.attr_SoftwareCwLimit_read:
                            print('The expected position position ', self.targetPosition, ' is among the range from ', self.attr_SoftwareCcwLimit_read, ' to ', self.attr_SoftwareCwLimit_read)
                            # self.setMoveParameters() # MovePostion(self)_Note
                            self.getValue(str('{} t 1\n'.format(self.NodeID)))
                            self.attr_SetPoint_read = 0
                        else:
                            print('The expected position ', self.targetPosition, ' is not among the range from ', self.attr_SoftwareCcwLimit_read, ' to ', self.attr_SoftwareCwLimit_read)
                    else:
                        print('Check Device State please.{}'.format(self.print_log('time_msg')))
            # 3.Velocity move.
            elif self.ProfileType==2:
                # self.setMoveParameters() # MovePostion(self)_Note
                # cmd_pos = self.setParameterCmd( '0xca', direction) # Velocity move = 1 for positive, -1 for negative.
                # self.getValue(str(cmd_pos))
                self.getValue(str('{} t 1\n'.format(self.NodeID)))
        # 这里是作为扩充，只是为了形式上的完整，对于速度模式，只要是速度不为零，即开始运动
        elif self.Mode=='Speed':
            self.write_Velocity(self.attr_Velocity_read)
        # 对于电流模式，只要是0x24设置为1，即开始运动
        elif self.Mode=='Current':
            cmd = self.setParamCmd('0x24', 1)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            result = 'ERROR'
            print('Check Device State please.{}'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	CopleyControl.Move
        return result
    def StopMove(self):
        ''' 
            stops a movement immediately.
        '''
        # self.debug_stream('StopMove()')
        #----- PROTECTED REGION ID(CmdMethodsClass.StopMove) ENABLED START -----#
        if self.Mode=='Position': # Programmed Position Mode
            cmd = self.setParamCmd('t', 0)
            result1 = self.getValue(cmd) # self.write(cmd)
            cmd = self.setParamCmd('0xcb', 0)
            result2 = self.getValue(cmd) # self.write(cmd)
            result = result1 # + result2
        elif self.Mode == 'Speed': # Programmed Speed Mode
            cmd = self.setParamCmd('0x2f', 0)
            result = self.getValue(cmd) # self.write(cmd)
        elif self.Mode == 'Current': # Programmed Current Mode
            # [issue]:
            # 如果突然关闭驱动器可能出现一些问题，比如无法维持当前位置，考虑切换成位置模式
            # 与此同时，要再度开启力矩模式就需要再重设0x24参数，需要更改Move()方法
            cmd = self.setParamCmd('0x24', 21)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('StopMove() is ERROR.{}'.format(self.print_log('time_msg')))
            result = 'ERROR'
        #----- PROTECTED REGION END -----#	//	CmdMethodsClass.StopMove
        return result
    ## ------------------------Amplifire------------------------
    def StopAmplifire(self):
        """
            stop the amplifire
            0x24
        """
        # self.debug_stream('StopMotor()')
        #----- PROTECTED REGION ID(CmdMethodsClass.StopMotor) ENABLED START -----#
        # [issue]:
        # 需要检测一下位置，看看是否发生移动，确保真的停止了
        # 考虑增加一个stopmotor的方法
        # 另外需要检测一下返回值是否是ok
        cmd = self.setParamCmd('0x24', 0)
        result = self.getValue(cmd) # self.write(cmd)
        #----- PROTECTED REGION END -----#	//	CmdMethodsClass.StopMotor
        return result
    def ResetAmplifire(self):
        ''' 
            `r\n` Reset the amplifier immediately. 
            The amplifier baud rate is set to 9600 when the amplifier restarts.
            
            NOTE: 
                if a reset command is issued to an amplifier on a multi-drop network, error code 32, 'CAN Network communications failure,' will be received. 
                This is because the amplifier reset before responding to the gateway amplifier. 
                This error can be safely ignored in this circumstance.
        '''
        #----- PROTECTED REGION ID(CmdMethodsClass.ResetMotor) ENABLED START -----#
        cmd = self.setParamCmd('r')
        result = self.getValue(cmd) # self.write(cmd)
        #----- PROTECTED REGION END -----#	//	CmdMethodsClass.ResetMotor
        # [issue]:
        # error code 32, 'CAN Network communications failure'
        return result

# %%
class CheckHomeStatueClass(CheckEventStateClass):
    def read_CwLimit(self): # -> attribute
        '''
            0xb8    R F Positive hardware limit.
                                2^9 = 512 正限位开关有效(Positive limit switch active)[电机轴已经接触到正限位开关。]
                                2^10 = 1024 负限位开关有效(Negative limit switch active)[电机轴已经接触到负限位开关。]
            
            [issue]:
            没有制造出这两个状态，但是有16、17；感觉这个9、10应该就是设置了b8、b9
        '''
        #----- PROTECTED REGION ID(HomingMethodClass.CwLimit_read) ENABLED START -----#  
        value = self.is_int(self.readLatchedEventStatus(), 0)
        self.attr_CwLimit_read = (int(value)&512)!=0
        if self.attr_CwLimit_read:
            print('Positive limit switche is active.{}'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.CwLimit_read
        return self.attr_CwLimit_read
    def read_CcwLimit(self): # -> attribute
        '''
            0xb9    R F Negative hardware limit.
        '''
        #----- PROTECTED REGION ID(HomingMethodClass.CcwLimit_read) ENABLED START -----#  
        value = self.is_int(self.readLatchedEventStatus(), 0)
        self.attr_CcwLimit_read = (int(value)&1024)!=0
        if self.attr_CcwLimit_read:
            print('Negative limit switche is active.{}'.format(self.print_log('time_msg')))   
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.CcwLimit_read
        return self.attr_CcwLimit_read
    def checkLimit(self):
        '''
            Check the Hardware limit switches.
        '''
        #----- PROTECTED REGION ID(CopleyControl.programmer_methods) ENABLED START -----#
        # self.clearLatchedStatus()
        value = self.is_int(self.readLatchedEventStatus(), 0)
        if (int(value)&1536)!=0: # 9/10
            print('Positive and Negative limit switches are active.{}'.format(self.print_log('time_msg')))
            return 3
        elif (int(value)&512)!=0: # 9
            print('Positive limit switch is active.{}'.format(self.print_log('time_msg')))
            return 1
        elif (int(value)&1024)!=0: # 10
            print('Negative limit switch is active.{}'.format(self.print_log('time_msg')))
            return 2 
        elif int(value)==0 or (int(value)&131072)!=0 or (int(value)&65536)!=0 or (int(value)&67108864)!=0:  
            # Bit_17: Negative software limit condition
            # Bit_16: Positive software limit condition
            # Bit_26: Home switch is active
            print('NO limit switch is active.{}'.format(self.print_log('time_msg')))
            return 0
    def checkHomeStatus(self):
        '''
            Check the Home Switch status.
        '''
        # self.clearLatchedStatus()
        value = self.is_int(self.readLatchedEventStatus(), 0)
        if (value&67108864)!=0: # Bit_26: Home switch is active
            print('Home Switch is active.')
            return 1
        else:            
            print('Home Switch is not active.')
            return 0

class SetHomeMethodClass(SetModeClass,CheckHomeStatueClass):
    '''
        SoftwareLimit
        HardwareLimit
        Homing
        AttrHardware
    '''
    ## ------------------------Homing------------------------
    def read_HomingMethod(self): # -> attribute # 0xc2
        '''
            0xc2    R F Homing Method Configuration.
        '''
        #----- PROTECTED REGION ID(CopleyControl.HomingMethod_read) ENABLED START -----#
        cmd = self.getParamCmd('0xc2')
        homing = self.is_int(self.getValue(cmd), self.attr_HomingMethod_read)
        if self.DesiredState==21:
            self.attr_HomingMethod_read = homing
            argout = BitsMapped_HM('0xC2', homing) # -> str
        else:
            argout = 'ERROR'
            print('The Desired State is {}, doesn`t position mode.{}'.format(self.print_log('time_msg')))
        print('The homing method is {}'.format(argout, self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	CopleyControl.HomingMethod_read
        return self.attr_HomingMethod_read
    def write_HomingMethod(self, data): # -> attribute
        '''
            0xc2

            [512, 544, 560, 513, 529, 545, 561, 514, 530, 546, 562, 610, 626, 516, 532, 548, 564, 771, 787, 515, 531, 803, 819, 867, 883, 547, 563, 611, 627,15]
        '''
        data = self.is_int(data, self.attr_HomingMethod_read)
        #----- PROTECTED REGION ID(CopleyControl.HomingMethod_write) ENABLED START -----#
        HomeRefNrList = [512, 544, 560, 513, 529, 545, 561, 514, 530, 546, 562, 610, 626, 516, 532, 548, 564, 771, 787, 515, 531, 803, 819, 867, 883, 547, 563, 611, 627,15]
        if data in HomeRefNrList:
            cmd = self.setParamCmd('0xc2', data)
            result = self.getValue(cmd)
        else:
            result = 'ERROR'
            print('Input home reference number: {} is not valid.{}'.format(data, self.print_log('time_msg')))
        
        self.attr_HomingMethod_read = self.setValue(result, data, self.attr_HomingMethod_read)
        #----- PROTECTED REGION END -----#	//	CopleyControl.HomingMethod_write
        return result
    def read_HomingVelocityFast(self): # -> attribute # 0xc3
        """
            0xc3    R F Homing Velocity (fast moves). Units: 0.1 counts/s.
                                This velocity value is used during segments of homing procedure that may be handled at high speed. Generally, this means moves in which home sensor is being located, but edge of sensor is not being found.
        """
        # self.debug_stream('read_HomingVelocityFast()')
        #----- PROTECTED REGION ID(HomingMethodClass.read_HomingVelocityFast) ENABLED START -----#
        cmd = self.getParamCmd('0xc3')
        data = self.is_int(self.getValue(cmd), self.attr_HomingVelocityFast_read)
        self.attr_HomingVelocityFast_read = data * unit_0xc3
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.read_HomingVelocityFast
        return self.attr_HomingVelocityFast_read
    def write_HomingVelocityFast(self, data): # -> attribute
        '''
        '''
        # self.debug_stream('write_HomingVelocityFast()')
        data = self.is_int(data, self.attr_HomingVelocityFast_read)
        #----- PROTECTED REGION ID(RWAttributesClass.write_HomingVelocityFast) ENABLED START -----#
        velocity = data / unit_0xc3
        cmd = self.setParamCmd('0xc3', velocity)
        result = self.getValue(cmd) # self.write(cmd)
        self.attr_HomingVelocityFast_read = self.setValue(result, data, self.attr_HomingVelocityFast_read)
        # print('set homing velocity fast to  ', str(velocity), 'counts/s.'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.write_HomingVelocityFast
        return result
    def read_HomingVelocitySlow(self): # -> attribute # 0xc4
        """
            0xc4    R F Homing Velocity (slow moves). Units: 0.1 counts/s.
                                This velocity value is used for homing segments that require low speed, such as cases where edge of a homing sensor is being sought.
        """
        # self.debug_stream('read_HomingVelocitySlow()')
        #----- PROTECTED REGION ID(HomingMethodClass.read_HomingVelocitySlow) ENABLED START -----#
        cmd = self.getParamCmd('0xc4')
        data = self.is_int(self.getValue(cmd), self.attr_HomingVelocitySlow_read)
        self.attr_HomingVelocitySlow_read = data * unit_0xc4
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.read_HomingVelocitySlow
        return self.attr_HomingVelocitySlow_read
    def write_HomingVelocitySlow(self, data): # -> attribute
        '''
            0xc4
        '''
        # self.debug_stream('write_HomingVelocitySlow()')
        data = self.is_int(data, self.attr_HomingVelocitySlow_read)
        #----- PROTECTED REGION ID(RWAttributesClass.write_HomingVelocitySlow) ENABLED START -----#
        velocity = data / unit_0xc4
        cmd = self.setParamCmd('0xc4', velocity)
        result = self.getValue(cmd) # self.write(cmd)
        self.attr_HomingVelocitySlow_read = self.setValue(result, data, self.attr_HomingVelocityFast_read)
        # print('set homing velocity slow to  ', str(velocity), 'counts/s.'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.write_HomingVelocitySlow
        return result
    def read_HomingAccDec(self): # -> attribute # 0xc5
        """
            0xc5    R F Homing Acceleration/Deceleration. Units: 10 counts/s2.
                                This value defines acceleration used for all homing moves. Same value is used at beginning and ending of moves (i.e. no separate deceleration value).
        """
        # self.debug_stream('read_HomingAccDec()')
        #----- PROTECTED REGION ID(HomingMethodClass.read_HomingAccDec) ENABLED START -----#
        cmd = self.getParamCmd('0xc5')
        data = self.is_int(self.getValue(cmd), self.attr_HomingAccDec_read)
        self.attr_HomingAccDec_read = data * unit_0xc5
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.read_HomingAccDec
        return self.attr_HomingAccDec_read
    def write_HomingAccDec(self, data): # -> attribute
        # self.debug_stream('write_HomingAccDec()')
        data = self.is_int(data, self.attr_HomingAccDec_read)
        #----- PROTECTED REGION ID(RWAttributesClass.write_HomingAccDec) ENABLED START -----#
        accdec = data / unit_0xc5
        cmd = self.setParamCmd('0xc5', accdec)
        result = self.getValue(cmd) # self.write(cmd)
        self.attr_HomingAccDec_read = self.setValue(result, data, self.attr_HomingAccDec_read)
        # print('set homing acc\dec to  ', str(accdec), 'counts/s2.'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.write_HomingAccDec
        return result
    def read_HomeOffset(self): # -> attribute # 0xc6/0
        '''
            0xc6    R F Home Offset. Units: counts.
                Home offset is difference between zero position for application and machine home position (found during homing). Once homing is completed, new zero position determined by homing state machine will be located sensor position plus this offset. All subsequent absolute moves shall be taken relative to this new zero position.
            
            默认值为0，这个数值可以忽略
        '''
        # self.debug_stream('read_HomeOffset()')
        #----- PROTECTED REGION ID(HomingMethodClass.HomeOffset_read) ENABLED START -----#
        cmd = self.getParamCmd('0xc6')
        self.attr_HomeOffset_read = self.is_int(self.getValue(cmd), self.attr_HomeOffset_read)
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.HomeOffset_read
        return self.attr_HomeOffset_read
    def write_HomeOffset(self, data):
        '''
        '''
        # self.debug_stream('write_HomeOffset()')
        #----- PROTECTED REGION ID(HomingMethodClass.HomeOffset_write) ENABLED START -----#
        data = self.is_int(data, self.attr_HomeOffset_read)
        cmd = self.setParamCmd('0xc6', data)
        result = self.getValue(cmd)

        self.attr_HomeOffset_read = self.setValue(result, data, self.attr_HomeOffset_read)
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.HomeOffset_write
        return result
    def read_HomingCurrentLimit(self): # -> attribute # 0xc7
        """
            0xc7    R F Homing Current Limit. Units: 0.01 A.
                                Used in Home to Hard Stop mode only, this current is used to determine when drive has reached end of travel (hard stop). Used in conjunction with Home to Hard Stop Delay Time (0xBF).
            
            unit: A -> mA
        """
        # self.debug_stream('read_HomingCurrentLimit()')
        #----- PROTECTED REGION ID(HomingMethodClass.read_HomingCurrentLimit) ENABLED START -----#
        cmd = self.getParamCmd('0xc7')
        data = self.is_int(self.getValue(cmd), self.attr_HomingCurrentLimit_read)
        self.attr_HomingCurrentLimit_read = data * unit_0xc7
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.read_HomingCurrentLimit
        return self.attr_HomingCurrentLimit_read
    def write_HomingCurrentLimit(self, data): # -> attribute
        # self.debug_stream('write_HomingCurrentLimit()')
        data = self.is_int(data, self.attr_HomingCurrentLimit_read)
        #----- PROTECTED REGION ID(RWAttributesClass.write_HomingCurrentLimit) ENABLED START -----#
        curlimit = data / unit_0xc7
        cmd = self.setParamCmd('0xc7', curlimit)
        result = self.getValue(cmd) # self.write(cmd)
        self.attr_HomingCurrentLimit_read = self.setValue(result, data, self.attr_HomingCurrentLimit_read)
        # print('set homing current limit to  ', str(curlimit), 'mA.'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.write_HomingCurrentLimit
        return result
    ## ------------------------SoftwareLimit------------------------
    def read_SoftwareCwLimit(self): # -> attribute # 0xb8
        '''
            0xb8    R F Positive Software Limit value. Units: counts. 
                This parameter is only available on drives that support trajectory generation and homing. 
                Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). 
                Set to less than negative software limit to disable.
        '''
        # self.debug_stream('In read_SoftwareCwLimit()')
        #----- PROTECTED REGION ID(HomingMethodClass.SoftwareCwLimit_read) ENABLED START -----#
        cmd = self.getParamCmd('0xb8')
        self.attr_SoftwareCwLimit_read = self.is_int(self.getValue(cmd), self.attr_SoftwareCwLimit_read)
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.SoftwareCwLimit_read
        return self.attr_SoftwareCwLimit_read
    def write_SoftwareCwLimit(self, data): # -> attribute
        '''
            0xb8
        '''
        # self.debug_stream('In write_SoftwareCwLimit()')
        data = self.is_int(data, self.attr_SoftwareCwLimit_read)
        #----- PROTECTED REGION ID(HomingMethodClass.SoftwareCwLimit_write) ENABLED START -----#
        # print('SoftwareCwLimit:', data, 'current position: ', self.attr_Position_read, 'Ccwlimit: ', self.attr_SoftwareCcwLimit_read, 'Cwlimit: ', self.attr_SoftwareCwLimit_read)
        self.targetPosition = self.attr_Position_read + self.attr_SetPoint_read
        if self.targetPosition in range(self.attr_SoftwareCcwLimit_read, data):
            cmd = self.setParamCmd('0xb8', data)
            result = self.getValue(cmd)
        else:
            result = 'ERROR'
            print('SoftwareCwLimit must be higher than `current Position` + `current SetPoint`.{}'.format(self.print_log('time_msg')))
        self.attr_SoftwareCwLimit_read = self.setValue(result, data, self.attr_SoftwareCwLimit_read)
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.SoftwareCwLimit_write
        return result
    def read_SoftwareCcwLimit(self): # -> attribute # 0xb9
        '''
            # 0xb9 R F  Negative Software Limit. Units: counts. 
                Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). Set to greater than positive software limit to disable.
        '''
        #----- PROTECTED REGION ID(HomingMethodClass.read_SoftwareCcwLimit) ENABLED START -----#
        cmd = self.getParamCmd('0xb9')
        self.attr_SoftwareCcwLimit_read = self.is_int(self.getValue(cmd), self.attr_SoftwareCcwLimit_read)
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.read_SoftwareCcwLimit
        return self.attr_SoftwareCcwLimit_read
    def write_SoftwareCcwLimit(self, data): # -> attribute
        '''
        '''
        data = self.is_int(data, self.attr_SoftwareCcwLimit_read)
        #----- PROTECTED REGION ID(HomingMethodClass.write_SoftwareCcwLimit) ENABLED START -----#
        self.targetPosition = self.attr_Position_read + self.attr_SetPoint_read
        if data < self.targetPosition:
            cmd = self.setParamCmd('0xb9', data)
            result = self.getValue(cmd)
        else:
            result = 'ERROR'
            print('SoftwareCcwLimit must be smaller than `Position` + `SetPoint`.{}'.format(self.print_log('time_msg')))
        
        self.setValue(result, data, self.attr_SoftwareCcwLimit_read)
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.write_SoftwareCcwLimit
        return result
    def read_SoftwareCwDialLimit(self): # -> attribute # 0xb8
        '''
            0xb8    R F Positive Software Limit value. Units: counts. 
                This parameter is only available on drives that support trajectory generation and homing. 
                Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). 
                Set to less than negative software limit to disable.
        '''
        #----- PROTECTED REGION ID(CopleyControl.SoftwareCwDialLimit_read) ENABLED START -----#
        self.attr_SoftwareCwLimit_read = self.read_SoftwareCwLimit()
        self.attr_SoftwareCwDialLimit_read = int(float(self.attr_SoftwareCwLimit_read) / float(self.attr_Conversion_read))
        #----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCwDialLimit_read
        return self.attr_SoftwareCwDialLimit_read
    def write_SoftwareCwDialLimit(self, data): # -> attribute
        '''
        '''
        data = self.is_int(data, self.attr_SoftwareCwDialLimit_read)
        #----- PROTECTED REGION ID(CopleyControl.SoftwareCwDialLimit_write) ENABLED START -----#
        self.attr_SoftwareCwLimit_read = self.attr_Conversion_read * data
        cmd = self.setParamCmd('0xb8', self.attr_SoftwareCwLimit_read)
        result = self.getValue(cmd)

        self.attr_SoftwareCwDialLimit_read = self.setValue(result, data, self.attr_SoftwareCwDialLimit_read)
        #----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCwDialLimit_write
        return result
    def read_SoftwareCcwDialLimit(self): # -> attribute # 0xb9
        '''
            0xb9    R F Negative Software Limit. Units: counts. 
                Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). 
                Set to greater than positive software limit to disable.
        '''
        #----- PROTECTED REGION ID(CopleyControl.SoftwareCcwDialLimit_read) ENABLED START -----#
        self.attr_SoftwareCcwLimit_read = self.read_SoftwareCcwLimit()
        self.attr_SoftwareCcwDialLimit_read = int(float(self.attr_SoftwareCcwLimit_read) / float(self.attr_Conversion_read))
        #----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCcwDialLimit_read
        return self.attr_SoftwareCcwDialLimit_read
    def write_SoftwareCcwDialLimit(self, data): # -> attribute
        '''
        '''
        data = self.is_int(data, self.attr_SoftwareCcwDialLimit_read)
        #----- PROTECTED REGION ID(CopleyControl.SoftwareCcwDialLimit_write) ENABLED START -----#
        self.attr_SoftwareCcwLimit_read = self.attr_Conversion_read * data
        cmd = self.setParamCmd('0xb9', self.attr_SoftwareCcwLimit_read)
        result = self.getValue(cmd)

        self.attr_SoftwareCcwDialLimit_read = self.setValue(result, data, self.attr_SoftwareCcwDialLimit_read)
        #----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCcwDialLimit_write
        return result
    ## ------------------------HardwareLimit------------------------
    def read_attr_hardware(self): # -> attribute
        self.debug_stream('read_attr_hardware()')
        #----- PROTECTED REGION ID(HomingMethodClass.read_attr_hardware) ENABLED START -----#
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.read_attr_hardware
    def read_CurrentDelayTime(self): # -> attribute # 0xbf(->0xc7)/250
        """
            0xbf    R F Home to Hard Stop Delay Time. Units: ms. 
                                When performing home to hard stop, drive will push against stop for this long before sampling home position.
            0xc7
        """
        # self.debug_stream('read_CurrentDelayTime()')
        #----- PROTECTED REGION ID(HomingMethodClass.read_CurrentDelayTime) ENABLED START -----#
        cmd = self.getParamCmd('0xc3')
        data = self.is_int(self.getValue(cmd), self.attr_CurrentDelayTime_read)
        self.attr_CurrentDelayTime_read = data
        #----- PROTECTED REGION END -----#	//	HomingMethodClass.read_CurrentDelayTime
        return self.attr_CurrentDelayTime_read
    def write_CurrentDelayTime(self, data): # -> attribute
        '''
            0xbf
        '''
        # self.debug_stream('write_CurrentDelayTime()')
        data = self.is_int(data, self.attr_CurrentDelayTime_read)
        #----- PROTECTED REGION ID(RWAttributesClass.write_CurrentDelayTime) ENABLED START -----#
        cmd = self.setParamCmd('0xc3', data)
        result = self.getValue(cmd) # self.write(cmd)
        self.attr_CurrentDelayTime_read = self.setValue(result, data, self.attr_CurrentDelayTime_read)
        # print('set current delay time to  ', str(data), 'ms.'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.write_CurrentDelayTime
        return result
    ## ------------------------setHomeParam------------------------
    def setHomeParams(self, homing=512):
        '''
            Set the Homing parameters using the input Homing method value
            0xc2    R F Homing Method Configuration.
                                # 参数字典.pdf
                                Homing Method Configuration. Bits: 0~15
            0xc3    R F Homing Velocity (fast moves). Units: 0.1 counts/s.
                                This velocity value is used during segments of homing procedure that may be handled at high speed. Generally, this means moves in which home sensor is being located, but edge of sensor is not being found.
            0xc4    R F Homing Velocity (slow moves). Units: 0.1 counts/s.
                                This velocity value is used for homing segments that require low speed, such as cases where edge of a homing sensor is being sought.
            0xc5    R F Homing Acceleration/Deceleration. Units: 10 counts/s2.
                                This value defines acceleration used for all homing moves. Same value is used at beginning and ending of moves (i.e. no separate deceleration value).
            0xc6    R F Home Offset. Units: counts. 
                                Home offset is difference between zero position for application and machine home position (found during homing). Once homing is completed, new zero position determined by homing state machine will be located sensor position plus this offset. All subsequent absolute moves shall be taken relative to this new zero position.
            0xc7    R F Homing Current Limit. Units: 0.01 A.
                                Used in Home to Hard Stop mode only, this current is used to determine when drive has reached end of travel (hard stop). Used in conjunction with Home to Hard Stop Delay Time (0xBF).
            0xc8	R F	Give trajectory profile mode(0xc8).
                                # Profile type: 
                                #  0 / 0 0000 0000 = Absolute move, trapezoidal profile.
                                #*  1 / 0 0000 0001 = Absolute move, S-curve profile.
                                #     256 /1 0000 0000(2^8) = Relative move, trapezoidal profile.
                                #     257 /1 0000 0001(2^8+1) = Relative move, S-curve profile.
                                #  2 / 0 0000 0010 = Velocity move.
            # Trajectory Status Register
            0xc9 R* Trajectory Status Register. This parameter gives status information about the trajectory generator.
                                # 0-8 Reserved.
                                # 9 Cam table underflow.
                                # 10 Reserved.
                                # 11 Homing error. If set, an error occurred in last home attempt. Cleared by a home command.
                                # 12 Referenced. Set when homing command has been successfully executed. Cleared by home command.
                                # 13 Homing. If set, drive is running home command.
                                # 14 Set when move is aborted. Cleared at start of next move.
                                # 15 In-Motion Bit. If set, trajectory generator is presently generating profile.

            0xca	R F	Trajectory Generator Position Command(0xca). Units: Counts.
                                # This value gives destination position for absolute moves or move distance for relative moves. 
                                # Relative move = the distance of the move.
                                # Absolute move = the target position of the move.
                                # Velocity move = 1 for positive direction,
                                #         -1 for negative direction.
            # Software Limit value
            0xb8    R F Positive Software Limit value. Units: counts.
                                This parameter is only available on drives that support trajectory generation and homing. Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). Set to less than negative software limit to disable.
            0xb9    R F Negative Software Limit. Units: counts. 
                                Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). Set to greater than positive software limit to disable.

            t 2               Execute homing. Assumes all homing parameters have been previously set.
        '''
        self.attr_HomingMethod_read = self.is_int(homing, 512) # 512: Set Current Position as Home.

        cmd_DesiredState = self.write_DesiredState(self.DesiredState) # 0x24/21
        cmd_HomingMethod = self.write_HomingMethod(self.attr_HomingMethod_read) # 0xc2
        cmd_FastVelocity = self.write_HomingVelocityFast(self.attr_HomingVelocityFast_read) # 0xc3=Velocity
        cmd_SlowVelocity = self.write_HomingVelocitySlow(self.attr_HomingVelocitySlow_read) # 0xc4=3333
        cmd_Acceleration = self.write_HomingAccDec(self.attr_HomingAccDec_read) # 0xc5=acc
        cmd_HomeOffset = self.write_HomeOffset(self.attr_HomeOffset_read) # 0xc6=0
        cmd_CurrentLimit = self.write_HomingCurrentLimit(self.attr_HomingCurrentLimit_read) # 0xc7=173、19mA
        cmd_PositiveSoftwareLimit = self.write_SoftwareCwLimit(self.attr_SoftwareCwLimit_read) # 0xb8
        cmd_NegativeSoftwareLimit = self.write_SoftwareCcwLimit(self.attr_SoftwareCcwLimit_read) # 0xb9
        cmd_ProfileMode = self.write_Profile(self.ProfileType) # 0xc8
        # [issue]:
        # 不确定这个数值对归位方法有什么影响，这里用的write_Position会有什么影响，还需要考虑
        # cmd_Position = self.write_Position(self.attr_Position_read) # 0

        if cmd_DesiredState==cmd_HomingMethod==cmd_FastVelocity==\
            cmd_SlowVelocity==cmd_Acceleration==cmd_HomeOffset==\
            cmd_CurrentLimit==cmd_PositiveSoftwareLimit==cmd_NegativeSoftwareLimit==\
            cmd_ProfileMode==cmd_ProfileMode and cmd_DesiredState=='ok':
            result = 'ok'
            print('SetHomeParams() is OK.{}'.format(self.print_log('time_msg')))
        else:
            print('SetHomeParams() is ERROR.{}'.format(self.print_log('time_msg')))
            result = 'ERROR'        
        return result

class MoveHomeClass(SetHomeMethodClass):
    '''
        CopleyControl command methods
        properties: 由设备中的名称标识。通常，设备属性用于提供一种配置设备的方法。
        commands: 也由名称标识。命令执行时可能接收或不接收参数，并且可能会返回值。
    '''
    ## ------------------------MoveHome/Limit------------------------
    def MoveHome(self):
        ''' 
            executes the homing procedure.
        '''
        # self.debug_stream('In MoveHome()')
        argout = ''
        #----- PROTECTED REGION ID(CopleyControl.MoveHome) ENABLED START -----#
        cmd = self.setParamCmd('t', 2)
        argout = self.getValue(cmd)
        #----- PROTECTED REGION END -----#	//	CopleyControl.MoveHome
        return argout
    def MoveToCwLimit(self):
        '''
            moves the motor until the CW limit is reached (positive step direction). 
            Software limits are ignored. 
            StopMove works.
        '''
        argout = 0
        #----- PROTECTED REGION ID(CopleyControl.MoveToCwLimit) ENABLED START -----#
        limitStatus = self.checkLimit()
        if limitStatus != 1: # Positive limit switch is active.
            self.getValue(self.setParamCmd('0xc2', 516)) # Hard Stop - Positive
            self.MoveHome()
        else:
            print('Check Device State please.{}'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	CopleyControl.MoveToCwLimit
        return argout
    def MoveToCcwLimit(self):
        '''
            moves the motor until the CcW limit is reached (negative step direction). 
            Software limits are ignored. 
            StopMove works.
        '''
        argout = 0
        #----- PROTECTED REGION ID(CopleyControl.MoveToCcwLimit) ENABLED START -----#
        limitStatus = self.checkLimit()
        if limitStatus != 2: # Negative limit switch is active.
            self.getValue(self.setParamCmd('0xc2', 532)) # Hard Stop - Negative
            self.MoveHome()
        else:
            print('Check Device State please.{}'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	CopleyControl.MoveToCcwLimit
        return argout

# %%
class CopleyControlClass(MoveMotorClass,MoveHomeClass):
    '''
        Copley Control Class
    '''
# ------------------------------------------------------------------------------------------------
#                  CopleyControl Initial Device
# ------------------------------------------------------------------------------------------------
    def __init__(self, PortID, NodeID, Mode):
        #----- PROTECTED REGION ID(CopleyControl.__init__) ENABLED START -----#
        super(CopleyControlClass,self).__init__(PortID=PortID, NodeID=NodeID, Mode=Mode)
        self.inits_param()
        self.inits_device()
        # CopleyControlClass.init_device(self)
        #----- PROTECTED REGION END -----#	//	CopleyControl.__init__
    def __str__(self):
        msg = 'Copley Control Class'
        return msg
    def inits_param(self):
        # inits the device
        # self.debug_stream('In init_device()') # Sends the given message to the tango debug stream.
        self.attr_Position_read = 0 # 0x17: Limited position. targetPosition = Position + SetPoint
        self.attr_SetPoint_read = 0 # 0xca: Trajectory Generator Position Command(0xca).
        self.attr_DialPosition_read = 0
        self.attr_Conversion_read = 1 # The ratio between the position and the dial position. The default value is 1.0
        self.attr_Velocity_read = 0 # 0x18: Actual velocity. 这里将0xcb替换成了0x18
        self.attr_Acceleration_read = 0 # 0xcc: Maximum acceleration rate.
        self.attr_Deceleration_read = 0 # 0xcd: Maximum deceleration rate.
        self.attr_Current_read = 0 # 0x02: Programmed current value.
        self.attr_Current_ramp = 0 # 0x6a: Current ramp limit.

        self.attr_SoftwareCwLimit_read = 0 # 0xb8: Positive Software Limit
        self.attr_SoftwareCcwLimit_read = 0 # 0xb9: Negative Software Limit
        self.attr_SoftwareCwDialLimit_read = 0
        self.attr_SoftwareCcwDialLimit_read = 0
        self.attr_CwLimit_read = False # Positive limit switche is active
        self.attr_CcwLimit_read = False # Negative limit switche is active

        self.attr_HomingMethod_read = 0  # 0xc2 归位方法
        self.attr_HomingVelocityFast_read = 0 # 0xc3
        self.attr_HomingVelocitySlow_read = 0 # 0xc4
        self.attr_HomingAccDec_read = 0 # 0xc5
        self.attr_HomeOffset_read = 0 # 0xc6: Home Offset.
        self.attr_HomingCurrentLimit_read = 0 # 0xc7(0xbf)
        self.attr_CurrentDelayTime_read = 250 # 0xbf(0xc7)/ms
        
        self.argout = 'UNKNOWN'
        #----- PROTECTED REGION ID(CopleyControl.init_device) ENABLED START -----#
        self.DesiredState = 11
        self.ProfileType = 0 # 0xc8: Give trajectory profile mode(0xc8). Bits: *0\1\*256\257\*2

        self.targetPosition = 0
        self.attr_SetPoint_read = 0
        self.attr_Velocity_read = 0
        self.attr_Acceleration_read = 500
        self.attr_Deceleration_read = 500
        self.attr_Current_read = 0
        self.attr_Current_ramp = 0
    def inits_device(self):
        InitialDeviceClass.connectSerial(self, baud=defaultBaud, timeout=defaultTimeout)
        # InitialDeviceClass.changeSerialSpeed(self, baud=highBaud)
        # self.setInitParameters() # 由于涉及参数较多，直接在调用函数中传参，另外可以考虑将其单独作为了一个Class
        #----- PROTECTED REGION END -----#	//	CopleyControl.init_device
    def delete_device(self):
        # self.debug_stream('In delete_device()')
        # ----- PROTECTED REGION ID(CopleyControl.delete_device) ENABLED START -----#
        print('Delete Device.{}'.format(self.print_log('time_msg')))
        #----- PROTECTED REGION END -----#	//	CopleyControl.delete_device
    def always_executed_hook(self):
        # self.debug_stream('In always_excuted_hook()')
        #----- PROTECTED REGION ID(CopleyControl.always_executed_hook) ENABLED START -----#
        pass
        #----- PROTECTED REGION END -----#	//	CopleyControl.always_executed_hook


def main():
    copleycontrol = CopleyControlClass()

if __name__ == '__main__':
    main()