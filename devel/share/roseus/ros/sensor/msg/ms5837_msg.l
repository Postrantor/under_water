;; Auto-generated. Do not edit!


(when (boundp 'sensor::ms5837_msg)
  (if (not (find-package "SENSOR"))
    (make-package "SENSOR"))
  (shadow 'ms5837_msg (find-package "SENSOR")))
(unless (find-package "SENSOR::MS5837_MSG")
  (make-package "SENSOR::MS5837_MSG"))

(in-package "ROS")
;;//! \htmlinclude ms5837_msg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sensor::ms5837_msg
  :super ros::object
  :slots (_header _psr_mbar _psr_atm _psr_Pa _temp_C _temp_F _temp_K _depth_fresh _depth_salt _altitude ))

(defmethod sensor::ms5837_msg
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:psr_mbar __psr_mbar) 0.0)
    ((:psr_atm __psr_atm) 0.0)
    ((:psr_Pa __psr_Pa) 0.0)
    ((:temp_C __temp_C) 0.0)
    ((:temp_F __temp_F) 0.0)
    ((:temp_K __temp_K) 0.0)
    ((:depth_fresh __depth_fresh) 0.0)
    ((:depth_salt __depth_salt) 0.0)
    ((:altitude __altitude) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _psr_mbar (float __psr_mbar))
   (setq _psr_atm (float __psr_atm))
   (setq _psr_Pa (float __psr_Pa))
   (setq _temp_C (float __temp_C))
   (setq _temp_F (float __temp_F))
   (setq _temp_K (float __temp_K))
   (setq _depth_fresh (float __depth_fresh))
   (setq _depth_salt (float __depth_salt))
   (setq _altitude (float __altitude))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:psr_mbar
   (&optional __psr_mbar)
   (if __psr_mbar (setq _psr_mbar __psr_mbar)) _psr_mbar)
  (:psr_atm
   (&optional __psr_atm)
   (if __psr_atm (setq _psr_atm __psr_atm)) _psr_atm)
  (:psr_Pa
   (&optional __psr_Pa)
   (if __psr_Pa (setq _psr_Pa __psr_Pa)) _psr_Pa)
  (:temp_C
   (&optional __temp_C)
   (if __temp_C (setq _temp_C __temp_C)) _temp_C)
  (:temp_F
   (&optional __temp_F)
   (if __temp_F (setq _temp_F __temp_F)) _temp_F)
  (:temp_K
   (&optional __temp_K)
   (if __temp_K (setq _temp_K __temp_K)) _temp_K)
  (:depth_fresh
   (&optional __depth_fresh)
   (if __depth_fresh (setq _depth_fresh __depth_fresh)) _depth_fresh)
  (:depth_salt
   (&optional __depth_salt)
   (if __depth_salt (setq _depth_salt __depth_salt)) _depth_salt)
  (:altitude
   (&optional __altitude)
   (if __altitude (setq _altitude __altitude)) _altitude)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _psr_mbar
    4
    ;; float32 _psr_atm
    4
    ;; float32 _psr_Pa
    4
    ;; float32 _temp_C
    4
    ;; float32 _temp_F
    4
    ;; float32 _temp_K
    4
    ;; float32 _depth_fresh
    4
    ;; float32 _depth_salt
    4
    ;; float32 _altitude
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _psr_mbar
       (sys::poke _psr_mbar (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _psr_atm
       (sys::poke _psr_atm (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _psr_Pa
       (sys::poke _psr_Pa (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _temp_C
       (sys::poke _temp_C (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _temp_F
       (sys::poke _temp_F (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _temp_K
       (sys::poke _temp_K (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _depth_fresh
       (sys::poke _depth_fresh (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _depth_salt
       (sys::poke _depth_salt (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _altitude
       (sys::poke _altitude (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _psr_mbar
     (setq _psr_mbar (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _psr_atm
     (setq _psr_atm (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _psr_Pa
     (setq _psr_Pa (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _temp_C
     (setq _temp_C (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _temp_F
     (setq _temp_F (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _temp_K
     (setq _temp_K (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _depth_fresh
     (setq _depth_fresh (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _depth_salt
     (setq _depth_salt (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _altitude
     (setq _altitude (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get sensor::ms5837_msg :md5sum-) "2465bb52020c0c434b014d6184497bf3")
(setf (get sensor::ms5837_msg :datatype-) "sensor/ms5837_msg")
(setf (get sensor::ms5837_msg :definition-)
      "# define deep sensor MS5837_30B message format
# Header
Header header
# Pressure
float32 psr_mbar
float32 psr_atm
float32 psr_Pa
# temperature
float32 temp_C
float32 temp_F
float32 temp_K
# depth
float32 depth_fresh
float32 depth_salt
# altitude
float32 altitude
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



(provide :sensor/ms5837_msg "2465bb52020c0c434b014d6184497bf3")


