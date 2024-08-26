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

class motor_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.motor_l = null;
      this.motor_r = null;
    }
    else {
      if (initObj.hasOwnProperty('motor_l')) {
        this.motor_l = initObj.motor_l
      }
      else {
        this.motor_l = 0.0;
      }
      if (initObj.hasOwnProperty('motor_r')) {
        this.motor_r = initObj.motor_r
      }
      else {
        this.motor_r = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type motor_msg
    // Serialize message field [motor_l]
    bufferOffset = _serializer.float32(obj.motor_l, buffer, bufferOffset);
    // Serialize message field [motor_r]
    bufferOffset = _serializer.float32(obj.motor_r, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type motor_msg
    let len;
    let data = new motor_msg(null);
    // Deserialize message field [motor_l]
    data.motor_l = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [motor_r]
    data.motor_r = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'copley/motor_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a89bd8697ea6757cb756a3e8b2bd3f98';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new motor_msg(null);
    if (msg.motor_l !== undefined) {
      resolved.motor_l = msg.motor_l;
    }
    else {
      resolved.motor_l = 0.0
    }

    if (msg.motor_r !== undefined) {
      resolved.motor_r = msg.motor_r;
    }
    else {
      resolved.motor_r = 0.0
    }

    return resolved;
    }
};

module.exports = motor_msg;
