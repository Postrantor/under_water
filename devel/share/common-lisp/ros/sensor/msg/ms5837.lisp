; Auto-generated. Do not edit!


(cl:in-package sensor-msg)


;//! \htmlinclude ms5837.msg.html

(cl:defclass <ms5837> (roslisp-msg-protocol:ros-message)
  ((psr_atm
    :reader psr_atm
    :initarg :psr_atm
    :type cl:float
    :initform 0.0)
   (psr_Torr
    :reader psr_Torr
    :initarg :psr_Torr
    :type cl:float
    :initform 0.0)
   (psr_psi
    :reader psr_psi
    :initarg :psr_psi
    :type cl:float
    :initform 0.0)
   (temp_C
    :reader temp_C
    :initarg :temp_C
    :type cl:float
    :initform 0.0)
   (temp_F
    :reader temp_F
    :initarg :temp_F
    :type cl:float
    :initform 0.0)
   (temp_K
    :reader temp_K
    :initarg :temp_K
    :type cl:float
    :initform 0.0)
   (freshDepth
    :reader freshDepth
    :initarg :freshDepth
    :type cl:float
    :initform 0.0)
   (saltDepth
    :reader saltDepth
    :initarg :saltDepth
    :type cl:float
    :initform 0.0)
   (altitude
    :reader altitude
    :initarg :altitude
    :type cl:float
    :initform 0.0))
)

(cl:defclass ms5837 (<ms5837>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ms5837>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ms5837)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor-msg:<ms5837> is deprecated: use sensor-msg:ms5837 instead.")))

(cl:ensure-generic-function 'psr_atm-val :lambda-list '(m))
(cl:defmethod psr_atm-val ((m <ms5837>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:psr_atm-val is deprecated.  Use sensor-msg:psr_atm instead.")
  (psr_atm m))

(cl:ensure-generic-function 'psr_Torr-val :lambda-list '(m))
(cl:defmethod psr_Torr-val ((m <ms5837>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:psr_Torr-val is deprecated.  Use sensor-msg:psr_Torr instead.")
  (psr_Torr m))

(cl:ensure-generic-function 'psr_psi-val :lambda-list '(m))
(cl:defmethod psr_psi-val ((m <ms5837>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:psr_psi-val is deprecated.  Use sensor-msg:psr_psi instead.")
  (psr_psi m))

(cl:ensure-generic-function 'temp_C-val :lambda-list '(m))
(cl:defmethod temp_C-val ((m <ms5837>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:temp_C-val is deprecated.  Use sensor-msg:temp_C instead.")
  (temp_C m))

(cl:ensure-generic-function 'temp_F-val :lambda-list '(m))
(cl:defmethod temp_F-val ((m <ms5837>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:temp_F-val is deprecated.  Use sensor-msg:temp_F instead.")
  (temp_F m))

(cl:ensure-generic-function 'temp_K-val :lambda-list '(m))
(cl:defmethod temp_K-val ((m <ms5837>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:temp_K-val is deprecated.  Use sensor-msg:temp_K instead.")
  (temp_K m))

(cl:ensure-generic-function 'freshDepth-val :lambda-list '(m))
(cl:defmethod freshDepth-val ((m <ms5837>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:freshDepth-val is deprecated.  Use sensor-msg:freshDepth instead.")
  (freshDepth m))

(cl:ensure-generic-function 'saltDepth-val :lambda-list '(m))
(cl:defmethod saltDepth-val ((m <ms5837>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:saltDepth-val is deprecated.  Use sensor-msg:saltDepth instead.")
  (saltDepth m))

(cl:ensure-generic-function 'altitude-val :lambda-list '(m))
(cl:defmethod altitude-val ((m <ms5837>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:altitude-val is deprecated.  Use sensor-msg:altitude instead.")
  (altitude m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ms5837>) ostream)
  "Serializes a message object of type '<ms5837>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'psr_atm))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'psr_Torr))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'psr_psi))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'temp_C))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'temp_F))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'temp_K))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'freshDepth))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'saltDepth))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'altitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ms5837>) istream)
  "Deserializes a message object of type '<ms5837>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'psr_atm) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'psr_Torr) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'psr_psi) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'temp_C) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'temp_F) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'temp_K) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'freshDepth) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'saltDepth) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'altitude) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ms5837>)))
  "Returns string type for a message object of type '<ms5837>"
  "sensor/ms5837")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ms5837)))
  "Returns string type for a message object of type 'ms5837"
  "sensor/ms5837")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ms5837>)))
  "Returns md5sum for a message object of type '<ms5837>"
  "b7b0b58529fcdad3a20813b27c552e2d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ms5837)))
  "Returns md5sum for a message object of type 'ms5837"
  "b7b0b58529fcdad3a20813b27c552e2d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ms5837>)))
  "Returns full string definition for message of type '<ms5837>"
  (cl:format cl:nil "# define deep sensor MS5837_30B message format~%# Pressure~%float32 psr_atm~%float32 psr_Torr~%float32 psr_psi~%# temperature~%float32 temp_C~%float32 temp_F~%float32 temp_K~%# depth~%float32 freshDepth~%float32 saltDepth~%# altitude~%float32 altitude~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ms5837)))
  "Returns full string definition for message of type 'ms5837"
  (cl:format cl:nil "# define deep sensor MS5837_30B message format~%# Pressure~%float32 psr_atm~%float32 psr_Torr~%float32 psr_psi~%# temperature~%float32 temp_C~%float32 temp_F~%float32 temp_K~%# depth~%float32 freshDepth~%float32 saltDepth~%# altitude~%float32 altitude~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ms5837>))
  (cl:+ 0
     4
     4
     4
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ms5837>))
  "Converts a ROS message object to a list"
  (cl:list 'ms5837
    (cl:cons ':psr_atm (psr_atm msg))
    (cl:cons ':psr_Torr (psr_Torr msg))
    (cl:cons ':psr_psi (psr_psi msg))
    (cl:cons ':temp_C (temp_C msg))
    (cl:cons ':temp_F (temp_F msg))
    (cl:cons ':temp_K (temp_K msg))
    (cl:cons ':freshDepth (freshDepth msg))
    (cl:cons ':saltDepth (saltDepth msg))
    (cl:cons ':altitude (altitude msg))
))
