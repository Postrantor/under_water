;; Auto-generated. Do not edit!


(when (boundp 'sensor::power_msg)
  (if (not (find-package "SENSOR"))
    (make-package "SENSOR"))
  (shadow 'power_msg (find-package "SENSOR")))
(unless (find-package "SENSOR::POWER_MSG")
  (make-package "SENSOR::POWER_MSG"))

(in-package "ROS")
;;//! \htmlinclude power_msg.msg.html


(defclass sensor::power_msg
  :super ros::object
  :slots (_remaining _consumed _capacity _percentage ))

(defmethod sensor::power_msg
  (:init
   (&key
    ((:remaining __remaining) 0.0)
    ((:consumed __consumed) 0)
    ((:capacity __capacity) 0.0)
    ((:percentage __percentage) 0.0)
    )
   (send-super :init)
   (setq _remaining (float __remaining))
   (setq _consumed (round __consumed))
   (setq _capacity (float __capacity))
   (setq _percentage (float __percentage))
   self)
  (:remaining
   (&optional __remaining)
   (if __remaining (setq _remaining __remaining)) _remaining)
  (:consumed
   (&optional __consumed)
   (if __consumed (setq _consumed __consumed)) _consumed)
  (:capacity
   (&optional __capacity)
   (if __capacity (setq _capacity __capacity)) _capacity)
  (:percentage
   (&optional __percentage)
   (if __percentage (setq _percentage __percentage)) _percentage)
  (:serialization-length
   ()
   (+
    ;; float32 _remaining
    4
    ;; int16 _consumed
    2
    ;; float32 _capacity
    4
    ;; float32 _percentage
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _remaining
       (sys::poke _remaining (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int16 _consumed
       (write-word _consumed s)
     ;; float32 _capacity
       (sys::poke _capacity (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _percentage
       (sys::poke _percentage (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _remaining
     (setq _remaining (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int16 _consumed
     (setq _consumed (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float32 _capacity
     (setq _capacity (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _percentage
     (setq _percentage (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get sensor::power_msg :md5sum-) "6985abf14ffd1aad6747673ddb5719f6")
(setf (get sensor::power_msg :datatype-) "sensor/power_msg")
(setf (get sensor::power_msg :definition-)
      "# 定义一个4维向量用于传输电量的数据
float32 remaining
int16 consumed
float32 capacity
float32 percentage
")



(provide :sensor/power_msg "6985abf14ffd1aad6747673ddb5719f6")


