# -*- coding:utf-8 -*-
'''md
    from copley.scripts.constant_lib.Constant_Motor import Maxon_306090
    print(Maxon_306090.Axial_play)

    [20210324]:
        1. 部分数字添加了.，转变为float，若做除法可能会变为零
'''
'''
# rated current 与nominal current 的区别是什么？
    In respect to Current Transformers, Nominal Current is the allowable current in amperes which can be transmitted by each contact continuously and simultaneously.
    对电流变压器而言，Nominal Current 是可通过的电流（单位为安培），该电流可同时并连续地由每个接触点传送。
    The rated current is the continuous, not interrupted current a connector can take when simultaneous power on all contacts is given, without exceeding the maximum temperature.
    Rated current 是在不超过最高温度的情况下，当电力同时供给所有接触点时，连接器可承受的持续不间断电流。
    Connector 连接器是一种供作电流连通及切断的一种插拨零件。本身含有多支镀金的插针，做为插焊在板子孔内生根的阳性外形部份。其背面另有阴性外形的插座部份，可供其他外来的插接。通常电路板欲与其他的排线(Cable)接头，或另与电路板的金手指区连通时，即可由此连接器执行。
    综上所述，Nominal Current 是针对变压器而言的额定电流；而 rated current是针对连接器的额定电流。
'''
# %%
# 309060
class RE_268214():
    """
        RE 30 Ø30 mm, 石墨电刷, 60 Watt 268214
        https://www.maxongroup.com.cn/maxon/view/product/motor/dcmotor/re/re30/268214
        https://www.maxongroup.co.uk/maxon/view/product/motor/dcmotor/re/re30/268214
    """
    # Values at Nominal Voltage
    Nominal_voltage = 24 # V # 额定电压
    No_load_speed = 8810. # rpm # 空载转速
    No_load_current = 165. # mA # 空载电流
    Nominal_speed = 8050. # rpm # 额定转速
    Nominal_torque = max_continuous_torque = 85.6 # mNm # 额定转矩（最大连续转矩）
    Nominal_current = max_continuous_current = 3.47 # A # 额定电流（最大连续负载电流）
    Stall_torque = 1020. # mNm # 堵转转矩
    Stall_current = 39.3 # A # 堵转电流
    Max_efficiency = 87. # % # 最大效率
    # Characteristics/特征值
    Terminal_resistance = 0.611 # Ω # 相间电阻
    Terminal_inductance = 0.119 # mH # 相间电感
    Torque_constant = 25.9 # mNm/A # 转矩常数
    Speed_constant = 369. # rpm/V # 转速常数
    Speed_Torque_gradient = 8.7 # rpm/mNm # 转速/转矩斜率
    Mechanical_time_constant = 3.05 # ms # 机械时间常数
    Rotor_inertia = 33.5 # gcm² # 子惯量
    # Thermal Data/热参数
    Thermal_resistance_housing_ambient = 6. # K/W # 外壳-环境热阻
    Thermal_resistance_winding_housing = 1.7 # K/W # 绕组-外壳热阻
    Thermal_time_constant_winding = 16.3 # s # 绕组热时间常数
    Thermal_time_constant_motor = 593. # s # 电机热时间常数
    Min_Ambient_temperature = -30. # °C # 环境温度(最小)
    Max_Ambient_temperature = +100 # °C # 环境温度(最大)
    Max_winding_temperature = +125 # °C # 绕组最高允许温度
    # Mechanical Data/机械参数
    Bearing_type = 'ball_bearings' # 轴承类型
    Max_speed = 12000. # rpm # 最大允许转速
    Axial_play = 0.1 # mm # 轴向间隙_0.05 - 0.15
    Radial_play = 0.025 # mm # 径向间隙
    Max_axial_load_dynamic = 5.6 # N # 最大轴向载荷（动态）
    Max_force_for_press_fits_static = 110. # N # 最大轴向压配合力（静态）
    static_shaft_supported = 1200. # N # （静态，支撑轴）
    Max_radial_load = 28. # N, 5 mm from flange # 最大径向载荷（距离法兰）
    # Other Specifications # 其它参数
    Number_of_pole_pairs = 1 # 极对数
    Number_of_commutator_segments = 13 # 换向片数量
    Number_of_autoclave_cycles = 0 # 高温高压灭菌次数
    # Product/产品
    Weight = 260. # g # 重量
# 309060
class MR_225787():
    """
        编码器MR,型号L，1024脉冲，3通道，带线性驱动Line Driver
        产品编号 225787
        https://www.maxongroup.com.cn/maxon/view/product/sensor/encoder/Magnetische-Encoder/ENCODERMR/ENCODER-MR-TYPL-256-1024IMP-3KANAL/225787
        https://www.maxongroup.co.uk/maxon/view/product/sensor/encoder/Magnetische-Encoder/ENCODERMR/ENCODER-MR-TYPL-256-1024IMP-3KANAL/225787
    """
    # General information  型号
    Counts_per_turn = 1024 # 每旋转一周的脉冲数
    Number_of_channels = 3 # 通道数
    Four_times_frequency = 4 # 4倍频，自己加的
    Line_Driver = True # 线驱动
    Max_mechanical_speed = 18750. # rpm 最大转速
    # Technical Data  技术参数
    Supply_voltage_Vcc = 5. # 4.7...5.2 V 供电电压
    Driver_used_logic = 'TTL' # 驱动逻辑
    Output_current_per_channel = 2.5 # 0...5 mA 每通道输出电流
    Phase_shift = 90 # °e 相移
    Phase_shift_inaccuracy = 45 # °e 相移，误差
    Index_synchronized_to_AB = True # 零位信号与A/B通道信号同步
    Max_moment_of_inertia_of_code_wheel = 1.7 # gcm² 编码盘最大惯量
    Min_Operating_temperature = -25. # °C 工作温度
    Max_Operating_temperature = +85. # °C 工作温度
# 309060
class GP_166167():
    '''
        行星齿轮箱 GP 32 A Ø32 mm, 0.75 - 4.5 Nm, 金属材质
        产品编号 166167
        https://www.maxongroup.com.cn/maxon/view/product/gear/planetary/gp32/166167
        https://www.maxongroup.co.uk/maxon/view/product/gear/planetary/gp32/166167
    '''
    # General information  一般数据
    Gearhead_type = 'GP' # 齿轮箱类型
    Outer_diameter = 32. # mm 外径
    Version = 'Standard_version' # 版本
    # Gearhead Data  齿轮箱数据
    Reduction = 86 # : 1 减速比
    Absolute_reduction = 14976/175. # 绝对减速比
    Max_motor_shaft_diameter = 4 # mm 最大电机轴直径
    Number_of_stages = 3 # 级数
    Max_continuous_torque = 4.5 # Nm 最大连续转矩
    Max_intermittent_torque = 6.5 # Nm 瞬时允许输出转矩
    Direction_of_rotation_drive_to_output = 'ERROR' # ! 输出端相对于输入端的旋转方向
    Max_efficiency = 70. # % 最大效率
    Average_backlash_no_load = 1 # ° 空载下齿轮箱平均背隙
    Mass_inertia = 0.7 # gcm² 惯量
    Gearhead_length_L1 = 43.1 # mm 齿轮箱长度（L1）
    Max_transmittable_power_continuous = 38. # W 最大连续输出功率
    Max_transmittable_power_intermittent = 25. # W 最大瞬时输出功率
    # Technical Data  技术参数
    Radial_play_max = 0.14 # mm, 5 mm from flange 径向间隙
    Axial_play_max = 0.4 # mm 轴向间隙
    Max_radial_load = 200. # N, 10 mm from flange 最大径向载荷
    Max_axial_load_dynamic = 120. # N 最大轴向载荷（动态）
    Max_force_for_press_fits = 120. # N 最大轴向压配合力
    Max_continuous_input_speed = 6000. # rpm 最大连续输入转速
    Max_intermittent_input_speed = 6000. # rpm 最大瞬时输入转速
    Min_Recommended_temperature_range = -20. # °C 建议温度范围
    Max_Recommended_temperature_range = +100. # °C 建议温度范围
    Extended_temperature_range = -40. # °C 扩展温度范围
    Extended_temperature_range = +100. # °C 扩展温度范围
    Number_of_autoclave_cycles = 0 # 高温高压灭菌次数
    # Product  产品
    Weight = 190. # g 重量
# 305474/266761
class RE_118752():
    '''
        RE 25 Ø25 mm, 石墨电刷, 20 Watt
        产品编号 118752
        https://www.maxongroup.com.cn/maxon/view/product/motor/dcmotor/re/re30/118752
        https://www.maxongroup.co.uk/maxon/view/product/motor/dcmotor/re/re30/118752
    '''
    # Values at nominal voltage  额定电压值
    Nominal_voltage = 24. # V 额定电压
    No_load_speed = 9560. # rpm 空载转速
    No_load_current = 36.9 # mA 空载电流
    Nominal_speed = 8330. # rpm 额定转速
    Nominal_torque = max_continuous_torque = 26.3 # mNm 额定转矩（最大连续转矩）
    Nominal_current = max_continuous_current = 1.16 # A 额定电流（最大连续负载电流）
    Stall_torque = 243. # mNm 堵转转矩
    Stall_current = 10.4 # A 堵转电流
    Max_efficiency = 85. # % 最大效率
    # Characteristics  特征值
    Terminal_resistance = 2.32 # Ω 相间电阻
    Terminal_inductance = 0.238 # mH 相间电感
    Torque_constant = 23.4 # mNm/A 转矩常数
    Speed_constant = 408. # rpm/V 转速常数
    Speed_Torque_gradient = 40.3 # rpm/mNm 转速/转矩斜率
    Mechanical_time_constant = 4.55 # ms 机械时间常数
    Rotor_inertia = 10.8 # gcm² 转子惯量
    # Thermal data  热参数
    Thermal_resistance_housing_ambient = 14. # K/W 外壳-环境热阻
    Thermal_resistance_winding_housing = 3.1 # K/W 绕组-外壳热阻
    Thermal_time_constant_winding = 12.5 # s 绕组热时间常数
    Thermal_time_constant_motor = 612. # s 电机热时间常数
    Min_Ambient_temperature = -30. # °C 环境温度
    Max_Ambient_temperature = +100. # °C 环境温度
    Max_winding_temperature = +125. # °C 绕组最高允许温度
    # Mechanical data  机械参数
    Bearing_type = 'ball_bearings' # 轴承类型
    Max_speed = 14000. # rpm 最大允许转速
    Axial_play = 0.1 # 0.05 - 0.15 mm 轴向间隙
    Radial_play = 0.025 # mm 径向间隙
    Max_axial_load_dynamic = 3.2 # N 最大轴向载荷（动态）
    Max_force_for_press_fits_static = 64. # N 最大轴向压配合力（静态）
    static_shaft_supported = 800. # N （静态，支撑轴）
    Max_radial_load = 16. # N, 5 mm from flange 最大径向载荷
    # Other specifications  其它参数
    Number_of_pole_pairs = 1 # 极对数
    Number_of_commutator_segments = 11 # 换向片数量
    Number_of_autoclave_cycles = 0 # 高温高压灭菌次数
    # Product  产品
    Weight = 130. # g 重量
# 305474/266761
class MR_225780():
    """
        编码器MR,型号ML，1000次脉冲，3通道，带线性驱动Line Driver
        产品编号 225780
        https://www.maxongroup.com.cn/maxon/view/product/sensor/encoder/Magnetische-Encoder/ENCODERMR/ENCODER-MR-TYPML-128-1000IMP-3KANAL/225780
        https://www.maxongroup.co.uk/maxon/view/product/sensor/encoder/Magnetische-Encoder/ENCODERMR/ENCODER-MR-TYPML-128-1000IMP-3KANAL/225780
    """
    # General information  型号
    Counts_per_turn = 1000 # 每旋转一周的脉冲数
    Number_of_channels = 3 # 通道数
    Four_times_frequency = 4 # 4倍频，自己加的
    Line_Driver = True # 线驱动
    Max_mechanical_speed = 12000. # rpm 最大转速
    # Technical Data  技术参数
    Supply_voltage_Vcc = 5.0 # 4.7...5.2 V 供电电压
    Driver_used_logic = 'TTL' # 驱动逻辑
    Output_current_per_channel = 0.25 # 0...5 mA 每通道输出电流
    Phase_shift = 90 # °e 相移
    Phase_shift_inaccuracy = 45 # °e 相移，误差
    Index_synchronized_to_AB = True # Yes 零位信号与A/B通道信号同步
    Max_moment_of_inertia_of_code_wheel = 0.7 # gcm² 编码盘最大惯量
    Min_Operating_temperature = -25. # °C 工作温度
    Max_Operating_temperature = +85. # °C 工作温度
# 305474
class GP_166936():
    '''
        行星齿轮箱 GP 32 C Ø32 mm, 1.0 - 6.0 Nm, 陶瓷材质
        产品编号 166936
        https://www.maxongroup.com.cn/maxon/view/product/gear/planetary/gp32/166936
        https://www.maxongroup.co.uk/maxon/view/product/gear/planetary/gp32/166936
    '''
    # General information  一般数据
    Gearhead_type = 'GP' # 齿轮箱类型
    Outer_diameter = 32. # mm 外径
    Version = 'Ceramic_version' # 版本
    # Gearhead Data  齿轮箱数据
    Reduction = 23 # : 1 减速比
    Absolute_reduction = 576/25. # 绝对减速比
    Max_motor_shaft_diameter = 4. # mm 最大电机轴直径
    Number_of_stages = 2 # 级数
    Max_continuous_torque = 3. # Nm 最大连续转矩
    Max_intermittent_torque = 3.75 # Nm 瞬时允许输出转矩
    Direction_of_rotation_drive_to_output = 'ERROR' # ! 输出端相对于输入端的旋转方向
    Max_efficiency = 75. # % 最大效率
    Average_backlash_no_load = 0.8 # ° 空载下齿轮箱平均背隙
    Mass_inertia = 0.8 # gcm² 惯量
    Gearhead_length_L1 = 36.4 # mm 齿轮箱长度（L1）
    Max_transmittable_power_continuous = 110. # W 最大连续输出功率
    Max_transmittable_power_intermittent = 140. # W 最大瞬时输出功率
    # Technical Data  技术参数
    Radial_play_max = 0.14 # mm, 5 mm from flange 径向间隙
    Axial_play_max = 0.4 # mm 轴向间隙
    Max_radial_load = 140. # N, 10 mm from flange 最大径向载荷
    Max_axial_load_dynamic = 120. # N 最大轴向载荷（动态）
    Max_force_for_press_fits = 120. # N 最大轴向压配合力
    Max_continuous_input_speed = 8000. # rpm 最大连续输入转速
    Max_intermittent_input_speed = 8000. # rpm 最大瞬时输入转速
    Recommended_temperature_range = -40. # °C 建议温度范围
    Recommended_temperature_range = +100. # °C 建议温度范围
    Number_of_autoclave_cycles = 0 # 高温高压灭菌次数
    # Product  产品
    Weight = 160. # g 重量
# 266761
class GP_144043():
    '''
        行星齿轮箱 GP 26 B Ø26 mm, 0.5 - 2.0 Nm, 陶瓷材质 | 陶瓷版
        产品编号 144043
        https://www.maxongroup.com.cn/maxon/view/product/gear/planetary/GP-Sonderprogramm/144043
        https://www.maxongroup.co.uk/maxon/view/product/gear/planetary/GP-Sonderprogramm/144043
    '''
    # General information  一般数据
    Gearhead_type = 'GP' # 齿轮箱类型
    Outer_diameter = 26. # mm 外径
    Version = 'Standard_version' # 版本
    # Gearhead Data  齿轮箱数据
    Reduction = 128 # : 1 减速比
    Absolute_reduction = 41553/325. # 绝对减速比
    Max_motor_shaft_diameter = 3.2 # mm 最大电机轴直径
    Number_of_stages = 3 # 级数
    Max_continuous_torque = 1.3 # Nm 最大连续转矩
    Max_intermittent_torque = 1.9 # Nm 瞬时允许输出转矩
    Direction_of_rotation_drive_to_output = 'ERROR' # ! 输出端相对于输入端的旋转方向
    Max_efficiency = 59. # % 最大效率
    Average_backlash_no_load = 1.6 # ° 空载下齿轮箱平均背隙
    Mass_inertia = 0.4 # gcm² 惯量
    Gearhead_length_L1 = 42.8 # mm 齿轮箱长度（L1）
    Max_transmittable_power_continuous = 8.5 # W 最大连续输出功率
    Max_transmittable_power_intermittent = 12. # W 最大瞬时输出功率
    # Technical Data  技术参数
    Radial_play = 0.08 # max. 0.08 mm, 10 mm from flange 径向间隙（距离法兰）
    Axial_play = 0.05 # 0 - 0.1 mm 轴向间隙
    Max_radial_load = 100. # N, 10 mm from flange 最大径向载荷（距离法兰）
    Max_axial_load_dynamic = 100. # N 最大轴向载荷（动态）
    Max_force_for_press_fits = 100. # N 最大轴向压配合力
    Max_continuous_input_speed = 8000. # rpm 最大连续输入转速
    Max_intermittent_input_speed = 8000. # rpm 最大瞬时输入转速
    Min_Recommended_temperature_range = -40. # °C 建议温度范围
    Max_Recommended_temperature_range = +100. # °C 建议温度范围
    Number_of_autoclave_cycles = 0 # 高温高压灭菌次数
    # Product  产品
    Weight = 100. # g 重量

# %%
class Maxon_306090(GP_166167, RE_268214, MR_225787):
    """
    drive
    后驱 - 左侧 - 逆时针 - 前进
    后驱 - 左侧 - 顺时针 - 前进
    """
    # Max_Vel = (Nominal_speed * Counts_per_turn * Four_times_frequency) / 60
     # unit: (counts/min)/60 -> counts/s
    Max_Vel = (RE_268214.Nominal_speed * MR_225787.Counts_per_turn * MR_225787.Four_times_frequency) / 60
    
    # Counts_per_Reduction = Counts_per_turn * Four_times_frequency * Reduction
     # `输出轴`转一圈的编码器计数。参考这个单词来定义的变量Counts_per_turn
    Counts_per_Reduction = MR_225787.Counts_per_turn * MR_225787.Four_times_frequency * GP_166167.Reduction
class Maxon_305474(GP_166936, RE_118752, MR_225780):
    """
    wing
    后驱 - 左侧 - 顺时针 - 打开
    后驱 - 右侧 - 逆时针 - 打开
    """
    Max_Vel = RE_118752.Nominal_speed * MR_225780.Counts_per_turn * MR_225780.Four_times_frequency / 60
    Counts_per_Reduction = MR_225780.Counts_per_turn * MR_225780.Four_times_frequency * GP_166936.Reduction
    # 机构行程(注意要加小数点)
    Stroke = Counts_per_Reduction * (46./360) * 10
class Maxon_266761(GP_144043, RE_118752, MR_225780):
    """
    sting
    后驱 - 左侧 - 顺时针 - 伸出
    后驱 - 右侧 - 逆时针 - 伸出
    """
    Max_Vel = RE_118752.Nominal_speed * MR_225780.Counts_per_turn * MR_225780.Four_times_frequency / 60
    Counts_per_Reduction = MR_225780.Counts_per_turn * MR_225780.Four_times_frequency * GP_144043.Reduction
    Stroke = Counts_per_Reduction * (35./360)