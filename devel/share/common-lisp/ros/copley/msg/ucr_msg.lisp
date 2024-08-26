; Auto-generated. Do not edit!


(cl:in-package copley-msg)


;//! \htmlinclude ucr_msg.msg.html

(cl:defclass <ucr_msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (current
    :reader current
    :initarg :current
    :type copley-msg:motors_msg
    :initform (cl:make-instance 'copley-msg:motors_msg))
   (velocity
    :reader velocity
    :initarg :velocity
    :type copley-msg:motors_msg
    :initform (cl:make-instance 'copley-msg:motors_msg))
   (position
    :reader position
    :initarg :position
    :type copley-msg:motors_msg
    :initform (cl:make-instance 'copley-msg:motors_msg)))
)

(cl:defclass ucr_msg (<ucr_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ucr_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ucr_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name copley-msg:<ucr_msg> is deprecated: use copley-msg:ucr_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ucr_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:header-val is deprecated.  Use copley-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'current-val :lambda-list '(m))
(cl:defmethod current-val ((m <ucr_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:current-val is deprecated.  Use copley-msg:current instead.")
  (current m))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <ucr_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:velocity-val is deprecated.  Use copley-msg:velocity instead.")
  (velocity m))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <ucr_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:position-val is deprecated.  Use copley-msg:position instead.")
  (position m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ucr_msg>) ostream)
  "Serializes a message object of type '<ucr_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'current) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'velocity) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'position) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ucr_msg>) istream)
  "Deserializes a message object of type '<ucr_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'current) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'velocity) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'position) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ucr_msg>)))
  "Returns string type for a message object of type '<ucr_msg>"
  "copley/ucr_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ucr_msg)))
  "Returns string type for a message object of type 'ucr_msg"
  "copley/ucr_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ucr_msg>)))
  "Returns md5sum for a message object of type '<ucr_msg>"
  "697cf9df9ce516a16d261952c472d294")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ucr_msg)))
  "Returns md5sum for a message object of type 'ucr_msg"
  "697cf9df9ce516a16d261952c472d294")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ucr_msg>)))
  "Returns full string definition for message of type '<ucr_msg>"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Header~%Header header~%# Drive~%copley/motors_msg current~%copley/motors_msg velocity~%copley/motors_msg position~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: copley/motors_msg~%# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%copley/motor_msg drive~%copley/motor_msg wing~%copley/motor_msg sting~%================================================================================~%MSG: copley/motor_msg~%# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Control~%float32 motor_l~%float32 motor_r~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ucr_msg)))
  "Returns full string definition for message of type 'ucr_msg"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Header~%Header header~%# Drive~%copley/motors_msg current~%copley/motors_msg velocity~%copley/motors_msg position~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: copley/motors_msg~%# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%copley/motor_msg drive~%copley/motor_msg wing~%copley/motor_msg sting~%================================================================================~%MSG: copley/motor_msg~%# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Control~%float32 motor_l~%float32 motor_r~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ucr_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'current))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'velocity))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'position))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ucr_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'ucr_msg
    (cl:cons ':header (header msg))
    (cl:cons ':current (current msg))
    (cl:cons ':velocity (velocity msg))
    (cl:cons ':position (position msg))
))
