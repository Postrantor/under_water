; Auto-generated. Do not edit!


(cl:in-package sensor-msg)


;//! \htmlinclude coulomb_msg.msg.html

(cl:defclass <coulomb_msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (watt
    :reader watt
    :initarg :watt
    :type sensor-msg:watt_msg
    :initform (cl:make-instance 'sensor-msg:watt_msg))
   (power
    :reader power
    :initarg :power
    :type sensor-msg:power_msg
    :initform (cl:make-instance 'sensor-msg:power_msg)))
)

(cl:defclass coulomb_msg (<coulomb_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <coulomb_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'coulomb_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor-msg:<coulomb_msg> is deprecated: use sensor-msg:coulomb_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <coulomb_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:header-val is deprecated.  Use sensor-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'watt-val :lambda-list '(m))
(cl:defmethod watt-val ((m <coulomb_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:watt-val is deprecated.  Use sensor-msg:watt instead.")
  (watt m))

(cl:ensure-generic-function 'power-val :lambda-list '(m))
(cl:defmethod power-val ((m <coulomb_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor-msg:power-val is deprecated.  Use sensor-msg:power instead.")
  (power m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <coulomb_msg>) ostream)
  "Serializes a message object of type '<coulomb_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'watt) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'power) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <coulomb_msg>) istream)
  "Deserializes a message object of type '<coulomb_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'watt) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'power) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<coulomb_msg>)))
  "Returns string type for a message object of type '<coulomb_msg>"
  "sensor/coulomb_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'coulomb_msg)))
  "Returns string type for a message object of type 'coulomb_msg"
  "sensor/coulomb_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<coulomb_msg>)))
  "Returns md5sum for a message object of type '<coulomb_msg>"
  "c5cd7058055ef3a00c048e9d3583364c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'coulomb_msg)))
  "Returns md5sum for a message object of type 'coulomb_msg"
  "c5cd7058055ef3a00c048e9d3583364c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<coulomb_msg>)))
  "Returns full string definition for message of type '<coulomb_msg>"
  (cl:format cl:nil "# define coulomb sensor XLDN_1602 message format~%# Header~%Header header~%# Watt~%sensor/watt_msg watt~%# Power~%sensor/power_msg power~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: sensor/watt_msg~%# 定义一个4维向量用于传输功率的数据~%float32 voltage~%float32 current~%float32 resistance~%float32 watt~%================================================================================~%MSG: sensor/power_msg~%# 定义一个4维向量用于传输电量的数据~%float32 remaining~%int16 consumed~%float32 capacity~%float32 percentage~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'coulomb_msg)))
  "Returns full string definition for message of type 'coulomb_msg"
  (cl:format cl:nil "# define coulomb sensor XLDN_1602 message format~%# Header~%Header header~%# Watt~%sensor/watt_msg watt~%# Power~%sensor/power_msg power~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: sensor/watt_msg~%# 定义一个4维向量用于传输功率的数据~%float32 voltage~%float32 current~%float32 resistance~%float32 watt~%================================================================================~%MSG: sensor/power_msg~%# 定义一个4维向量用于传输电量的数据~%float32 remaining~%int16 consumed~%float32 capacity~%float32 percentage~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <coulomb_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'watt))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'power))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <coulomb_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'coulomb_msg
    (cl:cons ':header (header msg))
    (cl:cons ':watt (watt msg))
    (cl:cons ':power (power msg))
))
