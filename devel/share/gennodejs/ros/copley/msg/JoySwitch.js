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

class JoySwitch {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.wing_l = null;
      this.wing_r = null;
      this.sting_l = null;
      this.sting_r = null;
      this.backhome = null;
    }
    else {
      if (initObj.hasOwnProperty('wing_l')) {
        this.wing_l = initObj.wing_l
      }
      else {
        this.wing_l = 0.0;
      }
      if (initObj.hasOwnProperty('wing_r')) {
        this.wing_r = initObj.wing_r
      }
      else {
        this.wing_r = 0.0;
      }
      if (initObj.hasOwnProperty('sting_l')) {
        this.sting_l = initObj.sting_l
      }
      else {
        this.sting_l = 0.0;
      }
      if (initObj.hasOwnProperty('sting_r')) {
        this.sting_r = initObj.sting_r
      }
      else {
        this.sting_r = 0.0;
      }
      if (initObj.hasOwnProperty('backhome')) {
        this.backhome = initObj.backhome
      }
      else {
        this.backhome = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type JoySwitch
    // Serialize message field [wing_l]
    bufferOffset = _serializer.float32(obj.wing_l, buffer, bufferOffset);
    // Serialize message field [wing_r]
    bufferOffset = _serializer.float32(obj.wing_r, buffer, bufferOffset);
    // Serialize message field [sting_l]
    bufferOffset = _serializer.float32(obj.sting_l, buffer, bufferOffset);
    // Serialize message field [sting_r]
    bufferOffset = _serializer.float32(obj.sting_r, buffer, bufferOffset);
    // Serialize message field [backhome]
    bufferOffset = _serializer.float32(obj.backhome, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type JoySwitch
    let len;
    let data = new JoySwitch(null);
    // Deserialize message field [wing_l]
    data.wing_l = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [wing_r]
    data.wing_r = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [sting_l]
    data.sting_l = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [sting_r]
    data.sting_r = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [backhome]
    data.backhome = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'copley/JoySwitch';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c7e797131241ec68ef8622ca9235a2be';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 wing_l
    float32 wing_r
    float32 sting_l
    float32 sting_r
    float32 backhome
    
    # 定义PS3手柄上的右侧遥感，包含5个值，分别对应推拉机构的推出、收缩；钩刺机构的推出、收缩；推拉机构与钩刺机构的归位；
    # 用于控制钩刺机构和推拉机构的运动
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new JoySwitch(null);
    if (msg.wing_l !== undefined) {
      resolved.wing_l = msg.wing_l;
    }
    else {
      resolved.wing_l = 0.0
    }

    if (msg.wing_r !== undefined) {
      resolved.wing_r = msg.wing_r;
    }
    else {
      resolved.wing_r = 0.0
    }

    if (msg.sting_l !== undefined) {
      resolved.sting_l = msg.sting_l;
    }
    else {
      resolved.sting_l = 0.0
    }

    if (msg.sting_r !== undefined) {
      resolved.sting_r = msg.sting_r;
    }
    else {
      resolved.sting_r = 0.0
    }

    if (msg.backhome !== undefined) {
      resolved.backhome = msg.backhome;
    }
    else {
      resolved.backhome = 0.0
    }

    return resolved;
    }
};

module.exports = JoySwitch;
