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

class control_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.motor_0 = null;
      this.motor_1 = null;
      this.motor_2 = null;
      this.motor_3 = null;
      this.motor_4 = null;
      this.motor_5 = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('motor_0')) {
        this.motor_0 = initObj.motor_0
      }
      else {
        this.motor_0 = 0.0;
      }
      if (initObj.hasOwnProperty('motor_1')) {
        this.motor_1 = initObj.motor_1
      }
      else {
        this.motor_1 = 0.0;
      }
      if (initObj.hasOwnProperty('motor_2')) {
        this.motor_2 = initObj.motor_2
      }
      else {
        this.motor_2 = 0.0;
      }
      if (initObj.hasOwnProperty('motor_3')) {
        this.motor_3 = initObj.motor_3
      }
      else {
        this.motor_3 = 0.0;
      }
      if (initObj.hasOwnProperty('motor_4')) {
        this.motor_4 = initObj.motor_4
      }
      else {
        this.motor_4 = 0.0;
      }
      if (initObj.hasOwnProperty('motor_5')) {
        this.motor_5 = initObj.motor_5
      }
      else {
        this.motor_5 = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type control_msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [motor_0]
    bufferOffset = _serializer.float32(obj.motor_0, buffer, bufferOffset);
    // Serialize message field [motor_1]
    bufferOffset = _serializer.float32(obj.motor_1, buffer, bufferOffset);
    // Serialize message field [motor_2]
    bufferOffset = _serializer.float32(obj.motor_2, buffer, bufferOffset);
    // Serialize message field [motor_3]
    bufferOffset = _serializer.float32(obj.motor_3, buffer, bufferOffset);
    // Serialize message field [motor_4]
    bufferOffset = _serializer.float32(obj.motor_4, buffer, bufferOffset);
    // Serialize message field [motor_5]
    bufferOffset = _serializer.float32(obj.motor_5, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type control_msg
    let len;
    let data = new control_msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [motor_0]
    data.motor_0 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_1]
    data.motor_1 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_2]
    data.motor_2 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_3]
    data.motor_3 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_4]
    data.motor_4 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_5]
    data.motor_5 = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'copley/control_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a888e664d4832aa9d46846c07b169702';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # -*- coding:utf-8 -*-
    # $ catkin_make -DCATKIN_WHITELIST_PACKAGES="copley"
    # 这个是用来读取多个电机的控制指令的数据
    # 主要是为了方便， 暂时写了六个，不一定都用上，留作扩充，就是个数量问题
    # 另外，编号按照node_id来编排
    
    # Header
    Header header
    # Control
    float32 motor_0
    float32 motor_1
    float32 motor_2
    float32 motor_3
    float32 motor_4
    float32 motor_5
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
    const resolved = new control_msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.motor_0 !== undefined) {
      resolved.motor_0 = msg.motor_0;
    }
    else {
      resolved.motor_0 = 0.0
    }

    if (msg.motor_1 !== undefined) {
      resolved.motor_1 = msg.motor_1;
    }
    else {
      resolved.motor_1 = 0.0
    }

    if (msg.motor_2 !== undefined) {
      resolved.motor_2 = msg.motor_2;
    }
    else {
      resolved.motor_2 = 0.0
    }

    if (msg.motor_3 !== undefined) {
      resolved.motor_3 = msg.motor_3;
    }
    else {
      resolved.motor_3 = 0.0
    }

    if (msg.motor_4 !== undefined) {
      resolved.motor_4 = msg.motor_4;
    }
    else {
      resolved.motor_4 = 0.0
    }

    if (msg.motor_5 !== undefined) {
      resolved.motor_5 = msg.motor_5;
    }
    else {
      resolved.motor_5 = 0.0
    }

    return resolved;
    }
};

module.exports = control_msg;
