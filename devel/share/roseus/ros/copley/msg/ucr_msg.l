;; Auto-generated. Do not edit!


(when (boundp 'copley::ucr_msg)
  (if (not (find-package "COPLEY"))
    (make-package "COPLEY"))
  (shadow 'ucr_msg (find-package "COPLEY")))
(unless (find-package "COPLEY::UCR_MSG")
  (make-package "COPLEY::UCR_MSG"))

(in-package "ROS")
;;//! \htmlinclude ucr_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass copley::ucr_msg
  :super ros::object
  :slots (_header _current _velocity _position ))

(defmethod copley::ucr_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:current __current) (instance copley::motors_msg :init))
    ((:velocity __velocity) (instance copley::motors_msg :init))
    ((:position __position) (instance copley::motors_msg :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _current __current)
   (setq _velocity __velocity)
   (setq _position __position)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:current
   (&rest __current)
   (if (keywordp (car __current))
       (send* _current __current)
     (progn
       (if __current (setq _current (car __current)))
       _current)))
  (:velocity
   (&rest __velocity)
   (if (keywordp (car __velocity))
       (send* _velocity __velocity)
     (progn
       (if __velocity (setq _velocity (car __velocity)))
       _velocity)))
  (:position
   (&rest __position)
   (if (keywordp (car __position))
       (send* _position __position)
     (progn
       (if __position (setq _position (car __position)))
       _position)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; copley/motors_msg _current
    (send _current :serialization-length)
    ;; copley/motors_msg _velocity
    (send _velocity :serialization-length)
    ;; copley/motors_msg _position
    (send _position :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; copley/motors_msg _current
       (send _current :serialize s)
     ;; copley/motors_msg _velocity
       (send _velocity :serialize s)
     ;; copley/motors_msg _position
       (send _position :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; copley/motors_msg _current
     (send _current :deserialize buf ptr-) (incf ptr- (send _current :serialization-length))
   ;; copley/motors_msg _velocity
     (send _velocity :deserialize buf ptr-) (incf ptr- (send _velocity :serialization-length))
   ;; copley/motors_msg _position
     (send _position :deserialize buf ptr-) (incf ptr- (send _position :serialization-length))
   ;;
   self)
  )

(setf (get copley::ucr_msg :md5sum-) "697cf9df9ce516a16d261952c472d294")
(setf (get copley::ucr_msg :datatype-) "copley/ucr_msg")
(setf (get copley::ucr_msg :definition-)
      "# -*- coding:utf-8 -*-
# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"

# Header
Header header
# Drive
copley/motors_msg current
copley/motors_msg velocity
copley/motors_msg position

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
MSG: copley/motors_msg
# -*- coding:utf-8 -*-
# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"

copley/motor_msg drive
copley/motor_msg wing
copley/motor_msg sting
================================================================================
MSG: copley/motor_msg
# -*- coding:utf-8 -*-
# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"

# Control
float32 motor_l
float32 motor_r
")



(provide :copley/ucr_msg "697cf9df9ce516a16d261952c472d294")


