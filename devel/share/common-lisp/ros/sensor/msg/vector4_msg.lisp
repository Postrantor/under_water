; Auto-generated. Do not edit!


(cl:in-package sensor-msg)


;//! \htmlinclude vector4_msg.msg.html

(cl:defclass <vector4_msg> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type cl:float
    :initform 0.0)
   (b
    :reader b
    :initarg :b
    :type cl:float
    :initform 0.0)
   (c
    :reader c
    :initarg :c
    :type cl:float
    :initform 0.0)
   (d
    :reader d
    :initarg :d
    :type cl:float
    :initform 0.0))
)

(cl:defclass vector4_msg (<vector4_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <vector4_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'vector4_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor-msg:<vector4_msg> is deprecated: use sensor-msg:vector4_msg instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <vector4_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:a-val is deprecated.  Use sensor-msg:a instead.")
  (a m))

(cl:ensure-generic-function 'b-val :lambda-list '(m))
(cl:defmethod b-val ((m <vector4_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:b-val is deprecated.  Use sensor-msg:b instead.")
  (b m))

(cl:ensure-generic-function 'c-val :lambda-list '(m))
(cl:defmethod c-val ((m <vector4_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:c-val is deprecated.  Use sensor-msg:c instead.")
  (c m))

(cl:ensure-generic-function 'd-val :lambda-list '(m))
(cl:defmethod d-val ((m <vector4_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:d-val is deprecated.  Use sensor-msg:d instead.")
  (d m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <vector4_msg>) ostream)
  "Serializes a message object of type '<vector4_msg>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'a))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'b))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'c))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'd))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <vector4_msg>) istream)
  "Deserializes a message object of type '<vector4_msg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'a) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'b) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'c) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'd) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<vector4_msg>)))
  "Returns string type for a message object of type '<vector4_msg>"
  "sensor/vector4_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'vector4_msg)))
  "Returns string type for a message object of type 'vector4_msg"
  "sensor/vector4_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<vector4_msg>)))
  "Returns md5sum for a message object of type '<vector4_msg>"
  "8d86ed09ecfcaeb2855e47ec69fad1dd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'vector4_msg)))
  "Returns md5sum for a message object of type 'vector4_msg"
  "8d86ed09ecfcaeb2855e47ec69fad1dd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<vector4_msg>)))
  "Returns full string definition for message of type '<vector4_msg>"
  (cl:format cl:nil "# 定义一个思维向量用~%float32 a~%float32 b~%float32 c~%float32 d~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'vector4_msg)))
  "Returns full string definition for message of type 'vector4_msg"
  (cl:format cl:nil "# 定义一个思维向量用~%float32 a~%float32 b~%float32 c~%float32 d~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <vector4_msg>))
  (cl:+ 0
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <vector4_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'vector4_msg
    (cl:cons ':a (a msg))
    (cl:cons ':b (b msg))
    (cl:cons ':c (c msg))
    (cl:cons ':d (d msg))
))
