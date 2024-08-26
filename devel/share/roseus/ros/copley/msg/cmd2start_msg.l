;; Auto-generated. Do not edit!


(when (boundp 'copley::cmd2start_msg)
  (if (not (find-package "COPLEY"))
    (make-package "COPLEY"))
  (shadow 'cmd2start_msg (find-package "COPLEY")))
(unless (find-package "COPLEY::CMD2START_MSG")
  (make-package "COPLEY::CMD2START_MSG"))

(in-package "ROS")
;;//! \htmlinclude cmd2start_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass copley::cmd2start_msg
  :super ros::object
  :slots (_header _rpi_host _copley_motor ))

(defmethod copley::cmd2start_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:rpi_host __rpi_host) 0)
    ((:copley_motor __copley_motor) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _rpi_host (round __rpi_host))
   (setq _copley_motor (round __copley_motor))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:rpi_host
   (&optional __rpi_host)
   (if __rpi_host (setq _rpi_host __rpi_host)) _rpi_host)
  (:copley_motor
   (&optional __copley_motor)
   (if __copley_motor (setq _copley_motor __copley_motor)) _copley_motor)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int16 _rpi_host
    2
    ;; int16 _copley_motor
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int16 _rpi_host
       (write-word _rpi_host s)
     ;; int16 _copley_motor
       (write-word _copley_motor s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int16 _rpi_host
     (setq _rpi_host (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _copley_motor
     (setq _copley_motor (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get copley::cmd2start_msg :md5sum-) "111b1a1fda8851b8a4f1107ff12e3c61")
(setf (get copley::cmd2start_msg :datatype-) "copley/cmd2start_msg")
(setf (get copley::cmd2start_msg :definition-)
      "# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"

# Header
Header header
# Start_Joy
int16 rpi_host
int16 copley_motor # 采用int变量而不是bool，可能再分出第三种情况，如重启
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



(provide :copley/cmd2start_msg "111b1a1fda8851b8a4f1107ff12e3c61")


