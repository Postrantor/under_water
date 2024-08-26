// Auto-generated. Do not edit!

// (in-package sensor.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class vector4_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.a = null;
      this.b = null;
      this.c = null;
      this.d = null;
    }
    else {
      if (initObj.hasOwnProperty('a')) {
        this.a = initObj.a
      }
      else {
        this.a = 0.0;
      }
      if (initObj.hasOwnProperty('b')) {
        this.b = initObj.b
      }
      else {
        this.b = 0.0;
      }
      if (initObj.hasOwnProperty('c')) {
        this.c = initObj.c
      }
      else {
        this.c = 0.0;
      }
      if (initObj.hasOwnProperty('d')) {
        this.d = initObj.d
      }
      else {
        this.d = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type vector4_msg
    // Serialize message field [a]
    bufferOffset = _serializer.float32(obj.a, buffer, bufferOffset);
    // Serialize message field [b]
    bufferOffset = _serializer.float32(obj.b, buffer, bufferOffset);
    // Serialize message field [c]
    bufferOffset = _serializer.float32(obj.c, buffer, bufferOffset);
    // Serialize message field [d]
    bufferOffset = _serializer.float32(obj.d, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type vector4_msg
    let len;
    let data = new vector4_msg(null);
    // Deserialize message field [a]
    data.a = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [b]
    data.b = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [c]
    data.c = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [d]
    data.d = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sensor/vector4_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8d86ed09ecfcaeb2855e47ec69fad1dd';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # 定义一个思维向量用
    float32 a
    float32 b
    float32 c
    float32 d
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new vector4_msg(null);
    if (msg.a !== undefined) {
      resolved.a = msg.a;
    }
    else {
      resolved.a = 0.0
    }

    if (msg.b !== undefined) {
      resolved.b = msg.b;
    }
    else {
      resolved.b = 0.0
    }

    if (msg.c !== undefined) {
      resolved.c = msg.c;
    }
    else {
      resolved.c = 0.0
    }

    if (msg.d !== undefined) {
      resolved.d = msg.d;
    }
    else {
      resolved.d = 0.0
    }

    return resolved;
    }
};

module.exports = vector4_msg;
