; Auto-generated. Do not edit!


(cl:in-package sensor-msg)


;//! \htmlinclude sht30_msg.msg.html

(cl:defclass <sht30_msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (temperature
    :reader temperature
    :initarg :temperature
    :type cl:float
    :initform 0.0)
   (humidity
    :reader humidity
    :initarg :humidity
    :type cl:float
    :initform 0.0))
)

(cl:defclass sht30_msg (<sht30_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <sht30_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'sht30_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor-msg:<sht30_msg> is deprecated: use sensor-msg:sht30_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <sht30_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:header-val is deprecated.  Use sensor-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'temperature-val :lambda-list '(m))
(cl:defmethod temperature-val ((m <sht30_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:temperature-val is deprecated.  Use sensor-msg:temperature instead.")
  (temperature m))

(cl:ensure-generic-function 'humidity-val :lambda-list '(m))
(cl:defmethod humidity-val ((m <sht30_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:humidity-val is deprecated.  Use sensor-msg:humidity instead.")
  (humidity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <sht30_msg>) ostream)
  "Serializes a message object of type '<sht30_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'temperature))))
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <sht30_msg>) istream)
  "Deserializes a message object of type '<sht30_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
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
    (cl:setf (cl:slot-value msg 'humidity) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<sht30_msg>)))
  "Returns string type for a message object of type '<sht30_msg>"
  "sensor/sht30_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sht30_msg)))
  "Returns string type for a message object of type 'sht30_msg"
  "sensor/sht30_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<sht30_msg>)))
  "Returns md5sum for a message object of type '<sht30_msg>"
  "894330594d2fa263a3df4bb6c44bb2ed")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'sht30_msg)))
  "Returns md5sum for a message object of type 'sht30_msg"
  "894330594d2fa263a3df4bb6c44bb2ed")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<sht30_msg>)))
  "Returns full string definition for message of type '<sht30_msg>"
  (cl:format cl:nil "# defain environment sensor sht30 message format~%# Header~%Header header~%# temperature~%float32 temperature~%# humidity~%float32 humidity~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'sht30_msg)))
  "Returns full string definition for message of type 'sht30_msg"
  (cl:format cl:nil "# defain environment sensor sht30 message format~%# Header~%Header header~%# temperature~%float32 temperature~%# humidity~%float32 humidity~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <sht30_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <sht30_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'sht30_msg
    (cl:cons ':header (header msg))
    (cl:cons ':temperature (temperature msg))
    (cl:cons ':humidity (humidity msg))
))
