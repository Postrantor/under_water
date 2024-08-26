; Auto-generated. Do not edit!


(cl:in-package copley-msg)


;//! \htmlinclude JoySwitch.msg.html

(cl:defclass <JoySwitch> (roslisp-msg-protocol:ros-message)
  ((wing_l
    :reader wing_l
    :initarg :wing_l
    :type cl:float
    :initform 0.0)
   (wing_r
    :reader wing_r
    :initarg :wing_r
    :type cl:float
    :initform 0.0)
   (sting_l
    :reader sting_l
    :initarg :sting_l
    :type cl:float
    :initform 0.0)
   (sting_r
    :reader sting_r
    :initarg :sting_r
    :type cl:float
    :initform 0.0)
   (backhome
    :reader backhome
    :initarg :backhome
    :type cl:float
    :initform 0.0))
)

(cl:defclass JoySwitch (<JoySwitch>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <JoySwitch>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'JoySwitch)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name copley-msg:<JoySwitch> is deprecated: use copley-msg:JoySwitch instead.")))

(cl:ensure-generic-function 'wing_l-val :lambda-list '(m))
(cl:defmethod wing_l-val ((m <JoySwitch>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:wing_l-val is deprecated.  Use copley-msg:wing_l instead.")
  (wing_l m))

(cl:ensure-generic-function 'wing_r-val :lambda-list '(m))
(cl:defmethod wing_r-val ((m <JoySwitch>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:wing_r-val is deprecated.  Use copley-msg:wing_r instead.")
  (wing_r m))

(cl:ensure-generic-function 'sting_l-val :lambda-list '(m))
(cl:defmethod sting_l-val ((m <JoySwitch>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:sting_l-val is deprecated.  Use copley-msg:sting_l instead.")
  (sting_l m))

(cl:ensure-generic-function 'sting_r-val :lambda-list '(m))
(cl:defmethod sting_r-val ((m <JoySwitch>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:sting_r-val is deprecated.  Use copley-msg:sting_r instead.")
  (sting_r m))

(cl:ensure-generic-function 'backhome-val :lambda-list '(m))
(cl:defmethod backhome-val ((m <JoySwitch>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:backhome-val is deprecated.  Use copley-msg:backhome instead.")
  (backhome m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <JoySwitch>) ostream)
  "Serializes a message object of type '<JoySwitch>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'wing_l))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'wing_r))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'sting_l))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'sting_r))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'backhome))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <JoySwitch>) istream)
  "Deserializes a message object of type '<JoySwitch>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'wing_l) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'wing_r) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'sting_l) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'sting_r) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'backhome) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<JoySwitch>)))
  "Returns string type for a message object of type '<JoySwitch>"
  "copley/JoySwitch")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'JoySwitch)))
  "Returns string type for a message object of type 'JoySwitch"
  "copley/JoySwitch")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<JoySwitch>)))
  "Returns md5sum for a message object of type '<JoySwitch>"
  "c7e797131241ec68ef8622ca9235a2be")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'JoySwitch)))
  "Returns md5sum for a message object of type 'JoySwitch"
  "c7e797131241ec68ef8622ca9235a2be")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<JoySwitch>)))
  "Returns full string definition for message of type '<JoySwitch>"
  (cl:format cl:nil "float32 wing_l~%float32 wing_r~%float32 sting_l~%float32 sting_r~%float32 backhome~%~%# 定义PS3手柄上的右侧遥感，包含5个值，分别对应推拉机构的推出、收缩；钩刺机构的推出、收缩；推拉机构与钩刺机构的归位；~%# 用于控制钩刺机构和推拉机构的运动~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'JoySwitch)))
  "Returns full string definition for message of type 'JoySwitch"
  (cl:format cl:nil "float32 wing_l~%float32 wing_r~%float32 sting_l~%float32 sting_r~%float32 backhome~%~%# 定义PS3手柄上的右侧遥感，包含5个值，分别对应推拉机构的推出、收缩；钩刺机构的推出、收缩；推拉机构与钩刺机构的归位；~%# 用于控制钩刺机构和推拉机构的运动~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <JoySwitch>))
  (cl:+ 0
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <JoySwitch>))
  "Converts a ROS message object to a list"
  (cl:list 'JoySwitch
    (cl:cons ':wing_l (wing_l msg))
    (cl:cons ':wing_r (wing_r msg))
    (cl:cons ':sting_l (sting_l msg))
    (cl:cons ':sting_r (sting_r msg))
    (cl:cons ':backhome (backhome msg))
))
