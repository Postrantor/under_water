#! /usr/bin/env python
# -*- coding:utf-8 -*-
# %% import
import time
import serial
# import sys
# import os
from copley_lib.ErrorCodes import CodesMapped

# %% constant
from constant_lib.Constant_Unit import *
from constant_lib.Constant_Serial import *

# %% class


class InitialDeviceClass(object):
    '''
        Initial with the pyserial device.
        :def connectSerial: connect the device with the default parameters.
        :def changeSerialSpeed: change the baudrate to specified num.
        :def openSerialPort:
        :def is_number: confirm the input is number when set attributes.
        :def print_log: debug, output the device info and time.

        initial the devide ports info.
        :@param PortID->(str): serial port id.
        :@param NodeID->(int): canopen node ID. 暂时先留着吧
        :@param Mode->(str): sets programmed mode.
    '''

    def initialParameter(self, PortID='/dev/ttyUSB0', NodeID=0, Mode='Position'):
        # ----- PROTECTED REGION ID(CopleyControl.__init__) ENABLED START -----#
        if isinstance(PortID, str):
            self.PortID = PortID
        else:
            print('NodeID is not string: {}'.format(PortID))
        # [issue]:
        # 整个系统已经舍弃了self.NodeID参数，因为一个串口上传了多个电机，而self.NodeID最好只绑定一个值
        # 但是这个暂时先留着吧
        try:
            self.NodeID = str(int(NodeID))
        except Exception:
            print('NodeID is not number: {}'.format(NodeID))
        if isinstance(Mode, str) and (Mode == 'Position' or Mode == 'Speed' or Mode == 'Current'):
            self.Mode = Mode
        else:
            print('NodeID is not defined string(Position, Speed, Current): {}'.format(Mode))
        # [issue]: 放在这里不太完美
        self.connectSerial()
    # ------------------------

    def connectSerial(self, baud=defaultBaud, timeout=defaultTimeout):
        '''
            connects with the pyserial device and make the pyserial state be open.
        '''
        # self.debug_stream('connectSerial')
        # ----- PROTECTED REGION ID(InitialDeviceClass.connectSerial) ENABLED START -----#
        self.dev_serial = serial.Serial()
        self.dev_serial.port = self.PortID  # 获取当前usb端口: `python -m serial.tools.list_ports`
        self.dev_serial.baudrate = baud  # serial port baud rate: 9600 ~ 115200
        self.dev_serial.timeout = timeout  # 超时设置，None=永远等待操作；0=立即返回请求结果；Num(其他数值)=等待时间(s)
        # self.dev_serial.parity=PARITY_EVEN,
        # self.dev_serial.stopbits=STOPBITS_ONE,
        # self.dev_serial.bytesize=SEVENBITS, # 该处会使编码发生变化，需要注释
        # self.dev_serial.xonxoff=0 # 软件流控
        self.openSerialPort()
        # [issue]: 在每次重启系统的时候，是否需要重置编码器的位置
        # 有些参数需要重置，比如编码器位置，如果不是断电重启的话，是不会复位的；
        # 但是如果是在运行途中系统问题，仅仅需要重启系统，而且不方便调整机械机构的话，就不能要这行代码，不然编码器的位置会被清除
        # 可以折中，使用日志文件的方式来记录，最后时刻的位置
        # 判断上位机端口是否打开
        if self.dev_serial.isOpen() and self.dev_serial.readable():
            # 尝试以9600发送0x90指令，并获取返回值；若返回值存在，且为9600， 则执行changeSerialSpeed()
            if self.getSerialBaud(baud=defaultBaud):
                self.changeSerialBaud()
            # 若返回值为None，则尝试以115200发送0x90指令，并获取返回值；若返回值存在,且为115200，则退出
            elif self.getSerialBaud(baud=highBaud):
                print('Successful connect the port: {}'.format(self.print_log('full_msg')))
            # 实在没办法了，试试呗
            else:
                # self.dev_serial.close()
                # self.dev_serial.baudrate=9600
                # time.sleep(1)
                # self.openSerialPort()
                # self.dev_serial.write('{} r\n'.format(self.NodeID))
                # time.sleep(5)
                # self.changeSerialBaud()
                print('Serial Port is ERROR.{}'.format(self.print_log('full_msg')))
        else:
            print('Serial Port is Close.{}'.format(self.print_log('full_msg')))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.connectSerial

    def getSerialBaud(self, node_id=0, baud=defaultBaud):
        '''
            match the current port baudrate
        '''
        # ----- PROTECTED REGION ID(InitialDeviceClass.getSerialBaud) ENABLED START -----#
        self.dev_serial.close()
        self.dev_serial.baudrate = baud
        time.sleep(1)
        self.openSerialPort()
        self.dev_serial.write('{} g r0x90\n'.format(node_id))  # serial port baud rate. Units: bits/s.
        current_baud = self.dev_serial.read_until('\r')[2:-1]
        if current_baud.isdigit():
            print('The port baud rate: {}'.format(self.dev_serial.baudrate))
            return True
        else:
            print('Current Baudrates do not match: {}'.format(self.dev_serial.baudrate))
            return False
        # ----- PROTECTED REGION END -----#	//	CopleyControl.getSerialBaud

    def changeSerialBaud(self, node_id=0, baud=highBaud):
        '''
            change the serial port baudrate
        '''
        # ----- PROTECTED REGION ID(InitialDeviceClass.changeSerialSpeed) ENABLED START -----#
        self.openSerialPort()
        self.dev_serial.write('{} s r0x90 {}\n'.format(node_id, baud))  # serial port baud rate. Units: bits/s.
        self.dev_serial.close()
        self.dev_serial.baudrate = baud
        time.sleep(1)
        self.openSerialPort()
        self.dev_serial.write('{} g r0x90\n'.format(node_id))  # serial port baud rate. Units: bits/s.
        current_baud = self.dev_serial.read_until('\r')[2:-1]
        if current_baud.isdigit():
            print('Successful change the port baud rate: {}'.format(self.dev_serial.baudrate))
        else:
            print('Failure change the port baud rate: {}'.format(self.dev_serial.baudrate))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.changeSerialSpeed

    def openSerialPort(self):
        '''
            open serial port and catch exceptions

            如果有端口连接的问题，打开print来调试
            在这里使用try捕获异常来取代close方法，是因为避免出现两个实例同时调用一个端口，但是有一个实例正在写入，而另一个端口突然将其关闭的情况；
            self.dev_serial.close()
            self.dev_serial.open()
        '''
        # ----- PROTECTED REGION ID(InitialDeviceClass.openSerialPort) ENABLED START -----#
        try:
            self.dev_serial.open()
        except Exception as result:
            # print('{}{}'.format(result, self.print_log()))
            pass  # not need print
        # flushInput = self.dev_serial.flushInput() # 丢弃接收缓存中的所有数据
        # flushOutput = self.dev_serial.flushOutput() # 终止当前写操作，并丢弃发送缓存中的数据。
        # ----- PROTECTED REGION END -----#	//	CopleyControl.openSerialPort
    # ------------------------

    def is_number(self, num):
        '''
            str.isdigit()
        '''
        # ----- PROTECTED REGION ID(InitialDeviceClass.is_number) ENABLED START -----#
        try:
            float(num)
            return True
        except ValueError:
            print('Input is not numbers: {}'.format(num))
        return False
        # ----- PROTECTED REGION END -----#	//	CopleyControl.is_number

    def print_log(self, log='time_msg', node_id=0):
        '''
            print('Serial Port is OK{}'.format(self.print_log('time_msg')))
        '''
        # ----- PROTECTED REGION ID(InitialDeviceClass.print_log) ENABLED START -----#
        if log == 'full_msg':
            msg = '\n\t- PortID: {}\n\t- NodeID: {}\n\t- Buad: {}\n\t- Timeout: {}\n\t- Time: {}'.format(self.dev_serial.port, node_id, self.dev_serial.baudrate, self.dev_serial.timeout, time.asctime())
        elif log == 'time_msg':
            msg = '\n\t- PortID: {}\n\t- NodeID: {}\n\t- Time: {}'.format(self.dev_serial.port, node_id, time.asctime())
        else:
            msg = '\n\t- PortID: {}'.format(self.dev_serial.port)
        return msg
        # ----- PROTECTED REGION END -----#	//	CopleyControl.print_log

    def debug_stream(self, *msg):
        '''
            output debug info
            [issue]:
            目前没办法把node_id加进来
        '''
        # ----- PROTECTED REGION ID(InitialDeviceClass.debug_stream) ENABLED START -----#
        strs = ''
        for target_tuple in reversed(msg):
            strs = str(target_tuple) + '\t' + strs
        print(strs + '{}'.format(self.print_log('time_msg', node_id='debug')))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.debug_stream

    def debug_log(self, msg, node_id=0):
        '''
            output debug info

            退而求其次，再写一个调试的函数，相比之下，这个可以添加node_id
        '''
        # ----- PROTECTED REGION ID(InitialDeviceClass.debug_stream) ENABLED START -----#
        strs = str(msg)
        print(strs + '{}'.format(self.print_log('time_msg', node_id)))
        # ----- PROTECTED REGION END -----#	//	CopleyControl.debug_stream

    def is_int(self, input, output=0):
        """
        若read方法中为attribute值，则在write方法中不能使用is_int直接将返回值给attribute
        """
        try:
            result = int(input)
        except Exception:
            if output == 'No Power':
                result = output
            else:
                # 这行可以避免在单位转换的时候出现float小数
                result = int(output)
                print('The value: {} is not number, and return is {}.{}'.format(input, output, self.print_log('time_msg')))
        return result

# %%


class FormatCmdClass(InitialDeviceClass):  # InitialParametersClass
    '''
        :def write: write command to the serial line.\n
        :def WriteRead: writes a command to the serial line and gets the result of this command from the amplifier.\n
        :def handShake: check the reply to confirm whether the command is sent successfully or not.\n
        :def setParamCmd: Return the Set Command with NodeID, command and data for copley control.\n
        :def getParamCmd: Return the Get Command with NodeID, command for copley control.\n
        :def getValue: Get the mathematical value of the answer after sending the command.\n

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
        # self.debug_stream('write()')
        # ----- PROTECTED REGION ID(FormatCmdClass.write) ENABLED START -----#
        self.openSerialPort()
        self.dev_serial.write(cmd)
        # ----- PROTECTED REGION END -----#	//	FormatCmdClass.write

    def WriteRead(self, argin):
        '''
            writes a command to the serial line and gets the result of this command from the amplifier.

            :param port_id: serial port id
            :param argin: wait to command(acsii)
        '''
        # self.debug_stream('WriteRead()')
        argout = ''
        # ----- PROTECTED REGION ID(FormatCmdClass.WriteRead) ENABLED START -----#
        raw_result = ''
        self.openSerialPort()
        self.dev_serial.write(argin)
        raw_result = self.dev_serial.read_until('\r')
        try:
            if (raw_result[-1] == '\r' or raw_result[-1] == '\n'):
                argout = raw_result[0:-1]
        except Exception as e:
            argout = None
            self.debug_stream(e)
        # ----- PROTECTED REGION END -----#	//	FormatCmdClass.WriteRead
        return argout

    def handShake(self, reply):
        '''
            1. check the reply to confirm whether the command is sent successfully or not.\n
            2. find error code\n
        '''
        # ----- PROTECTED REGION ID(FormatCmdClass.handShake) ENABLED START -----#
        if reply == 'No power' or 'ok' or reply[0:1] == 'e' or reply[0:1] == 'v':
            return True
        else:
            return False
        # ----- PROTECTED REGION END -----#	//	FormatCmdClass.handShake

    def setParamCmd(self, ascii, data=0, node_id=0):
        ''' 
            Return the Set Command with NodeID, command and data for copley control.

            * r \n
                The `r` command is used to reset the drive. The command requires no additional parameters. The drive baud rate is set to 9600 when the drive restarts. The drive does not respond to this message.
                NOTE: if a reset command is issued to a drive on a multi-drop network, error code 32, “CAN Network communications failure,” will be received. This is because the drive reset before responding to the gateway drive. In this case, the error can be ignored.
                The axis letter has no effect with this command because the reset command applies to all axes of a multi-axis drive.
                Syntax: [optional node ID] r<CR>
                Example: `3 r` # response: none, The drive with CAN node ID of 3 is reset.
        '''
        # ----- PROTECTED REGION ID(FormatCmdClass.setParamCmd) ENABLED START -----#
        try:
            data = int(data)
            if ascii[:2] == '0x':
                cmd = '{} s r{} {}\n'.format(node_id, ascii, data)
            elif ascii == 't':
                cmd = '{} {} {}\n'.format(node_id, ascii, data)
            elif ascii == 'r':
                cmd = '{} {}\n'.format(node_id, ascii)
            else:
                cmd = 'command error.\nformat command: [node ID][<.>axis letter] [cmd code] [cmd parameters] <CR>'
        except Exception:
            print('the input value is not numbers.{}'.format(self.print_log('time_msg')))
        return cmd
        # ----- PROTECTED REGION END -----#	//	FormatCmdClass.setParamCmd

    def getParamCmd(self, cmd, node_id=0):
        '''
            Return the Get Command with NodeID, command for copley control.\n
        '''
        # ----- PROTECTED REGION ID(FormatCmdClass.getParamCmd) ENABLED START -----#
        return '{} g r{}\n'.format(node_id, cmd)
        # ----- PROTECTED REGION END -----#	//	FormatCmdClass.getParamCmd

    def setValue(self, result, new, old):
        '''
            Set the mathematical value of the answer to the attribute after sending the command.\n
            主要针对读取方法为属性类的参数，这样省了一步
        '''
        # ----- PROTECTED REGION ID(FormatCmdClass.setValue) ENABLED START -----#
        try:
            if result == 'ok':
                return new
            else:
                print('The result is ERROR: {} is not number, and return old value: {}.{}'.format(result[0:-1], old, self.print_log('time_msg')))
                return old
        except Exception:
            self.debug_stream(result, new, old)
            return old
        # ----- PROTECTED REGION END -----#	//	FormatCmdClass.setValue

    def getValue(self, cmd):
        '''
            get the mathematical value of the answer after sending the command.\n
        '''
        # ----- PROTECTED REGION ID(FormatCmdClass.getValue) ENABLED START -----#
        reply = self.WriteRead(cmd)
        if self.handShake(reply):
            try:
                if reply[0:1] == 'v':
                    argout = str(reply[2:])
                    return argout
                elif reply[0:1] == 'e':
                    idx, argout = CodesMapped(code=reply[2:])
                    return argout
                else:
                    return reply
            except Exception:
                return None
        else:
            print('Handshake() ERROR.{}'.format(self.print_log('full_msg')))
        # ----- PROTECTED REGION END -----#	//	FormatCmdClass.getValue
