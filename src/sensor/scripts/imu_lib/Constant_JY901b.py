#! /usr/bin/env python
# -*- coding:utf-8 -*-

# %%
DEFAULT_ADDRESS = 0x50
# 寄存器地址表
SAVE = 0x00 # 保存当前配置
CALSW = 0x01 # 校准

# %%
RSW = 0x02 # 回传数据内容
RATE = 0x03 # 回传数据速率
# 7.2.9 设置回传速率
# 0xFF 0xAA 0x03 RATE 0x00
# RATE：回传速率
# 0x01：0.1Hz
# 0x02：0.5Hz
# 0x03：1Hz
# 0x04：2Hz
# 0x05：5Hz
# 0x06：10Hz（默认）
# 0x07：20Hz
# 0x08：50Hz
# 0x09：100Hz
# 0x0a：无（保留）
# 0x0b：200Hz
# 0x0c：单次输出
# 设置完成以后需要点保存配置按钮，再给模块重新上电后生效
BAUD = 0x04 # 串口波特率
# 7.2.10 设置串口波特率
# 0xFF 0xAA 0x04 BAUD 0x00
# BAUD：波特率设置
# 0x00：2400
# 0x01：4800
# 0x02：9600（默认）
# 0x03：19200
# 0x04：38400
# 0x05：57600
# 0x06：115200
# 0x07：230400
# 0x08：460800
# 0x09：921600

AXOFFSET = 0x05 # X 轴加速度零偏
AYOFFSET = 0x06 # Y 轴加速度零偏
AZOFFSET = 0x07 # Z 轴加速度零偏
GXOFFSET = 0x08 # X 轴角速度零偏
GYOFFSET = 0x09 # Y 轴角速度零偏
GZOFFSET = 0x0a # Z 轴角速度零偏
HXOFFSET = 0x0b # X 轴磁场零偏
HYOFFSET = 0x0c # Y 轴磁场零偏
HZOFFSET = 0x0d # Z 轴磁场零偏
D0MODE = 0x0e # D0 模式
D1MODE = 0x0f # D1 模式
D2MODE = 0x10 # D2 模式
D3MODE = 0x11 # D3 模式
D0PWMH_D0PWM = 0x12 # 高电平宽度
D1PWMH_D1PWM = 0x13 # 高电平宽度
D2PWMH_D2PWM = 0x14 # 高电平宽度
D3PWMH_D3PWM = 0x15 # 高电平宽度
D0PWMT_D0PWM = 0x16 # 周期
D1PWMT_D1PWM = 0x17 # 周期
D2PWMT_D2PWM = 0x18 # 周期
D3PWMT_D3PWM = 0x19 # 周期
IICADDR_IIC = 0x1a # 地址
LEDOFF = 0x1b # 关闭LED 指示灯
GPSBAUD = 0x1c # GPS 连接波特率

YYMM = 0x30 # 年、月
DDHH = 0x31 # 日、时
MMSS = 0x32 # 分、秒
MS = 0x33 # 毫秒

AX = 0x34 # X 轴加速度
AY = 0x35 # Y 轴加速度
AZ = 0x36 # Z 轴加速度
GX = 0x37 # X 轴角速度
GY = 0x38 # Y 轴角速度
GZ = 0x39 # Z 轴角速度
HX = 0x3a # X 轴磁场
HY = 0x3b # Y 轴磁场
HZ = 0x3c # Z 轴磁场
ROLL_X = 0x3d # 轴角度
PITCH_Y = 0x3e # 轴角度
YAW_Z = 0x3f # 轴角度

TEMP = 0x40 # 模块温度

D0STATUS = 0x41 # 端口D0 状态
D1STATUS = 0x42 # 端口D1 状态
D2STATUS = 0x43 # 端口D2 状态
D3STATUS = 0x44 # 端口D3 状态

PRESSUREL = 0x45 # 气压低字
PRESSUREH = 0x46 # 气压高字
HEIGHTL = 0x47 # 高度低字
HEIGHTH = 0x48 # 高度高字

LONL = 0x49 # 经度低字
LONH = 0x4a # 经度高字
LATL = 0x4b # 纬度低字
LATH = 0x4c # 纬度高字
GPSHEIGHT_GPS = 0x4d # 高度
GPSYAW_GPS = 0x4e # 航向角
GPSVL_GPS = 0x4f # 地速低字
GPSVH_GPS = 0x50 # 地速高字

Q0 = 0x51 # 四元素Q0
Q1 = 0x52 # 四元素Q1
Q2 = 0x53 # 四元素Q2
Q3 = 0x54 # 四元素Q3

# 7.2.1 解锁指令
# 0xFF 0xAA 0x69 0x88 0xB5
# 对模块进行指令控制时必须先发送解锁指令，指令控制才能发送成功。
# 7.2.2 保持配置
# 0xFF 0xAA 0x00 SAVE 0x00
# SAVE：设置
# 0：保持当前配置
# 1：恢复默认（出厂）配置并保存
# 7.2.3 设置校准
# 0xFF 0xAA 0x01 CALSW 0x00
# CALSW：设置校准模式
# 0：退出校准模式
# 1：进入加速度计校准模式
# 2：进入磁场校准模式
# 3：高度置0
# 0xFF 0xAA 0x01 0x04 0x00
# Z 轴角度归零，只在切换成6 轴算法下才能成功置零。
# 7.2.4 设置安装方向
# 0xFF 0xAA 0x23 DIRECTION 0x00
# DIRECTION：设置安装方向
# 0：设置为水平安装
# 1：设置为垂直安装
# 7.2.5 休眠与解休眠
# 0xFF 0xAA 0x22 0x01 0x00
# 发送该指令模块进入休眠（待机）状态，再发送一次，模块从待机状态进入工作状态。
# 7.2.6 算法转换
# 0xFF 0xAA 0x24 ALG 0x00
# ALG：九轴算法与六轴算法设置
# 0：设置成9 轴算法
# 1：设置成6 轴算法

# %%7.2.7 陀螺仪自动校准
# 0xFF 0xAA 0x63 GYRO 0x00
# GYRO：陀螺仪校准设置
# 0：选择陀螺仪自动校准
# 1：去掉陀螺仪自动校准
# 7.2.8 设置回传内容
# 0xFF 0xAA 0x02 RSWL RSWH
# RSWL 位定义
# 位7 6 5 4 3 2 1 0
# 名称0x57 包0x56 包0x55 包0x54 包0x53 包0x52 包0x51 包0x50 包
# 默认值0 0 0 1 1 1 1 0
# RSWH 位定义
# 位7 6 5 4 3 2 1 0
# 名称X X X X X 0x5A 包0x59 包0x58 包
# 默认值0 0 0 0 0 0 0 0
# X 为未定义名称。
# 0x50 包：时间信息包
# 0：不输出0x50 数据包
# 1：输出0x50 数据包
# 0x51 包：加速度信息包
# 0：不输出0x51 数据包
# 1：输出0x51 数据包
# 0x52 包：角速度信息包
# 0：不输出0x52 数据包
# 1：输出0x52 数据包
# 0x53 包：角度信息包
# 0：不输出0x53 数据包
# 1：输出0x53 数据包
# 0x54 包：磁场信息包
# 0：不输出0x54 数据包
# 1：输出0x54 数据包
# 0x55 包：端口状态
# 0：不输出0x55 数据包
# 1：输出0x55 数据包
# 0x56 包：气压&高度包
# 0：不输出0x56 数据包
# 1：输出0x56 数据包
# 0x57 包：经纬度包
# 0：不输出0x57 数据包
# 1：输出0x57 数据包
# 0x58 包：地速数据包
# 0：不输出0x58 数据包
# 1：输出0x58 数据包
# 0x59 包:四元素输出包
# 0：不输出0x59 数据包
# 1：输出0x59 数据包
# 0x5A:卫星定位精度
# 0：不输出0x5A 数据包
# 1：输出0x5A 数据包

# %% 7.2.11 设置X 轴加速度零偏
# 0xFF 0xAA 0x05 AXOFFSETL AXOFFSETH
# AXOFFSETL：X 轴加速度零偏低字节
# AXOFFSETH：X 轴加速度零偏高字节
# AXOFFSET= (AXOFFSETH <<8) | AXOFFSETL
# 说明：设置加速度零偏以后，加速度的输出值为传感器测量值减去零偏值。
# 7.2.12 设置Y 轴加速度零偏
# 0xFF 0xAA 0x06 AYOFFSETL AYOFFSETH
# AYOFFSETL：Y 轴加速度零偏低字节
# AYOFFSETH：Y 轴加速度零偏高字节
# AYOFFSET= (AYOFFSETH <<8) | AYOFFSETL
# 说明：设置加速度零偏以后，加速度的输出值为传感器测量值减去零偏值。
# 7.2.13 设置Z 轴加速度零偏
# 0xFF 0xAA 0x07 AZOFFSETL AZOFFSETH
# AZOFFSETL：Z 轴加速度零偏低字节
# AZOFFSETH：Z 轴加速度零偏高字节
# AZOFFSET= (AZOFFSETH <<8) | AZOFFSETL
# 说明：设置加速度零偏以后，加速度的输出值为传感器测量值减去零偏值。

# %% 7.2.14 设置X 轴角速度零偏
# 0xFF 0xAA 0x08 GXOFFSETL GXOFFSETH
# GXOFFSETL：X 轴角速度零偏低字节
# GXOFFSETH：X 轴角速度零偏高字节
# GXOFFSET= (GXOFFSETH <<8) | GXOFFSETL
# 说明：设置角速度零偏以后，角速度的输出值为传感器测量值减去零偏值。
# 7.2.15 设置Y 轴角速度零偏
# 0xFF 0xAA 0x09 GYOFFSETL GYOFFSETH
# GYOFFSETL：Y 轴角速度零偏低字节
# GYOFFSETH：Y 轴角速度零偏高字节
# GYOFFSET= (GYOFFSETH <<8) | GYOFFSETL
# 说明：设置角速度零偏以后，角速度的输出值为传感器测量值减去零偏值。
# 7.2.16 设置Z 轴角速度零偏
# 0xFF 0xAA 0x0A GXOFFSETL GXOFFSETH
# GZOFFSETL：Z 轴角速度零偏低字节
# GZOFFSETH：Z 轴角速度零偏高字节
# GZOFFSET= (GZOFFSETH <<8) | GZOFFSETL
# 说明：设置角速度零偏以后，角速度的输出值为传感器测量值减去零偏值。

# %% 7.2.17 设置X 轴磁场零偏
# 0xFF 0xAA 0x0b HXOFFSETL HXOFFSETH
# HXOFFSETL：X 轴磁场零偏低字节
# HXOFFSETH：X 轴磁场零偏高字节
# HXOFFSET= (HXOFFSETH <<8) | HXOFFSETL
# 说明：设置磁场零偏以后，磁场的输出值为传感器测量值减去零偏值。
# 7.2.18 设置Y 轴磁场零偏
# 0xFF 0xAA 0x0c HXOFFSETL HXOFFSETH
# HXOFFSETL：X 轴磁场零偏低字节
# HXOFFSETH：X 轴磁场零偏高字节
# HXOFFSET= (HXOFFSETH <<8) | HXOFFSETL
# 说明：设置磁场零偏以后，磁场的输出值为传感器测量值减去零偏值。
# 7.2.19 设置Z 轴磁场零偏
# 0xFF 0xAA 0x0d HXOFFSETL HXOFFSETH
# HXOFFSETL：Z 轴磁场零偏低字节
# HXOFFSETH：Z 轴磁场零偏高字节
# HXOFFSET= (HXOFFSETH <<8) | HXOFFSETL
# 说明：设置磁场零偏以后，磁场的输出值为传感器测量值减去零偏值。

# %% 7.2.20 设置端口D0 模式
# 0xFF 0xAA 0x0e D0MODE 0x00
# D0MODE：D0 端口模式
# 0x00：模拟输入（默认）
# 0x01：数字输入
# 0x02：输出数字高电平
# 0x03：输出数字低电平
# 0x04：输出PWM
# 7.2.21 设置端口D1 模式
# 0xFF 0xAA 0x0f D1MODE 0x00
# D1MODE：D1 端口模式
# 0x00：模拟输入（默认）
# 0x01：数字输入
# 0x02：输出数字高电平
# 0x03：输出数字低电平
# 0x04：输出PWM
# 0x05：CLR 相对姿态
# 7.2.22 设置端口D2 模式
# 0xFF 0xAA 0x10 D2MODE 0x00
# D2MODE：D2 端口模式
# 0x00：模拟输入（默认）
# 0x01：数字输入
# 0x02：输出数字高电平
# 0x03：输出数字低电平
# 0x04：输出PWM
# 7.2.23 设置端口D3 模式
# 0xFF 0xAA 0x11 D3MODE 0x00
# D3MODE：D3 端口模式
# 0x00：模拟输入（默认）
# 0x01：数字输入
# 0x02：输出数字高电平
# 0x03：输出数字低电平
# 0x04：输出PWM

# %% 7.2.24 设置端口D0 的PWM 高电平宽度
# 0xFF 0xAA 0x12 D0PWMHL D0PWMHH
# D0PWMHL：D0 端口的高电平宽度低字节
# D0PWMHH：D0 端口的高电平宽度高字节
# D0PWMH = (D0PWMHH<<8) | D0PWMHL
# 说明：PWM 的高电平宽度和周期都以us 为单位，例如高电平宽度1500us，只需要将
# D0PWMH 设置为1500。
# 7.2.25 设置端口D1 的PWM 高电平宽度
# 0xFF 0xAA 0x13 D1PWMHL D1PWMHH
# D1PWMHL：D1 端口的高电平宽度低字节
# D1PWMHH：D1 端口的高电平宽度高字节
# D1PWMH = (D1PWMHH<<8) | D1PWMHL
# 说明：PWM 的高电平宽度和周期都以us 为单位，例如高电平宽度1500us，周期20000us
# 的舵机控制信号，只需要将D1PWMH 设置为1500 即可。
# 7.2.26 设置端口D2 的PWM 高电平宽度
# 0xFF 0xAA 0x14 D2PWMHL D2PWMHH
# D2PWMHL：D2 端口的高电平宽度低字节
# D2PWMHH：D2 端口的高电平宽度高字节
# D2PWMH = (D2PWMHH<<8) | D2PWMHL
# 说明：PWM 的高电平宽度和周期都以us 为单位，例如高电平宽度1500us，周期20000us
# 的舵机控制信号，只需要将D2PWMH 设置为1500 即可。
# 7.2.27 设置端口D3 的PWM 高电平宽度
# 0xFF 0xAA 0x15 D3PWMHL D3PWMHH
# D3PWMHL：D3 端口的高电平宽度低字节
# D3PWMHH：D3 端口的高电平宽度高字节
# D3PWMH = (D3PWMHH<<8) | D3PWMHL
# 说明：PWM 的高电平宽度和周期都以us 为单位，例如高电平宽度1500us，周期20000us
# 的舵机控制信号，只需要将D3PWMH 设置为1500 即可。

# %% 7.2.28 设置端口D0 的PWM 周期
# 0xFF 0xAA 0x16 D0PWMTL D0PWMTH
# D0PWMTL：D0 端口的PWM 信号周期宽度低字节
# D0PWMTH：D0 端口的PWM 信号周期宽度高字节
# D0PWMT = (D0PWMTH<<8) | D0PWMTL
# 说明：PWM 的高电平宽度和周期都以us 为单位，例如高电平宽度1500us，周期20000us
# 的舵机控制信号，只需要将D0PWMH 设置为1500，D0PWMT 设置为20000 即可。
# 7.2.29 设置端口D1 的PWM 周期
# 0xFF 0xAA 0x17 D1PWMTL D1PWMTH
# D1PWMTL：D1 端口的PWM 信号周期宽度低字节
# D1PWMTH：D1 端口的PWM 信号周期宽度高字节
# D1PWMT = (D1PWMTH<<8) | D1PWMTL
# 说明：PWM 的高电平宽度和周期都以us 为单位，例如高电平宽度1500us，周期20000us
# 的舵机控制信号，只需要将D1PWMH 设置为1500，D1PWMT 设置为20000 即可。
# 7.2.30 设置端口D2 的PWM 周期
# 0xFF 0xAA 0x18 D2PWMTL D2PWMTH
# D2PWMTL：D2 端口的PWM 信号周期宽度低字节
# D2PWMTH：D2 端口的PWM 信号周期宽度高字节
# D2PWMT = (D2PWMTH<<8) | D2PWMTL
# 说明：PWM 的高电平宽度和周期都以us 为单位，例如高电平宽度1500us，周期20000us
# 的舵机控制信号，只需要将D2PWMH 设置为1500，D2PWMT 设置为20000 即可。
# 7.2.31 设置端口D3 的PWM 周期
# 0xFF 0xAA 0x19 D3PWMTL D3PWMTH
# D3PWMTL：D3 端口的PWM 信号周期宽度低字节
# D3PWMTH：D3 端口的PWM 信号周期宽度高字节
# D3PWMT = (D3PWMTH<<8) | D3PWMTL
# 说明：PWM 的高电平宽度和周期都以us 为单位，例如高电平宽度1500us，周期20000us
# 的舵机控制信号，只需要将D3PWMH 设置为1500，D3PWMT 设置为20000 即可。

# %% 7.2.32 设置IIC 地址
# 0xFF 0xAA 0x1a IICADDR 0x00
# IICADDR：模块的IIC 地址，默认是0x50。IIC 地址采用7bit 地址，最大不能超过0x7f。
# 设置完成以后需要点保存配置按钮，再给模块重新上电后生效

# %% 7.2.33 设置LED 指示灯
# 0xFF 0xAA 0x1b LEDOFF 0x00
# LEDOFF：关闭LED 指示灯
# 0x01：关闭LED 指示灯
# 0x00：开启LED 指示灯

# %% 7.2.34 设置GPS 通信速率
# 0xFF 0xAA 0x1c GPSBAUD 0x00
# GPSBAUD：GPS 通信速率
# BAUD：时间信息包
# 0x00：2400
# 0x01：4800
# 0x02：9600（默认）
# 0x03：19200
# 0x04：38400
# 0x05：57600
# 0x06：115200
# 0x07：230400
# 0x08：460800
# 0x09：921600
# 设置完成以后需要点保存配置按钮，再给模块重新上电后生效。

# %% 7.2.35 设置模块报警
# 1. X 轴角度最小值设置
# 0xFF 0xAA 0x5A DATEL DATAH
# 比如FF AA 5A E4 F8 设置的是X 轴角度最小值位-10 度。
# 2. X 轴角度最大值设置
# 0xFF 0xAA 0x5B DATEL DATAH
# 比如FF AA 5B 1C 07 设置的是X 轴角度最大值位10 度。
# 071C 转换成是进制为1820，
# 1820*180/32768=9.997。
# 3. Y 轴角度最小值设置
# 0xFF 0xAA 0x5E DATEL DATAH
# 比如FF AA 5E E4 F8 设置的是Y 轴角度最小值位-10 度。
# 4. Y 轴角度最大值设置
# 0xFF 0xAA 0x5F DATEL DATAH
# 比如FF AA 5F 1C 07 设置的是X 轴角度最大值位10 度。
# 5. 确认时间设置
# 0xFF 0xAA 0x68 DATEL DATAH
# 比如FF AA 68 00 00 设置的确认时间是0ms。
# 6. 保持时间设置
# 0xFF 0xAA 0x59 DATEL DATAH
# 比如FF AA 59 64 00 设置的保持时间是100ms。
# 7. 报警电平设置
# 0xFF 0xAA 0x62 DATEL DATAH
# 比如FF AA 62 00 00 设置的报警电平是0。