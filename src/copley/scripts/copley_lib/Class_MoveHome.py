#! /usr/bin/env python
# -*- coding:utf-8 -*-
from copley_lib.Class_InitialParameter import *
from copley_lib.Class_MoveMotor import CheckEventStateClass, SetModeClass

from copley_lib.ParamDict_HomingMethod import HomingMethod as BitsMapped_HM

# %%


class CheckHomeStatueClass(CheckEventStateClass):
    def read_CwLimit(self, node_id=0):  # -> attribute
        '''
            0xb8    R F Positive hardware limit.
                                2^9 = 512 正限位开关有效(Positive limit switch active)[电机轴已经接触到正限位开关。]
                                2^10 = 1024 负限位开关有效(Negative limit switch active)[电机轴已经接触到负限位开关。]

            [issue]:
            没有制造出这两个状态，但是有16、17；感觉这个9、10应该就是设置了b8、b9
        '''
        # ----- PROTECTED REGION ID(HomingMethodClass.CwLimit_read) ENABLED START -----#
        value = self.is_int(self.readLatchedEventStatus(), 0)
        self.attr_CwLimit_read = (int(value) & 512) != 0
        if self.attr_CwLimit_read:
            print('Positive limit switche is active.{}'.format(self.print_log('time_msg', node_id)))
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.CwLimit_read
        return self.attr_CwLimit_read

    def read_CcwLimit(self, node_id=0):  # -> attribute
        '''
            0xb9    R F Negative hardware limit.
        '''
        # ----- PROTECTED REGION ID(HomingMethodClass.CcwLimit_read) ENABLED START -----#
        value = self.is_int(self.readLatchedEventStatus(), 0)
        self.attr_CcwLimit_read = (int(value) & 1024) != 0
        if self.attr_CcwLimit_read:
            print('Negative limit switche is active.{}'.format(self.print_log('time_msg', node_id)))
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.CcwLimit_read
        return self.attr_CcwLimit_read

    def checkLimit(self, node_id=0):
        '''
            Check the Hardware limit switches.
        '''
        # ----- PROTECTED REGION ID(CopleyControl.programmer_methods) ENABLED START -----#
        # self.clearLatchedStatus()
        value = self.is_int(self.readLatchedEventStatus(), 0)
        if (int(value) & 1536) != 0:  # 9/10
            print('Positive and Negative limit switches are active.{}'.format(self.print_log('time_msg', node_id)))
            return 3
        elif (int(value) & 512) != 0:  # 9
            print('Positive limit switch is active.{}'.format(self.print_log('time_msg', node_id)))
            return 1
        elif (int(value) & 1024) != 0:  # 10
            print('Negative limit switch is active.{}'.format(self.print_log('time_msg', node_id)))
            return 2
        elif int(value) == 0 or (int(value) & 131072) != 0 or (int(value) & 65536) != 0 or (int(value) & 67108864) != 0:
            # Bit_17: Negative software limit condition
            # Bit_16: Positive software limit condition
            # Bit_26: Home switch is active
            print('NO limit switch is active.{}'.format(self.print_log('time_msg', node_id)))
            return 0

    def checkHomeStatus(self):
        '''
            Check the Home Switch status.
        '''
        # self.clearLatchedStatus()
        value = self.is_int(self.readLatchedEventStatus(), 0)
        if (value & 67108864) != 0:  # Bit_26: Home switch is active
            print('Home Switch is active.')
            return 1
        else:
            print('Home Switch is not active.')
            return 0


class SetHomeMethodClass(SetModeClass, CheckHomeStatueClass):
    '''
        SoftwareLimit
        HardwareLimit
        Homing
        AttrHardware
    '''
    # ------------------------Homing------------------------

    def read_HomingMethod(self, node_id=0):  # -> attribute # 0xc2
        '''
            0xc2    R F Homing Method Configuration.
        '''
        # ----- PROTECTED REGION ID(CopleyControl.HomingMethod_read) ENABLED START -----#
        cmd = self.getParamCmd('0xc2', node_id)
        homing = self.is_int(self.getValue(cmd), self.attr_HomingMethod_read)
        if self.DesiredState == 21:
            self.attr_HomingMethod_read = homing
            argout = BitsMapped_HM('0xC2', homing)  # -> str
        else:
            argout = 'ERROR'
            print('The Desired State is {}, doesn`t position mode.{}'.format(self.print_log('time_msg', node_id)))
        print('The homing method is {}'.format(argout, self.print_log('time_msg', node_id)))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.HomingMethod_read
        return self.attr_HomingMethod_read

    def write_HomingMethod(self, data, node_id=0):  # -> attribute
        '''
            0xc2

            [512, 544, 560, 513, 529, 545, 561, 514, 530, 546, 562, 610, 626, 516, 532, 548, 564, 771, 787, 515, 531, 803, 819, 867, 883, 547, 563, 611, 627,15]
        '''
        data = self.is_int(data, self.attr_HomingMethod_read)
        # ----- PROTECTED REGION ID(CopleyControl.HomingMethod_write) ENABLED START -----#
        HomeRefNrList = [512, 544, 560, 513, 529, 545, 561, 514, 530, 546, 562, 610, 626, 516, 532, 548, 564, 771, 787, 515, 531, 803, 819, 867, 883, 547, 563, 611, 627, 15]
        if data in HomeRefNrList:
            cmd = self.setParamCmd('0xc2', data, node_id)
            result = self.getValue(cmd)
        else:
            result = 'ERROR'
            print('Input home reference number: {} is not valid.{}'.format(data, self.print_log('time_msg', node_id)))

        self.attr_HomingMethod_read = self.setValue(result, data, self.attr_HomingMethod_read)
        # ----- PROTECTED REGION END -----#	//	CopleyControl.HomingMethod_write
        return result

    def read_HomingVelocityFast(self, node_id=0):  # -> attribute # 0xc3
        """
            0xc3    R F Homing Velocity (fast moves). Units: 0.1 counts/s.
                                This velocity value is used during segments of homing procedure that may be handled at high speed. Generally, this means moves in which home sensor is being located, but edge of sensor is not being found.
        """
        # self.debug_stream('read_HomingVelocityFast()')
        # ----- PROTECTED REGION ID(HomingMethodClass.read_HomingVelocityFast) ENABLED START -----#
        cmd = self.getParamCmd('0xc3', node_id)
        data = self.is_int(self.getValue(cmd), self.attr_HomingVelocityFast_read)
        self.attr_HomingVelocityFast_read = data * unit_0xc3
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.read_HomingVelocityFast
        return self.attr_HomingVelocityFast_read

    def write_HomingVelocityFast(self, data, node_id=0):  # -> attribute
        '''
        '''
        # self.debug_stream('write_HomingVelocityFast()')
        data = self.is_int(data, self.attr_HomingVelocityFast_read)
        # ----- PROTECTED REGION ID(RWAttributesClass.write_HomingVelocityFast) ENABLED START -----#
        velocity = data / unit_0xc3
        cmd = self.setParamCmd('0xc3', velocity, node_id)
        result = self.getValue(cmd)  # self.write(cmd)
        self.attr_HomingVelocityFast_read = self.setValue(result, data, self.attr_HomingVelocityFast_read)
        # print('set homing velocity fast to  ', str(velocity), 'counts/s.'.format(self.print_log('time_msg', node_id)))
        # ----- PROTECTED REGION END -----#	//	RWAttributesClass.write_HomingVelocityFast
        return result

    def read_HomingVelocitySlow(self, node_id=0):  # -> attribute # 0xc4
        """
            0xc4    R F Homing Velocity (slow moves). Units: 0.1 counts/s.
                                This velocity value is used for homing segments that require low speed, such as cases where edge of a homing sensor is being sought.
        """
        # self.debug_stream('read_HomingVelocitySlow()')
        # ----- PROTECTED REGION ID(HomingMethodClass.read_HomingVelocitySlow) ENABLED START -----#
        cmd = self.getParamCmd('0xc4', node_id)
        data = self.is_int(self.getValue(cmd), self.attr_HomingVelocitySlow_read)
        self.attr_HomingVelocitySlow_read = data * unit_0xc4
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.read_HomingVelocitySlow
        return self.attr_HomingVelocitySlow_read

    def write_HomingVelocitySlow(self, data, node_id=0):  # -> attribute
        '''
            0xc4
        '''
        # self.debug_stream('write_HomingVelocitySlow()')
        data = self.is_int(data, self.attr_HomingVelocitySlow_read)
        # ----- PROTECTED REGION ID(RWAttributesClass.write_HomingVelocitySlow) ENABLED START -----#
        velocity = data / unit_0xc4
        cmd = self.setParamCmd('0xc4', velocity, node_id)
        result = self.getValue(cmd)  # self.write(cmd)
        self.attr_HomingVelocitySlow_read = self.setValue(result, data, self.attr_HomingVelocityFast_read)
        # print('set homing velocity slow to  ', str(velocity), 'counts/s.'.format(self.print_log('time_msg', node_id)))
        # ----- PROTECTED REGION END -----#	//	RWAttributesClass.write_HomingVelocitySlow
        return result

    def read_HomingAccDec(self, node_id=0):  # -> attribute # 0xc5
        """
            0xc5    R F Homing Acceleration/Deceleration. Units: 10 counts/s2.
                                This value defines acceleration used for all homing moves. Same value is used at beginning and ending of moves (i.e. no separate deceleration value).
        """
        # self.debug_stream('read_HomingAccDec()')
        # ----- PROTECTED REGION ID(HomingMethodClass.read_HomingAccDec) ENABLED START -----#
        cmd = self.getParamCmd('0xc5', node_id)
        data = self.is_int(self.getValue(cmd), self.attr_HomingAccDec_read)
        self.attr_HomingAccDec_read = data * unit_0xc5
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.read_HomingAccDec
        return self.attr_HomingAccDec_read

    def write_HomingAccDec(self, data, node_id=0):  # -> attribute
        # self.debug_stream('write_HomingAccDec()')
        data = self.is_int(data, self.attr_HomingAccDec_read)
        # ----- PROTECTED REGION ID(RWAttributesClass.write_HomingAccDec) ENABLED START -----#
        accdec = data / unit_0xc5
        cmd = self.setParamCmd('0xc5', accdec, node_id)
        result = self.getValue(cmd)  # self.write(cmd)
        self.attr_HomingAccDec_read = self.setValue(result, data, self.attr_HomingAccDec_read)
        # print('set homing acc\dec to  ', str(accdec), 'counts/s2.'.format(self.print_log('time_msg', node_id)))
        # ----- PROTECTED REGION END -----#	//	RWAttributesClass.write_HomingAccDec
        return result

    def read_HomeOffset(self, node_id=0):  # -> attribute # 0xc6/0
        '''
            0xc6    R F Home Offset. Units: counts.
                Home offset is difference between zero position for application and machine home position (found during homing). Once homing is completed, new zero position determined by homing state machine will be located sensor position plus this offset. All subsequent absolute moves shall be taken relative to this new zero position.

            默认值为0，这个数值可以忽略
        '''
        # self.debug_stream('read_HomeOffset()')
        # ----- PROTECTED REGION ID(HomingMethodClass.HomeOffset_read) ENABLED START -----#
        cmd = self.getParamCmd('0xc6', node_id)
        self.attr_HomeOffset_read = self.is_int(self.getValue(cmd), self.attr_HomeOffset_read)
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.HomeOffset_read
        return self.attr_HomeOffset_read

    def write_HomeOffset(self, data, node_id=0):
        '''
        '''
        # self.debug_stream('write_HomeOffset()')
        # ----- PROTECTED REGION ID(HomingMethodClass.HomeOffset_write) ENABLED START -----#
        data = self.is_int(data, self.attr_HomeOffset_read)
        cmd = self.setParamCmd('0xc6', data, node_id)
        result = self.getValue(cmd)

        self.attr_HomeOffset_read = self.setValue(result, data, self.attr_HomeOffset_read)
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.HomeOffset_write
        return result

    def read_HomingCurrentLimit(self, node_id=0):  # -> attribute # 0xc7
        """
            0xc7    R F Homing Current Limit. Units: 0.01 A.
                                Used in Home to Hard Stop mode only, this current is used to determine when drive has reached end of travel (hard stop). Used in conjunction with Home to Hard Stop Delay Time (0xBF).

            unit: A -> mA
        """
        # self.debug_stream('read_HomingCurrentLimit()')
        # ----- PROTECTED REGION ID(HomingMethodClass.read_HomingCurrentLimit) ENABLED START -----#
        cmd = self.getParamCmd('0xc7', node_id)
        data = self.is_int(self.getValue(cmd), self.attr_HomingCurrentLimit_read)
        self.attr_HomingCurrentLimit_read = data * unit_0xc7
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.read_HomingCurrentLimit
        return self.attr_HomingCurrentLimit_read

    def write_HomingCurrentLimit(self, data, node_id=0):  # -> attribute
        # self.debug_stream('write_HomingCurrentLimit()')
        data = self.is_int(data, self.attr_HomingCurrentLimit_read)
        # ----- PROTECTED REGION ID(RWAttributesClass.write_HomingCurrentLimit) ENABLED START -----#
        curlimit = data / unit_0xc7
        cmd = self.setParamCmd('0xc7', curlimit, node_id)
        result = self.getValue(cmd)  # self.write(cmd)
        self.attr_HomingCurrentLimit_read = self.setValue(result, data, self.attr_HomingCurrentLimit_read)
        # print('set homing current limit to  ', str(curlimit), 'mA.'.format(self.print_log('time_msg', node_id)))
        # ----- PROTECTED REGION END -----#	//	RWAttributesClass.write_HomingCurrentLimit
        return result
    # ------------------------SoftwareLimit------------------------

    def read_SoftwareCwLimit(self, node_id=0):  # -> attribute # 0xb8
        '''
            0xb8    R F Positive Software Limit value. Units: counts. 
                This parameter is only available on drives that support trajectory generation and homing. 
                Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). 
                Set to less than negative software limit to disable.
        '''
        # self.debug_stream('In read_SoftwareCwLimit()')
        # ----- PROTECTED REGION ID(HomingMethodClass.SoftwareCwLimit_read) ENABLED START -----#
        cmd = self.getParamCmd('0xb8', node_id)
        self.attr_SoftwareCwLimit_read = self.is_int(self.getValue(cmd), self.attr_SoftwareCwLimit_read)
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.SoftwareCwLimit_read
        return self.attr_SoftwareCwLimit_read

    def write_SoftwareCwLimit(self, data, node_id=0):  # -> attribute
        '''
            0xb8
        '''
        # self.debug_stream('In write_SoftwareCwLimit()')
        data = self.is_int(data, self.attr_SoftwareCwLimit_read)
        # ----- PROTECTED REGION ID(HomingMethodClass.SoftwareCwLimit_write) ENABLED START -----#
        # print('SoftwareCwLimit:', data, 'current position: ', self.attr_Position_read, 'Ccwlimit: ', self.attr_SoftwareCcwLimit_read, 'Cwlimit: ', self.attr_SoftwareCwLimit_read)
        self.targetPosition = self.attr_Position_read + self.attr_SetPoint_read
        if self.targetPosition in range(self.attr_SoftwareCcwLimit_read, data):
            cmd = self.setParamCmd('0xb8', data, node_id)
            result = self.getValue(cmd)
        else:
            result = 'ERROR'
            print('SoftwareCwLimit must be higher than `current Position` + `current SetPoint`.{}'.format(self.print_log('time_msg', node_id)))
        self.attr_SoftwareCwLimit_read = self.setValue(result, data, self.attr_SoftwareCwLimit_read)
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.SoftwareCwLimit_write
        return result

    def read_SoftwareCcwLimit(self, node_id=0):  # -> attribute # 0xb9
        '''
            # 0xb9 R F  Negative Software Limit. Units: counts. 
                Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). Set to greater than positive software limit to disable.
        '''
        # ----- PROTECTED REGION ID(HomingMethodClass.read_SoftwareCcwLimit) ENABLED START -----#
        cmd = self.getParamCmd('0xb9', node_id)
        self.attr_SoftwareCcwLimit_read = self.is_int(self.getValue(cmd), self.attr_SoftwareCcwLimit_read)
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.read_SoftwareCcwLimit
        return self.attr_SoftwareCcwLimit_read

    def write_SoftwareCcwLimit(self, data, node_id=0):  # -> attribute
        '''
        '''
        data = self.is_int(data, self.attr_SoftwareCcwLimit_read)
        # ----- PROTECTED REGION ID(HomingMethodClass.write_SoftwareCcwLimit) ENABLED START -----#
        self.targetPosition = self.attr_Position_read + self.attr_SetPoint_read
        if data < self.targetPosition:
            cmd = self.setParamCmd('0xb9', data, node_id)
            result = self.getValue(cmd)
        else:
            result = 'ERROR'
            print('SoftwareCcwLimit must be smaller than `Position` + `SetPoint`.{}'.format(self.print_log('time_msg', node_id)))

        self.setValue(result, data, self.attr_SoftwareCcwLimit_read)
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.write_SoftwareCcwLimit
        return result

    def read_SoftwareCwDialLimit(self):  # -> attribute # 0xb8
        '''
            0xb8    R F Positive Software Limit value. Units: counts. 
                This parameter is only available on drives that support trajectory generation and homing. 
                Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). 
                Set to less than negative software limit to disable.
        '''
        # ----- PROTECTED REGION ID(CopleyControl.SoftwareCwDialLimit_read) ENABLED START -----#
        self.attr_SoftwareCwLimit_read = self.read_SoftwareCwLimit()
        self.attr_SoftwareCwDialLimit_read = int(float(self.attr_SoftwareCwLimit_read) / float(self.attr_Conversion_read))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCwDialLimit_read
        return self.attr_SoftwareCwDialLimit_read

    def write_SoftwareCwDialLimit(self, data, node_id=0):  # -> attribute
        '''
        '''
        data = self.is_int(data, self.attr_SoftwareCwDialLimit_read)
        # ----- PROTECTED REGION ID(CopleyControl.SoftwareCwDialLimit_write) ENABLED START -----#
        self.attr_SoftwareCwLimit_read = self.attr_Conversion_read * data
        cmd = self.setParamCmd('0xb8', self.attr_SoftwareCwLimit_read, node_id)
        result = self.getValue(cmd)

        self.attr_SoftwareCwDialLimit_read = self.setValue(result, data, self.attr_SoftwareCwDialLimit_read)
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCwDialLimit_write
        return result

    def read_SoftwareCcwDialLimit(self):  # -> attribute # 0xb9
        '''
            0xb9    R F Negative Software Limit. Units: counts. 
                Software limits are only in effect after drive has been referenced (i.e. homing has been successfully completed). 
                Set to greater than positive software limit to disable.
        '''
        # ----- PROTECTED REGION ID(CopleyControl.SoftwareCcwDialLimit_read) ENABLED START -----#
        self.attr_SoftwareCcwLimit_read = self.read_SoftwareCcwLimit()
        self.attr_SoftwareCcwDialLimit_read = int(float(self.attr_SoftwareCcwLimit_read) / float(self.attr_Conversion_read))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCcwDialLimit_read
        return self.attr_SoftwareCcwDialLimit_read

    def write_SoftwareCcwDialLimit(self, data, node_id=0):  # -> attribute
        '''
        '''
        data = self.is_int(data, self.attr_SoftwareCcwDialLimit_read)
        # ----- PROTECTED REGION ID(CopleyControl.SoftwareCcwDialLimit_write) ENABLED START -----#
        self.attr_SoftwareCcwLimit_read = self.attr_Conversion_read * data
        cmd = self.setParamCmd('0xb9', self.attr_SoftwareCcwLimit_read, node_id)
        result = self.getValue(cmd)

        self.attr_SoftwareCcwDialLimit_read = self.setValue(result, data, self.attr_SoftwareCcwDialLimit_read)
        # ----- PROTECTED REGION END -----#	//	CopleyControl.SoftwareCcwDialLimit_write
        return result
    # ------------------------HardwareLimit------------------------

    def read_attr_hardware(self):  # -> attribute
        self.debug_stream('read_attr_hardware()')
        # ----- PROTECTED REGION ID(HomingMethodClass.read_attr_hardware) ENABLED START -----#
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.read_attr_hardware

    def read_CurrentDelayTime(self, node_id=0):  # -> attribute # 0xbf(->0xc7)/250
        """
            0xbf    R F Home to Hard Stop Delay Time. Units: ms. 
                                When performing home to hard stop, drive will push against stop for this long before sampling home position.
            0xc7
        """
        # self.debug_stream('read_CurrentDelayTime()')
        # ----- PROTECTED REGION ID(HomingMethodClass.read_CurrentDelayTime) ENABLED START -----#
        cmd = self.getParamCmd('0xc3', node_id)
        data = self.is_int(self.getValue(cmd), self.attr_CurrentDelayTime_read)
        self.attr_CurrentDelayTime_read = data
        # ----- PROTECTED REGION END -----#	//	HomingMethodClass.read_CurrentDelayTime
        return self.attr_CurrentDelayTime_read

    def write_CurrentDelayTime(self, data, node_id=0):  # -> attribute
        '''
            0xbf
        '''
        # self.debug_stream('write_CurrentDelayTime()')
        data = self.is_int(data, self.attr_CurrentDelayTime_read)
        # ----- PROTECTED REGION ID(RWAttributesClass.write_CurrentDelayTime) ENABLED START -----#
        cmd = self.setParamCmd('0xc3', data, node_id)
        result = self.getValue(cmd)  # self.write(cmd)
        self.attr_CurrentDelayTime_read = self.setValue(result, data, self.attr_CurrentDelayTime_read)
        # print('set current delay time to  ', str(data), 'ms.'.format(self.print_log('time_msg', node_id)))
        # ----- PROTECTED REGION END -----#	//	RWAttributesClass.write_CurrentDelayTime
        return result
    # ------------------------setHomeParam------------------------

    def setHomeParams(self, homing=512, node_id=0):
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
        self.attr_HomingMethod_read = self.is_int(homing, 512)  # 512: Set Current Position as Home.

        cmd_DesiredState = self.write_DesiredState(self.DesiredState, node_id)  # 0x24/21
        cmd_HomingMethod = self.write_HomingMethod(self.attr_HomingMethod_read, node_id)  # 0xc2
        cmd_FastVelocity = self.write_HomingVelocityFast(self.attr_HomingVelocityFast_read, node_id)  # 0xc3=Velocity
        cmd_SlowVelocity = self.write_HomingVelocitySlow(self.attr_HomingVelocitySlow_read, node_id)  # 0xc4=3333
        cmd_Acceleration = self.write_HomingAccDec(self.attr_HomingAccDec_read, node_id)  # 0xc5=acc
        cmd_HomeOffset = self.write_HomeOffset(self.attr_HomeOffset_read, node_id)  # 0xc6=0
        cmd_CurrentLimit = self.write_HomingCurrentLimit(self.attr_HomingCurrentLimit_read, node_id)  # 0xc7=173、19mA
        cmd_PositiveSoftwareLimit = self.write_SoftwareCwLimit(self.attr_SoftwareCwLimit_read, node_id)  # 0xb8
        cmd_NegativeSoftwareLimit = self.write_SoftwareCcwLimit(self.attr_SoftwareCcwLimit_read, node_id)  # 0xb9
        cmd_ProfileMode = self.write_Profile(self.ProfileType)  # 0xc8
        # [issue]:
        # 不确定这个数值对归位方法有什么影响，这里用的write_Position会有什么影响，还需要考虑
        # cmd_Position = self.write_Position(self.attr_Position_read) # 0

        if cmd_DesiredState == cmd_HomingMethod == cmd_FastVelocity ==\
                cmd_SlowVelocity == cmd_Acceleration == cmd_HomeOffset ==\
                cmd_CurrentLimit == cmd_PositiveSoftwareLimit == cmd_NegativeSoftwareLimit ==\
                cmd_ProfileMode == cmd_ProfileMode and cmd_DesiredState == 'ok':
            result = 'ok'
            print('SetHomeParams() is OK.{}'.format(self.print_log('time_msg', node_id)))
        else:
            print('SetHomeParams() is ERROR.{}'.format(self.print_log('time_msg', node_id)))
            result = 'ERROR'
        return result


class MoveHomeClass(SetHomeMethodClass):
    '''
        CopleyControl command methods
        properties: 由设备中的名称标识。通常，设备属性用于提供一种配置设备的方法。
        commands: 也由名称标识。命令执行时可能接收或不接收参数，并且可能会返回值。
    '''
    # ------------------------MoveHome/Limit------------------------

    def MoveHome(self, node_id=0):
        ''' 
            executes the homing procedure.
        '''
        # self.debug_stream('In MoveHome()')
        argout = ''
        # ----- PROTECTED REGION ID(CopleyControl.MoveHome) ENABLED START -----#
        cmd = self.setParamCmd('t', 2, node_id)
        argout = self.getValue(cmd)
        # ----- PROTECTED REGION END -----#	//	CopleyControl.MoveHome
        return argout

    def MoveToCwLimit(self, node_id=0):
        '''
            moves the motor until the CW limit is reached (positive step direction). 
            Software limits are ignored. 
            StopMove works.
        '''
        argout = 0
        # ----- PROTECTED REGION ID(CopleyControl.MoveToCwLimit) ENABLED START -----#
        limitStatus = self.checkLimit()
        if limitStatus != 1:  # Positive limit switch is active.
            self.getValue(self.setParamCmd('0xc2', 516, node_id))  # Hard Stop - Positive
            self.MoveHome()
        else:
            print('Check Device State please.{}'.format(self.print_log('time_msg', node_id)))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.MoveToCwLimit
        return argout

    def MoveToCcwLimit(self, node_id=0):
        '''
            moves the motor until the CcW limit is reached (negative step direction). 
            Software limits are ignored. 
            StopMove works.
        '''
        argout = 0
        # ----- PROTECTED REGION ID(CopleyControl.MoveToCcwLimit) ENABLED START -----#
        limitStatus = self.checkLimit()
        if limitStatus != 2:  # Negative limit switch is active.
            self.getValue(self.setParamCmd('0xc2', 532, node_id))  # Hard Stop - Negative
            self.MoveHome()
        else:
            print('Check Device State please.{}'.format(self.print_log('time_msg', node_id)))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.MoveToCcwLimit
        return argout
