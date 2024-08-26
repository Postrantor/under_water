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

//-----------------------------------------------------------

class motors_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.drive = null;
      this.wing = null;
      this.sting = null;
    }
    else {
      if (initObj.hasOwnProperty('drive')) {
        this.drive = initObj.drive
      }
      else {
        this.drive = new motor_msg();
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
    // Serializes a message object of type motors_msg
    // Serialize message field [drive]
    bufferOffset = motor_msg.serialize(obj.drive, buffer, bufferOffset);
    // Serialize message field [wing]
    bufferOffset = motor_msg.serialize(obj.wing, buffer, bufferOffset);
    // Serialize message field [sting]
    bufferOffset = motor_msg.serialize(obj.sting, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type motors_msg
    let len;
    let data = new motors_msg(null);
    // Deserialize message field [drive]
    data.drive = motor_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [wing]
    data.wing = motor_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [sting]
    data.sting = motor_msg.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'copley/motors_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e82ee222b0e96a1635070adf737cc004';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # -*- coding:utf-8 -*-
    # $ catkin_make -DCATKIN_WHITELIST_PACKAGES="copley"
    
    copley/motor_msg drive
    copley/motor_msg wing
    copley/motor_msg sting
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
    const resolved = new motors_msg(null);
    if (msg.drive !== undefined) {
      resolved.drive = motor_msg.Resolve(msg.drive)
    }
    else {
      resolved.drive = new motor_msg()
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

module.exports = motors_msg;
