; Auto-generated. Do not edit!


(cl:in-package sensor-msg)


;//! \htmlinclude ms5837_msg.msg.html

(cl:defclass <ms5837_msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (psr_mbar
    :reader psr_mbar
    :initarg :psr_mbar
    :type cl:float
    :initform 0.0)
   (psr_atm
    :reader psr_atm
    :initarg :psr_atm
    :type cl:float
    :initform 0.0)
   (psr_Pa
    :reader psr_Pa
    :initarg :psr_Pa
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
   (depth_fresh
    :reader depth_fresh
    :initarg :depth_fresh
    :type cl:float
    :initform 0.0)
   (depth_salt
    :reader depth_salt
    :initarg :depth_salt
    :type cl:float
    :initform 0.0)
   (altitude
    :reader altitude
    :initarg :altitude
    :type cl:float
    :initform 0.0))
)

(cl:defclass ms5837_msg (<ms5837_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ms5837_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ms5837_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor-msg:<ms5837_msg> is deprecated: use sensor-msg:ms5837_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ms5837_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:header-val is deprecated.  Use sensor-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'psr_mbar-val :lambda-list '(m))
(cl:defmethod psr_mbar-val ((m <ms5837_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:psr_mbar-val is deprecated.  Use sensor-msg:psr_mbar instead.")
  (psr_mbar m))

(cl:ensure-generic-function 'psr_atm-val :lambda-list '(m))
(cl:defmethod psr_atm-val ((m <ms5837_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:psr_atm-val is deprecated.  Use sensor-msg:psr_atm instead.")
  (psr_atm m))

(cl:ensure-generic-function 'psr_Pa-val :lambda-list '(m))
(cl:defmethod psr_Pa-val ((m <ms5837_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:psr_Pa-val is deprecated.  Use sensor-msg:psr_Pa instead.")
  (psr_Pa m))

(cl:ensure-generic-function 'temp_C-val :lambda-list '(m))
(cl:defmethod temp_C-val ((m <ms5837_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:temp_C-val is deprecated.  Use sensor-msg:temp_C instead.")
  (temp_C m))

(cl:ensure-generic-function 'temp_F-val :lambda-list '(m))
(cl:defmethod temp_F-val ((m <ms5837_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:temp_F-val is deprecated.  Use sensor-msg:temp_F instead.")
  (temp_F m))

(cl:ensure-generic-function 'temp_K-val :lambda-list '(m))
(cl:defmethod temp_K-val ((m <ms5837_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:temp_K-val is deprecated.  Use sensor-msg:temp_K instead.")
  (temp_K m))

(cl:ensure-generic-function 'depth_fresh-val :lambda-list '(m))
(cl:defmethod depth_fresh-val ((m <ms5837_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:depth_fresh-val is deprecated.  Use sensor-msg:depth_fresh instead.")
  (depth_fresh m))

(cl:ensure-generic-function 'depth_salt-val :lambda-list '(m))
(cl:defmethod depth_salt-val ((m <ms5837_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:depth_salt-val is deprecated.  Use sensor-msg:depth_salt instead.")
  (depth_salt m))

(cl:ensure-generic-function 'altitude-val :lambda-list '(m))
(cl:defmethod altitude-val ((m <ms5837_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:altitude-val is deprecated.  Use sensor-msg:altitude instead.")
  (altitude m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ms5837_msg>) ostream)
  "Serializes a message object of type '<ms5837_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'psr_mbar))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'psr_atm))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'psr_Pa))))
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
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'depth_fresh))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'depth_salt))))
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ms5837_msg>) istream)
  "Deserializes a message object of type '<ms5837_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'psr_mbar) (roslisp-utils:decode-single-float-bits bits)))
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
    (cl:setf (cl:slot-value msg 'psr_Pa) (roslisp-utils:decode-single-float-bits bits)))
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
    (cl:setf (cl:slot-value msg 'depth_fresh) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'depth_salt) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'altitude) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ms5837_msg>)))
  "Returns string type for a message object of type '<ms5837_msg>"
  "sensor/ms5837_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ms5837_msg)))
  "Returns string type for a message object of type 'ms5837_msg"
  "sensor/ms5837_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ms5837_msg>)))
  "Returns md5sum for a message object of type '<ms5837_msg>"
  "2465bb52020c0c434b014d6184497bf3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ms5837_msg)))
  "Returns md5sum for a message object of type 'ms5837_msg"
  "2465bb52020c0c434b014d6184497bf3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ms5837_msg>)))
  "Returns full string definition for message of type '<ms5837_msg>"
  (cl:format cl:nil "# define deep sensor MS5837_30B message format~%# Header~%Header header~%# Pressure~%float32 psr_mbar~%float32 psr_atm~%float32 psr_Pa~%# temperature~%float32 temp_C~%float32 temp_F~%float32 temp_K~%# depth~%float32 depth_fresh~%float32 depth_salt~%# altitude~%float32 altitude~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ms5837_msg)))
  "Returns full string definition for message of type 'ms5837_msg"
  (cl:format cl:nil "# define deep sensor MS5837_30B message format~%# Header~%Header header~%# Pressure~%float32 psr_mbar~%float32 psr_atm~%float32 psr_Pa~%# temperature~%float32 temp_C~%float32 temp_F~%float32 temp_K~%# depth~%float32 depth_fresh~%float32 depth_salt~%# altitude~%float32 altitude~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ms5837_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
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
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ms5837_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'ms5837_msg
    (cl:cons ':header (header msg))
    (cl:cons ':psr_mbar (psr_mbar msg))
    (cl:cons ':psr_atm (psr_atm msg))
    (cl:cons ':psr_Pa (psr_Pa msg))
    (cl:cons ':temp_C (temp_C msg))
    (cl:cons ':temp_F (temp_F msg))
    (cl:cons ':temp_K (temp_K msg))
    (cl:cons ':depth_fresh (depth_fresh msg))
    (cl:cons ':depth_salt (depth_salt msg))
    (cl:cons ':altitude (altitude msg))
))
