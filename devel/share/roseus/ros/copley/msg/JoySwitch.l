;; Auto-generated. Do not edit!


(when (boundp 'copley::JoySwitch)
  (if (not (find-package "COPLEY"))
    (make-package "COPLEY"))
  (shadow 'JoySwitch (find-package "COPLEY")))
(unless (find-package "COPLEY::JOYSWITCH")
  (make-package "COPLEY::JOYSWITCH"))

(in-package "ROS")
;;//! \htmlinclude JoySwitch.msg.html


(defclass copley::JoySwitch
  :super ros::object
  :slots (_wing_l _wing_r _sting_l _sting_r _backhome ))

(defmethod copley::JoySwitch
  (:init
   (&key
    ((:wing_l __wing_l) 0.0)
    ((:wing_r __wing_r) 0.0)
    ((:sting_l __sting_l) 0.0)
    ((:sting_r __sting_r) 0.0)
    ((:backhome __backhome) 0.0)
    )
   (send-super :init)
   (setq _wing_l (float __wing_l))
   (setq _wing_r (float __wing_r))
   (setq _sting_l (float __sting_l))
   (setq _sting_r (float __sting_r))
   (setq _backhome (float __backhome))
   self)
  (:wing_l
   (&optional __wing_l)
   (if __wing_l (setq _wing_l __wing_l)) _wing_l)
  (:wing_r
   (&optional __wing_r)
   (if __wing_r (setq _wing_r __wing_r)) _wing_r)
  (:sting_l
   (&optional __sting_l)
   (if __sting_l (setq _sting_l __sting_l)) _sting_l)
  (:sting_r
   (&optional __sting_r)
   (if __sting_r (setq _sting_r __sting_r)) _sting_r)
  (:backhome
   (&optional __backhome)
   (if __backhome (setq _backhome __backhome)) _backhome)
  (:serialization-length
   ()
   (+
    ;; float32 _wing_l
    4
    ;; float32 _wing_r
    4
    ;; float32 _sting_l
    4
    ;; float32 _sting_r
    4
    ;; float32 _backhome
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _wing_l
       (sys::poke _wing_l (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _wing_r
       (sys::poke _wing_r (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _sting_l
       (sys::poke _sting_l (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _sting_r
       (sys::poke _sting_r (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _backhome
       (sys::poke _backhome (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _wing_l
     (setq _wing_l (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _wing_r
     (setq _wing_r (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _sting_l
     (setq _sting_l (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _sting_r
     (setq _sting_r (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _backhome
     (setq _backhome (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get copley::JoySwitch :md5sum-) "c7e797131241ec68ef8622ca9235a2be")
(setf (get copley::JoySwitch :datatype-) "copley/JoySwitch")
(setf (get copley::JoySwitch :definition-)
      "float32 wing_l
float32 wing_r
float32 sting_l
float32 sting_r
float32 backhome

# 定义PS3手柄上的右侧遥感，包含5个值，分别对应推拉机构的推出、收缩；钩刺机构的推出、收缩；推拉机构与钩刺机构的归位；
# 用于控制钩刺机构和推拉机构的运动
")



(provide :copley/JoySwitch "c7e797131241ec68ef8622ca9235a2be")


