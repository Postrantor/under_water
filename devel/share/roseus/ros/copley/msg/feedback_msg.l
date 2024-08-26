;; Auto-generated. Do not edit!


(when (boundp 'copley::feedback_msg)
  (if (not (find-package "COPLEY"))
    (make-package "COPLEY"))
  (shadow 'feedback_msg (find-package "COPLEY")))
(unless (find-package "COPLEY::FEEDBACK_MSG")
  (make-package "COPLEY::FEEDBACK_MSG"))

(in-package "ROS")
;;//! \htmlinclude feedback_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass copley::feedback_msg
  :super ros::object
  :slots (_header _motor_drive_left _motor_drive_right _motor_wing_left _motor_wing_right _motor_sting_left _motor_sting_right ))

(defmethod copley::feedback_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:motor_drive_left __motor_drive_left) 0.0)
    ((:motor_drive_right __motor_drive_right) 0.0)
    ((:motor_wing_left __motor_wing_left) 0.0)
    ((:motor_wing_right __motor_wing_right) 0.0)
    ((:motor_sting_left __motor_sting_left) 0.0)
    ((:motor_sting_right __motor_sting_right) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _motor_drive_left (float __motor_drive_left))
   (setq _motor_drive_right (float __motor_drive_right))
   (setq _motor_wing_left (float __motor_wing_left))
   (setq _motor_wing_right (float __motor_wing_right))
   (setq _motor_sting_left (float __motor_sting_left))
   (setq _motor_sting_right (float __motor_sting_right))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:motor_drive_left
   (&optional __motor_drive_left)
   (if __motor_drive_left (setq _motor_drive_left __motor_drive_left)) _motor_drive_left)
  (:motor_drive_right
   (&optional __motor_drive_right)
   (if __motor_drive_right (setq _motor_drive_right __motor_drive_right)) _motor_drive_right)
  (:motor_wing_left
   (&optional __motor_wing_left)
   (if __motor_wing_left (setq _motor_wing_left __motor_wing_left)) _motor_wing_left)
  (:motor_wing_right
   (&optional __motor_wing_right)
   (if __motor_wing_right (setq _motor_wing_right __motor_wing_right)) _motor_wing_right)
  (:motor_sting_left
   (&optional __motor_sting_left)
   (if __motor_sting_left (setq _motor_sting_left __motor_sting_left)) _motor_sting_left)
  (:motor_sting_right
   (&optional __motor_sting_right)
   (if __motor_sting_right (setq _motor_sting_right __motor_sting_right)) _motor_sting_right)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _motor_drive_left
    4
    ;; float32 _motor_drive_right
    4
    ;; float32 _motor_wing_left
    4
    ;; float32 _motor_wing_right
    4
    ;; float32 _motor_sting_left
    4
    ;; float32 _motor_sting_right
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _motor_drive_left
       (sys::poke _motor_drive_left (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_drive_right
       (sys::poke _motor_drive_right (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_wing_left
       (sys::poke _motor_wing_left (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_wing_right
       (sys::poke _motor_wing_right (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_sting_left
       (sys::poke _motor_sting_left (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_sting_right
       (sys::poke _motor_sting_right (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _motor_drive_left
     (setq _motor_drive_left (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_drive_right
     (setq _motor_drive_right (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_wing_left
     (setq _motor_wing_left (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_wing_right
     (setq _motor_wing_right (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_sting_left
     (setq _motor_sting_left (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_sting_right
     (setq _motor_sting_right (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get copley::feedback_msg :md5sum-) "14692d936e10ff6e773f574cec4f6e90")
(setf (get copley::feedback_msg :datatype-) "copley/feedback_msg")
(setf (get copley::feedback_msg :definition-)
      "# -*- coding:utf-8 -*-
# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"
# 这个是用来读取多个电机的数据，可以是控制指令或者编码器，都用这一个就行，只要实例化不同的对象就可以
# 主要是为了方便， 暂时写了六个，不一定都用上，留作扩充，就是个数量问题
# 另外，编号按照node_id来编排

# Header
Header header
# Control
float32 motor_drive_left
float32 motor_drive_right
float32 motor_wing_left
float32 motor_wing_right
float32 motor_sting_left
float32 motor_sting_right
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



(provide :copley/feedback_msg "14692d936e10ff6e773f574cec4f6e90")


