#! /usr/bin/env python
# -*- coding:utf-8 -*-
# %% README
'''md
# 20210121:
    1.需要先执行inits_start()
'''


# %%
# OS
import os # 加载os模块，调用shell命令
# Lib
import can # pip install python-can


# %%
class CANClass():
    """
    docstring
    """
    def __init__(self):
        self.inits_start()
        self.inits_param()

    def inits_start(self, defname='can0'):
        setup_cmd = 'sudo ip link set ' + defname + ' type can bitrate 100000' # bits/s
        start_cmd = 'sudo ifconfig ' + defname + ' up'
        os.system(setup_cmd)
        os.system(start_cmd)

    def inits_param(self):
        self.can0 = can.interface.Bus(bustype ='socketcan_native', channel='can0')  # socketcan_native

    def stop(self, defname='can0'):
        stop_cmd = 'sudo ifconfig ' + defname + ' down'
        os.system(stop_cmd)

    def send(self):
        '''
        CANopen Rules: Node-ID 0 is reserved for bus master Slave node-ID range is 0x01~0x7F (1~127). All slave node-ID’s must be unique.
        CANopen规则：节点ID 0保留用于总线主设备从节点ID的范围为0x01～0x7F（1～127）。所有从节点ID必须是唯一的。
        's r0x24 0\r' # 73 20 72 30 78 32 34 20 30 0D
        'ok\r' # 6F 6B 0D
        '''
        msg = can.Message(arbitration_id=0x01, data=['s ', 'r', 0x24, 0x00], extended_id=False)
        try:
            self.can0.send(msg, timeout=0.1)
        except can.CanError:
            print('the message could not be sent')

    def receive(self):
        while True:
            msg = self.can0.recv(1.0)
            if msg is None:
                print('Timeout occurred, no message.')
            else:
                print('{}:{}'.format(msg.arbitration_id, msg.data))
                print(msg)

    def notifier(self):
        '''
        use an asynchronous notifier
        '''
        notidier = can.Notifier(self.can0, [can.Logger('recorded.log'), can.Printer()])

def main():
    can = CANClass()
    # can.send()
    can.receive()
    can.stop()

# %%
if __name__ == "__main__":
    main()