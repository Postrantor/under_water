#! /usr/bin/env python
# -*- coding:utf-8 -*-
# %%
defaultBaud = 9600 # Defaults to 9,600 on power up or reset.
highBaud = 115200 # 9,600 to 115,200
defaultTimeout = .1 # .1/None
# %%
# UCR: Underwater Climbing Robot，水下攀爬机器人
    # UCR: 主驱动
    # Wing: 侧翼
    # Sting: 刺
PortID_UCR = '/dev/UCR_Drive' # 主驱动
PortID_Wing = '/dev/UCR_Wing' # 钩刺机构
PortID_Sting = '/dev/UCR_Sting' # 推拉机构