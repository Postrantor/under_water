; Auto-generated. Do not edit!


(cl:in-package copley-msg)


;//! \htmlinclude joy2switch_msg.msg.html

(cl:defclass <joy2switch_msg> (roslisp-msg-protocol:ros-message)
  ((adjust_left
    :reader adjust_left
    :initarg :adjust_left
    :type cl:fixnum
    :initform 0)
   (adjust_right
    :reader adjust_right
    :initarg :adjust_right
    :type cl:fixnum
    :initform 0)
   (enc_wing
    :reader enc_wing
    :initarg :enc_wing
    :type cl:boolean
    :initform cl:nil)
   (enc_sting
    :reader enc_sting
    :initarg :enc_sting
    :type cl:boolean
    :initform cl:nil)
   (wing_left
    :reader wing_left
    :initarg :wing_left
    :type cl:fixnum
    :initform 0)
   (wing_right
    :reader wing_right
    :initarg :wing_right
    :type cl:fixnum
    :initform 0)
   (sting_left
    :reader sting_left
    :initarg :sting_left
    :type cl:fixnum
    :initform 0)
   (sting_right
    :reader sting_right
    :initarg :sting_right
    :type cl:fixnum
    :initform 0))
)

(cl:defclass joy2switch_msg (<joy2switch_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <joy2switch_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'joy2switch_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name copley-msg:<joy2switch_msg> is deprecated: use copley-msg:joy2switch_msg instead.")))

(cl:ensure-generic-function 'adjust_left-val :lambda-list '(m))
(cl:defmethod adjust_left-val ((m <joy2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:adjust_left-val is deprecated.  Use copley-msg:adjust_left instead.")
  (adjust_left m))

(cl:ensure-generic-function 'adjust_right-val :lambda-list '(m))
(cl:defmethod adjust_right-val ((m <joy2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:adjust_right-val is deprecated.  Use copley-msg:adjust_right instead.")
  (adjust_right m))

(cl:ensure-generic-function 'enc_wing-val :lambda-list '(m))
(cl:defmethod enc_wing-val ((m <joy2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:enc_wing-val is deprecated.  Use copley-msg:enc_wing instead.")
  (enc_wing m))

(cl:ensure-generic-function 'enc_sting-val :lambda-list '(m))
(cl:defmethod enc_sting-val ((m <joy2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:enc_sting-val is deprecated.  Use copley-msg:enc_sting instead.")
  (enc_sting m))

(cl:ensure-generic-function 'wing_left-val :lambda-list '(m))
(cl:defmethod wing_left-val ((m <joy2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:wing_left-val is deprecated.  Use copley-msg:wing_left instead.")
  (wing_left m))

(cl:ensure-generic-function 'wing_right-val :lambda-list '(m))
(cl:defmethod wing_right-val ((m <joy2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:wing_right-val is deprecated.  Use copley-msg:wing_right instead.")
  (wing_right m))

(cl:ensure-generic-function 'sting_left-val :lambda-list '(m))
(cl:defmethod sting_left-val ((m <joy2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:sting_left-val is deprecated.  Use copley-msg:sting_left instead.")
  (sting_left m))

(cl:ensure-generic-function 'sting_right-val :lambda-list '(m))
(cl:defmethod sting_right-val ((m <joy2switch_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:sting_right-val is deprecated.  Use copley-msg:sting_right instead.")
  (sting_right m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <joy2switch_msg>) ostream)
  "Serializes a message object of type '<joy2switch_msg>"
  (cl:let* ((signed (cl:slot-value msg 'adjust_left)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'adjust_right)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'enc_wing) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'enc_sting) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'wing_left)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'wing_right)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'sting_left)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'sting_right)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <joy2switch_msg>) istream)
  "Deserializes a message object of type '<joy2switch_msg>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'adjust_left) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'adjust_right) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:setf (cl:slot-value msg 'enc_wing) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'enc_sting) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'wing_left) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'wing_right) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sting_left) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sting_right) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<joy2switch_msg>)))
  "Returns string type for a message object of type '<joy2switch_msg>"
  "copley/joy2switch_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'joy2switch_msg)))
  "Returns string type for a message object of type 'joy2switch_msg"
  "copley/joy2switch_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<joy2switch_msg>)))
  "Returns md5sum for a message object of type '<joy2switch_msg>"
  "90b5ad54d03689fd411144777332d6f9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'joy2switch_msg)))
  "Returns md5sum for a message object of type 'joy2switch_msg"
  "90b5ad54d03689fd411144777332d6f9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<joy2switch_msg>)))
  "Returns full string definition for message of type '<joy2switch_msg>"
  (cl:format cl:nil "# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%# [issue]:~%# 这个可以和cmd的合并在一起~%# 考虑自定义twist~%~%# Joy~%int8 adjust_left~%int8 adjust_right~%bool enc_wing~%bool enc_sting~%~%int8 wing_left~%int8 wing_right~%int8 sting_left~%int8 sting_right~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'joy2switch_msg)))
  "Returns full string definition for message of type 'joy2switch_msg"
  (cl:format cl:nil "# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%# [issue]:~%# 这个可以和cmd的合并在一起~%# 考虑自定义twist~%~%# Joy~%int8 adjust_left~%int8 adjust_right~%bool enc_wing~%bool enc_sting~%~%int8 wing_left~%int8 wing_right~%int8 sting_left~%int8 sting_right~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <joy2switch_msg>))
  (cl:+ 0
     1
     1
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <joy2switch_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'joy2switch_msg
    (cl:cons ':adjust_left (adjust_left msg))
    (cl:cons ':adjust_right (adjust_right msg))
    (cl:cons ':enc_wing (enc_wing msg))
    (cl:cons ':enc_sting (enc_sting msg))
    (cl:cons ':wing_left (wing_left msg))
    (cl:cons ':wing_right (wing_right msg))
    (cl:cons ':sting_left (sting_left msg))
    (cl:cons ':sting_right (sting_right msg))
))
