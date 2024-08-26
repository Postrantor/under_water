;; Auto-generated. Do not edit!


(when (boundp 'copley::cmd2drive_msg)
  (if (not (find-package "COPLEY"))
    (make-package "COPLEY"))
  (shadow 'cmd2drive_msg (find-package "COPLEY")))
(unless (find-package "COPLEY::CMD2DRIVE_MSG")
  (make-package "COPLEY::CMD2DRIVE_MSG"))

(in-package "ROS")
;;//! \htmlinclude cmd2drive_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass copley::cmd2drive_msg
  :super ros::object
  :slots (_header _drive ))

(defmethod copley::cmd2drive_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:drive __drive) (instance copley::motor_msg :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _drive __drive)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:drive
   (&rest __drive)
   (if (keywordp (car __drive))
       (send* _drive __drive)
     (progn
       (if __drive (setq _drive (car __drive)))
       _drive)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; copley/motor_msg _drive
    (send _drive :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; copley/motor_msg _drive
       (send _drive :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; copley/motor_msg _drive
     (send _drive :deserialize buf ptr-) (incf ptr- (send _drive :serialization-length))
   ;;
   self)
  )

(setf (get copley::cmd2drive_msg :md5sum-) "49b69f086ac244e027a573abc129a395")
(setf (get copley::cmd2drive_msg :datatype-) "copley/cmd2drive_msg")
(setf (get copley::cmd2drive_msg :definition-)
      "# -*- coding:utf-8 -*-
# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"

# Header
Header header
# Drive
copley/motor_msg drive
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



(provide :copley/cmd2drive_msg "49b69f086ac244e027a573abc129a395")


