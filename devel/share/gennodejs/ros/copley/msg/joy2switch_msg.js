// Auto-generated. Do not edit!

// (in-package copley.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class joy2switch_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.adjust_left = null;
      this.adjust_right = null;
      this.enc_wing = null;
      this.enc_sting = null;
      this.wing_left = null;
      this.wing_right = null;
      this.sting_left = null;
      this.sting_right = null;
    }
    else {
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
      if (initObj.hasOwnProperty('wing_left')) {
        this.wing_left = initObj.wing_left
      }
      else {
        this.wing_left = 0;
      }
      if (initObj.hasOwnProperty('wing_right')) {
        this.wing_right = initObj.wing_right
      }
      else {
        this.wing_right = 0;
      }
      if (initObj.hasOwnProperty('sting_left')) {
        this.sting_left = initObj.sting_left
      }
      else {
        this.sting_left = 0;
      }
      if (initObj.hasOwnProperty('sting_right')) {
        this.sting_right = initObj.sting_right
      }
      else {
        this.sting_right = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type joy2switch_msg
    // Serialize message field [adjust_left]
    bufferOffset = _serializer.int8(obj.adjust_left, buffer, bufferOffset);
    // Serialize message field [adjust_right]
    bufferOffset = _serializer.int8(obj.adjust_right, buffer, bufferOffset);
    // Serialize message field [enc_wing]
    bufferOffset = _serializer.bool(obj.enc_wing, buffer, bufferOffset);
    // Serialize message field [enc_sting]
    bufferOffset = _serializer.bool(obj.enc_sting, buffer, bufferOffset);
    // Serialize message field [wing_left]
    bufferOffset = _serializer.int8(obj.wing_left, buffer, bufferOffset);
    // Serialize message field [wing_right]
    bufferOffset = _serializer.int8(obj.wing_right, buffer, bufferOffset);
    // Serialize message field [sting_left]
    bufferOffset = _serializer.int8(obj.sting_left, buffer, bufferOffset);
    // Serialize message field [sting_right]
    bufferOffset = _serializer.int8(obj.sting_right, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type joy2switch_msg
    let len;
    let data = new joy2switch_msg(null);
    // Deserialize message field [adjust_left]
    data.adjust_left = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [adjust_right]
    data.adjust_right = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [enc_wing]
    data.enc_wing = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [enc_sting]
    data.enc_sting = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [wing_left]
    data.wing_left = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [wing_right]
    data.wing_right = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [sting_left]
    data.sting_left = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [sting_right]
    data.sting_right = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'copley/joy2switch_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '90b5ad54d03689fd411144777332d6f9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # $ catkin_make -DCATKIN_WHITELIST_PACKAGES="copley"
    # [issue]:
    # 这个可以和cmd的合并在一起
    # 考虑自定义twist
    
    # Joy
    int8 adjust_left
    int8 adjust_right
    bool enc_wing
    bool enc_sting
    
    int8 wing_left
    int8 wing_right
    int8 sting_left
    int8 sting_right
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new joy2switch_msg(null);
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

    if (msg.wing_left !== undefined) {
      resolved.wing_left = msg.wing_left;
    }
    else {
      resolved.wing_left = 0
    }

    if (msg.wing_right !== undefined) {
      resolved.wing_right = msg.wing_right;
    }
    else {
      resolved.wing_right = 0
    }

    if (msg.sting_left !== undefined) {
      resolved.sting_left = msg.sting_left;
    }
    else {
      resolved.sting_left = 0
    }

    if (msg.sting_right !== undefined) {
      resolved.sting_right = msg.sting_right;
    }
    else {
      resolved.sting_right = 0
    }

    return resolved;
    }
};

module.exports = joy2switch_msg;
