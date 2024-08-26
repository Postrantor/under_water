;; Auto-generated. Do not edit!


(when (boundp 'copley::cmd2switch_msg)
  (if (not (find-package "COPLEY"))
    (make-package "COPLEY"))
  (shadow 'cmd2switch_msg (find-package "COPLEY")))
(unless (find-package "COPLEY::CMD2SWITCH_MSG")
  (make-package "COPLEY::CMD2SWITCH_MSG"))

(in-package "ROS")
;;//! \htmlinclude cmd2switch_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass copley::cmd2switch_msg
  :super ros::object
  :slots (_header _adjust_left _adjust_right _enc_wing _enc_sting _wing _sting ))

(defmethod copley::cmd2switch_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:adjust_left __adjust_left) 0)
    ((:adjust_right __adjust_right) 0)
    ((:enc_wing __enc_wing) nil)
    ((:enc_sting __enc_sting) nil)
    ((:wing __wing) (instance copley::motor_msg :init))
    ((:sting __sting) (instance copley::motor_msg :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _adjust_left (round __adjust_left))
   (setq _adjust_right (round __adjust_right))
   (setq _enc_wing __enc_wing)
   (setq _enc_sting __enc_sting)
   (setq _wing __wing)
   (setq _sting __sting)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:adjust_left
   (&optional __adjust_left)
   (if __adjust_left (setq _adjust_left __adjust_left)) _adjust_left)
  (:adjust_right
   (&optional __adjust_right)
   (if __adjust_right (setq _adjust_right __adjust_right)) _adjust_right)
  (:enc_wing
   (&optional __enc_wing)
   (if __enc_wing (setq _enc_wing __enc_wing)) _enc_wing)
  (:enc_sting
   (&optional __enc_sting)
   (if __enc_sting (setq _enc_sting __enc_sting)) _enc_sting)
  (:wing
   (&rest __wing)
   (if (keywordp (car __wing))
       (send* _wing __wing)
     (progn
       (if __wing (setq _wing (car __wing)))
       _wing)))
  (:sting
   (&rest __sting)
   (if (keywordp (car __sting))
       (send* _sting __sting)
     (progn
       (if __sting (setq _sting (car __sting)))
       _sting)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int8 _adjust_left
    1
    ;; int8 _adjust_right
    1
    ;; bool _enc_wing
    1
    ;; bool _enc_sting
    1
    ;; copley/motor_msg _wing
    (send _wing :serialization-length)
    ;; copley/motor_msg _sting
    (send _sting :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int8 _adjust_left
       (write-byte _adjust_left s)
     ;; int8 _adjust_right
       (write-byte _adjust_right s)
     ;; bool _enc_wing
       (if _enc_wing (write-byte -1 s) (write-byte 0 s))
     ;; bool _enc_sting
       (if _enc_sting (write-byte -1 s) (write-byte 0 s))
     ;; copley/motor_msg _wing
       (send _wing :serialize s)
     ;; copley/motor_msg _sting
       (send _sting :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int8 _adjust_left
     (setq _adjust_left (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _adjust_left 127) (setq _adjust_left (- _adjust_left 256)))
   ;; int8 _adjust_right
     (setq _adjust_right (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _adjust_right 127) (setq _adjust_right (- _adjust_right 256)))
   ;; bool _enc_wing
     (setq _enc_wing (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _enc_sting
     (setq _enc_sting (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; copley/motor_msg _wing
     (send _wing :deserialize buf ptr-) (incf ptr- (send _wing :serialization-length))
   ;; copley/motor_msg _sting
     (send _sting :deserialize buf ptr-) (incf ptr- (send _sting :serialization-length))
   ;;
   self)
  )

(setf (get copley::cmd2switch_msg :md5sum-) "19a90ae0a917ebed802b29fa446ac872")
(setf (get copley::cmd2switch_msg :datatype-) "copley/cmd2switch_msg")
(setf (get copley::cmd2switch_msg :definition-)
      "# -*- coding:utf-8 -*-
# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"
# 用于控制钩刺机构和推拉机构的运动
# Header
Header header
# Switch
int8 adjust_left
int8 adjust_right
bool enc_wing
bool enc_sting
copley/motor_msg wing
copley/motor_msg sting
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

================================================================================
MSG: copley/motor_msg
# -*- coding:utf-8 -*-
# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"

# Control
float32 motor_l
float32 motor_r
")



(provide :copley/cmd2switch_msg "19a90ae0a917ebed802b29fa446ac872")


