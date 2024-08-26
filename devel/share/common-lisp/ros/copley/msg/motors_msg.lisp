; Auto-generated. Do not edit!


(cl:in-package copley-msg)


;//! \htmlinclude motors_msg.msg.html

(cl:defclass <motors_msg> (roslisp-msg-protocol:ros-message)
  ((drive
    :reader drive
    :initarg :drive
    :type copley-msg:motor_msg
    :initform (cl:make-instance 'copley-msg:motor_msg))
   (wing
    :reader wing
    :initarg :wing
    :type copley-msg:motor_msg
    :initform (cl:make-instance 'copley-msg:motor_msg))
   (sting
    :reader sting
    :initarg :sting
    :type copley-msg:motor_msg
    :initform (cl:make-instance 'copley-msg:motor_msg)))
)

(cl:defclass motors_msg (<motors_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <motors_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'motors_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name copley-msg:<motors_msg> is deprecated: use copley-msg:motors_msg instead.")))

(cl:ensure-generic-function 'drive-val :lambda-list '(m))
(cl:defmethod drive-val ((m <motors_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:drive-val is deprecated.  Use copley-msg:drive instead.")
  (drive m))

(cl:ensure-generic-function 'wing-val :lambda-list '(m))
(cl:defmethod wing-val ((m <motors_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:wing-val is deprecated.  Use copley-msg:wing instead.")
  (wing m))

(cl:ensure-generic-function 'sting-val :lambda-list '(m))
(cl:defmethod sting-val ((m <motors_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:sting-val is deprecated.  Use copley-msg:sting instead.")
  (sting m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <motors_msg>) ostream)
  "Serializes a message object of type '<motors_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'drive) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'wing) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'sting) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <motors_msg>) istream)
  "Deserializes a message object of type '<motors_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'drive) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'wing) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'sting) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<motors_msg>)))
  "Returns string type for a message object of type '<motors_msg>"
  "copley/motors_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'motors_msg)))
  "Returns string type for a message object of type 'motors_msg"
  "copley/motors_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<motors_msg>)))
  "Returns md5sum for a message object of type '<motors_msg>"
  "e82ee222b0e96a1635070adf737cc004")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'motors_msg)))
  "Returns md5sum for a message object of type 'motors_msg"
  "e82ee222b0e96a1635070adf737cc004")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<motors_msg>)))
  "Returns full string definition for message of type '<motors_msg>"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%copley/motor_msg drive~%copley/motor_msg wing~%copley/motor_msg sting~%================================================================================~%MSG: copley/motor_msg~%# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Control~%float32 motor_l~%float32 motor_r~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'motors_msg)))
  "Returns full string definition for message of type 'motors_msg"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%copley/motor_msg drive~%copley/motor_msg wing~%copley/motor_msg sting~%================================================================================~%MSG: copley/motor_msg~%# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Control~%float32 motor_l~%float32 motor_r~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <motors_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'drive))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'wing))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'sting))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <motors_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'motors_msg
    (cl:cons ':drive (drive msg))
    (cl:cons ':wing (wing msg))
    (cl:cons ':sting (sting msg))
))
