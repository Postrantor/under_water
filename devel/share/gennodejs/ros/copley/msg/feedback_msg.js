// Auto-generated. Do not edit!

// (in-package copley.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class feedback_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.motor_drive_left = null;
      this.motor_drive_right = null;
      this.motor_wing_left = null;
      this.motor_wing_right = null;
      this.motor_sting_left = null;
      this.motor_sting_right = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('motor_drive_left')) {
        this.motor_drive_left = initObj.motor_drive_left
      }
      else {
        this.motor_drive_left = 0.0;
      }
      if (initObj.hasOwnProperty('motor_drive_right')) {
        this.motor_drive_right = initObj.motor_drive_right
      }
      else {
        this.motor_drive_right = 0.0;
      }
      if (initObj.hasOwnProperty('motor_wing_left')) {
        this.motor_wing_left = initObj.motor_wing_left
      }
      else {
        this.motor_wing_left = 0.0;
      }
      if (initObj.hasOwnProperty('motor_wing_right')) {
        this.motor_wing_right = initObj.motor_wing_right
      }
      else {
        this.motor_wing_right = 0.0;
      }
      if (initObj.hasOwnProperty('motor_sting_left')) {
        this.motor_sting_left = initObj.motor_sting_left
      }
      else {
        this.motor_sting_left = 0.0;
      }
      if (initObj.hasOwnProperty('motor_sting_right')) {
        this.motor_sting_right = initObj.motor_sting_right
      }
      else {
        this.motor_sting_right = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type feedback_msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [motor_drive_left]
    bufferOffset = _serializer.float32(obj.motor_drive_left, buffer, bufferOffset);
    // Serialize message field [motor_drive_right]
    bufferOffset = _serializer.float32(obj.motor_drive_right, buffer, bufferOffset);
    // Serialize message field [motor_wing_left]
    bufferOffset = _serializer.float32(obj.motor_wing_left, buffer, bufferOffset);
    // Serialize message field [motor_wing_right]
    bufferOffset = _serializer.float32(obj.motor_wing_right, buffer, bufferOffset);
    // Serialize message field [motor_sting_left]
    bufferOffset = _serializer.float32(obj.motor_sting_left, buffer, bufferOffset);
    // Serialize message field [motor_sting_right]
    bufferOffset = _serializer.float32(obj.motor_sting_right, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type feedback_msg
    let len;
    let data = new feedback_msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [motor_drive_left]
    data.motor_drive_left = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_drive_right]
    data.motor_drive_right = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_wing_left]
    data.motor_wing_left = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_wing_right]
    data.motor_wing_right = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_sting_left]
    data.motor_sting_left = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_sting_right]
    data.motor_sting_right = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'copley/feedback_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '14692d936e10ff6e773f574cec4f6e90';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # -*- coding:utf-8 -*-
    # $ catkin_make -DCATKIN_WHITELIST_PACKAGES="copley"
    # 这个是用来读取多个电机的数据，可以是控制指令或者编码器，都用这一个就行，只要实例化不同的对象就可以
    # 主要是为了方便， 暂时写了六个，不一定都用上，留作扩充，就是个数量问题
    # 另外，编号按照node_id来编排
    
    # Header
    Header header
    # Control
    float32 motor_drive_left
    float32 motor_drive_right
    float32 motor_wing_left
    float32 motor_wing_right
    float32 motor_sting_left
    float32 motor_sting_right
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new feedback_msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.motor_drive_left !== undefined) {
      resolved.motor_drive_left = msg.motor_drive_left;
    }
    else {
      resolved.motor_drive_left = 0.0
    }

    if (msg.motor_drive_right !== undefined) {
      resolved.motor_drive_right = msg.motor_drive_right;
    }
    else {
      resolved.motor_drive_right = 0.0
    }

    if (msg.motor_wing_left !== undefined) {
      resolved.motor_wing_left = msg.motor_wing_left;
    }
    else {
      resolved.motor_wing_left = 0.0
    }

    if (msg.motor_wing_right !== undefined) {
      resolved.motor_wing_right = msg.motor_wing_right;
    }
    else {
      resolved.motor_wing_right = 0.0
    }

    if (msg.motor_sting_left !== undefined) {
      resolved.motor_sting_left = msg.motor_sting_left;
    }
    else {
      resolved.motor_sting_left = 0.0
    }

    if (msg.motor_sting_right !== undefined) {
      resolved.motor_sting_right = msg.motor_sting_right;
    }
    else {
      resolved.motor_sting_right = 0.0
    }

    return resolved;
    }
};

module.exports = feedback_msg;
