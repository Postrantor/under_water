#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    [20210904]:
        暂时先注释掉
        [issue]: `Software Limits are not set.` - 323
        [issue]: `Software Limits are not set.` - 366
'''
# %% import
from copley_lib.Class_InitialParameter import FormatCmdClass
from copley_lib.ParamDict_EventStatus import BitsMapped as BitsMapped_ES

# %% constant
from constant_lib.Constant_Unit import *
from constant_lib.Constant_Serial import *

# %% class
class CheckEventStateClass(FormatCmdClass):
    '''
        device state
        latched event status register
    '''
    ## ------------------------EventStatusRegister------------------------
    def readEventStatusRegister(self, node_id=0):
        '''
            return the event status register(0xa0_R*)
        '''
        #----- PROTECTED REGION ID(StateRegisteClass.readEventStatusRegister) ENABLED START -----#
        cmd = self.getParamCmd('0xa0', node_id)
        value = self.is_int(self.getValue(cmd), 'No Power')
        self.argout = str(value)
        #----- PROTECTED REGION END -----#	//	StateRegisteClass.readEventStatusRegister
        return self.argout
    def readLatchedEventStatus(self, node_id=0):
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
        cmd = self.getParamCmd('0xa1', node_id)
        value = self.is_int(self.getValue(cmd), 'No Power')
        self.argout = str(value)
        #----- PROTECTED REGION END -----#	//	StateRegisteClass.readLatchedEventStatus
        return self.argout
    def clearLatchedStatus(self, node_id=0):
        '''
            clear the latched status
            0xffffffff = b11111111111111111111111111111111 = o4294967295

            [issue]:
            竟然要先清除这个错误，在清除a1才能全部清除，否则a1的不能清除
            也就是如果a1中的22位有问题，需要先调用这里
        '''
        #----- PROTECTED REGION ID(StateRegisteClass.clearLatchedStatus) ENABLED START -----#
        self.clearFaultRegister()
        cmd_setLatched = self.setParamCmd('0xa1', 4294967295, node_id)
        value_setLatched =  self.getValue(cmd_setLatched)
        # [issue]:
        # 在这里需要判断一个返回的数据是什么，是ok还是数字，然后根据返回值，决定是return一个true或者其他；
        # 以此来告诉调用对象，现在的状态，不光是打印一串字符；
        result = 'clear the latched register and the current status is {}{}'.format(value_setLatched, self.print_log('time_msg', node_id))
        #----- PROTECTED REGION END -----#	//	StateRegisteClass.clearLatchedStatus
        return result
    def readFaultRegisterStatus(self, node_id=0):
        '''
            return the latched fault register status(0xA4)
            
            When latching fault has occurred, the fault bit (bit 22) of Event Status Register (0xA0) is set. 
            Cause of fault can be read from this register. To clear fault condition, write a 1 to associated bit in this register. Events that cause drive to latch fault are programmable. See Fault Mask (0xA7) for details.
        '''
        #----- PROTECTED REGION ID(StateRegisteClass.readFaultRegisterStatus) ENABLED START -----#
        cmd = self.getParamCmd('0xa4', node_id)
        value = self.is_int(self.getValue(cmd), 'No Power')
        self.argout = str(value)
        #----- PROTECTED REGION END -----#	//	StateRegisteClass.readFaultRegisterStatus
        return self.argout
    def clearFaultRegister(self, node_id=0):
        '''
            clear latched fault register
            0xffff = b1111111111111111 = o65535
        '''
        #----- PROTECTED REGION ID(StateRegisteClass.clearFaultRegister) ENABLED START -----#
        cmd_setFault = self.setParamCmd('0xa4', 65535, node_id)
        value_setFault =  self.getValue(cmd_setFault)
        # [issue]:
        # 在这里需要判断一个返回的数据是什么，是ok还是数字，然后根据返回值，决定是return一个true或者其他；
        # 以此来告诉调用对象，现在的状态，不光是打印一串字符；
        result = 'clear fault register and the current status is {}{}'.format(value_setFault, self.print_log('time_msg', node_id))
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
    def read_DesiredState(self, node_id=0): # -> attribute
        '''
            Desired State(0x24). Bits: 0~42(P19).
        '''
        # self.debug_stream('read_DesiredState()')
        #----- PROTECTED REGION ID(RWAttributesClass.read_DesiredState) ENABLED START -----#
        cmd = self.getParamCmd('0x24', node_id)
        data =  self.getValue(cmd)
        self.DesiredState = self.is_int(data, self.DesiredState)
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.read_DesiredState
        return self.DesiredState
    def write_DesiredState(self, data, node_id=0): # -> attribute
        '''
            * 0x24	R F	Desired state:\n
                                0 = Drive disabled.\n
                                1 = Programmed current value drives current loop\n
                                21 = Programmed Position Mode, Servo\n
                                31 = Programmed Position Mode, Stepper\n
        '''
        # self.debug_stream('write_DesiredState()')
        #----- PROTECTED REGION ID(RWAttributesClass.write_DesiredState) ENABLED START -----#
        data = self.is_int(data, self.DesiredState)
        cmd = self.setParamCmd('0x24', data, node_id)
        result = self.getValue(cmd)

        self.DesiredState = self.setValue(result, data, self.DesiredState)
        # print('Set Desired State to  ', str(self.DesiredState), 'counts/s.'.format(self.print_log('time_msg', node_id)))
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.write_DesiredState
        return result
    def read_Profile(self, node_id=0): # -> attribute
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
        cmd = self.getParamCmd('0xc8', node_id)
        data = self.getValue(cmd)
        self.ProfileType = self.is_int(data, self.ProfileType)
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.read_Profile
        return self.ProfileType
    def write_Profile(self, data, node_id=0): # -> attribute
        '''
            Profile type:
             - 0 = Absolute move, trapezoidal profile.
             - 1 = Absolute move, S-curve profile.
             - 256 = Relative move, trapezoidal profile.
             - 257 = Relative move, S-curve profile.
             - 2 = Velocity move.
        '''
        # self.debug_stream('write_Profile()')
        #----- PROTECTED REGION ID(RWAttributesClass.write_Profile) ENABLED START -----#
        data = self.is_int(data, self.ProfileType)
        if self.DesiredState==21: # Programmed Position Mode
            cmd = self.setParamCmd('0xc8', data, node_id)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('this is not position mode and the "DesiredState" is {}.{}'.format(self.DesiredState, self.print_log('time_msg', node_id)))
            result = 'ERROR'
        self.ProfileType = self.setValue(result, data, self.ProfileType)
        return result
        # print('Set Profile type to  ', str(self.ProfileType), 'counts/s.'.format(self.print_log('time_msg', node_id)))
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.write_Profile
    ## ------------------------AttrEncoder------------------------
    def write_Encoder(self, data, node_id=0): # -> order
        '''
            设置编码器的数值
            主要目的是为了设置编码器的位置为零，但是多加了一个参数，可以设定其他数值
            这个也算是为后面的力矩模式做准备，可以不将极限位置设置为0，也就是传其他数值的参数

            0x17    R F Actual Position. Units: Counts. 
                                Used to close position loop in drive every servo cycle. For single feedback systems, this value is same as Actual Motor Position (0x32). For dual feedback systems, this value is same as Load Encoder Position (0x112).
                                CANopen objects 0x6064 and 0x6063 hold same value.
            0x32    R* Actual Motor Position. Units: counts. 
                                Gives feedback position of motor. For single feedback systems, this is same as Actual Position (0x17).
        '''
        # self.debug_stream('write_Encoder()')
        #----- PROTECTED REGION ID(RWAttributesClass.Position_write) ENABLED START -----#
        data = self.is_int(data, self.attr_EncoderInitial_read)
        cmd = self.setParamCmd('0x17', data, node_id)
        result = self.getValue(cmd)

        self.attr_EncoderInitial_read = self.setValue(result, data, self.attr_EncoderInitial_read)
        #----- PROTECTED REGION END -----#	//	CopleyControl.Position_write
        return result # ok
    ## ------------------------AttrPosition------------------------
    def read_Position(self, node_id=0): # -> actual
        '''
            read actual position and convert unit to count.

            * 0x17	R	Actual Position. Units: Counts. 
                                Used to close position loop in drive every servo cycle. 
                                For single feedback systems, this value is same as Actual Motor Position (0x32). 
                                For dual feedback systems, this value is same as Load Encoder Position (0x112). 
                                CANopen objects 0x6064 and 0x6063 hold same value.
            [issue]:
            由0x17 -> 0x2d，0x2d在速度模式下是限制位置，位置模式下是实际位置；0x17在速度模式和位置模式下都可以用
            换句话说，取消了读取所有的限制值，后面可以考虑再写一些函数专门用来读取限制值
        '''
        # self.debug_stream('read_Position()')
        # print('read_Position()'+'{}'.format(self.print_log('time_msg', node_id)))
        #----- PROTECTED REGION ID(RWAttributesClass.Position_read) ENABLED START -----#   
        cmd = self.getParamCmd('0x17', node_id)
        data = self.getValue(cmd)
        self.attr_Position_read = self.is_int(data, self.attr_Position_read)
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Position_read
        return self.attr_Position_read
    def write_Position(self, data, node_id=0): # -> order
        '''
            absolute move

            * 0xca	R F	Trajectory Generator Position Command. Units: Counts.\n
                                This value gives destination position for absolute moves or move distance for relative moves. \n
                                Relative move = the distance of the move.\n
                                Absolute move = the target position of the move.\n
                                Velocity move = 1 for positive direction,\n
                                                              -1 for negative direction.\n
            [issue]: 需要设置软限位；这个已经在home中设置了，回头再看看
            0xb8
            0xb9
        '''
        # self.debug_log('write_Position()', node_id)
        #----- PROTECTED REGION ID(RWAttributesClass.Position_write) ENABLED START -----#
        self.targetPosition = self.is_int(data, self.targetPosition)
        # set attr_SetPoint_read
        self.attr_Position_read = self.read_Position(node_id)
        if self.ProfileType==256 or self.ProfileType==257: # relative move
            self.attr_SetPoint_read = self.targetPosition - int(self.attr_Position_read)
        elif self.ProfileType==0 or self.ProfileType==1: # absolute move
            self.attr_SetPoint_read = self.targetPosition
        # write attr_SetPoint_read to command
        # [issue]:
        # 在使用这个软件限制之前，是不是应该先读取一下
        if self.attr_SoftwareCwLimit_read==0 and self.attr_SoftwareCcwLimit_read==0:
            # [issue]: `Software Limits are not set.` - 323
            # print('Software Limits are not set.{}'.format(self.print_log('time_msg', node_id)))
            cmd = self.setParamCmd('0xca', self.attr_SetPoint_read, node_id)
            result = self.getValue(cmd)
        elif self.targetPosition in range(self.attr_SoftwareCcwLimit_read, self.attr_SoftwareCwLimit_read):
            cmd = self.setParamCmd('0xca', self.attr_SetPoint_read, node_id)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('The input is out of the valid range, check the software limits.{}'.format(self.print_log('time_msg', node_id)))
            result = 'ERROR'
        return result
        #----- PROTECTED REGION END -----#	//	CopleyControl.Position_write
    def read_SetPoint(self): # -> attribute
        # self.debug_stream('In read_SetPoint()')
        #----- PROTECTED REGION ID(CopleyControl.SetPoint_read) ENABLED START -----#

        #----- PROTECTED REGION END -----#	//	CopleyControl.SetPoint_read
        return self.attr_SetPoint_read
    def write_SetPoint(self, data, node_id=0): # -> order
        '''
            relative move

            0xca	R F	Trajectory Generator Position Command. Units: Counts.
                                This value gives destination position for absolute moves or move distance for relative moves. 
                                Relative move = the distance of the move.
                                Absolute move = the target position of the move.
                                Velocity move = 1 for positive direction,
                                                              -1 for negative direction.
            [issue]: 需要设置软限位
            0xb8
            0xb9
        '''
        # self.debug_stream('write_SetPoint()')
        #----- PROTECTED REGION ID(CopleyControl.SetPoint_write) ENABLED START -----#
        data = self.is_int(data, self.attr_SetPoint_read)
        # set targetPosition
        self.attr_Position_read = self.read_Position(node_id)
        if self.ProfileType==256 or self.ProfileType==257:
            self.targetPosition = data
        elif self.ProfileType==0 or self.ProfileType==1:
            self.targetPosition = data + self.attr_Position_read
        # write attr_SetPoint_read to command
        if self.attr_SoftwareCwLimit_read==0 and self.attr_SoftwareCcwLimit_read==0:
            # [issue]: `Software Limits are not set.` - 366
            # print('Software Limits are not set.{}'.format(self.print_log('time_msg', node_id)))
            cmd = self.setParamCmd('0xca', self.targetPosition, node_id)
            result = self.getValue(cmd) # self.write(cmd)
        elif self.targetPosition in range(self.attr_SoftwareCcwLimit_read, self.attr_SoftwareCwLimit_read):
            # print('SetPoint:', data, 'expected position: ', self.targetPosition, 'Ccwlimit: ', self.attr_SoftwareCcwLimit_read, 'Cwlimit: ', self.attr_SoftwareCwLimit_read)
            cmd = self.setParamCmd('0xca', self.targetPosition, node_id)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            # print('The input is out of range of the software limits.{}'.format(self.print_log('time_msg', node_id)))
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
    def write_DialPosition(self, data, node_id=0): # -> order
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
            cmd = self.setParamCmd('0xca', data_new, node_id)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('DialPosition is out of range.{}'.format(self.print_log('time_msg', node_id)))
            result = 'ERROR'
        return result
        #----- PROTECTED REGION END -----#	//	CopleyControl.DialPosition_write
    ## ------------------------AttrConversion------------------------
    def read_Conversion(self, node_id=0): # -> attribute
        '''
            The ratio between the position and the dial position. The default value is 1.0
        '''
        # self.debug_stream('In read_Conversion()')
        #----- PROTECTED REGION ID(RWAttributesClass.Conversion_read) ENABLED START -----#
        print('In ', self.dev_serial.port, '::read_Conversion()')
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Conversion_read
    def write_Conversion(self, data, node_id=0): # -> attribute
        '''
            The ratio between the position and the dial position. The default value is 1.0
        '''
        # self.debug_stream('In write_Conversion()')
        #----- PROTECTED REGION ID(RWAttributesClass.Conversion_write) ENABLED START -----#
        # [issue]: 应该有一个ascii
        self.attr_Conversion_read = data
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Conversion_write
    ## ------------------------AttrVelocity------------------------
    def read_Velocity(self, node_id=0): # -> actual
        '''
            read actual velocity and convert unit to counts/s, so data=data*unit
            This variable(0x18) differentiates between positive and negative

            - 0x18  R*   Actual Velocity. Units: 0.1 encoder counts/s.
                                For estimated velocity. Units: 0.01 RPM.
                                For stepper mode: Units: 0.1 microsteps/s.

            这里将0xcb -> 0x18，即读取实际的速度值且有符号，区别于0xcb读取的是设定的最大速度数值（是位置模式下的命令）
        '''
        # self.debug_stream('read_Velocity()')
        # print('read_Velocity()'+'{}'.format(self.print_log('time_msg', node_id)))
        #----- PROTECTED REGION ID(RWAttributesClass.Velocity_read) ENABLED START -----#
        cmd = self.getParamCmd('0x18', node_id)
        data = self.is_int(self.getValue(cmd), self.attr_Velocity_read)
        # [issue]:
        # 在这里转换成了int，想着这个单位是0.1，所以没有关系
        # 另外，在ROS里面发布的数值有一些变化
        self.attr_Velocity_read = data * unit_0x18
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Velocity_read
        return self.attr_Velocity_read
    def write_Velocity(self, data, node_id=0): # -> order
        '''
            write the target velocity value to the amplifire. include position & speed mode.

            * Programmed Position Mode(21)\n
                0xcb    R F Trajectory Maximum Velocity. Units: 0.1 counts/s.
                                    Trajectory generator will attempt to reach this velocity during a move.
            * Programmed Speed Mode(11)\n
                0x2f    R F Programmed Velocity Command(0x2f). Units: 0.1 encoder counts/s.
                                    Only used in Programmed Velocity Mode (Desired State (0x24) = 11)
                                    For estimated velocity. Units: 0.01 RPM.
                                    For stepper mode. Units: 0.1 microsteps/s.
        '''
        # [issue]:
        # 有些属性没有电流模式，应该是需要修改的
        # 但是电流模式感觉啥都没法控制
        argout = None
        # self.debug_stream('write_Velocity()')
        data = self.is_int(data, self.attr_Velocity_read)
        #----- PROTECTED REGION ID(RWAttributesClass.Velocity_write) ENABLED START -----#
        if self.DesiredState==21: # Programmed Position Mode
            velocity = data / unit_0xcb
            cmd = self.setParamCmd('0xcb', velocity, node_id)
            argout = self.getValue(cmd)
            # [issue]:
            # 需要完善，当设置为速度模式时候，速度的方向是由0xca指定的(1/-1)
        elif self.DesiredState==11: # Programmed Speed Mode
            velocity = data / unit_0x2f
            cmd = self.setParamCmd('0x2f', velocity, node_id)
            argout = self.getValue(cmd)
            # print('this is not position/speed mode and the "DesiredState" is {}.{}'.format(self.DesiredState, self.print_log('time_msg', node_id)))
        else:
            print('this is not position/speed mode and the "DesiredState" is {}.{}'.format(self.DesiredState, self.print_log('time_msg', node_id)))
            argout = 'ERROR'
        return argout
        # print('Set maximum(command) velocity to  ', str(velocity), 'counts/s.'.format(self.print_log('time_msg', node_id)))
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Velocity_write
    ## ------------------------AttrAc/Deceleration------------------------
    def read_Acceleration(self, node_id=0): # -> attribute
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
            cmd = self.getParamCmd('0xcc', node_id)
            data = self.is_int(self.getValue(cmd), self.attr_Acceleration_read)
            self.attr_Acceleration_read = data * unit_0xcc
        elif self.DesiredState==11: # Programmed Speed Mode
            cmd = self.getParamCmd('0x36', node_id)
            data = self.is_int(self.getValue(cmd), self.attr_Acceleration_read)
            self.attr_Acceleration_read = data * unit_0x36
        # print('Read maximum acceleration: ', str(acceleration), 'counts/s2')
        # conversion = 0.0025
        # realAcceleration = self.attr_Acceleration_read * conversion
        # print('Read motor real maximum acceleration: ', str(realAcceleration), 'counts/s2)')
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Acceleration_read
        return self.attr_Acceleration_read
    def write_Acceleration(self, data, node_id=0): # -> order
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
            cmd = self.setParamCmd('0xcc', acceleration, node_id)
            result = self.getValue(cmd)
        elif self.DesiredState==11: # Programmed Speed Mode
            acceleration = data / unit_0x36
            cmd = self.setParamCmd('0x36', acceleration, node_id)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('this is not position/speed mode and the "DesiredState" is {}.{}'.format(self.DesiredState, self.print_log('time_msg', node_id)))
            result = 'ERROR'
        self.attr_Acceleration_read = self.setValue(result, data, self.attr_Acceleration_read)
        return result
        # print('Set maximum acceleration to  ', str(acc), 'counts/s2.')
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Acceleration_write
    def read_Deceleration(self, node_id=0): # -> attribute
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
            cmd = self.getParamCmd('0xcd', node_id)
            data = self.is_int(self.getValue(cmd), self.attr_Deceleration_read)
            self.attr_Deceleration_read = data * unit_0xcd
        elif self.DesiredState==11: # Programmed Speed Mode
            cmd = self.getParamCmd('0x37', node_id)
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
    def write_Deceleration(self, data, node_id=0): # -> order
        '''
        '''
        # self.debug_stream('write_Deceleration()')
        data = self.is_int(data, self.attr_Deceleration_read)
        #----- PROTECTED REGION ID(RWAttributesClass.Deceleration_write) ENABLED START -----#
        #print('realDeceleration input is: ', int(data))
        #self.attr_Deceleration_read = int(data)*400
        if self.DesiredState==21: # Programmed Position Mode
            deceleration = data / unit_0xcd
            cmd = self.setParamCmd('0xcd', deceleration, node_id)
            result = self.getValue(cmd) # self.write(cmd)
        elif self.DesiredState==11: # Programmed Speed Mode
            deceleration = data / unit_0x37
            cmd = self.setParamCmd('0x37', deceleration, node_id)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('this is not position/speed mode and the "DesiredState" is {}.{}'.format(self.DesiredState, self.print_log('time_msg', node_id)))
            result = 'ERROR'
        self.attr_Deceleration_read = self.setValue(result, data, self.attr_Deceleration_read)
        return result
        # print('Set maximum deceleration to  ', str(deceleration), 'counts/s2.')
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Deceleration_write
    ## ------------------------AttrCurrent------------------------
    def read_Current(self, node_id=0): # ->actural
        '''
            - 0x0b  R*  Actual Current, D axis of rotor space. Units: 0.01 A.
            - 0x0c  R*  Actual Current, Q axis of rotor space. Units: 0.01 A.
                                The d axis, also known as the direct axis, is the axis by which flux is produced by the field winding. The q axis, or the quadrature axis is the axis on which torque is produced.
            - *0x38    R*  Actual Motor Current. Units: 0.01 A. This current is calculated based on both D and Q axis currents.
            
            A -> mA
        '''
        # self.debug_stream('read_Current()')
        # print('read_Current()'+'{}'.format(self.print_log('time_msg', node_id)))
        #----- PROTECTED REGION ID(RWAttributesClass.read_Current) ENABLED START -----#
        cmd = self.getParamCmd('0x38', node_id)
        data = self.is_int(self.getValue(cmd), self.attr_Current_read)
        self.attr_Current_read = data * unit_0x38 # mA
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.read_Current
        return self.attr_Current_read
    def write_Current(self, data, node_id=0): # -> attribute
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
            cmd = self.setParamCmd('0x02', current, node_id)
            result = self.getValue(cmd) # self.write(cmd)
            self.attr_Current_read = self.setValue(result, data, self.attr_Current_read)
        else:
            print('this is not current mode and the "DesiredState" is {}.{}'.format(self.DesiredState, self.print_log('time_msg', node_id)))
            result = 'ERROR'
        return result
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.Current_write
    def read_CurrentRamp(self, node_id=0): # ->attribute
        '''
            0x6a  R F Commanded Current Ramp Limit. Units: mA/s. 
                                Used when running in Current (Torque) mode. 
                                Setting this to zero disables slope limiting.
        '''
        # self.debug_stream('read_CurrentRamp')
        #----- PROTECTED REGION ID(RWAttributesClass.CurrentRamp_read) ENABLED START -----#
        cmd = self.getParamCmd('0x6a', node_id)
        data = self.is_int(self.getValue(cmd), self.attr_Current_ramp)
        self.attr_Current_ramp = data * unit_0x6a
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.CurrentRamp_read
        return self.attr_Current_ramp
    def write_CurrentRamp(self, data, node_id=0): # -> attribute
        '''
        '''
        # self.debug_stream('write_CurrentRamp')
        data = self.is_int(data, self.attr_Current_ramp)
        #----- PROTECTED REGION ID(RWAttributesClass.CurrentRamp_write) ENABLED START -----#
        if self.DesiredState==1: # Programmed Current Mode
            ramp = data / unit_0x6a
            cmd = self.setParamCmd('0x6a', ramp, node_id)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('this is not current mode and the "DesiredState" is {}.{}'.format(self.DesiredState, self.print_log('time_msg', node_id)))
            result = 'ERROR'
        self.attr_Current_ramp = self.setValue(result, data, self.attr_Current_ramp)
        return result
        #----- PROTECTED REGION END -----#	//	RWAttributesClass.CurrentRamp_write
    ## ------------------------@SetMode------------------------
    def setInitParameters(self, profile=1, pos=0, vel=0, acc=100, dec=100, cur=0, rap=0, node_id=0):
        '''
            initial parameters and sent to specified mode.
            :param profile:
            :param pos:
            :param vel:
            :param acc:
            :param dec:
            :param cur:
            :param rap:

            :param limit_p:
            :param limit_n:
            [issue]:
            这有一个作用，除了统一进行初始化外，还可以进行模式间的切换。
            例如，当前为速度模式运行，机器人暂时停顿一下(模式切换必要停顿0x24)，若此时设置了位置数值，也就暗示要切换成位置模式
            此时，直接在设置位置数值的下方再添加一句话就行，即调用相应的模式。因为调用模式的函数所传入的参数和初始化的参数是分离的，实际传入的是实时指定的数值。

            位置模式下也有速度模式，但是速度模式下能达到的速度值更大。位置模式下过大的速度会出现位置跟随错误，所以虽然位置模式也有速度模式，但是并不能舍弃速度模式。

            初始化参数如果是位置模式，需要增加两个限位，这里的限位不是用串口设置的，而是在软件里面；
            起初需要手动调整到合适的位置，调整之后，将此位置设置为0。
            之前也考虑过用串口来设置，但是这个限位在后来考虑过，发现主要是用在力矩模式下的，但是力矩模式下不能靠串口设定的值来限制（貌似只在位置模式下起作用），所以通过软限制来实现
        '''
        #----- PROTECTED REGION ID(SetModeClass.setInitParameters) ENABLED START -----#
        if self.Mode == 'Position':
            self.DesiredState = 21
            self.ProfileType = profile
            self.attr_SetPoint_read = pos
            self.attr_Velocity_read = vel
            self.attr_Acceleration_read = acc
            self.attr_Deceleration_read = dec
            self.setPositionMode(node_id)
        elif self.Mode == 'Speed':
            # [issue]: 这个初始化的参数会让电机直接动起来
            # 除非初始化的速度是0，所以有一点不安全
            self.DesiredState = 11
            self.attr_Velocity_read = vel
            self.attr_Acceleration_read = acc
            self.attr_Deceleration_read = dec
            self.setSpeedMode(node_id)
        elif self.Mode == 'Current':
            # [issue]: 这个初始化的参数会让电机直接动起来
            # 是否应该让这个参数1放在Move()方法中
            self.DesiredState = 1 # 应该设置为0合适，这里可以不设置为21，和停止不同，这个是初始化
            self.attr_Current_read = cur
            self.attr_Current_ramp = rap
            self.setCurrentMode(node_id)
        else:
            print('SetInitParameters() is ERROR{}'.format(self.print_log('time_msg', node_id)))
        #----- PROTECTED REGION END -----#	//	SetModeClass.setInitParameters
    def setPositionMode(self, node_id=0):
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
        cmd_state = self.write_DesiredState(self.DesiredState, node_id) # 21
        cmd_profile = self.write_Profile(self.ProfileType, node_id)
        cmd_pos = self.write_SetPoint(self.attr_SetPoint_read, node_id)
        cmd_vel = self.write_Velocity(self.attr_Velocity_read, node_id)
        cmd_acc = self.write_Acceleration(self.attr_Acceleration_read, node_id)
        cmd_dec = self.write_Deceleration(self.attr_Deceleration_read, node_id)
        if cmd_state==cmd_profile==cmd_pos==cmd_vel==cmd_acc==cmd_dec and cmd_state== 'ok':
            result = 'ok'
            print('SetPositionMode() is OK{}'.format(self.print_log('time_msg', node_id)))
        else:
            result = 'ERROR'
            print('SetPositionMode() is ERROR{}'.format(self.print_log('time_msg', node_id)))
        #----- PROTECTED REGION END -----#	//	SetModeClass.setPositionMode
        return result
    def setSpeedMode(self, node_id=0):
        ''' 
            Sets Programmed Speed Mode

            编程速度模式将驱动器的输出设置为编程速度。 在此模式下启用驱动器后，或更改了编程速度时，电动机速度将以编程速度升至新的水平。
            Parameter ID	Bank	Description
            * 0x24	R F	Programmed Velocity Mode (11).\n
            * 0x2f    R F Programmed Velocity Command(0x2f). Units: 0.1 encoder counts/s.\n
                                Only used in Programmed Velocity Mode (Desired State (0x24) = 11)
                                For estimated velocity. Units: 0.01 RPM.
                                For stepper mode. Units: 0.1 microsteps/s.
            * 0x36	R F	Velocity acceleration limit. Units: 1000 counts/second2\n
            * 0x37	R F	Velocity deceleration limit. Units: 1000 counts/second2\n
            [issue]:
            * 0x38	R*	Actual Motor Current. Units: 0.01 A. \n
                                This current is calculated based on both D and Q axis currents.\n
            * 0x39	R F	Fast stop ramp. Units: 1000 counts/second2\n
        '''
        #----- PROTECTED REGION ID(SetModeClass.setSpeedMode) ENABLED START -----#
        cmd_state = self.write_DesiredState(self.DesiredState, node_id) # 11
        cmd_vel = self.write_Velocity(self.attr_Velocity_read, node_id)
        cmd_acc = self.write_Acceleration(self.attr_Acceleration_read, node_id)
        cmd_dec = self.write_Deceleration(self.attr_Deceleration_read, node_id)
        if cmd_state==cmd_vel==cmd_acc==cmd_dec and cmd_state=='ok':
            result = 'ok'
            print('SetSpeedMode() is OK{}'.format(self.print_log('time_msg', node_id)))
        else:
            result = 'ERROR'
            print('SetSpeedMode() is ERROR{}'.format(self.print_log('time_msg', node_id)))
        #----- PROTECTED REGION END -----#	//	SetModeClass.setSpeedMode
        return result
    def setCurrentMode(self, node_id=0):
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
        cmd_state = self.write_DesiredState(self.DesiredState, node_id) # 1
        cmd_cur = self.write_Current(self.attr_Current_read, node_id)
        cmd_rap = self.write_CurrentRamp(self.attr_Current_ramp, node_id)
        if cmd_state==cmd_cur==cmd_rap and cmd_state=='ok':
            result = 'ok'
            print('SetCurrentMode() is OK{}'.format(self.print_log('time_msg', node_id)))
        else:
            result = 'ERROR'
            print('SetCurrentMode() is ERROR{}'.format(self.print_log('time_msg', node_id)))
        #----- PROTECTED REGION END -----#	//	SetModeClass.setCurrentMode
        return result

# %%
class MoveMotorClass(SetModeClass):
    '''
        Stop/Move
    '''
    def Move(self, node_id=0):
        ''' 
            triggers the motor to move.

            Trajectory Generator Position Command(0xca). Units: Counts.
            This value gives destination position for absolute moves or move distance for relative moves.
            Commanded Position(0x2d_R*). Units: counts. 
            
            [issue]:
            是否考虑要加入其它模式，相对stopMove()函数而言
        '''
        argout = None
        #----- PROTECTED REGION ID(CopleyControl.Move) ENABLED START -----#
        # 当数据都准备好了，然后再来调用的，因为只有一条指令，前面的都是验证是否满足执行的要求
        if self.Mode=='Position': # 这里不用DesiredState参数，是因为在电流模式初始化的时候，可能设置为0(防止突然启动)
            # 1.Relative move
            if self.ProfileType==256 or self.ProfileType==257:
                if self.attr_SetPoint_read==0: # 位置差已经消除变为零，但是这个差要从哪里获取，一直读参数吗？
                    print('The expected position is achieved.{}'.format(self.print_log('time_msg', node_id)))
                elif self.attr_SoftwareCwLimit_read==0 and self.attr_SoftwareCcwLimit_read==0:
                    # print('NO software limits are set.')
                    # self.setMoveParameters() # MovePostion(self)_Note
                    argout = self.getValue(self.setParamCmd('t', 1, node_id))
                    self.attr_SetPoint_read = 0 # 是否检测判断一下更好呢
                else:
                    status = str(self.dev_status())
                    current_position = self.getValue(self.getParamCmd('0x2d', node_id)) # Commanded Position(0x2d_R*).
                    self.targetPosition = int(current_position) + int(self.attr_SetPoint_read)
                    # 首先判断驱动器的状态是否可用，则设定参数，开始执行
                    if status=='Status is STANDBY' or status=='Positive limit switch Active' or status=='Negative limit switch Active':
                        if self.targetPosition in range(self.attr_SoftwareCcwLimit_read, self.attr_SoftwareCwLimit_read):
                            # print('The expected position ', self.targetPosition, ' is among the range from ', int(self.attr_SoftwareCcwLimit_read), ' to ', int(self.attr_SoftwareCwLimit_read))
                            # self.setMoveParameters() # MovePostion(self)_Note
                            argout = self.getValue(self.setParamCmd('t', 1, node_id))
                            self.attr_SetPoint_read = 0
                        else:
                            print('The expected position ', self.targetPosition, ' is not among the range from ', int(self.attr_SoftwareCcwLimit_read), ' to ', int(self.attr_SoftwareCwLimit_read))
                    else:
                        print('Check Device State please.{}'.format(self.print_log('time_msg', node_id)))
            # 2.Absolute move
            elif self.ProfileType==0 or self.ProfileType==1:
                if self.attr_SoftwareCcwLimit_read==0 and self.attr_SoftwareCwLimit_read==0:
                    # print('NO software limits are set.')
                    # self.setMoveParameters() # MovePostion(self)_Note
                    argout = self.getValue(self.setParamCmd('t', 1, node_id))
                    self.attr_SetPoint_read = 0
                else:
                    status = str(self.dev_status())
                    current_position = self.getValue(self.getParamCmd('0x17', node_id)) # 0x2d
                    self.targetPosition = int(current_position) + int(self.attr_SetPoint_read)

                    if status == 'Status is STANDBY' or status == 'Positive limit switch Active' or status == 'Negative limit switch Active':
                        if self.targetPosition >=self.attr_SoftwareCcwLimit_read and self.targetPosition <= self.attr_SoftwareCwLimit_read:
                            print('The expected position position ', self.targetPosition, ' is among the range from ', self.attr_SoftwareCcwLimit_read, ' to ', self.attr_SoftwareCwLimit_read)
                            # self.setMoveParameters() # MovePostion(self)_Note
                            argout = self.getValue(self.setParamCmd('t', 1, node_id))
                            self.attr_SetPoint_read = 0
                        else:
                            print('The expected position ', self.targetPosition, ' is not among the range from ', self.attr_SoftwareCcwLimit_read, ' to ', self.attr_SoftwareCwLimit_read)
                    else:
                        print('Check Device State please.{}'.format(self.print_log('time_msg', node_id)))
            # 3.Velocity move.
            elif self.ProfileType==2:
                # [issue]:
                # 方向的问题放在write_Position函数里面了
                argout = self.getValue(self.setParamCmd('t', 1, node_id))
        # 对于速度模式，只要是速度不为零，即开始运动
        elif self.Mode=='Speed':
            self.write_Velocity(self.attr_Velocity_read, node_id)
        # 对于电流模式，只要是0x24设置为1，即开始运动
        elif self.Mode=='Current':
            argout = self.getValue(self.setParamCmd('0x24', 1, node_id))
        else:
            argout = 'ERROR'
            print('Check Device State please.{}'.format(self.print_log('time_msg', node_id)))
        #----- PROTECTED REGION END -----#	//	CopleyControl.Move
        return argout
    def StopMove(self, node_id=0):
        ''' 
            stops a movement immediately.
            [issue]:
            这个需要考虑一下，当处于位置模式的时候，如果节点突然中断，或者人为中断，要电机立刻停转
        '''
        # self.debug_stream('StopMove()')
        #----- PROTECTED REGION ID(CmdMethodsClass.StopMove) ENABLED START -----#
        if self.Mode=='Position': # Programmed Position Mode
            cmd = self.setParamCmd('t', 0, node_id)
            result1 = self.getValue(cmd) # self.write(cmd)
            cmd = self.setParamCmd('0xcb', 0, node_id)
            result2 = self.getValue(cmd) # self.write(cmd)
            result = result1 # + result2
        elif self.Mode == 'Speed': # Programmed Speed Mode
            cmd = self.setParamCmd('0x2f', 0, node_id)
            result = self.getValue(cmd) # self.write(cmd)
        elif self.Mode == 'Current': # Programmed Current Mode
            # [issue]:
            # 如果突然关闭驱动器可能出现一些问题，比如无法维持当前位置，考虑切换成位置模式
            # 与此同时，要再度开启力矩模式就需要再重设0x24参数，需要更改Move()方法
            cmd = self.setParamCmd('0x24', 21, node_id)
            result = self.getValue(cmd) # self.write(cmd)
        else:
            print('StopMove() is ERROR.{}'.format(self.print_log('time_msg', node_id)))
            result = 'ERROR'
        #----- PROTECTED REGION END -----#	//	CmdMethodsClass.StopMove
        return result
    ## ------------------------Amplifire------------------------
    def StopAmplifire(self, node_id):
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
        cmd = self.setParamCmd('0x24', 0, node_id)
        result = self.getValue(cmd) # self.write(cmd)
        #----- PROTECTED REGION END -----#	//	CmdMethodsClass.StopMotor
        return result
    def ResetAmplifire(self, node_id=0):
        ''' 
            `r\n` Reset the amplifier immediately. 
            The amplifier baud rate is set to 9600 when the amplifier restarts.
            
            NOTE: 
                if a reset command is issued to an amplifier on a multi-drop network, error code 32, 'CAN Network communications failure,' will be received. 
                This is because the amplifier reset before responding to the gateway amplifier. 
                This error can be safely ignored in this circumstance.
        '''
        #----- PROTECTED REGION ID(CmdMethodsClass.ResetMotor) ENABLED START -----#
        cmd = self.setParamCmd('r', node_id)
        result = self.getValue(cmd) # self.write(cmd)
        #----- PROTECTED REGION END -----#	//	CmdMethodsClass.ResetMotor
        # [issue]:
        # error code 32, 'CAN Network communications failure'
        return result
