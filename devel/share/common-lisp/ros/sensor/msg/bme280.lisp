; Auto-generated. Do not edit!


(cl:in-package sensor-msg)


;//! \htmlinclude bme280.msg.html

(cl:defclass <bme280> (roslisp-msg-protocol:ros-message)
  ((chip_id
    :reader chip_id
    :initarg :chip_id
    :type cl:fixnum
    :initform 0)
   (chip_version
    :reader chip_version
    :initarg :chip_version
    :type cl:fixnum
    :initform 0)
   (temperature
    :reader temperature
    :initarg :temperature
    :type cl:float
    :initform 0.0)
   (pressure
    :reader pressure
    :initarg :pressure
    :type cl:float
    :initform 0.0)
   (humidity
    :reader humidity
    :initarg :humidity
    :type cl:float
    :initform 0.0))
)

(cl:defclass bme280 (<bme280>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <bme280>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'bme280)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor-msg:<bme280> is deprecated: use sensor-msg:bme280 instead.")))

(cl:ensure-generic-function 'chip_id-val :lambda-list '(m))
(cl:defmethod chip_id-val ((m <bme280>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:chip_id-val is deprecated.  Use sensor-msg:chip_id instead.")
  (chip_id m))

(cl:ensure-generic-function 'chip_version-val :lambda-list '(m))
(cl:defmethod chip_version-val ((m <bme280>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:chip_version-val is deprecated.  Use sensor-msg:chip_version instead.")
  (chip_version m))

(cl:ensure-generic-function 'temperature-val :lambda-list '(m))
(cl:defmethod temperature-val ((m <bme280>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:temperature-val is deprecated.  Use sensor-msg:temperature instead.")
  (temperature m))

(cl:ensure-generic-function 'pressure-val :lambda-list '(m))
(cl:defmethod pressure-val ((m <bme280>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:pressure-val is deprecated.  Use sensor-msg:pressure instead.")
  (pressure m))

(cl:ensure-generic-function 'humidity-val :lambda-list '(m))
(cl:defmethod humidity-val ((m <bme280>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:humidity-val is deprecated.  Use sensor-msg:humidity instead.")
  (humidity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <bme280>) ostream)
  "Serializes a message object of type '<bme280>"
  (cl:let* ((signed (cl:slot-value msg 'chip_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'chip_version)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'temperature))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pressure))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'humidity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <bme280>) istream)
  "Deserializes a message object of type '<bme280>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'chip_id) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'chip_version) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'temperature) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pressure) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'humidity) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<bme280>)))
  "Returns string type for a message object of type '<bme280>"
  "sensor/bme280")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'bme280)))
  "Returns string type for a message object of type 'bme280"
  "sensor/bme280")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<bme280>)))
  "Returns md5sum for a message object of type '<bme280>"
  "cf334dd156db771a2125cf250be13097")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'bme280)))
  "Returns md5sum for a message object of type 'bme280"
  "cf334dd156db771a2125cf250be13097")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<bme280>)))
  "Returns full string definition for message of type '<bme280>"
  (cl:format cl:nil "# defain environment sensor bme280 message format~%# ID~%int8 chip_id~%int8 chip_version~%# temperature~%float32 temperature~%# air pressure~%float32 pressure~%# humidity~%float32 humidity~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'bme280)))
  "Returns full string definition for message of type 'bme280"
  (cl:format cl:nil "# defain environment sensor bme280 message format~%# ID~%int8 chip_id~%int8 chip_version~%# temperature~%float32 temperature~%# air pressure~%float32 pressure~%# humidity~%float32 humidity~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <bme280>))
  (cl:+ 0
     1
     1
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <bme280>))
  "Converts a ROS message object to a list"
  (cl:list 'bme280
    (cl:cons ':chip_id (chip_id msg))
    (cl:cons ':chip_version (chip_version msg))
    (cl:cons ':temperature (temperature msg))
    (cl:cons ':pressure (pressure msg))
    (cl:cons ':humidity (humidity msg))
))
