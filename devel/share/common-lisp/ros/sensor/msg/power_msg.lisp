; Auto-generated. Do not edit!


(cl:in-package sensor-msg)


;//! \htmlinclude power_msg.msg.html

(cl:defclass <power_msg> (roslisp-msg-protocol:ros-message)
  ((remaining
    :reader remaining
    :initarg :remaining
    :type cl:float
    :initform 0.0)
   (consumed
    :reader consumed
    :initarg :consumed
    :type cl:fixnum
    :initform 0)
   (capacity
    :reader capacity
    :initarg :capacity
    :type cl:float
    :initform 0.0)
   (percentage
    :reader percentage
    :initarg :percentage
    :type cl:float
    :initform 0.0))
)

(cl:defclass power_msg (<power_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <power_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'power_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor-msg:<power_msg> is deprecated: use sensor-msg:power_msg instead.")))

(cl:ensure-generic-function 'remaining-val :lambda-list '(m))
(cl:defmethod remaining-val ((m <power_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:remaining-val is deprecated.  Use sensor-msg:remaining instead.")
  (remaining m))

(cl:ensure-generic-function 'consumed-val :lambda-list '(m))
(cl:defmethod consumed-val ((m <power_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:consumed-val is deprecated.  Use sensor-msg:consumed instead.")
  (consumed m))

(cl:ensure-generic-function 'capacity-val :lambda-list '(m))
(cl:defmethod capacity-val ((m <power_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:capacity-val is deprecated.  Use sensor-msg:capacity instead.")
  (capacity m))

(cl:ensure-generic-function 'percentage-val :lambda-list '(m))
(cl:defmethod percentage-val ((m <power_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:percentage-val is deprecated.  Use sensor-msg:percentage instead.")
  (percentage m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <power_msg>) ostream)
  "Serializes a message object of type '<power_msg>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'remaining))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'consumed)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'capacity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'percentage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <power_msg>) istream)
  "Deserializes a message object of type '<power_msg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'remaining) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'consumed) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'capacity) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'percentage) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<power_msg>)))
  "Returns string type for a message object of type '<power_msg>"
  "sensor/power_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'power_msg)))
  "Returns string type for a message object of type 'power_msg"
  "sensor/power_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<power_msg>)))
  "Returns md5sum for a message object of type '<power_msg>"
  "6985abf14ffd1aad6747673ddb5719f6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'power_msg)))
  "Returns md5sum for a message object of type 'power_msg"
  "6985abf14ffd1aad6747673ddb5719f6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<power_msg>)))
  "Returns full string definition for message of type '<power_msg>"
  (cl:format cl:nil "# 定义一个4维向量用于传输电量的数据~%float32 remaining~%int16 consumed~%float32 capacity~%float32 percentage~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'power_msg)))
  "Returns full string definition for message of type 'power_msg"
  (cl:format cl:nil "# 定义一个4维向量用于传输电量的数据~%float32 remaining~%int16 consumed~%float32 capacity~%float32 percentage~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <power_msg>))
  (cl:+ 0
     4
     2
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <power_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'power_msg
    (cl:cons ':remaining (remaining msg))
    (cl:cons ':consumed (consumed msg))
    (cl:cons ':capacity (capacity msg))
    (cl:cons ':percentage (percentage msg))
))
