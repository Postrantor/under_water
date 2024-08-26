;; Auto-generated. Do not edit!


(when (boundp 'copley::motors_msg)
  (if (not (find-package "COPLEY"))
    (make-package "COPLEY"))
  (shadow 'motors_msg (find-package "COPLEY")))
(unless (find-package "COPLEY::MOTORS_MSG")
  (make-package "COPLEY::MOTORS_MSG"))

(in-package "ROS")
;;//! \htmlinclude motors_msg.msg.html


(defclass copley::motors_msg
  :super ros::object
  :slots (_drive _wing _sting ))

(defmethod copley::motors_msg
  (:init
   (&key
    ((:drive __drive) (instance copley::motor_msg :init))
    ((:wing __wing) (instance copley::motor_msg :init))
    ((:sting __sting) (instance copley::motor_msg :init))
    )
   (send-super :init)
   (setq _drive __drive)
   (setq _wing __wing)
   (setq _sting __sting)
   self)
  (:drive
   (&rest __drive)
   (if (keywordp (car __drive))
       (send* _drive __drive)
     (progn
       (if __drive (setq _drive (car __drive)))
       _drive)))
  (:wing
   (&rest __wing)
   (if (keywordp (car __wing))
       (send* _wing __wing)
     (progn
       (if __wing (setq _wing (car __wing)))
       _wing)))
  (:sting
   (&rest __sting)
   (if (keywordp (car __sting))
       (send* _sting __sting)
     (progn
       (if __sting (setq _sting (car __sting)))
       _sting)))
  (:serialization-length
   ()
   (+
    ;; copley/motor_msg _drive
    (send _drive :serialization-length)
    ;; copley/motor_msg _wing
    (send _wing :serialization-length)
    ;; copley/motor_msg _sting
    (send _sting :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; copley/motor_msg _drive
       (send _drive :serialize s)
     ;; copley/motor_msg _wing
       (send _wing :serialize s)
     ;; copley/motor_msg _sting
       (send _sting :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; copley/motor_msg _drive
     (send _drive :deserialize buf ptr-) (incf ptr- (send _drive :serialization-length))
   ;; copley/motor_msg _wing
     (send _wing :deserialize buf ptr-) (incf ptr- (send _wing :serialization-length))
   ;; copley/motor_msg _sting
     (send _sting :deserialize buf ptr-) (incf ptr- (send _sting :serialization-length))
   ;;
   self)
  )

(setf (get copley::motors_msg :md5sum-) "e82ee222b0e96a1635070adf737cc004")
(setf (get copley::motors_msg :datatype-) "copley/motors_msg")
(setf (get copley::motors_msg :definition-)
      "# -*- coding:utf-8 -*-
# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"

copley/motor_msg drive
copley/motor_msg wing
copley/motor_msg sting
================================================================================
MSG: copley/motor_msg
# -*- coding:utf-8 -*-
# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"

# Control
float32 motor_l
float32 motor_r
")



(provide :copley/motors_msg "e82ee222b0e96a1635070adf737cc004")


