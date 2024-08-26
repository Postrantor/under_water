;; Auto-generated. Do not edit!


(when (boundp 'copley::control_msg)
  (if (not (find-package "COPLEY"))
    (make-package "COPLEY"))
  (shadow 'control_msg (find-package "COPLEY")))
(unless (find-package "COPLEY::CONTROL_MSG")
  (make-package "COPLEY::CONTROL_MSG"))

(in-package "ROS")
;;//! \htmlinclude control_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass copley::control_msg
  :super ros::object
  :slots (_header _motor_0 _motor_1 _motor_2 _motor_3 _motor_4 _motor_5 ))

(defmethod copley::control_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:motor_0 __motor_0) 0.0)
    ((:motor_1 __motor_1) 0.0)
    ((:motor_2 __motor_2) 0.0)
    ((:motor_3 __motor_3) 0.0)
    ((:motor_4 __motor_4) 0.0)
    ((:motor_5 __motor_5) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _motor_0 (float __motor_0))
   (setq _motor_1 (float __motor_1))
   (setq _motor_2 (float __motor_2))
   (setq _motor_3 (float __motor_3))
   (setq _motor_4 (float __motor_4))
   (setq _motor_5 (float __motor_5))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:motor_0
   (&optional __motor_0)
   (if __motor_0 (setq _motor_0 __motor_0)) _motor_0)
  (:motor_1
   (&optional __motor_1)
   (if __motor_1 (setq _motor_1 __motor_1)) _motor_1)
  (:motor_2
   (&optional __motor_2)
   (if __motor_2 (setq _motor_2 __motor_2)) _motor_2)
  (:motor_3
   (&optional __motor_3)
   (if __motor_3 (setq _motor_3 __motor_3)) _motor_3)
  (:motor_4
   (&optional __motor_4)
   (if __motor_4 (setq _motor_4 __motor_4)) _motor_4)
  (:motor_5
   (&optional __motor_5)
   (if __motor_5 (setq _motor_5 __motor_5)) _motor_5)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _motor_0
    4
    ;; float32 _motor_1
    4
    ;; float32 _motor_2
    4
    ;; float32 _motor_3
    4
    ;; float32 _motor_4
    4
    ;; float32 _motor_5
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _motor_0
       (sys::poke _motor_0 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_1
       (sys::poke _motor_1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_2
       (sys::poke _motor_2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_3
       (sys::poke _motor_3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_4
       (sys::poke _motor_4 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_5
       (sys::poke _motor_5 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _motor_0
     (setq _motor_0 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_1
     (setq _motor_1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_2
     (setq _motor_2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_3
     (setq _motor_3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_4
     (setq _motor_4 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_5
     (setq _motor_5 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get copley::control_msg :md5sum-) "a888e664d4832aa9d46846c07b169702")
(setf (get copley::control_msg :datatype-) "copley/control_msg")
(setf (get copley::control_msg :definition-)
      "# -*- coding:utf-8 -*-
# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"
# 这个是用来读取多个电机的控制指令的数据
# 主要是为了方便， 暂时写了六个，不一定都用上，留作扩充，就是个数量问题
# 另外，编号按照node_id来编排

# Header
Header header
# Control
float32 motor_0
float32 motor_1
float32 motor_2
float32 motor_3
float32 motor_4
float32 motor_5
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :copley/control_msg "a888e664d4832aa9d46846c07b169702")


