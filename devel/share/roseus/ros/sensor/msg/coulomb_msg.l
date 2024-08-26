;; Auto-generated. Do not edit!


(when (boundp 'sensor::coulomb_msg)
  (if (not (find-package "SENSOR"))
    (make-package "SENSOR"))
  (shadow 'coulomb_msg (find-package "SENSOR")))
(unless (find-package "SENSOR::COULOMB_MSG")
  (make-package "SENSOR::COULOMB_MSG"))

(in-package "ROS")
;;//! \htmlinclude coulomb_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sensor::coulomb_msg
  :super ros::object
  :slots (_header _watt _power ))

(defmethod sensor::coulomb_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:watt __watt) (instance sensor::watt_msg :init))
    ((:power __power) (instance sensor::power_msg :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _watt __watt)
   (setq _power __power)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:watt
   (&rest __watt)
   (if (keywordp (car __watt))
       (send* _watt __watt)
     (progn
       (if __watt (setq _watt (car __watt)))
       _watt)))
  (:power
   (&rest __power)
   (if (keywordp (car __power))
       (send* _power __power)
     (progn
       (if __power (setq _power (car __power)))
       _power)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; sensor/watt_msg _watt
    (send _watt :serialization-length)
    ;; sensor/power_msg _power
    (send _power :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; sensor/watt_msg _watt
       (send _watt :serialize s)
     ;; sensor/power_msg _power
       (send _power :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; sensor/watt_msg _watt
     (send _watt :deserialize buf ptr-) (incf ptr- (send _watt :serialization-length))
   ;; sensor/power_msg _power
     (send _power :deserialize buf ptr-) (incf ptr- (send _power :serialization-length))
   ;;
   self)
  )

(setf (get sensor::coulomb_msg :md5sum-) "c5cd7058055ef3a00c048e9d3583364c")
(setf (get sensor::coulomb_msg :datatype-) "sensor/coulomb_msg")
(setf (get sensor::coulomb_msg :definition-)
      "# define coulomb sensor XLDN_1602 message format
# Header
Header header
# Watt
sensor/watt_msg watt
# Power
sensor/power_msg power
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
MSG: sensor/watt_msg
# 定义一个4维向量用于传输功率的数据
float32 voltage
float32 current
float32 resistance
float32 watt
================================================================================
MSG: sensor/power_msg
# 定义一个4维向量用于传输电量的数据
float32 remaining
int16 consumed
float32 capacity
float32 percentage
")



(provide :sensor/coulomb_msg "c5cd7058055ef3a00c048e9d3583364c")


