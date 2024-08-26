;; Auto-generated. Do not edit!


(when (boundp 'sensor::ms5837)
  (if (not (find-package "SENSOR"))
    (make-package "SENSOR"))
  (shadow 'ms5837 (find-package "SENSOR")))
(unless (find-package "SENSOR::MS5837")
  (make-package "SENSOR::MS5837"))

(in-package "ROS")
;;//! \htmlinclude ms5837.msg.html


(defclass sensor::ms5837
  :super ros::object
  :slots (_psr_atm _psr_Torr _psr_psi _temp_C _temp_F _temp_K _freshDepth _saltDepth _altitude ))

(defmethod sensor::ms5837
  (:init
   (&key
    ((:psr_atm __psr_atm) 0.0)
    ((:psr_Torr __psr_Torr) 0.0)
    ((:psr_psi __psr_psi) 0.0)
    ((:temp_C __temp_C) 0.0)
    ((:temp_F __temp_F) 0.0)
    ((:temp_K __temp_K) 0.0)
    ((:freshDepth __freshDepth) 0.0)
    ((:saltDepth __saltDepth) 0.0)
    ((:altitude __altitude) 0.0)
    )
   (send-super :init)
   (setq _psr_atm (float __psr_atm))
   (setq _psr_Torr (float __psr_Torr))
   (setq _psr_psi (float __psr_psi))
   (setq _temp_C (float __temp_C))
   (setq _temp_F (float __temp_F))
   (setq _temp_K (float __temp_K))
   (setq _freshDepth (float __freshDepth))
   (setq _saltDepth (float __saltDepth))
   (setq _altitude (float __altitude))
   self)
  (:psr_atm
   (&optional __psr_atm)
   (if __psr_atm (setq _psr_atm __psr_atm)) _psr_atm)
  (:psr_Torr
   (&optional __psr_Torr)
   (if __psr_Torr (setq _psr_Torr __psr_Torr)) _psr_Torr)
  (:psr_psi
   (&optional __psr_psi)
   (if __psr_psi (setq _psr_psi __psr_psi)) _psr_psi)
  (:temp_C
   (&optional __temp_C)
   (if __temp_C (setq _temp_C __temp_C)) _temp_C)
  (:temp_F
   (&optional __temp_F)
   (if __temp_F (setq _temp_F __temp_F)) _temp_F)
  (:temp_K
   (&optional __temp_K)
   (if __temp_K (setq _temp_K __temp_K)) _temp_K)
  (:freshDepth
   (&optional __freshDepth)
   (if __freshDepth (setq _freshDepth __freshDepth)) _freshDepth)
  (:saltDepth
   (&optional __saltDepth)
   (if __saltDepth (setq _saltDepth __saltDepth)) _saltDepth)
  (:altitude
   (&optional __altitude)
   (if __altitude (setq _altitude __altitude)) _altitude)
  (:serialization-length
   ()
   (+
    ;; float32 _psr_atm
    4
    ;; float32 _psr_Torr
    4
    ;; float32 _psr_psi
    4
    ;; float32 _temp_C
    4
    ;; float32 _temp_F
    4
    ;; float32 _temp_K
    4
    ;; float32 _freshDepth
    4
    ;; float32 _saltDepth
    4
    ;; float32 _altitude
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _psr_atm
       (sys::poke _psr_atm (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _psr_Torr
       (sys::poke _psr_Torr (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _psr_psi
       (sys::poke _psr_psi (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _temp_C
       (sys::poke _temp_C (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _temp_F
       (sys::poke _temp_F (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _temp_K
       (sys::poke _temp_K (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _freshDepth
       (sys::poke _freshDepth (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _saltDepth
       (sys::poke _saltDepth (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _altitude
       (sys::poke _altitude (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _psr_atm
     (setq _psr_atm (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _psr_Torr
     (setq _psr_Torr (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _psr_psi
     (setq _psr_psi (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _temp_C
     (setq _temp_C (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _temp_F
     (setq _temp_F (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _temp_K
     (setq _temp_K (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _freshDepth
     (setq _freshDepth (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _saltDepth
     (setq _saltDepth (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _altitude
     (setq _altitude (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get sensor::ms5837 :md5sum-) "b7b0b58529fcdad3a20813b27c552e2d")
(setf (get sensor::ms5837 :datatype-) "sensor/ms5837")
(setf (get sensor::ms5837 :definition-)
      "# define deep sensor MS5837_30B message format
# Pressure
float32 psr_atm
float32 psr_Torr
float32 psr_psi
# temperature
float32 temp_C
float32 temp_F
float32 temp_K
# depth
float32 freshDepth
float32 saltDepth
# altitude
float32 altitude

")



(provide :sensor/ms5837 "b7b0b58529fcdad3a20813b27c552e2d")


