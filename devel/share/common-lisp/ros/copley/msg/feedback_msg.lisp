; Auto-generated. Do not edit!


(cl:in-package copley-msg)


;//! \htmlinclude feedback_msg.msg.html

(cl:defclass <feedback_msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (motor_drive_left
    :reader motor_drive_left
    :initarg :motor_drive_left
    :type cl:float
    :initform 0.0)
   (motor_drive_right
    :reader motor_drive_right
    :initarg :motor_drive_right
    :type cl:float
    :initform 0.0)
   (motor_wing_left
    :reader motor_wing_left
    :initarg :motor_wing_left
    :type cl:float
    :initform 0.0)
   (motor_wing_right
    :reader motor_wing_right
    :initarg :motor_wing_right
    :type cl:float
    :initform 0.0)
   (motor_sting_left
    :reader motor_sting_left
    :initarg :motor_sting_left
    :type cl:float
    :initform 0.0)
   (motor_sting_right
    :reader motor_sting_right
    :initarg :motor_sting_right
    :type cl:float
    :initform 0.0))
)

(cl:defclass feedback_msg (<feedback_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <feedback_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'feedback_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name copley-msg:<feedback_msg> is deprecated: use copley-msg:feedback_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <feedback_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:header-val is deprecated.  Use copley-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'motor_drive_left-val :lambda-list '(m))
(cl:defmethod motor_drive_left-val ((m <feedback_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_drive_left-val is deprecated.  Use copley-msg:motor_drive_left instead.")
  (motor_drive_left m))

(cl:ensure-generic-function 'motor_drive_right-val :lambda-list '(m))
(cl:defmethod motor_drive_right-val ((m <feedback_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_drive_right-val is deprecated.  Use copley-msg:motor_drive_right instead.")
  (motor_drive_right m))

(cl:ensure-generic-function 'motor_wing_left-val :lambda-list '(m))
(cl:defmethod motor_wing_left-val ((m <feedback_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_wing_left-val is deprecated.  Use copley-msg:motor_wing_left instead.")
  (motor_wing_left m))

(cl:ensure-generic-function 'motor_wing_right-val :lambda-list '(m))
(cl:defmethod motor_wing_right-val ((m <feedback_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_wing_right-val is deprecated.  Use copley-msg:motor_wing_right instead.")
  (motor_wing_right m))

(cl:ensure-generic-function 'motor_sting_left-val :lambda-list '(m))
(cl:defmethod motor_sting_left-val ((m <feedback_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_sting_left-val is deprecated.  Use copley-msg:motor_sting_left instead.")
  (motor_sting_left m))

(cl:ensure-generic-function 'motor_sting_right-val :lambda-list '(m))
(cl:defmethod motor_sting_right-val ((m <feedback_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_sting_right-val is deprecated.  Use copley-msg:motor_sting_right instead.")
  (motor_sting_right m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <feedback_msg>) ostream)
  "Serializes a message object of type '<feedback_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_drive_left))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_drive_right))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_wing_left))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_wing_right))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_sting_left))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_sting_right))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <feedback_msg>) istream)
  "Deserializes a message object of type '<feedback_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_drive_left) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_drive_right) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_wing_left) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_wing_right) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_sting_left) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_sting_right) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<feedback_msg>)))
  "Returns string type for a message object of type '<feedback_msg>"
  "copley/feedback_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'feedback_msg)))
  "Returns string type for a message object of type 'feedback_msg"
  "copley/feedback_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<feedback_msg>)))
  "Returns md5sum for a message object of type '<feedback_msg>"
  "14692d936e10ff6e773f574cec4f6e90")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'feedback_msg)))
  "Returns md5sum for a message object of type 'feedback_msg"
  "14692d936e10ff6e773f574cec4f6e90")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<feedback_msg>)))
  "Returns full string definition for message of type '<feedback_msg>"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%# 这个是用来读取多个电机的数据，可以是控制指令或者编码器，都用这一个就行，只要实例化不同的对象就可以~%# 主要是为了方便， 暂时写了六个，不一定都用上，留作扩充，就是个数量问题~%# 另外，编号按照node_id来编排~%~%# Header~%Header header~%# Control~%float32 motor_drive_left~%float32 motor_drive_right~%float32 motor_wing_left~%float32 motor_wing_right~%float32 motor_sting_left~%float32 motor_sting_right~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'feedback_msg)))
  "Returns full string definition for message of type 'feedback_msg"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%# 这个是用来读取多个电机的数据，可以是控制指令或者编码器，都用这一个就行，只要实例化不同的对象就可以~%# 主要是为了方便， 暂时写了六个，不一定都用上，留作扩充，就是个数量问题~%# 另外，编号按照node_id来编排~%~%# Header~%Header header~%# Control~%float32 motor_drive_left~%float32 motor_drive_right~%float32 motor_wing_left~%float32 motor_wing_right~%float32 motor_sting_left~%float32 motor_sting_right~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <feedback_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <feedback_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'feedback_msg
    (cl:cons ':header (header msg))
    (cl:cons ':motor_drive_left (motor_drive_left msg))
    (cl:cons ':motor_drive_right (motor_drive_right msg))
    (cl:cons ':motor_wing_left (motor_wing_left msg))
    (cl:cons ':motor_wing_right (motor_wing_right msg))
    (cl:cons ':motor_sting_left (motor_sting_left msg))
    (cl:cons ':motor_sting_right (motor_sting_right msg))
))
