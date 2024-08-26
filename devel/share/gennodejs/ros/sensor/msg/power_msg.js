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

class power_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.remaining = null;
      this.consumed = null;
      this.capacity = null;
      this.percentage = null;
    }
    else {
      if (initObj.hasOwnProperty('remaining')) {
        this.remaining = initObj.remaining
      }
      else {
        this.remaining = 0.0;
      }
      if (initObj.hasOwnProperty('consumed')) {
        this.consumed = initObj.consumed
      }
      else {
        this.consumed = 0;
      }
      if (initObj.hasOwnProperty('capacity')) {
        this.capacity = initObj.capacity
      }
      else {
        this.capacity = 0.0;
      }
      if (initObj.hasOwnProperty('percentage')) {
        this.percentage = initObj.percentage
      }
      else {
        this.percentage = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type power_msg
    // Serialize message field [remaining]
    bufferOffset = _serializer.float32(obj.remaining, buffer, bufferOffset);
    // Serialize message field [consumed]
    bufferOffset = _serializer.int16(obj.consumed, buffer, bufferOffset);
    // Serialize message field [capacity]
    bufferOffset = _serializer.float32(obj.capacity, buffer, bufferOffset);
    // Serialize message field [percentage]
    bufferOffset = _serializer.float32(obj.percentage, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type power_msg
    let len;
    let data = new power_msg(null);
    // Deserialize message field [remaining]
    data.remaining = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [consumed]
    data.consumed = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [capacity]
    data.capacity = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [percentage]
    data.percentage = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 14;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sensor/power_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6985abf14ffd1aad6747673ddb5719f6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # 定义一个4维向量用于传输电量的数据
    float32 remaining
    int16 consumed
    float32 capacity
    float32 percentage
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new power_msg(null);
    if (msg.remaining !== undefined) {
      resolved.remaining = msg.remaining;
    }
    else {
      resolved.remaining = 0.0
    }

    if (msg.consumed !== undefined) {
      resolved.consumed = msg.consumed;
    }
    else {
      resolved.consumed = 0
    }

    if (msg.capacity !== undefined) {
      resolved.capacity = msg.capacity;
    }
    else {
      resolved.capacity = 0.0
    }

    if (msg.percentage !== undefined) {
      resolved.percentage = msg.percentage;
    }
    else {
      resolved.percentage = 0.0
    }

    return resolved;
    }
};

module.exports = power_msg;
