; Auto-generated. Do not edit!


(cl:in-package sensor-msg)


;//! \htmlinclude watt_msg.msg.html

(cl:defclass <watt_msg> (roslisp-msg-protocol:ros-message)
  ((voltage
    :reader voltage
    :initarg :voltage
    :type cl:float
    :initform 0.0)
   (current
    :reader current
    :initarg :current
    :type cl:float
    :initform 0.0)
   (resistance
    :reader resistance
    :initarg :resistance
    :type cl:float
    :initform 0.0)
   (watt
    :reader watt
    :initarg :watt
    :type cl:float
    :initform 0.0))
)

(cl:defclass watt_msg (<watt_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <watt_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'watt_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor-msg:<watt_msg> is deprecated: use sensor-msg:watt_msg instead.")))

(cl:ensure-generic-function 'voltage-val :lambda-list '(m))
(cl:defmethod voltage-val ((m <watt_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:voltage-val is deprecated.  Use sensor-msg:voltage instead.")
  (voltage m))

(cl:ensure-generic-function 'current-val :lambda-list '(m))
(cl:defmethod current-val ((m <watt_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:current-val is deprecated.  Use sensor-msg:current instead.")
  (current m))

(cl:ensure-generic-function 'resistance-val :lambda-list '(m))
(cl:defmethod resistance-val ((m <watt_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:resistance-val is deprecated.  Use sensor-msg:resistance instead.")
  (resistance m))

(cl:ensure-generic-function 'watt-val :lambda-list '(m))
(cl:defmethod watt-val ((m <watt_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:watt-val is deprecated.  Use sensor-msg:watt instead.")
  (watt m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <watt_msg>) ostream)
  "Serializes a message object of type '<watt_msg>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'voltage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'current))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'resistance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'watt))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <watt_msg>) istream)
  "Deserializes a message object of type '<watt_msg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'voltage) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'current) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'resistance) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'watt) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<watt_msg>)))
  "Returns string type for a message object of type '<watt_msg>"
  "sensor/watt_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'watt_msg)))
  "Returns string type for a message object of type 'watt_msg"
  "sensor/watt_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<watt_msg>)))
  "Returns md5sum for a message object of type '<watt_msg>"
  "136cc9f95f5d86898b1dfcc8b32f4a40")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'watt_msg)))
  "Returns md5sum for a message object of type 'watt_msg"
  "136cc9f95f5d86898b1dfcc8b32f4a40")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<watt_msg>)))
  "Returns full string definition for message of type '<watt_msg>"
  (cl:format cl:nil "# 定义一个4维向量用于传输功率的数据~%float32 voltage~%float32 current~%float32 resistance~%float32 watt~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'watt_msg)))
  "Returns full string definition for message of type 'watt_msg"
  (cl:format cl:nil "# 定义一个4维向量用于传输功率的数据~%float32 voltage~%float32 current~%float32 resistance~%float32 watt~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <watt_msg>))
  (cl:+ 0
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <watt_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'watt_msg
    (cl:cons ':voltage (voltage msg))
    (cl:cons ':current (current msg))
    (cl:cons ':resistance (resistance msg))
    (cl:cons ':watt (watt msg))
))
