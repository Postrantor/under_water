;; Auto-generated. Do not edit!


(when (boundp 'sensor::vector4_msg)
  (if (not (find-package "SENSOR"))
    (make-package "SENSOR"))
  (shadow 'vector4_msg (find-package "SENSOR")))
(unless (find-package "SENSOR::VECTOR4_MSG")
  (make-package "SENSOR::VECTOR4_MSG"))

(in-package "ROS")
;;//! \htmlinclude vector4_msg.msg.html


(defclass sensor::vector4_msg
  :super ros::object
  :slots (_a _b _c _d ))

(defmethod sensor::vector4_msg
  (:init
   (&key
    ((:a __a) 0.0)
    ((:b __b) 0.0)
    ((:c __c) 0.0)
    ((:d __d) 0.0)
    )
   (send-super :init)
   (setq _a (float __a))
   (setq _b (float __b))
   (setq _c (float __c))
   (setq _d (float __d))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:b
   (&optional __b)
   (if __b (setq _b __b)) _b)
  (:c
   (&optional __c)
   (if __c (setq _c __c)) _c)
  (:d
   (&optional __d)
   (if __d (setq _d __d)) _d)
  (:serialization-length
   ()
   (+
    ;; float32 _a
    4
    ;; float32 _b
    4
    ;; float32 _c
    4
    ;; float32 _d
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _a
       (sys::poke _a (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _b
       (sys::poke _b (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _c
       (sys::poke _c (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _d
       (sys::poke _d (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _a
     (setq _a (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _b
     (setq _b (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _c
     (setq _c (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _d
     (setq _d (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get sensor::vector4_msg :md5sum-) "8d86ed09ecfcaeb2855e47ec69fad1dd")
(setf (get sensor::vector4_msg :datatype-) "sensor/vector4_msg")
(setf (get sensor::vector4_msg :definition-)
      "# 定义一个思维向量用
float32 a
float32 b
float32 c
float32 d
")



(provide :sensor/vector4_msg "8d86ed09ecfcaeb2855e47ec69fad1dd")


