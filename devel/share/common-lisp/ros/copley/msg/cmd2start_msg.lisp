; Auto-generated. Do not edit!


(cl:in-package copley-msg)


;//! \htmlinclude cmd2start_msg.msg.html

(cl:defclass <cmd2start_msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (rpi_host
    :reader rpi_host
    :initarg :rpi_host
    :type cl:fixnum
    :initform 0)
   (copley_motor
    :reader copley_motor
    :initarg :copley_motor
    :type cl:fixnum
    :initform 0))
)

(cl:defclass cmd2start_msg (<cmd2start_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <cmd2start_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'cmd2start_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name copley-msg:<cmd2start_msg> is deprecated: use copley-msg:cmd2start_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <cmd2start_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:header-val is deprecated.  Use copley-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'rpi_host-val :lambda-list '(m))
(cl:defmethod rpi_host-val ((m <cmd2start_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:rpi_host-val is deprecated.  Use copley-msg:rpi_host instead.")
  (rpi_host m))

(cl:ensure-generic-function 'copley_motor-val :lambda-list '(m))
(cl:defmethod copley_motor-val ((m <cmd2start_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:copley_motor-val is deprecated.  Use copley-msg:copley_motor instead.")
  (copley_motor m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <cmd2start_msg>) ostream)
  "Serializes a message object of type '<cmd2start_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'rpi_host)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'copley_motor)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <cmd2start_msg>) istream)
  "Deserializes a message object of type '<cmd2start_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rpi_host) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'copley_motor) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<cmd2start_msg>)))
  "Returns string type for a message object of type '<cmd2start_msg>"
  "copley/cmd2start_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'cmd2start_msg)))
  "Returns string type for a message object of type 'cmd2start_msg"
  "copley/cmd2start_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<cmd2start_msg>)))
  "Returns md5sum for a message object of type '<cmd2start_msg>"
  "111b1a1fda8851b8a4f1107ff12e3c61")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'cmd2start_msg)))
  "Returns md5sum for a message object of type 'cmd2start_msg"
  "111b1a1fda8851b8a4f1107ff12e3c61")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<cmd2start_msg>)))
  "Returns full string definition for message of type '<cmd2start_msg>"
  (cl:format cl:nil "# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Header~%Header header~%# Start_Joy~%int16 rpi_host~%int16 copley_motor # 采用int变量而不是bool，可能再分出第三种情况，如重启~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'cmd2start_msg)))
  "Returns full string definition for message of type 'cmd2start_msg"
  (cl:format cl:nil "# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Header~%Header header~%# Start_Joy~%int16 rpi_host~%int16 copley_motor # 采用int变量而不是bool，可能再分出第三种情况，如重启~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <cmd2start_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <cmd2start_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'cmd2start_msg
    (cl:cons ':header (header msg))
    (cl:cons ':rpi_host (rpi_host msg))
    (cl:cons ':copley_motor (copley_motor msg))
))
