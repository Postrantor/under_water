;; Auto-generated. Do not edit!


(when (boundp 'sensor::bme280)
  (if (not (find-package "SENSOR"))
    (make-package "SENSOR"))
  (shadow 'bme280 (find-package "SENSOR")))
(unless (find-package "SENSOR::BME280")
  (make-package "SENSOR::BME280"))

(in-package "ROS")
;;//! \htmlinclude bme280.msg.html


(defclass sensor::bme280
  :super ros::object
  :slots (_chip_id _chip_version _temperature _pressure _humidity ))

(defmethod sensor::bme280
  (:init
   (&key
    ((:chip_id __chip_id) 0)
    ((:chip_version __chip_version) 0)
    ((:temperature __temperature) 0.0)
    ((:pressure __pressure) 0.0)
    ((:humidity __humidity) 0.0)
    )
   (send-super :init)
   (setq _chip_id (round __chip_id))
   (setq _chip_version (round __chip_version))
   (setq _temperature (float __temperature))
   (setq _pressure (float __pressure))
   (setq _humidity (float __humidity))
   self)
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

(setf (get sensor::bme280 :md5sum-) "cf334dd156db771a2125cf250be13097")
(setf (get sensor::bme280 :datatype-) "sensor/bme280")
(setf (get sensor::bme280 :definition-)
      "# defain environment sensor bme280 message format
# ID
int8 chip_id
int8 chip_version
# temperature
float32 temperature
# air pressure
float32 pressure
# humidity
float32 humidity
")



(provide :sensor/bme280 "cf334dd156db771a2125cf250be13097")


