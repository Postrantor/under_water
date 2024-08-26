; Auto-generated. Do not edit!


(cl:in-package copley-msg)


;//! \htmlinclude cmd2switch_msg.msg.html

(cl:defclass <cmd2switch_msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (adjust_left
    :reader adjust_left
    :initarg :adjust_left
    :type cl:fixnum
    :initform 0)
   (adjust_right
    :reader adjust_right
    :initarg :adjust_right
    :type cl:fixnum
    :initform 0)
   (enc_wing
    :reader enc_wing
    :initarg :enc_wing
    :type cl:boolean
    :initform cl:nil)
   (enc_sting
    :reader enc_sting
    :initarg :enc_sting
    :type cl:boolean
    :initform cl:nil)
   (wing
    :reader wing
    :initarg :wing
    :type copley-msg:motor_msg
    :initform (cl:make-instance 'copley-msg:motor_msg))
   (sting
    :reader sting
    :initarg :sting
    :type copley-msg:motor_msg
    :initform (cl:make-instance 'copley-msg:motor_msg)))
)

(cl:defclass cmd2switch_msg (<cmd2switch_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <cmd2switch_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'cmd2switch_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name copley-msg:<cmd2switch_msg> is deprecated: use copley-msg:cmd2switch_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <cmd2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:header-val is deprecated.  Use copley-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'adjust_left-val :lambda-list '(m))
(cl:defmethod adjust_left-val ((m <cmd2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:adjust_left-val is deprecated.  Use copley-msg:adjust_left instead.")
  (adjust_left m))

(cl:ensure-generic-function 'adjust_right-val :lambda-list '(m))
(cl:defmethod adjust_right-val ((m <cmd2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:adjust_right-val is deprecated.  Use copley-msg:adjust_right instead.")
  (adjust_right m))

(cl:ensure-generic-function 'enc_wing-val :lambda-list '(m))
(cl:defmethod enc_wing-val ((m <cmd2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:enc_wing-val is deprecated.  Use copley-msg:enc_wing instead.")
  (enc_wing m))

(cl:ensure-generic-function 'enc_sting-val :lambda-list '(m))
(cl:defmethod enc_sting-val ((m <cmd2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:enc_sting-val is deprecated.  Use copley-msg:enc_sting instead.")
  (enc_sting m))

(cl:ensure-generic-function 'wing-val :lambda-list '(m))
(cl:defmethod wing-val ((m <cmd2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:wing-val is deprecated.  Use copley-msg:wing instead.")
  (wing m))

(cl:ensure-generic-function 'sting-val :lambda-list '(m))
(cl:defmethod sting-val ((m <cmd2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:sting-val is deprecated.  Use copley-msg:sting instead.")
  (sting m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <cmd2switch_msg>) ostream)
  "Serializes a message object of type '<cmd2switch_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'adjust_left)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'adjust_right)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'enc_wing) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'enc_sting) 1 0)) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'wing) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'sting) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <cmd2switch_msg>) istream)
  "Deserializes a message object of type '<cmd2switch_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'adjust_left) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'adjust_right) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:setf (cl:slot-value msg 'enc_wing) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'enc_sting) (cl:not (cl:zerop (cl:read-byte istream))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'wing) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'sting) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<cmd2switch_msg>)))
  "Returns string type for a message object of type '<cmd2switch_msg>"
  "copley/cmd2switch_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'cmd2switch_msg)))
  "Returns string type for a message object of type 'cmd2switch_msg"
  "copley/cmd2switch_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<cmd2switch_msg>)))
  "Returns md5sum for a message object of type '<cmd2switch_msg>"
  "19a90ae0a917ebed802b29fa446ac872")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'cmd2switch_msg)))
  "Returns md5sum for a message object of type 'cmd2switch_msg"
  "19a90ae0a917ebed802b29fa446ac872")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<cmd2switch_msg>)))
  "Returns full string definition for message of type '<cmd2switch_msg>"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%# 用于控制钩刺机构和推拉机构的运动~%# Header~%Header header~%# Switch~%int8 adjust_left~%int8 adjust_right~%bool enc_wing~%bool enc_sting~%copley/motor_msg wing~%copley/motor_msg sting~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: copley/motor_msg~%# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Control~%float32 motor_l~%float32 motor_r~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'cmd2switch_msg)))
  "Returns full string definition for message of type 'cmd2switch_msg"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%# 用于控制钩刺机构和推拉机构的运动~%# Header~%Header header~%# Switch~%int8 adjust_left~%int8 adjust_right~%bool enc_wing~%bool enc_sting~%copley/motor_msg wing~%copley/motor_msg sting~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: copley/motor_msg~%# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Control~%float32 motor_l~%float32 motor_r~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <cmd2switch_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
     1
     1
     1
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'wing))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'sting))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <cmd2switch_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'cmd2switch_msg
    (cl:cons ':header (header msg))
    (cl:cons ':adjust_left (adjust_left msg))
    (cl:cons ':adjust_right (adjust_right msg))
    (cl:cons ':enc_wing (enc_wing msg))
    (cl:cons ':enc_sting (enc_sting msg))
    (cl:cons ':wing (wing msg))
    (cl:cons ':sting (sting msg))
))
