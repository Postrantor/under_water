;; Auto-generated. Do not edit!


(when (boundp 'sensor::sht30_msg)
  (if (not (find-package "SENSOR"))
    (make-package "SENSOR"))
  (shadow 'sht30_msg (find-package "SENSOR")))
(unless (find-package "SENSOR::SHT30_MSG")
  (make-package "SENSOR::SHT30_MSG"))

(in-package "ROS")
;;//! \htmlinclude sht30_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sensor::sht30_msg
  :super ros::object
  :slots (_header _temperature _humidity ))

(defmethod sensor::sht30_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:temperature __temperature) 0.0)
    ((:humidity __humidity) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _temperature (float __temperature))
   (setq _humidity (float __humidity))
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
  (:humidity
   (&optional __humidity)
   (if __humidity (setq _humidity __humidity)) _humidity)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _temperature
    4
    ;; float32 _humidity
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _temperature
       (sys::poke _temperature (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _humidity
       (sys::poke _humidity (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _temperature
     (setq _temperature (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _humidity
     (setq _humidity (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get sensor::sht30_msg :md5sum-) "894330594d2fa263a3df4bb6c44bb2ed")
(setf (get sensor::sht30_msg :datatype-) "sensor/sht30_msg")
(setf (get sensor::sht30_msg :definition-)
      "# defain environment sensor sht30 message format
# Header
Header header
# temperature
float32 temperature
# humidity
float32 humidity

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



(provide :sensor/sht30_msg "894330594d2fa263a3df4bb6c44bb2ed")


