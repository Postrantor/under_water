# [20210330]:

1. 更新 Joy_2\*消息，去除了 Header
   原则是，有记录价值的才添加 header，对于 Joy 这类初始的节点产生的上游数据并不需要记录
   ```bash
   cd catkin_ws
   catkin_make -DCATKIN_WHITELIST_PACKAGES='copley'
   ```
2. 添加 launch 文件
3. 修改参数服务器命名
