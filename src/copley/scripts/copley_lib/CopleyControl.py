#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    # 20210323:
        [issue]:
        增加一个前缀的e的判断，这个是错误代码，同时修改setvalue()
        [issue]:
        将单位设置为全局变量
    # 20210322：
        [Task]:
        1. 在位置模式的时候，还没有让位置限制的两个参数起作用
        2. 这两个参数需要作为输入可以由调用方传入
        3. 位置映射还没确定，极限位置的大小
        4. 电机正方向的问题
    # 20210317:
        [issue]:
            考虑将下面的类拆分成不同的.py，再通过包的形式导入进来
            这样的话，每个模式都是拆分出去，这样就不用每次都if了，而且每个模式有什么属性也都分明了

    # 20210306
        [Task]:
        1. 这里面的状态信息，返回给ros，记录的ros日志中
        2. 除了GUI还要加入键盘控制，不仅仅是手柄
        3. 考虑用多线程的方式调用两个电机的实例，达到电机同时转动
        √: 4. 尝试使用电机驱动
        5. 整理算法
        6. 做界面
        7. 保存数据
        8. 确定电机转动方向
        9. 位置模式需要增加参数，即限位
        √: 10. 调整波特率的函数需要调试
        √: 11. 关于返回值错误的33个，还没写成日志打印的方式
    # 20201119
        [Task]:
        1. 加入IMU
        2. 加入功率计
        3. 使用Location的ROS包
        4. 使用UUV
        5. 添加QT界面
        √: 6. 增强程序的容错性：端口故障
        [Issue]:
    # 20201119
        [Task]:
        1. 推拉机构以及钩刺机构的调试
        √: 2. 加入力矩模式
        [Issue]:
        因为不是绝对编码器，也没有限位开关所以对于机器人启动时候的初始状态不能判断，即硬件上不能进行初始化；
        考虑两种方法：1. 手柄进行微调；2. 使用日志文件进行复位以及初始化，但是这个需要考验电机的精度，担心多次启动后，会出现误差的累计；所以这个是不是需要和手动微调进行结合
        另外，在程序上不能和主驱动电机一样，停止的时候，直接发送0指令就可以了；对于两个辅助机构需要进行复位，即关机的时候进行
        但是有个问题，推拉机构的减速比是23:1，就是说可以直接手动调整；钩刺机构的减速比是128:1，这个不能手动调整的。如果可以手动调整，会对日志文件中保留的定位信息冲突；
        另外一种方法，对于推拉机构来说，可以不进行日志文件的记录，让机构收缩到平行位置，并继续运动，这样会碰触一些零件，此时电流会加大，检测到电流突然变大的时候，就认为是初始位置了；
    # 20201118
        [Task]:
        √: 1. 固定树莓派端口号
        √: 2. 添加算法接口代码
        √: 3. 调试其余4台电机
        [Issue]:
        ！: 端口号的固定，采用默认的接法就可以，至少暂时每次重启后端口号都能对应上；上面的先通电吧
        √: 添加算法接口代码，主要是的逻辑和MotorClass等一样，在主函数中进行初始化，可以使用ROS的动态参数配置进行动态调整参数，将该参数传递至算法类中；并且在算法接口代码中添加了开关量，可以选择关闭或启用该算法，可以方便切换不同的算法；
        √: 在变量的命名方式上，py文件采用首字母大写并添加下划线的方式，且下划线后的字母同样大写；定义的类名，采用首字母大写，没有下划线的方式；在主函数中导入包定义别名的时候，采用首字母大写尽可能使用一个单词的方式进行区分；在调用创建对象所拥有的属性时候采用首字母大写添加下划线的方式；在函数内部进行定义变量的时候，尽可能的采用全部小写字母以及下划线的方式；
            总的原则是，在主函数内部，外部导入的内容需要至少首字母大写，包的别名需要尽可能简洁，所以不使用下划线；创建类的属性时候，为了方便和其他类的属性区分，所以可以使用下划线，因为名字会变长；
    # 20201117
        [Task]:
        √: 1. 初步加入速度模式
            后面考虑加入一个手柄按键用于切换模式，考虑用一个按键循环切换还是用多个按键进行定义
        √: 2. 解决默认端口问题
        √: 3. 固定树莓派的端口号
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
__all__ = ['CopleyControlClass']  # 可用于模块导入时限制，只有__all__内指定的属性、方法、类可被导入
__docformat__ = 'restructuredtext'  # 允许诸如 epydoc之类的python文档生成器工具知道如何正确解析模块文档

# %% import
# import tango as PyTango
# Add additional import
# ----- PROTECTED REGION ID(CopleyControl.additionnal_import) ENABLED START -----#
from copley_lib.Class_InitialParameter import *
from copley_lib.Class_MoveMotor import MoveMotorClass
from copley_lib.Class_MoveHome import MoveHomeClass
# ----- PROTECTED REGION END -----#	//	CopleyControl.additionnal_import

# %% Constant
# -------- Add Global Variables Here ------------
# ----- PROTECTED REGION ID(CopleyControl.global_variables) ENABLED START -----#
from constant_lib.Constant_Unit import *
from constant_lib.Constant_Serial import *
# ----- PROTECTED REGION END -----#	//	CopleyControl.global_variables

# -------- Device States Description ------------
# MOVING : Moving
# ON : Device On
# FAULT : Amp is faulted and must be reset.
# ALARM : There is an alarm raised.
# INIT : The amp is initialising.

# %% Class


class CopleyControlClass(MoveMotorClass, MoveHomeClass):
    '''
        Copley Control Class
    '''

    def __str__(self):
        msg = 'Copley Control Class'
        return msg

    def __init__(self):
        # def __init__(self, PortID, NodeID, Mode):
        # ----- PROTECTED REGION ID(CopleyControl.__init__) ENABLED START -----#
        # super(CopleyControlClass,self).__init__(PortID=PortID, NodeID=NodeID, Mode=Mode)
        self.inits_parameters()
        self.inits_device()
        # ----- PROTECTED REGION END -----#	//	CopleyControl.__init__

    def inits_parameters(self):
        # inits the device
        # self.debug_stream('In init_device()') # Sends the given message to the tango debug stream.
        self.attr_EncoderInitial_read = 0  # 0x32/0x17: Motor position. Units: counts.
        self.attr_Position_read = 0  # 0x17: Limited position. targetPosition = Position + SetPoint
        self.attr_SetPoint_read = 0  # 0xca: Trajectory Generator Position Command(0xca).
        self.attr_DialPosition_read = 0
        self.attr_Conversion_read = 1  # The ratio between the position and the dial position. The default value is 1.0
        self.attr_Velocity_read = 0  # 0x18: Actual velocity.
        self.attr_Acceleration_read = 0  # 0xcc: Maximum acceleration rate.
        self.attr_Deceleration_read = 0  # 0xcd: Maximum deceleration rate.
        self.attr_Current_read = 0  # 0x02: Programmed current value.
        self.attr_Current_ramp = 0  # 0x6a: Current ramp limit.

        self.attr_SoftwareCwLimit_read = 0  # 0xb8: Positive Software Limit
        self.attr_SoftwareCcwLimit_read = 0  # 0xb9: Negative Software Limit
        self.attr_SoftwareCwDialLimit_read = 0
        self.attr_SoftwareCcwDialLimit_read = 0
        self.attr_CwLimit_read = False  # Positive limit switche is active
        self.attr_CcwLimit_read = False  # Negative limit switche is active

        self.attr_HomingMethod_read = 0  # 0xc2 归位方法
        self.attr_HomingVelocityFast_read = 0  # 0xc3
        self.attr_HomingVelocitySlow_read = 0  # 0xc4
        self.attr_HomingAccDec_read = 0  # 0xc5
        self.attr_HomeOffset_read = 0  # 0xc6: Home Offset.
        self.attr_HomingCurrentLimit_read = 0  # 0xc7(0xbf)
        self.attr_CurrentDelayTime_read = 250  # 0xbf(0xc7)/ms

        self.argout = 'UNKNOWN'
        # ----- PROTECTED REGION ID(CopleyControl.init_device) ENABLED START -----#
        self.DesiredState = 11
        self.ProfileType = 0  # 0xc8: Give trajectory profile mode(0xc8). Bits: *0\1\*256\257\*2

        self.targetPosition = 0
        self.attr_SetPoint_read = 0
        self.attr_Velocity_read = 0
        self.attr_Acceleration_read = 500
        self.attr_Deceleration_read = 500
        self.attr_Current_read = 0
        self.attr_Current_ramp = 0

    def inits_device(self):
        # self.debug_stream('In inits_device()')
        # ----- PROTECTED REGION ID(CopleyControl.inits_device) ENABLED START -----#
        # InitialDeviceClass.connectSerial() # 也单独在调用的地方初始化了，不然改一个参数得改一串
        # self.setInitParameters() # 由于涉及参数较多，直接在调用函数中传参，另外可以考虑将其单独作为了一个Class
        pass
        # ----- PROTECTED REGION END -----#	//	CopleyControl.init_device

    def delete_device(self):
        # self.debug_stream('In delete_device()')
        # ----- PROTECTED REGION ID(CopleyControl.delete_device) ENABLED START -----#
        # print('Delete Device.{}'.format(self.print_log('time_msg')))
        pass
        # ----- PROTECTED REGION END -----#	//	CopleyControl.delete_device

    def always_executed_hook(self):
        # self.debug_stream('In always_excuted_hook()')
        # ----- PROTECTED REGION ID(CopleyControl.always_executed_hook) ENABLED START -----#
        pass
        # ----- PROTECTED REGION END -----#	//	CopleyControl.always_executed_hook
