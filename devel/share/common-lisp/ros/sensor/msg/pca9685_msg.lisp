; Auto-generated. Do not edit!


(cl:in-package sensor-msg)


;//! \htmlinclude pca9685_msg.msg.html

(cl:defclass <pca9685_msg> (roslisp-msg-protocol:ros-message)
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
   (speed
    :reader speed
    :initarg :speed
    :type cl:fixnum
    :initform 0))
)

(cl:defclass pca9685_msg (<pca9685_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pca9685_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pca9685_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor-msg:<pca9685_msg> is deprecated: use sensor-msg:pca9685_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <pca9685_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:header-val is deprecated.  Use sensor-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'temperature-val :lambda-list '(m))
(cl:defmethod temperature-val ((m <pca9685_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:temperature-val is deprecated.  Use sensor-msg:temperature instead.")
  (temperature m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <pca9685_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:speed-val is deprecated.  Use sensor-msg:speed instead.")
  (speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pca9685_msg>) ostream)
  "Serializes a message object of type '<pca9685_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'temperature))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'speed)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pca9685_msg>) istream)
  "Deserializes a message object of type '<pca9685_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'temperature) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'speed) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pca9685_msg>)))
  "Returns string type for a message object of type '<pca9685_msg>"
  "sensor/pca9685_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pca9685_msg)))
  "Returns string type for a message object of type 'pca9685_msg"
  "sensor/pca9685_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pca9685_msg>)))
  "Returns md5sum for a message object of type '<pca9685_msg>"
  "d041db550ab3844083f2be693a00cbbd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pca9685_msg)))
  "Returns md5sum for a message object of type 'pca9685_msg"
  "d041db550ab3844083f2be693a00cbbd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pca9685_msg>)))
  "Returns full string definition for message of type '<pca9685_msg>"
  (cl:format cl:nil "# defain fan sensor pca9685 message format~%# Header~%Header header~%# ID~%# int8 chip_id~%# int8 chip_version~%# temperature~%float32 temperature~%# speed~%int16 speed~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pca9685_msg)))
  "Returns full string definition for message of type 'pca9685_msg"
  (cl:format cl:nil "# defain fan sensor pca9685 message format~%# Header~%Header header~%# ID~%# int8 chip_id~%# int8 chip_version~%# temperature~%float32 temperature~%# speed~%int16 speed~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pca9685_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pca9685_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'pca9685_msg
    (cl:cons ':header (header msg))
    (cl:cons ':temperature (temperature msg))
    (cl:cons ':speed (speed msg))
))
