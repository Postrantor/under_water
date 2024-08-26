; Auto-generated. Do not edit!


(cl:in-package copley-msg)


;//! \htmlinclude joy2start_msg.msg.html

(cl:defclass <joy2start_msg> (roslisp-msg-protocol:ros-message)
  ((rpi_host
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

(cl:defclass joy2start_msg (<joy2start_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <joy2start_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'joy2start_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name copley-msg:<joy2start_msg> is deprecated: use copley-msg:joy2start_msg instead.")))

(cl:ensure-generic-function 'rpi_host-val :lambda-list '(m))
(cl:defmethod rpi_host-val ((m <joy2start_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:rpi_host-val is deprecated.  Use copley-msg:rpi_host instead.")
  (rpi_host m))

(cl:ensure-generic-function 'copley_motor-val :lambda-list '(m))
(cl:defmethod copley_motor-val ((m <joy2start_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:copley_motor-val is deprecated.  Use copley-msg:copley_motor instead.")
  (copley_motor m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <joy2start_msg>) ostream)
  "Serializes a message object of type '<joy2start_msg>"
  (cl:let* ((signed (cl:slot-value msg 'rpi_host)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'copley_motor)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <joy2start_msg>) istream)
  "Deserializes a message object of type '<joy2start_msg>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<joy2start_msg>)))
  "Returns string type for a message object of type '<joy2start_msg>"
  "copley/joy2start_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'joy2start_msg)))
  "Returns string type for a message object of type 'joy2start_msg"
  "copley/joy2start_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<joy2start_msg>)))
  "Returns md5sum for a message object of type '<joy2start_msg>"
  "b630d1038f374b9c6d69706a70f018ec")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'joy2start_msg)))
  "Returns md5sum for a message object of type 'joy2start_msg"
  "b630d1038f374b9c6d69706a70f018ec")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<joy2start_msg>)))
  "Returns full string definition for message of type '<joy2start_msg>"
  (cl:format cl:nil "# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Start_Joy~%int16 rpi_host~%int16 copley_motor # 采用int变量而不是bool，可能再分出第三种情况，如重启~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'joy2start_msg)))
  "Returns full string definition for message of type 'joy2start_msg"
  (cl:format cl:nil "# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Start_Joy~%int16 rpi_host~%int16 copley_motor # 采用int变量而不是bool，可能再分出第三种情况，如重启~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <joy2start_msg>))
  (cl:+ 0
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <joy2start_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'joy2start_msg
    (cl:cons ':rpi_host (rpi_host msg))
    (cl:cons ':copley_motor (copley_motor msg))
))
