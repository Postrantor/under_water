# [20210330]:
1. 更新Joy_2*消息，去除了Header
    原则是，有记录价值的才添加header，对于Joy这类初始的节点产生的上游数据并不需要记录
    ```bash
    cd catkin_ws
    catkin_make -DCATKIN_WHITELIST_PACKAGES='copley'
    ```
2. 添加launch文件
3. 修改参数服务器命名