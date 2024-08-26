;; Auto-generated. Do not edit!


(when (boundp 'copley::joy2switch_msg)
  (if (not (find-package "COPLEY"))
    (make-package "COPLEY"))
  (shadow 'joy2switch_msg (find-package "COPLEY")))
(unless (find-package "COPLEY::JOY2SWITCH_MSG")
  (make-package "COPLEY::JOY2SWITCH_MSG"))

(in-package "ROS")
;;//! \htmlinclude joy2switch_msg.msg.html


(defclass copley::joy2switch_msg
  :super ros::object
  :slots (_adjust_left _adjust_right _enc_wing _enc_sting _wing_left _wing_right _sting_left _sting_right ))

(defmethod copley::joy2switch_msg
  (:init
   (&key
    ((:adjust_left __adjust_left) 0)
    ((:adjust_right __adjust_right) 0)
    ((:enc_wing __enc_wing) nil)
    ((:enc_sting __enc_sting) nil)
    ((:wing_left __wing_left) 0)
    ((:wing_right __wing_right) 0)
    ((:sting_left __sting_left) 0)
    ((:sting_right __sting_right) 0)
    )
   (send-super :init)
   (setq _adjust_left (round __adjust_left))
   (setq _adjust_right (round __adjust_right))
   (setq _enc_wing __enc_wing)
   (setq _enc_sting __enc_sting)
   (setq _wing_left (round __wing_left))
   (setq _wing_right (round __wing_right))
   (setq _sting_left (round __sting_left))
   (setq _sting_right (round __sting_right))
   self)
  (:adjust_left
   (&optional __adjust_left)
   (if __adjust_left (setq _adjust_left __adjust_left)) _adjust_left)
  (:adjust_right
   (&optional __adjust_right)
   (if __adjust_right (setq _adjust_right __adjust_right)) _adjust_right)
  (:enc_wing
   (&optional __enc_wing)
   (if __enc_wing (setq _enc_wing __enc_wing)) _enc_wing)
  (:enc_sting
   (&optional __enc_sting)
   (if __enc_sting (setq _enc_sting __enc_sting)) _enc_sting)
  (:wing_left
   (&optional __wing_left)
   (if __wing_left (setq _wing_left __wing_left)) _wing_left)
  (:wing_right
   (&optional __wing_right)
   (if __wing_right (setq _wing_right __wing_right)) _wing_right)
  (:sting_left
   (&optional __sting_left)
   (if __sting_left (setq _sting_left __sting_left)) _sting_left)
  (:sting_right
   (&optional __sting_right)
   (if __sting_right (setq _sting_right __sting_right)) _sting_right)
  (:serialization-length
   ()
   (+
    ;; int8 _adjust_left
    1
    ;; int8 _adjust_right
    1
    ;; bool _enc_wing
    1
    ;; bool _enc_sting
    1
    ;; int8 _wing_left
    1
    ;; int8 _wing_right
    1
    ;; int8 _sting_left
    1
    ;; int8 _sting_right
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _adjust_left
       (write-byte _adjust_left s)
     ;; int8 _adjust_right
       (write-byte _adjust_right s)
     ;; bool _enc_wing
       (if _enc_wing (write-byte -1 s) (write-byte 0 s))
     ;; bool _enc_sting
       (if _enc_sting (write-byte -1 s) (write-byte 0 s))
     ;; int8 _wing_left
       (write-byte _wing_left s)
     ;; int8 _wing_right
       (write-byte _wing_right s)
     ;; int8 _sting_left
       (write-byte _sting_left s)
     ;; int8 _sting_right
       (write-byte _sting_right s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _adjust_left
     (setq _adjust_left (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _adjust_left 127) (setq _adjust_left (- _adjust_left 256)))
   ;; int8 _adjust_right
     (setq _adjust_right (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _adjust_right 127) (setq _adjust_right (- _adjust_right 256)))
   ;; bool _enc_wing
     (setq _enc_wing (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _enc_sting
     (setq _enc_sting (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int8 _wing_left
     (setq _wing_left (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _wing_left 127) (setq _wing_left (- _wing_left 256)))
   ;; int8 _wing_right
     (setq _wing_right (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _wing_right 127) (setq _wing_right (- _wing_right 256)))
   ;; int8 _sting_left
     (setq _sting_left (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _sting_left 127) (setq _sting_left (- _sting_left 256)))
   ;; int8 _sting_right
     (setq _sting_right (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _sting_right 127) (setq _sting_right (- _sting_right 256)))
   ;;
   self)
  )

(setf (get copley::joy2switch_msg :md5sum-) "90b5ad54d03689fd411144777332d6f9")
(setf (get copley::joy2switch_msg :datatype-) "copley/joy2switch_msg")
(setf (get copley::joy2switch_msg :definition-)
      "# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"
# [issue]:
# 这个可以和cmd的合并在一起
# 考虑自定义twist

# Joy
int8 adjust_left
int8 adjust_right
bool enc_wing
bool enc_sting

int8 wing_left
int8 wing_right
int8 sting_left
int8 sting_right
")



(provide :copley/joy2switch_msg "90b5ad54d03689fd411144777332d6f9")


