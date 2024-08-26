;; Auto-generated. Do not edit!


(when (boundp 'sensor::bme280_msg)
  (if (not (find-package "SENSOR"))
    (make-package "SENSOR"))
  (shadow 'bme280_msg (find-package "SENSOR")))
(unless (find-package "SENSOR::BME280_MSG")
  (make-package "SENSOR::BME280_MSG"))

(in-package "ROS")
;;//! \htmlinclude bme280_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sensor::bme280_msg
  :super ros::object
  :slots (_header _chip_id _chip_version _temperature _pressure _humidity ))

(defmethod sensor::bme280_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:chip_id __chip_id) 0)
    ((:chip_version __chip_version) 0)
    ((:temperature __temperature) 0.0)
    ((:pressure __pressure) 0.0)
    ((:humidity __humidity) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _chip_id (round __chip_id))
   (setq _chip_version (round __chip_version))
   (setq _temperature (float __temperature))
   (setq _pressure (float __pressure))
   (setq _humidity (float __humidity))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:chip_id
   (&optional __chip_id)
   (if __chip_id (setq _chip_id __chip_id)) _chip_id)
  (:chip_version
   (&optional __chip_version)
   (if __chip_version (setq _chip_version __chip_version)) _chip_version)
  (:temperature
   (&optional __temperature)
   (if __temperature (setq _temperature __temperature)) _temperature)
  (:pressure
   (&optional __pressure)
   (if __pressure (setq _pressure __pressure)) _pressure)
  (:humidity
   (&optional __humidity)
   (if __humidity (setq _humidity __humidity)) _humidity)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int8 _chip_id
    1
    ;; int8 _chip_version
    1
    ;; float32 _temperature
    4
    ;; float32 _pressure
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
     ;; int8 _chip_id
       (write-byte _chip_id s)
     ;; int8 _chip_version
       (write-byte _chip_version s)
     ;; float32 _temperature
       (sys::poke _temperature (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pressure
       (sys::poke _pressure (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _humidity
       (sys::poke _humidity (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int8 _chip_id
     (setq _chip_id (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _chip_id 127) (setq _chip_id (- _chip_id 256)))
   ;; int8 _chip_version
     (setq _chip_version (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _chip_version 127) (setq _chip_version (- _chip_version 256)))
   ;; float32 _temperature
     (setq _temperature (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pressure
     (setq _pressure (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _humidity
     (setq _humidity (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get sensor::bme280_msg :md5sum-) "84b020ec127ee4e3c9286c9437c22c11")
(setf (get sensor::bme280_msg :datatype-) "sensor/bme280_msg")
(setf (get sensor::bme280_msg :definition-)
      "# defain environment sensor bme280 message format
# Header
Header header
# ID
int8 chip_id
int8 chip_version
# temperature
float32 temperature
# air pressure
float32 pressure
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



(provide :sensor/bme280_msg "84b020ec127ee4e3c9286c9437c22c11")


