#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    [20210319]:
        [issue]:
        √ 1. 将这些电机的物理参数写作常量，作为包的形式导入
    [20210318]:
        [issue]:
        √ 1. 将ColeyControlClass继承到MotorClass中，取消之前的在MotorClass中实例化的方式
        Note:
        1. 注意，在类中使用继承的方式，避免使用实例化
    这个就是作为一个库，主要是针对电机
    这里会调用驱动的函数，被主函数调用，就像接线一样
'''
# [issue]:
# 关于电机启动有顺序这件事，尝试过提前设置参数，然后最后发送运动指令
# 但是还是肉眼可见的先后运动，考虑使用多线程的方式来试试

# %% import
# Hardware
from copley_lib.CopleyControl import CopleyControlClass

# %% constant
from constant_lib.Constant_Motor import Maxon_306090, Maxon_266761, Maxon_305474

# %% class
class MotorClass(CopleyControlClass):
    '''
        # MotorClass

        1 .这个类主要是针对电机的一些物理参数进行设定，比如在使用多点RS232连接方式的时候，实例化多个电机
        而不是在节点中实例化多个，就算在节点中进行实例化，也不能够实现，因为就像物理上的接线一样
        如果是多点RS232连接两个电机，这两个电机就是用的一个串口，这一个串口在一个系统中调用的话，只能实例化一个
        本来想着可以实例化多个，但是实际测试是不可以的！
        2. 也就是这样，所以这些参数映射上的代码需要移植到上位机，换算好后再发送过来。这样，原则上，下位机的代码只接受下位机硬件直接相关的东西
        因为映射是和手柄有关系的，这样就不用担心，如果移植过多的话，如果下位机进行自治移动的话，代码不够用了
        3. 所以这个MotorClass只会是实现基础的功能，就像硬件接线一样。并不是简陋没有必要，而是基础且必要的存在。
    '''
# ==================================================
#                                             Initial_Parameters
# ==================================================
# [issue]:
# 添加钩刺机构和推拉机构在位置模式下的极限位置的参数
# 同时，处于力矩模式下的时候，辅助使用编码器的数值作为极限位置的限制
# 考虑这个电机的初始化，是否应该去除。不同的电机不同的模式就有不同的初始化方式
# 3*3=9，可能产生9种模式
    def __init__(self, PortID, NodeID, Mode, 
                        profile=1, pos=0, vel=100000, acc=1000000, dec=1000000, cur=0, rap=0):
        '''
            :param PortID: 
            :param NodeID: 
            :param Mode:
            :param Map:
        '''
    # Hardware
        self._inits_motor()
        self._inits_coply(PortID, NodeID, Mode, profile, pos, vel, acc, dec, cur, rap)
    def _inits_motor(self):
        '''
        '''
        pass
    def _inits_coply(self, PortID, NodeID, Mode, profile, pos, vel, acc, dec, cur, rap):
        '''
            同时控制几个电机，就要实例化几个setInitParameters参数，区别在于，传入不同的node_id参数

            :param PortID: 
            :param NodeID: 
            :param Mode:
        '''
        # [issue]:
        # 因为转换成作为类继承的关系，所以这个参数的初始化就需要单独执行
        # 这个调用方式可以接受，但是名字要改，和第二个初始化冲突了
        # 或者把这个函数移到别处去
        self.inits_parameters()
        self.initialParameter(PortID, NodeID, Mode)
        self.setInitParameters(profile, pos, vel, acc, dec, cur, rap, node_id=0)
        self.setInitParameters(profile, pos, vel, acc, dec, cur, rap, node_id=1)
# ==================================================
#                             Convert to motor commands
# ==================================================
    # 发送电机的控制指令 => 电机(ACSII)
    def cmdvel_2_motor(self, motor_cmd, node_id=0):
        self.attr_Velocity_read = motor_cmd
        # 若为位置环下的速度模式，则进行判断方向，不能和其他模式一样直接识别速度指令的正负号
        if self.DesiredState==21 and self.ProfileType==2:
            if motor_cmd >= 0:
                self.write_Position(1, node_id)
            if motor_cmd < 0:
                self.write_Position(-1, node_id)
            motor_cmd = abs(int(motor_cmd))
            self.write_Velocity(self.attr_Velocity_read, node_id) # 写入电机速度
        # 若为速度模式，仅调用Move()即可，将self.attr_Velocity_read写入
        self.Move(node_id)

    # 发送电机的控制指令 => 电机(ACSII)
    def cmdpos_2_motor(self, motor_cmd, node_id=0):
        self.write_Position(motor_cmd, node_id)
        # self.write_SetPoint(motor_cmd, node_id)
        self.Move(node_id)
# ==================================================
#                                    Algorithm_Application
# ==================================================
    # 1. 获取反馈值
    def feedback_motor(self, node_id=0):
        """
            get feedback from motor include current, velocity, position
        """
        current_amp = self.read_Current(node_id)
        velocity_amp = self.read_Velocity(node_id)
        position_amp = self.read_Position(node_id)
        return {'current_amp': current_amp, 'velocity_amp':velocity_amp, 'position_amp':position_amp}
    def trajectory_motor(self, node_id=0):
        """
        临时，为轨迹跟踪提供速度反馈
        """
        return self.read_Velocity(node_id)
    # 3. 控制量 - 速度
    def control_motor_vel(self, target, node_id=0):
        """
            set target speed value to motor
            :param target: 新的目标速度，对于伺服电机的速度模式，只需要更改目标速度即可。这里的速度值是区分正负的，所以不用单独的量来控制正负。
            :param node_id: 指定需要控制的电机，默认第一台电机，id=0。
        """
        self.attr_Velocity_read = target
        self.Move(node_id)
    # 3. 控制量 - 位置
    def control_motor_pos(self, adjust, enc_zero, CcwLimit, target, node_id=0):
        """
            set target position value to motor
            该函数同时适用于主驱动电机、钩刺电机、推拉电机，同时加入了调试至适当位置的功能，所以逻辑会显得有些复杂
        """
        # 处于调试模式并且对编码器置位时使用，适用单边电机
        if adjust and enc_zero:
            # 若向负极限调整，则此处应该是: `-(行程/2)`，CcwLimit=(-Maxon.Stroke/2)
            # [issue]:
            # 还可以进一步完善，即可以向正极限调整也可以向负极限调整
            self.write_Encoder(CcwLimit, node_id)
            return
        # 当处于调试模式时：
        if adjust:
            # 在相对位置模式下，进行调试功能
            # 若在相对位置模式下进行极限位置模式的切换需要设置正负极限位置
            # 所以还是建议在绝对位置模式下进行极限位置切换
            # 调试模式只能在相对位置模式下
            self.write_SetPoint(target, node_id)
        # 当处于正常模式时：
        else:
            # 在绝对位置模式下，进行极限位置的切换
            self.write_Position(target, node_id)

        self.Move(node_id)
    # 3. 控制量 - 位置/速度
    def control_motor_pos_vel(self, position, velocity, acceleration, node_id=0):
        """
            [issue]:
            在位置模式下同时控制位置和速度，主要用于勾刺推拉机构的阻抗控制模型
        """
        # 在绝对位置模式下，进行极限位置的切换
        self.write_Position(position, node_id)
        self.write_Velocity(velocity, node_id)
        self.write_Acceleration(acceleration, node_id)

        self.Move(node_id)