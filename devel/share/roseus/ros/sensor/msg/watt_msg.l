;; Auto-generated. Do not edit!


(when (boundp 'sensor::watt_msg)
  (if (not (find-package "SENSOR"))
    (make-package "SENSOR"))
  (shadow 'watt_msg (find-package "SENSOR")))
(unless (find-package "SENSOR::WATT_MSG")
  (make-package "SENSOR::WATT_MSG"))

(in-package "ROS")
;;//! \htmlinclude watt_msg.msg.html


(defclass sensor::watt_msg
  :super ros::object
  :slots (_voltage _current _resistance _watt ))

(defmethod sensor::watt_msg
  (:init
   (&key
    ((:voltage __voltage) 0.0)
    ((:current __current) 0.0)
    ((:resistance __resistance) 0.0)
    ((:watt __watt) 0.0)
    )
   (send-super :init)
   (setq _voltage (float __voltage))
   (setq _current (float __current))
   (setq _resistance (float __resistance))
   (setq _watt (float __watt))
   self)
  (:voltage
   (&optional __voltage)
   (if __voltage (setq _voltage __voltage)) _voltage)
  (:current
   (&optional __current)
   (if __current (setq _current __current)) _current)
  (:resistance
   (&optional __resistance)
   (if __resistance (setq _resistance __resistance)) _resistance)
  (:watt
   (&optional __watt)
   (if __watt (setq _watt __watt)) _watt)
  (:serialization-length
   ()
   (+
    ;; float32 _voltage
    4
    ;; float32 _current
    4
    ;; float32 _resistance
    4
    ;; float32 _watt
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _voltage
       (sys::poke _voltage (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _current
       (sys::poke _current (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _resistance
       (sys::poke _resistance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _watt
       (sys::poke _watt (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _voltage
     (setq _voltage (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _current
     (setq _current (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _resistance
     (setq _resistance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _watt
     (setq _watt (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get sensor::watt_msg :md5sum-) "136cc9f95f5d86898b1dfcc8b32f4a40")
(setf (get sensor::watt_msg :datatype-) "sensor/watt_msg")
(setf (get sensor::watt_msg :definition-)
      "# 定义一个4维向量用于传输功率的数据
float32 voltage
float32 current
float32 resistance
float32 watt
")



(provide :sensor/watt_msg "136cc9f95f5d86898b1dfcc8b32f4a40")


