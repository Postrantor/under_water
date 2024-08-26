;; Auto-generated. Do not edit!


(when (boundp 'copley::joy2start_msg)
  (if (not (find-package "COPLEY"))
    (make-package "COPLEY"))
  (shadow 'joy2start_msg (find-package "COPLEY")))
(unless (find-package "COPLEY::JOY2START_MSG")
  (make-package "COPLEY::JOY2START_MSG"))

(in-package "ROS")
;;//! \htmlinclude joy2start_msg.msg.html


(defclass copley::joy2start_msg
  :super ros::object
  :slots (_rpi_host _copley_motor ))

(defmethod copley::joy2start_msg
  (:init
   (&key
    ((:rpi_host __rpi_host) 0)
    ((:copley_motor __copley_motor) 0)
    )
   (send-super :init)
   (setq _rpi_host (round __rpi_host))
   (setq _copley_motor (round __copley_motor))
   self)
  (:rpi_host
   (&optional __rpi_host)
   (if __rpi_host (setq _rpi_host __rpi_host)) _rpi_host)
  (:copley_motor
   (&optional __copley_motor)
   (if __copley_motor (setq _copley_motor __copley_motor)) _copley_motor)
  (:serialization-length
   ()
   (+
    ;; int16 _rpi_host
    2
    ;; int16 _copley_motor
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _rpi_host
       (write-word _rpi_host s)
     ;; int16 _copley_motor
       (write-word _copley_motor s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _rpi_host
     (setq _rpi_host (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _copley_motor
     (setq _copley_motor (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get copley::joy2start_msg :md5sum-) "b630d1038f374b9c6d69706a70f018ec")
(setf (get copley::joy2start_msg :datatype-) "copley/joy2start_msg")
(setf (get copley::joy2start_msg :definition-)
      "# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"

# Start_Joy
int16 rpi_host
int16 copley_motor # 采用int变量而不是bool，可能再分出第三种情况，如重启
")



(provide :copley/joy2start_msg "b630d1038f374b9c6d69706a70f018ec")


