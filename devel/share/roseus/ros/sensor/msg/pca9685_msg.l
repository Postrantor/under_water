;; Auto-generated. Do not edit!


(when (boundp 'sensor::pca9685_msg)
  (if (not (find-package "SENSOR"))
    (make-package "SENSOR"))
  (shadow 'pca9685_msg (find-package "SENSOR")))
(unless (find-package "SENSOR::PCA9685_MSG")
  (make-package "SENSOR::PCA9685_MSG"))

(in-package "ROS")
;;//! \htmlinclude pca9685_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sensor::pca9685_msg
  :super ros::object
  :slots (_header _temperature _speed ))

(defmethod sensor::pca9685_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:temperature __temperature) 0.0)
    ((:speed __speed) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _temperature (float __temperature))
   (setq _speed (round __speed))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:temperature
   (&optional __temperature)
   (if __temperature (setq _temperature __temperature)) _temperature)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _temperature
    4
    ;; int16 _speed
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _temperature
       (sys::poke _temperature (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int16 _speed
       (write-word _speed s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _temperature
     (setq _temperature (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int16 _speed
     (setq _speed (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get sensor::pca9685_msg :md5sum-) "d041db550ab3844083f2be693a00cbbd")
(setf (get sensor::pca9685_msg :datatype-) "sensor/pca9685_msg")
(setf (get sensor::pca9685_msg :definition-)
      "# defain fan sensor pca9685 message format
# Header
Header header
# ID
# int8 chip_id
# int8 chip_version
# temperature
float32 temperature
# speed
int16 speed
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



(provide :sensor/pca9685_msg "d041db550ab3844083f2be693a00cbbd")


