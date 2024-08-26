// Auto-generated. Do not edit!

// (in-package copley.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let motor_msg = require('./motor_msg.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class cmd2switch_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.adjust_left = null;
      this.adjust_right = null;
      this.enc_wing = null;
      this.enc_sting = null;
      this.wing = null;
      this.sting = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('adjust_left')) {
        this.adjust_left = initObj.adjust_left
      }
      else {
        this.adjust_left = 0;
      }
      if (initObj.hasOwnProperty('adjust_right')) {
        this.adjust_right = initObj.adjust_right
      }
      else {
        this.adjust_right = 0;
      }
      if (initObj.hasOwnProperty('enc_wing')) {
        this.enc_wing = initObj.enc_wing
      }
      else {
        this.enc_wing = false;
      }
      if (initObj.hasOwnProperty('enc_sting')) {
        this.enc_sting = initObj.enc_sting
      }
      else {
        this.enc_sting = false;
      }
      if (initObj.hasOwnProperty('wing')) {
        this.wing = initObj.wing
      }
      else {
        this.wing = new motor_msg();
      }
      if (initObj.hasOwnProperty('sting')) {
        this.sting = initObj.sting
      }
      else {
        this.sting = new motor_msg();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type cmd2switch_msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [adjust_left]
    bufferOffset = _serializer.int8(obj.adjust_left, buffer, bufferOffset);
    // Serialize message field [adjust_right]
    bufferOffset = _serializer.int8(obj.adjust_right, buffer, bufferOffset);
    // Serialize message field [enc_wing]
    bufferOffset = _serializer.bool(obj.enc_wing, buffer, bufferOffset);
    // Serialize message field [enc_sting]
    bufferOffset = _serializer.bool(obj.enc_sting, buffer, bufferOffset);
    // Serialize message field [wing]
    bufferOffset = motor_msg.serialize(obj.wing, buffer, bufferOffset);
    // Serialize message field [sting]
    bufferOffset = motor_msg.serialize(obj.sting, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type cmd2switch_msg
    let len;
    let data = new cmd2switch_msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [adjust_left]
    data.adjust_left = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [adjust_right]
    data.adjust_right = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [enc_wing]
    data.enc_wing = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [enc_sting]
    data.enc_sting = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [wing]
    data.wing = motor_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [sting]
    data.sting = motor_msg.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'copley/cmd2switch_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '19a90ae0a917ebed802b29fa446ac872';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # -*- coding:utf-8 -*-
    # $ catkin_make -DCATKIN_WHITELIST_PACKAGES="copley"
    # 用于控制钩刺机构和推拉机构的运动
    # Header
    Header header
    # Switch
    int8 adjust_left
    int8 adjust_right
    bool enc_wing
    bool enc_sting
    copley/motor_msg wing
    copley/motor_msg sting
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
    
    ================================================================================
    MSG: copley/motor_msg
    # -*- coding:utf-8 -*-
    # $ catkin_make -DCATKIN_WHITELIST_PACKAGES="copley"
    
    # Control
    float32 motor_l
    float32 motor_r
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new cmd2switch_msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.adjust_left !== undefined) {
      resolved.adjust_left = msg.adjust_left;
    }
    else {
      resolved.adjust_left = 0
    }

    if (msg.adjust_right !== undefined) {
      resolved.adjust_right = msg.adjust_right;
    }
    else {
      resolved.adjust_right = 0
    }

    if (msg.enc_wing !== undefined) {
      resolved.enc_wing = msg.enc_wing;
    }
    else {
      resolved.enc_wing = false
    }

    if (msg.enc_sting !== undefined) {
      resolved.enc_sting = msg.enc_sting;
    }
    else {
      resolved.enc_sting = false
    }

    if (msg.wing !== undefined) {
      resolved.wing = motor_msg.Resolve(msg.wing)
    }
    else {
      resolved.wing = new motor_msg()
    }

    if (msg.sting !== undefined) {
      resolved.sting = motor_msg.Resolve(msg.sting)
    }
    else {
      resolved.sting = new motor_msg()
    }

    return resolved;
    }
};

module.exports = cmd2switch_msg;
