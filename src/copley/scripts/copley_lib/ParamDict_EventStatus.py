#! /usr/bin/env python
# -*- coding:utf-8 -*-

# %% doc
__all__ = ['BitsMapped'] # 可用于模块导入时限制，只有__all__内指定的属性、方法、类可被导入
__docformat__ = 'restructuredtext' # 允许诸如 epydoc之类的python文档生成器工具知道如何正确解析模块文档

# %%
class EventStatus(object):
    """
    0xA0, 0xA1, 0xA4, 0xA7
    """
    def __init__(self):
        # self.ascii = ascii
        # self.data = data
        pass

    def __str__(self):
        msg = 'from copley_lib.ParamDict_EventStatus import BitsMapped'
        return msg

def BitsMapped(ascii='0xA0', data=0):
    """
        其实也可以不用转换半天，直接拿返回值和一系列的数字&就行
        这样反而麻烦了，还要转换，再获取索引，再去取值
        但是这样的好处就是不用算了
    """
    argout = []
    value = reversed(list(bin(int(data))[2:]))
    for idx, val in enumerate(value):
        # print('idx: {}; value: {}'.format(idx, val))
        if int(val)&1!=0:
            if ascii=='0xA0':
                argout.append(BitsMapped_0xA0(idx))
            elif ascii=='0xA4':
                argout.append(BitsMapped_0xA4(idx))
    # convert list to str and output
    strs = ''
    for target_list in reversed(argout):
        strs = target_list + strs
    return strs # argout

def BitsMapped_0xA0(idx):
    '''#  0xA0 R* U32 Event Status Register.
        Bit-mapped as follows:
        Bits	Description	描述
        0	Short circuit detected	检测到短路
        1	Drive over temperature	驱动温度过高
        2	Over voltage	过电压
        3	Under voltage	欠电压
        4	Motor temperature sensor active	电机温度传感器有效
        5	Encoder power error	编码器电源错误
        6	Motor phasing error	电机定相误差
        7	Current output limited	电流输出限制
        8	Voltage output limited	电压输出限制
        9	Positive limit switch active	正限位开关有效
        10	Negative limit switch active	负限位开关有效
        11	Enable input not active	启用输入未激活
        12	Drive is disabled by software	驱动器已被软件禁用
        13	Trying to stop motor	试图停止电动机
        14	Motor brake activated	电机制动器已激活
        15	PWM outputs disabled	PWM输出禁用
        16	Positive software limit condition	正软件极限条件
        17	Negative software limit condition	负软件限制条件
        18	Following Error Fault. A following error has occurred, and drive is in following error mode.	跟随错误故障。发生跟随错误，驱动器处于跟随错误模式。
        19	Following Error Warning. Indicates position error is greater than position following warning.	出现错误警告之后。指示位置误差大于警告后的位置。
        20	Drive is currently in reset condition	驱动器当前处于重置状态
        21	Position has wrapped. Position variable cannot increase indefinitely. After reaching a certain value the variable rolls back. This type of counting is called position wrapping or modulo count	位置已经包裹。位置变量不能无限增加。达到某个值后，变量回滚。这种计数方式称为位置换行或模数计数。
        22	Drive fault. Fault configured as latching in Fault Mask (0xA7) has occurred. Latched faults may be cleared using Latching Fault Status Register (0xA4).	驱动器故障。发生配置为在故障掩码（0xA7）中锁存的故障。闩锁故障可以使用闩锁故障状态寄存器（0xA4）清除。
        23	Velocity limit (0x3A) has been reached	已达到速度限制（0x3A）
        24	Acceleration limit (0x36) has been reached	达到加速限制（0x36）
        25	Position Tracking. Position Loop Error (0x35) is outside of Following Error Fault Limit (0xBA).	位置跟踪。位置环错误（0x35）超出跟随错误故障限制（0xBA）。
        26	Home switch is active	家用开关处于活动状态
        27	In motion. Set if trajectory generator is running profile or Following Error Fault Limit (0xBA) is outside tracking window. Clear when drive is settled in position.	运动中。设置轨迹生成器是否正在运行配置文件或“跟踪错误故障限制”（0xBA）是否在跟踪窗口之外。当驱动器固定到位时清除。
        28	Velocity window. Set when velocity error is larger than programmed velocity window	速度窗口。当速度误差大于编程的速度窗口时设置
        29	Phase not yet initialized. If drive is phasing with no Halls, this bit is set until drive has initialized its phase.	阶段尚未初始化。如果驱动器定相且没有霍尔，则此位置1，直到驱动器初始化其相位为止。
        30	Command fault. CANopen or EtherCAT master not sending commands or PWM command not present. Note: If Allow 100% Output option is enabled by setting Bit 3 of Digital Input Command Configuration (0xA8) this fault will not detect missing PWM command.	命令故障。 CANopen或EtherCAT主站不发送命令或不存在PWM命令。注意：如果通过设置数字输入命令配置（0xA8）的位3启用了“允许100％输出”选项，则此故障将不会检测到丢失的PWM命令。
        31	Reserved.	预留的。
    '''
    if idx==0:
        argout = 'Bit_00: Short circuit detected\n'
    elif idx==1:
        argout = 'Bit_01: Drive over temperature\n'
    elif idx==2:
        argout = 'Bit_02: Over voltage\n'
    elif idx==3:
        argout = 'Bit_03: Under voltage\n'
    elif idx==4:
        argout = 'Bit_04: Motor temperature sensor active\n'
    elif idx==5:
        argout = 'Bit_05: Encoder power error\n'
    elif idx==6:
        argout = 'Bit_06: Motor phasing error\n'
    elif idx==7:
        argout = 'Bit_07: Current output limited\n'
        # [输出电流被I2T Algorithm公式所限制或者一个锁定的电流错误发生。]\n
    elif idx==8:
        argout = 'Bit_08: Voltage output limited\n'
        # [电流环正试图使用全部的母线电压去控制电流，一般发生在电机正占用全部的母线电压高速运行。]\n
    elif idx==9:
        argout = 'Bit_09: Positive limit switch active\n'
        # [电机轴已经接触到正限位开关。]\n
    elif idx==10:
        argout = 'Bit_10: Negative limit switch active\n'
        # [电机轴已经接触到负限位开关。]\n
    elif idx==11:
        argout = 'Bit_11: Enable input not active\n'
    elif idx==12:
        argout = 'Bit_12: Drive is disabled by software\n'
    elif idx==13:
        argout = 'Bit_13: Trying to stop motor\n'
        # [驱动器在速度或位置模式下，已经被去使能。在速度模式下，驱动器正使用“ Fast Stop Ramp”(详见Velocity Loop Limits)；在位置模式下，驱动器正使用"Abort Deceleration rate‘(详见Trajectory Limits)。输出保持有效直到驱动器重新使能。]"\n
    elif idx==14:
        argout = 'Bit_14: Motor brake activated\n'
    elif idx==15:
        argout = 'Bit_15: PWM outputs disabled\n'
    elif idx==16:
        argout = 'Bit_16: Positive software limit condition\n'
        # [实际位置已经超出正的软限位设置。请参考Homing.]\n
    elif idx==17:
        argout = 'Bit_17: Negative software limit condition\n'
        # [实际位置已经超出负的软限位设置。请参考Homing]\n
    elif idx==18:
        argout = 'Bit_18: Following Error Fault. A following error has occurred, and drive is in following error mode.\n'
        # [跟随误差已经达到设定的限制值。请参考Following Error Faults]\n
    elif idx==19:
        argout = 'Bit_19: Following Error Warning. Indicates position error is greater than position following warning.\n'
        # [跟随误差已经达到设定的报警值。请参考Following Error Faults]\n
    elif idx==20:
        argout = 'Bit_20: Drive is currently in reset condition\n'
    elif idx==21:
        argout = 'Bit_21: Position has wrapped. Position variable cannot increase indefinitely. After reaching a certain value the variable rolls back. This type of counting is called position wrapping or modulo count\n'
        # [位置脉冲计数已超过以下范围(-2^31 – 2^31-1)且已经设置位置包裹。驱动器其他功能不会受到影响。]\n
    elif idx==22:
        argout = 'Bit_22: Drive fault. Fault configured as latching in Fault Mask (0xA7) has occurred. Latched faults may be cleared using Latching Fault Status Register (0xA4).\n'
    elif idx==23:
        argout = 'Bit_23: Velocity limit (0x3A) has been reached\n'
        # [速度命令 (来自模拟量输入, PWM输入,或位置环) 已经超过了速度限制。请参考Velocity Loop Limits]\n
    elif idx==24:
        argout = 'Bit_24: Acceleration limit (0x36) has been reached\n'
        # [在速度模式下，电机已经达到速度环中设置的加速度和减速度限制的设定值。]\n
    elif idx==25:
        argout = 'Bit_25: Position Tracking. Position Loop Error (0x35) is outside of Following Error Fault Limit (0xBA).\n'
        # [跟随误差已经超过了设定值。请参考Position and Velocity Tracking Windows]\n[跟随误差已经超过了设定值。请参考Position and Velocity Tracking Windows]\n
    elif idx==26:
        argout = 'Bit_26: Home switch is active\n'
        # [电机轴已经接触到了原点开关。]\n
    elif idx==27:
        argout = 'Bit_27: In motion. Set if trajectory generator is running profile or Following Error Faul Limit (0xBA) is outside tracking window. Clear when drive is settled in position.\n'
        # [电机正在运行，或在一次运动后还没有整定结束。在运动结束时，当电机进入位置跟踪轨迹窗口并且保持设定的跟踪时间表示驱动器完成整定。一旦此项有效，它将保持有效直到一个新的运动开始。]\n
    elif idx==28:
        argout = 'Bit_28: Velocity window. Set when velocity error is larger than programmed velocity window.\n'
        # [目标速度和实际速度之间的误差超过了这个窗口的设定值。请参考Position and Velocity Tracking Windows]\n
    elif idx==29:
        argout = 'Bit_29: Phase not yet initialized. If drive is phasing with no Halls, this bit is set until drive has initialized its phase.\n'
        # [驱动器使用了相位初始化功能，但是相位没能被初始化。]\n
    elif idx==30:
        argout = 'Bit_30: Command fault. CANopen or EtherCAT master not sending commands or PWM command not present.\n'
        # [缺少PWM或其他命令信号 (例如EtherCAT主站)。如果在将“Digital InputCommand Configuration” Bit 3值为激活100%输出选项，驱动器将不会再检测PWM命令丢失，该错误不会出现。]\n
    elif idx==31:
        argout = 'Bit_31: Reserved.\n'

    return argout

def BitsMapped_0xA4(idx):
    """# 0xA4 R U32	Latching Fault Status Register. 
        Bit-mapped to show which latching faults have occurred in drive. When latching fault has occurred, the fault bit (bit 22) of Event Status Register (0xA0) is set. Cause of fault can be read from this register. To clear fault condition, write a 1 to associated bit in this register. Events that cause drive to latch fault are programmable. See Fault Mask (0xA7) for details.	锁存故障状态寄存器。位图以显示驱动器中发生了哪些闩锁故障。发生闩锁故障时，事件状态寄存器（0xA0）的*故障位（位22）*被置1。可以从该寄存器读取故障原因。要清除故障条件，请向该寄存器的相关位写入1。导致驱动器闩锁故障的事件是可编程的。有关详细信息，请参见故障屏蔽（0xA7）。
        Latched Faults	
        
        Bits	Fault Description	故障描述
        0	Data flash CRC failure. This fault is considered fatal and cannot be cleared. This bit is read-only and will always be set. If drive detects corrupted flash data values on startup it will remain disabled and indicate fault condition.	数据闪存CRC故障。该故障被认为是致命的，无法清除。该位是只读的，将始终被设置。如果驱动器在启动时检测到损坏的闪存数据值，它将保持禁用状态并指示故障情况。
        1	Drive internal error. This bit is read-only and will always be set. If drive fails its power-on self-test, it will remain disabled and indicate fault condition.	驱动器内部错误。该位是只读的，将始终被设置。如果驱动器无法通过开机自检，它将保持禁用状态并指示故障状态。
        2	Short circuit. If set: programs drive to latch a fault when short circuit is detected on motor outputs. If clear: programs drive to disable outputs for 100 ms after short circuit and then re-enable.	短路如果置位：当在电机输出上检测到短路时，程序将驱动以锁定故障。如果清除，则在短路后程序会在100毫秒内禁用输出，然后重新启用。
        3	Drive over temperature. If set: programs drive to latch a fault when drive over temperature event happens. If clear: programs drive to re-enable as soon as it cools sufficiently from over temperature event.	驱动温度过高。如果设置：当发生驱动器超温事件时，程序将驱动器锁存故障。如果清除，则表明程序在由于过热事件而充分冷却后立即重新启用。
        4	Motor over temperature. If set: programs drive to latch a fault when motor temperature sensor input activates. If clear: programs drive to re-enable as soon as over temperature input becomes inactive.	电机温度过高。如果置位：当电动机温度传感器输入激活时，程序将驱动以锁定故障。如果清除，则表明程序驱动器在温度输入无效时立即重新启用。
        5	Over voltage. If set: programs drive to latch a fault when excessive bus voltage is detected. If clear: programs drive to re-enable as soon as bus voltage is within normal range.	过电压。如果置位：当检测到总线电压过高时，程序将驱动程序以锁定故障。如果清除，则说明：总线电压在正常范围内时，程序将重新启用驱动器。
        6	Under voltage. If set: programs drive to latch a fault condition when inadequate bus voltage is detected. If clear: programs drive to re-enable as soon as bus voltage is within normal range.	欠电压。如果置位：当检测到总线电压不足时，程序将驱动以锁定故障状态。如果清除，则说明：总线电压在正常范围内时，程序将重新启用驱动器。
        7	Feedback fault. If set: programs drive to latch a fault when feedback faults occur. Feedback faults occur if too much current is drawn from 5 V source on drive, resolver or analog encoder is disconnected, or resolver or analog encoder has levels out of tolerance.	反馈故障。如果置位：程序会在发生反馈错误时锁存故障。如果从驱动器上的5 V电源汲取过多电流，分解器或模拟编码器断开连接，或者分解器或模拟编码器的电平超出容限，则会发生反馈故障。
        8	Phasing error. If set: programs drive to latch a fault when phasing errors occur. If clear: programs drive to re-enable when phasing error is removed.	分阶段错误。如果设置：当发生定相错误时，程序将驱动程序以锁定故障。如果清除，则说明：移相错误消除后，程序将重新启用。
        9	Following error. If set: programs the drive to latch a fault and disable drive when following error occurs. If clear: programs drive to abort current move and remain enabled when following error occurs.	跟随错误。如果设置：对驱动器进行编程以锁定故障，并在发生以下错误时禁用驱动器。如果清除，则程序将中止当前运动，并在发生以下错误时保持启用状态。
        10	If set: programs drive to latch a fault when output current is limited by I2T algorithm.	如果置位：当输出电流受I2T算法限制时，程序会驱动以锁定故障。
        11	FPGA failure. This bit is read-only.	FPGA故障。该位是只读的。
        12	Command input lost fault. If set: programs drive to latch a fault and disable when command input is lost.	命令输入丢失故障。如果设置，则程序将驱动程序以锁定故障并在丢失命令输入时禁用。
        13	Unable to initialize internal drive hardware. This bit is read-only.	无法初始化内部驱动器硬件。该位是只读的。
        14	If set, programs drive to latch a fault when there is safety circuit consistency check failure.	如果设置，当安全电路一致性检查失败时，程序将驱动程序以锁定故障。
        15	If set, programs drive to latch a fault when drive is unable to control motor current.	如果置位，程序将在驱动器无法控制电动机电流时锁定驱动器故障。
        16	If set, programs drive to latch a fault when motor wiring is disconnected, see Open Motor Wiring Check Current (0x19D).	如果置位，程序将在断开电动机接线时驱动程序以锁定故障，请参阅断开电动机接线检查电流（0x19D）。
        17	Reserved.	预订的。
        18	Safe torque off active	安全扭矩关闭有效
    """
    if idx==0:
        argout = 'Bit_00: (Data flash CRC failure. This fault is considered fatal and cannot be cleared. This bit is read-only and will always be set. If drive detects corrupted flash data idxs on startup it will remain disabled and indicate fault condition. )\n'
        # 数据闪存CRC故障。 该故障被认为是致命的，无法清除。 该位是只读的，将始终被设置。 如果驱动器检测到损坏的闪存数据启动时的值将保持禁用状态并指示故障情况。\n
    elif idx==1:
        argout = 'Bit_01: (Drive internal error. This bit is read-only and will always be set. If drive fails its power-on self-test, it will remain disabled and indicate fault condition.)\n'
        # 驱动器内部错误。 该位是只读的，将始终被设置。 如果驱动器无法通过开机自检，它将保持禁用状态并指示故障状态。\n
    elif idx==2:
        argout = 'Bit_02: (Short circuit. If set: programs drive to latch a fault when short circuit is detected on motor outputs. If clear: programs drive to disable outputs for 100 ms after short circuit and then re-enable.)\n'
        # 短路 如果置位：当在电机输出上检测到短路时，程序将驱动以锁定故障。 如果清除，则在短路后程序会在100毫秒内禁用输出，然后重新启用。\n'
    elif idx==3:
        argout = 'Bit_03: (Drive over temperature. If set: programs drive to latch a fault when drive over temperature event happens. If clear: programs drive to re-enable as soon as it cools sufficiently from over temperature event.) \n'
        # 驱动温度过高。 如果设置：当发生驱动器超温事件时，程序将驱动器锁存故障。 如果清除，则表明程序在由于过热事件而充分冷却后立即重新启用。\n
    elif idx==4:
        argout = 'Bit_04: (Motor over temperature. If set: programs drive to latch a fault when motor temperature sensor input activates. If clear: programs drive to re-enable as soon as over temperature input becomes inactive.)\n'
        # 电机温度过高。 如果置位：当电动机温度传感器输入激活时，程序将驱动以锁定故障。 如果清除，则表明驱动程序在温度输入无效时立即重新启用。\n
    elif idx==5:
        argout = 'Bit_05: (Over voltage. If set: programs drive to latch a fault when excessive bus voltage is detected. If clear: programs drive to re-enable as soon as bus voltage is within normal range.)\n'
        # 过电压。 如果设置：当检测到总线电压过高时，程序将驱动程序以锁定故障。 如果清除，则表明程序在总线电压处于正常范围内时立即重新启用。\n
    elif idx==6:
        argout = 'Bit_06: (Under voltage. If set: programs drive to latch a fault condition when inadequate bus voltage is detected. If clear: programs drive to re-enable as soon as bus voltage is within normal range.)\n'
        # 欠电压。 如果置位：当检测到总线电压不足时，程序将驱动以锁定故障状态。 如果清除，则表明程序在总线电压处于正常范围内时立即重新启用。\n
    elif idx==7:
        argout = 'Bit_07: (Feedback fault. If set: programs drive to latch a fault when feedback faults occur. Feedback faults occur if too much current is drawn from 5 V source on drive, resolver or analog encoder is disconnected, or resolver or analog encoder has levels out of tolerance. )\n'
        # 反馈故障。 如果设置：当发生反馈故障时，程序将驱动程序以锁定故障。 如果从驱动器上的5 V电源汲取过多电流，分解器或模拟编码器断开连接，或者分解器或模拟编码器的电平超出容限，则会发生反馈故障。\n
    elif idx==8:
        argout = 'Bit_08: (Phasing error. If set: programs drive to latch a fault when phasing errors occur. If clear: programs drive to re-enable when phasing error is removed.)\n'
        # 相位错误。 如果设置：当出现定相错误时，程序将驱动程序以锁定故障。 如果清除，则说明移相错误后程序将重新启用。\n
    elif idx==9:
        argout = 'Bit_09: (Following error. If set: programs the drive to latch a fault and disable drive when following error occurs. If clear: programs drive to abort current move and remain enabled when following error occurs.)\n'
    elif idx==10:
        argout = 'Bit_10: (If set: programs drive to latch a fault when output current is limited by I2T algorithm.)\n'
        # 如果置位：当输出电流受I2T算法限制时，程序将驱动程序锁定故障。\n
    elif idx==11:
        argout = 'Bit_11: (FPGA failure. This bit is read-only.)\n'
        # FPGA故障。 该位是只读的。\n
    elif idx==12:
        argout = 'Bit_12: (Command input lost fault. If set: programs drive to latch a fault and disable when command input is lost.)\n'
        # 命令输入丢失故障。 如果设置，则程序将驱动程序以锁定故障并在丢失命令输入时禁用。\n
    elif idx==13:
        argout = 'Bit_13: (Unable to initialize internal drive hardware. This bit is read-only.)\n'
        # 无法初始化内部驱动器硬件。 该位是只读的。\n
    elif idx==14:
        argout = 'Bit_14: (if set, programs drive to latch a fault when there is safety circuit consistency check failure.)\n'
        # 如果设置，当安全电路一致性检查失败时，程序将驱动以锁定故障。\n
    elif idx==15:
        argout = 'Bit_15: (If set, programs drive to latch a fault when drive is unable to control motor current.)\n'
        # 如果置位，程序将在驱动器无法控制电动机电流时锁存故障。\n
    elif idx==16:
        argout = 'Bit_16: (If set, programs drive to latch a fault when motor wiring is disconnected, see Open Motor Wiring Check Current (0x19D).)\n'
        # 如果置位，程序将在断开电动机接线时驱动程序以锁定故障，请参阅断开电动机接线检查电流（0x19D）。\n
    elif idx==17:
        argout = 'Bit_17: Reserved.\n'
    elif idx==18:
        argout = 'Bit_18: (Safe torque off active)\n'
        # 安全扭矩关闭有效\n

    return argout