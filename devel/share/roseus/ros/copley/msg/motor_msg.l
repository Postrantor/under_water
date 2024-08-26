;; Auto-generated. Do not edit!


(when (boundp 'copley::motor_msg)
  (if (not (find-package "COPLEY"))
    (make-package "COPLEY"))
  (shadow 'motor_msg (find-package "COPLEY")))
(unless (find-package "COPLEY::MOTOR_MSG")
  (make-package "COPLEY::MOTOR_MSG"))

(in-package "ROS")
;;//! \htmlinclude motor_msg.msg.html


(defclass copley::motor_msg
  :super ros::object
  :slots (_motor_l _motor_r ))

(defmethod copley::motor_msg
  (:init
   (&key
    ((:motor_l __motor_l) 0.0)
    ((:motor_r __motor_r) 0.0)
    )
   (send-super :init)
   (setq _motor_l (float __motor_l))
   (setq _motor_r (float __motor_r))
   self)
  (:motor_l
   (&optional __motor_l)
   (if __motor_l (setq _motor_l __motor_l)) _motor_l)
  (:motor_r
   (&optional __motor_r)
   (if __motor_r (setq _motor_r __motor_r)) _motor_r)
  (:serialization-length
   ()
   (+
    ;; float32 _motor_l
    4
    ;; float32 _motor_r
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _motor_l
       (sys::poke _motor_l (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _motor_r
       (sys::poke _motor_r (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _motor_l
     (setq _motor_l (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _motor_r
     (setq _motor_r (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get copley::motor_msg :md5sum-) "a89bd8697ea6757cb756a3e8b2bd3f98")
(setf (get copley::motor_msg :datatype-) "copley/motor_msg")
(setf (get copley::motor_msg :definition-)
      "# -*- coding:utf-8 -*-
# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"

# Control
float32 motor_l
float32 motor_r
")



(provide :copley/motor_msg "a89bd8697ea6757cb756a3e8b2bd3f98")


