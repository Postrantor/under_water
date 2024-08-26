#! /usr/bin/env python
# -*- coding:utf-8 -*-

# %% doc
__all__ = ['BitsMapped']  # 可用于模块导入时限制，只有__all__内指定的属性、方法、类可被导入
__docformat__ = 'restructuredtext'  # 允许诸如 epydoc之类的python文档生成器工具知道如何正确解析模块文档

# %%


class HomingMethod(object):
    """
    0xC2、0xC9
    """

    def __init__(self):
        # self.ascii = ascii
        # self.data = data
        pass

    def __str__(self):
        msg = 'from copley.scripts.copley_lib.ParamDict_HomingMethod import BitsMapped'
        return msg


def BitsMapped(ascii='0xC2', data=0):
    """
    docstring
    """
    if ascii == '0xC2':
        argout = BitsMapped_0xC2(int(data))
    elif ascii == '0xC9':
        argout = BitsMapped_0xC9(int(data))
    return argout


def BitsMapped_0xC2(idx):
    '''
        # 参数字典.pdf
        Homing Method Configuration. Bits: 0~15
            0~3
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

        # ASCII 编程指南 - 中文.pdf
        [512, 544, 560, 513, 529, 545, 561, 514, 530, 546, 562, 610, 626, 516, 532, 548, 564, 771, 787, 515, 531, 803, 819, 867, 883, 547, 563, 611, 627]
        1. Set Current Position as Home
            a. N/A 512 = 001000000000
        2. Next Index
            a. P 544 = 001000100000
            b. N 560 = 001000110000
        3. Limit Switch
            a. P 513 = 001000000001
            b. N 529 = 001000010001
        4. Limit Switch Out to Index
            a. P 545 = 001000100001
            b. N 561 = 001000110001
        5. Home Switch
            a. P 514 = 001000000010
            b. N 530 = 001000010010
        6. Home Switch Out to Index
            a. P 546 = 001000100010
            b. N 562 = 001000110010
        7. Home Switch In to Index
            a. P 610 = 001001100010
            b. N 626 = 001001110010
        8. Hard Stop
            a. P 516 = 001000000100
            b. N 532 = 001000010100
        9. Hard Stop Out to Index
            a. P 548 = 001000100100
            b. N 564 = 001000110100
        10. Lower Home
            a. P 771 = 001100000011
            b. N 787 = 001100010011
        11. Upper Home
            a. P 515 = 001000000011
            b. N 531 = 001000010011
        12. Lower Home Outside Index
            a. P 803 = 001100100011
            b. N 819 = 001100110011
        13. Lower Home Inside Index
            a. P 867 = 001101100011
            b. N 883 = 001101110011
        14. Upper Home Outside Index
            a. P 547 = 001000100011
            b. N 563 = 001000110011
        15. Upper Home Inside Index
            a. P 611 = 001001100011
            b. N 627 = 001001110011
        16. Immediate Home
            a. N/A 15

        # CME2 用户指南 - 原文.pdf
        P198 - APPENDIX B
    '''
    if idx == 512:  # 0010,0000,0000
        argout = '''Set Current Position as Home.
                        The current position is the home position.'''
        # 当前位置是主位置。
    elif idx == 544:  # 0010,0010,0000
        argout = '''Positive: Next Index.
                        Home is the first index pulse found in the positive direction. Direction of motion is positive. If a positive limit switch is activated before the index pulse, an error is generated.'''
        # 家是第一个指数脉冲发现的积极方向。运动的方向是正的。如果一个正的限位开关在指数脉冲之前被激活，就会产生一个错误。
    elif idx == 560:  # 0010,0011,0000
        argout = '''Negative: Next Index.
                        Home is the first index pulse found in negative direction. Direction of motion is negative. If a negative limit switch is activated before the index pulse, an error is generated.'''
        # Home是第一个在负方向发现的指数脉冲。运动方向是负的。如果在指数脉冲之前激活负限位开关，就会产生错误。
    elif idx == 513:  # 0010,0000,0001
        argout = '''Positive: Limit Switch.
                        Home is the transition of the positive limit switch. Initial direction of motion is positive if the positive limit switch is inactive.'''
        # Home是正向限位开关的过渡。如果正限位开关不活跃，运动的初始方向为正。
    elif idx == 529:  # 0010,0001,0001
        argout = '''Negative: Limit Switch.
                        Home is the transition of negative limit switch. Initial direction of motion is negative if the negative limit switch is inactive.'''
        # 家是过渡负限位开关。如果负限位开关不活动，运动的初始方向为负。
    elif idx == 545:  # 0010,0010,0001
        argout = '''Positive: Limit Switch Out to Index.
                        Home is the first index pulse to the negative side of the positive limit switch transition. Initial direction of motion is positive if the positive limit switch is inactive (shown here as low).'''
        # 首个指数脉冲是Home向负侧的正限位开关过渡。初始运动方向是正的，如果正的限位开关是不活跃的(在这里显示为低)。
    elif idx == 561:  # 0010,0011,0001
        argout = '''Negative: Limit Switch Out to Index.
                        Home is the first index pulse to the positive side of the negative limit switch transition. Initial direction of motion is negative if the negative limit switch is inactive (shown here as low).'''
        # 首阶指数脉冲是向正向一侧的负极限开关过渡。初始运动方向是负的，如果负限位开关是不活跃的(在这里显示为低)。
    elif idx == 514:  # 0010,0000,0010
        argout = '''Positive: Home Switch.
                        Home is the home switch transition. Initial direction of motion is positive if the home switch is inactive. If a limit switch is activated before the home switch transition, an error is generated.'''
        # Home是Home开关的转换。如果home开关处于非活动状态，初始运动方向为正。如果限位开关在主开关转换之前被激活，则会产生错误。
    elif idx == 530:  # 0010,0001,0010
        argout = '''Negative: Home Switch.
                        Home is the home switch transition. Initial direction of motion is negative if the home switch is inactive. If a limit switch is activated before the home switch transition, an error is generated.'''
        # Home是Home开关的转换。如果home开关处于非活动状态，则初始运动方向为负。如果限位开关在主开关转换之前被激活，则会产生错误。
    elif idx == 546:  # 0010,0010,0010
        argout = '''Positive: Home Switch Out to Index.
                        Home is the first index pulse to the negative side of the home switch transition. Initial direction of motion is positive if the home switch is inactive. If a limit switch is activated before the home switch transition, an error is generated.'''
        # Home是第一个指数脉冲到负侧Home开关的过渡。如果home开关处于非活动状态，初始运动方向为正。如果限位开关在主开关转换之前被激活，则会产生错误。
    elif idx == 562:  # 0010,0011,0010
        argout = '''Negative: Home Switch Out to Index.
                        Home is the first index pulse to the positive side of the home switch transition. Initial direction of motion is negative if the home switch is inactive. If a limit switch is activated before the home switch transition, an error is generated.'''
        # 归位是归位开关转换正端的第一个索引脉冲。 如果归零开关未激活，则初始运动方向为负。 如果在转换原点开关之前激活了限位开关，则会产生错误。
    elif idx == 610:  # 0010,0110,0010
        argout = '''Positive: Home Switch In to Index.
                        Home is the first index pulse to the positive side of the home switch transition. Initial direction of motion is positive if the home switch is inactive. If a limit switch is activated before the home switch transition, an error is generated.'''
        # 归位是归位开关转换正端的第一个索引脉冲。 如果归零开关未激活，则初始运动方向为正。 如果在转换原点开关之前激活了限位开关，则会产生错误。
    elif idx == 626:  # 0010,0111,0010
        argout = '''Negative: Home Switch In to Index.
                        Home is the first index pulse to the negative side of the home switch transition. Initial direction of motion is negative if the home switch is inactive. If a limit switch is activated before the home switch transition, an error is generated.'''
        # 归位是到归位开关转换的负侧的第一个索引脉冲。 如果归零开关未激活，则初始运动方向为负。 如果在转换原点开关之前激活了限位开关，则会产生错误。
    elif idx == 516:  # 0010,0000,0100
        argout = '''Positive: Hard Stop.
                        Home is the positive hard stop. Direction of motion is positive. In servo modes, the hard stop is reached when the amplifier outputs the homing Current Limit continuously for the amount of time specified in the Delay Time.
                        If a positive limit switch is activated before the hard stop, an error is generated.'''
        # 家是积极的硬停。 运动方向为正。 在伺服模式下，当放大器在“延迟时间”中指定的时间范围内连续输出归位电流限制时，将达到硬停止。如果在硬停止之前激活了正限位开关，则会产生错误。
    elif idx == 532:  # 0010,0001,0100
        argout = '''Negative: Hard Stop.
                        Home is the negative hard stop. Direction of motion is negative. The hard stop is reached when the amplifier outputs the homing Current Limit continuously for the amount of time specified in the Delay Time. If a negative limit switch is activated before the hard stop, an error is generated.'''
        # 家是负面的硬停。 运动方向为负。 当放大器在“延迟时间”中指定的时间范围内连续输出归位电流限制时，将达到硬停止。 如果在硬停止之前激活了负限位开关，则会产生错误。
    elif idx == 548:  # 0010,0010,0100
        argout = '''Positive: Hard Stop Out to Index.
                        Home is the first index pulse on the negative side of the positive hard stop. Initial direction of motion is positive. The hard stop is reached when the amplifier outputs the homing Current Limit continuously for the amount of time specified in the Delay Time. If a positive limit switch is activated before the hard stop, an error is generated.'''
        # 归位是正硬停止的负侧的第一个索引脉冲。 初始运动方向为正。 当放大器在“延迟时间”中指定的时间范围内连续输出归位电流限制时，将达到硬停止。 如果在硬停止之前激活了正限位开关，则会产生错误。
    elif idx == 564:  # 0010,0011,0100
        argout = '''Negative: Hard Stop Out to Index.
                        Home is the first index pulse on the positive side of the negative hard stop. Initial direction of motion is negative. The hard stop is reached when the amplifier outputs the homing Current Limit continuously for the amount of time specified in the Delay Time. If a negative limit switch is activated before the hard stop, an error is generated.'''
        # 归位是负硬停止的正侧上的第一个索引脉冲。 初始运动方向为负。 当放大器在“延迟时间”中指定的时间范围内连续输出归位电流限制时，将达到硬停止。 如果在硬停止之前激活了负限位开关，则会产生错误。
    elif idx == 771:  # 0011,0000,0011
        argout = '''Positive: Lower Home.
                        Home is the negative edge of a momentary home switch. Initial direction of motion is positive if the home switch is inactive. Motion will reverse if a positive limit switch is activated before the home switch; then, if a negative limit switch is activated before the home switch, an error is generated.'''
        # 归位是瞬时归位开关的下降沿。 如果归零开关未激活，则初始运动方向为正。 如果在回零开关之前激活了正限位开关，则运动会反向； 然后，如果在回零开关之前激活了负限位开关，则会产生错误。
    elif idx == 787:  # 0011,0001,0011
        argout = '''Negative: Lower Home.
                        Home is the negative edge of a momentary home switch. Initial direction of motion is negative. If the initial motion leads away from the home switch, the axis reverses on encountering the negative limit switch; then, if a positive limit switch is activated before the home switch, an error is generated.'''
        # 归位是瞬时归位开关的下降沿。 初始运动方向为负。 如果初始运动远离原点开关，则轴在遇到负限位开关时会反转；否则，轴将反转。 然后，如果在回零开关之前激活了正限位开关，则会产生错误。
    elif idx == 515:  # 0010,0000,0011
        argout = '''Positive: Upper Home.
                        Home is the positive edge of a momentary home switch. Initial direction of motion is positive. If the initial motion leads away from the home switch, the axis reverses on encountering the positive limit switch; then, if a negative limit switch is activated before the home switch, an error is generated.'''
        # 归位是瞬时归位切换的上升沿。 初始运动方向为正。 如果初始运动远离原点开关，则在遇到正向限位开关时轴将反转；否则，轴将反向运动。 然后，如果在回零开关之前激活了负限位开关，则会产生错误。
    elif idx == 531:  # 0010,0001,0011
        argout = '''Negative: Upper Home.
                        Home is the positive edge of momentary home switch. Initial direction of motion is negative if the home switch is inactive. If the initial motion leads away from the home switch, the axis reverses on encountering the negative limit switch; then, if a positive limit switch is activated before the home switch, an error is generated.'''
        # 归位是瞬时归位切换的上升沿。 如果归零开关未激活，则初始运动方向为负。 如果初始运动远离原点开关，则轴在遇到负限位开关时会反转；否则，轴将反转。 然后，如果在回零开关之前激活了正限位开关，则会产生错误。
    elif idx == 803:  # 0011,0010,0011
        argout = '''Positive: Lower Home Outside Index.
                        Home is the first index pulse on the negative side of the negative edge of a momentary home switch. Initial direction of motion is positive if the home switch is inactive. If the initial motion leads away from the home switch, the axis reverses on encountering the positive limit switch; then, if a negative limit switch is activated before the home switch, an error is generated.'''
        # 归位是瞬时归位开关负沿负侧的第一个索引脉冲。 如果归零开关未激活，则初始运动方向为正。 如果初始运动远离原点开关，则在遇到正向限位开关时轴将反转；否则，轴将反向运动。 然后，如果在回零开关之前激活了负限位开关，则会产生错误。
    elif idx == 819:  # 0011,0011,0011
        argout = '''Negative: Lower Home Outside Index.
                        Home is the first index pulse on the negative side of the negative edge of a momentary home switch. Initial direction of motion is negative. If the initial motion leads away from the home switch, the axis reverses on encountering the negative limit switch; then, if a negative limit switch is activated before the home switch, an error is generated.'''
        # 归位是瞬时归位开关负沿负侧的第一个索引脉冲。 初始运动方向为负。 如果初始运动远离原点开关，则轴在遇到负限位开关时会反转；否则，轴将反转。 然后，如果在回零开关之前激活了负限位开关，则会产生错误。
    elif idx == 867:  # 0011,0110,0011
        argout = '''Positive: Lower Home Inside Index.
                        Home is the first index pulse on the positive side of the negative edge of a momentary home switch. Initial direction of motion is positive if the home switch is inactive. If the initial motion leads away from the home switch, the axis reverses on encountering the positive limit switch; then, if a negative limit switch is activated before the home switch, an error is generated.'''
        # 归零是瞬时归零开关负沿的正侧的第一个索引脉冲。 如果归零开关未激活，则初始运动方向为正。 如果初始运动远离原点开关，则在遇到正向限位开关时轴将反转；否则，轴将反向运动。 然后，如果在回零开关之前激活了负限位开关，则会产生错误。
    elif idx == 883:  # 0011,0111,0011
        argout = '''Negative: Lower Home Inside Index.
                        Home is the first index pulse on the positive side of the negative edge of a momentary home switch. Initial direction of motion is negative. If the initial motion leads away from the home switch, the axis reverses on encountering the negative limit switch; then, if a negative limit switch is activated before the home switch, an error is generated.'''
        # 归零是瞬时归零开关负沿的正侧的第一个索引脉冲。 初始运动方向为负。 如果初始运动远离原点开关，则轴在遇到负限位开关时会反转；否则，轴将反转。 然后，如果在回零开关之前激活了负限位开关，则会产生错误。
    elif idx == 547:  # 0010,0010,0011
        argout = '''Positive: Upper Home Outside Index.
                        Home is the first index pulse on the positive side of the positive edge of a momentary home switch. Initial direction of motion is positive. If the initial motion leads away from the home switch, the axis reverses on encountering the positive limit switch; then, if a negative limit switch is activated before the home switch, an error is generated.'''
        # Home是瞬时Home开关正边缘正侧的第一个索引脉冲。初始运动方向为正。如果初始运动远离主开关，则轴在遇到正限位开关时反转；然后，如果在主开关之前激活负限位开关，则产生错误。
    elif idx == 563:  # 0010,0011,0011
        argout = '''Negative: Upper Home Outside Index.
                        Home is the first index pulse on the positive side of the positive edge of a momentary home switch. Initial direction of motion is negative if the home switch is inactive. If the initial position is right of the home position, the axis reverses on encountering the home switch.'''
        # Home是瞬时Home开关正边缘正侧的第一个索引脉冲。如果原点开关处于非活动状态，则初始运动方向为负。如果初始位置在起始位置的右侧，则轴在遇到起始开关时反转。
    elif idx == 611:  # 0010,0110,0011
        argout = '''Positive: Upper Home Inside Index.
                        Home is the first index pulse on the negative side of the positive edge of momentary home switch. Initial direction of motion is positive. If initial motion leads away from the home switch, the axis reverses on encountering the positive limit switch; then, if a negative limit switch is activated before the home switch, an error is generated.'''
        # Home是瞬时Home开关正边缘负侧的第一个索引脉冲。初始运动方向为正。如果初始运动远离原点开关，则轴在遇到正限位开关时反转；然后，如果在原点开关之前激活负限位开关，则产生错误。
    elif idx == 627:  # 0010,0111,0011
        argout = '''Negative: Upper Home Inside Index.
                        Home is the first index pulse on the negative side of the positive edge of a momentary home switch. Initial direction of motion is negative if the home switch is inactive. If initial motion leads away from the home switch, the axis reverses on encountering the negative limit; then, if a negative limit switch is activated before the home switch, an error is generated.'''
        # Home是瞬时Home开关正边缘负侧的第一个索引脉冲。如果原点开关处于非活动状态，则初始运动方向为负。如果初始运动远离原点开关，轴在遇到负限位时反转；然后，如果在原点开关之前激活负限位开关，则产生错误。
    elif idx == 15:  # 0000,0000,1111
        argout = '''Bit_15: Immediate Home.
                        Immediate home. This value causes the amp to be referenced immediately on power-up. Once encoder is initialized, home offset value is added to encoder position and result is set as current referenced position. This is primarily useful with absolute encoders.'''
        # 直接回家。此值使放大器在通电时立即被引用。一旦编码器初始化，原点偏移值被添加到编码器位置，结果被设置为当前参考位置。这主要适用于绝对编码器。
    return argout


def BitsMapped_0xC9(idx):
    '''
        0xc9    R*  Trajectory Status Register
        The trajectory register parameter (0xc9) provides trajectory generator status information. 0xc9 is read-only, and available in RAM only. Bit mapped values described below:
        Bit Description
            0-8 Reserved for future use.
            9    Cam table underflow.
            10  Reserved for future use
            11  Homing error. If set, an error occurred in the last home attempt. Cleared by a home command.
            12  Referenced. Set when a homing command has been successfully executed. Cleared by a home command.
            13  Homing. If set, the drive is running a home command.
            14  Set when a move is aborted. Cleared at the start of the next move.
            15  In-Motion Bit. If set, the trajectory generator is presently generating a profile.
    '''
    argout = ''
    if idx in [0, 1, 2, 4, 8, 16, 32, 64, 128, 256]:  # 0~8
        argout = '''Bit_00-08: Reserved for future use.'''
    elif idx == 512:  # 9
        argout = '''Bit_09: Cam table underflow.'''
    elif idx == 1024:  # 10
        argout = '''Bit_10: Reserved for future use'''
    elif idx == 2048:  # 11
        argout = '''Bit_11: Homing error. If set, an error occurred in the last home attempt. Cleared by a home command.'''
    elif idx == 4096:  # 12
        argout = '''Bit_12: Referenced. Set when a homing command has been successfully executed. Cleared by a home command.'''
    elif idx == 8192:  # 13
        argout = '''Bit_13: Homing. If set, the drive is running a home command.'''
    elif idx == 16384:  # 14
        argout = '''Bit_14: Set when a move is aborted. Cleared at the start of the next move.'''
    elif idx == 32758:  # 15
        argout = '''Bit_15: In-Motion Bit. If set, the trajectory generator is presently generating a profile.'''

    return argout
