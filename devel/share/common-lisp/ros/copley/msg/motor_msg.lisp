; Auto-generated. Do not edit!


(cl:in-package copley-msg)


;//! \htmlinclude motor_msg.msg.html

(cl:defclass <motor_msg> (roslisp-msg-protocol:ros-message)
  ((motor_l
    :reader motor_l
    :initarg :motor_l
    :type cl:float
    :initform 0.0)
   (motor_r
    :reader motor_r
    :initarg :motor_r
    :type cl:float
    :initform 0.0))
)

(cl:defclass motor_msg (<motor_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <motor_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'motor_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name copley-msg:<motor_msg> is deprecated: use copley-msg:motor_msg instead.")))

(cl:ensure-generic-function 'motor_l-val :lambda-list '(m))
(cl:defmethod motor_l-val ((m <motor_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_l-val is deprecated.  Use copley-msg:motor_l instead.")
  (motor_l m))

(cl:ensure-generic-function 'motor_r-val :lambda-list '(m))
(cl:defmethod motor_r-val ((m <motor_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_r-val is deprecated.  Use copley-msg:motor_r instead.")
  (motor_r m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <motor_msg>) ostream)
  "Serializes a message object of type '<motor_msg>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_l))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_r))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <motor_msg>) istream)
  "Deserializes a message object of type '<motor_msg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_l) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_r) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<motor_msg>)))
  "Returns string type for a message object of type '<motor_msg>"
  "copley/motor_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'motor_msg)))
  "Returns string type for a message object of type 'motor_msg"
  "copley/motor_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<motor_msg>)))
  "Returns md5sum for a message object of type '<motor_msg>"
  "a89bd8697ea6757cb756a3e8b2bd3f98")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'motor_msg)))
  "Returns md5sum for a message object of type 'motor_msg"
  "a89bd8697ea6757cb756a3e8b2bd3f98")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<motor_msg>)))
  "Returns full string definition for message of type '<motor_msg>"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Control~%float32 motor_l~%float32 motor_r~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'motor_msg)))
  "Returns full string definition for message of type 'motor_msg"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Control~%float32 motor_l~%float32 motor_r~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <motor_msg>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <motor_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'motor_msg
    (cl:cons ':motor_l (motor_l msg))
    (cl:cons ':motor_r (motor_r msg))
))
