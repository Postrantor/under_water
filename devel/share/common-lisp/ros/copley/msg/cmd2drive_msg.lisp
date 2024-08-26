; Auto-generated. Do not edit!


(cl:in-package copley-msg)


;//! \htmlinclude cmd2drive_msg.msg.html

(cl:defclass <cmd2drive_msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (drive
    :reader drive
    :initarg :drive
    :type copley-msg:motor_msg
    :initform (cl:make-instance 'copley-msg:motor_msg)))
)

(cl:defclass cmd2drive_msg (<cmd2drive_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <cmd2drive_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'cmd2drive_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name copley-msg:<cmd2drive_msg> is deprecated: use copley-msg:cmd2drive_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <cmd2drive_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:header-val is deprecated.  Use copley-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'drive-val :lambda-list '(m))
(cl:defmethod drive-val ((m <cmd2drive_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader copley-msg:drive-val is deprecated.  Use copley-msg:drive instead.")
  (drive m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <cmd2drive_msg>) ostream)
  "Serializes a message object of type '<cmd2drive_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'drive) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <cmd2drive_msg>) istream)
  "Deserializes a message object of type '<cmd2drive_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'drive) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<cmd2drive_msg>)))
  "Returns string type for a message object of type '<cmd2drive_msg>"
  "copley/cmd2drive_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'cmd2drive_msg)))
  "Returns string type for a message object of type 'cmd2drive_msg"
  "copley/cmd2drive_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<cmd2drive_msg>)))
  "Returns md5sum for a message object of type '<cmd2drive_msg>"
  "49b69f086ac244e027a573abc129a395")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'cmd2drive_msg)))
  "Returns md5sum for a message object of type 'cmd2drive_msg"
  "49b69f086ac244e027a573abc129a395")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<cmd2drive_msg>)))
  "Returns full string definition for message of type '<cmd2drive_msg>"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Header~%Header header~%# Drive~%copley/motor_msg drive~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: copley/motor_msg~%# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Control~%float32 motor_l~%float32 motor_r~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'cmd2drive_msg)))
  "Returns full string definition for message of type 'cmd2drive_msg"
  (cl:format cl:nil "# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Header~%Header header~%# Drive~%copley/motor_msg drive~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: copley/motor_msg~%# -*- coding:utf-8 -*-~%# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"~%~%# Control~%float32 motor_l~%float32 motor_r~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <cmd2drive_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'drive))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <cmd2drive_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'cmd2drive_msg
    (cl:cons ':header (header msg))
    (cl:cons ':drive (drive msg))
))
