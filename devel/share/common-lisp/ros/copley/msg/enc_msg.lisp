; Auto-generated. Do not edit!


(cl:in-package copley-msg)


;//! \htmlinclude enc_msg.msg.html

(cl:defclass <enc_msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (motor_0
    :reader motor_0
    :initarg :motor_0
    :type cl:float
    :initform 0.0)
   (motor_1
    :reader motor_1
    :initarg :motor_1
    :type cl:float
    :initform 0.0)
   (motor_2
    :reader motor_2
    :initarg :motor_2
    :type cl:float
    :initform 0.0)
   (motor_3
    :reader motor_3
    :initarg :motor_3
    :type cl:float
    :initform 0.0)
   (motor_4
    :reader motor_4
    :initarg :motor_4
    :type cl:float
    :initform 0.0)
   (motor_5
    :reader motor_5
    :initarg :motor_5
    :type cl:float
    :initform 0.0))
)

(cl:defclass enc_msg (<enc_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <enc_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'enc_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name copley-msg:<enc_msg> is deprecated: use copley-msg:enc_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <enc_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:header-val is deprecated.  Use copley-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'motor_0-val :lambda-list '(m))
(cl:defmethod motor_0-val ((m <enc_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_0-val is deprecated.  Use copley-msg:motor_0 instead.")
  (motor_0 m))

(cl:ensure-generic-function 'motor_1-val :lambda-list '(m))
(cl:defmethod motor_1-val ((m <enc_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_1-val is deprecated.  Use copley-msg:motor_1 instead.")
  (motor_1 m))

(cl:ensure-generic-function 'motor_2-val :lambda-list '(m))
(cl:defmethod motor_2-val ((m <enc_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_2-val is deprecated.  Use copley-msg:motor_2 instead.")
  (motor_2 m))

(cl:ensure-generic-function 'motor_3-val :lambda-list '(m))
(cl:defmethod motor_3-val ((m <enc_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_3-val is deprecated.  Use copley-msg:motor_3 instead.")
  (motor_3 m))

(cl:ensure-generic-function 'motor_4-val :lambda-list '(m))
(cl:defmethod motor_4-val ((m <enc_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_4-val is deprecated.  Use copley-msg:motor_4 instead.")
  (motor_4 m))

(cl:ensure-generic-function 'motor_5-val :lambda-list '(m))
(cl:defmethod motor_5-val ((m <enc_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:motor_5-val is deprecated.  Use copley-msg:motor_5 instead.")
  (motor_5 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <enc_msg>) ostream)
  "Serializes a message object of type '<enc_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_0))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_4))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'motor_5))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <enc_msg>) istream)
  "Deserializes a message object of type '<enc_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_0) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_3) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_4) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'motor_5) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<enc_msg>)))
  "Returns string type for a message object of type '<enc_msg>"
  "copley/enc_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'enc_msg)))
  "Returns string type for a message object of type 'enc_msg"
  "copley/enc_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<enc_msg>)))
  "Returns md5sum for a message object of type '<enc_msg>"
  "a888e664d4832aa9d46846c07b169702")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'enc_msg)))
  "Returns md5sum for a message object of type 'enc_msg"
  "a888e664d4832aa9d46846c07b169702")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<enc_msg>)))
  "Returns full string definition for message of type '<enc_msg>"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%# 这个是用来读取多个电机的控制指令的数据~%# 主要是为了方便， 暂时写了六个，不一定都用上，留作扩充，就是个数量问题~%# 另外，编号按照node_id来编排~%~%# Header~%Header header~%# Control~%float32 motor_0~%float32 motor_1~%float32 motor_2~%float32 motor_3~%float32 motor_4~%float32 motor_5~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'enc_msg)))
  "Returns full string definition for message of type 'enc_msg"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%# 这个是用来读取多个电机的控制指令的数据~%# 主要是为了方便， 暂时写了六个，不一定都用上，留作扩充，就是个数量问题~%# 另外，编号按照node_id来编排~%~%# Header~%Header header~%# Control~%float32 motor_0~%float32 motor_1~%float32 motor_2~%float32 motor_3~%float32 motor_4~%float32 motor_5~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <enc_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <enc_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'enc_msg
    (cl:cons ':header (header msg))
    (cl:cons ':motor_0 (motor_0 msg))
    (cl:cons ':motor_1 (motor_1 msg))
    (cl:cons ':motor_2 (motor_2 msg))
    (cl:cons ':motor_3 (motor_3 msg))
    (cl:cons ':motor_4 (motor_4 msg))
    (cl:cons ':motor_5 (motor_5 msg))
))
