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

class watt_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.voltage = null;
      this.current = null;
      this.resistance = null;
      this.watt = null;
    }
    else {
      if (initObj.hasOwnProperty('voltage')) {
        this.voltage = initObj.voltage
      }
      else {
        this.voltage = 0.0;
      }
      if (initObj.hasOwnProperty('current')) {
        this.current = initObj.current
      }
      else {
        this.current = 0.0;
      }
      if (initObj.hasOwnProperty('resistance')) {
        this.resistance = initObj.resistance
      }
      else {
        this.resistance = 0.0;
      }
      if (initObj.hasOwnProperty('watt')) {
        this.watt = initObj.watt
      }
      else {
        this.watt = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type watt_msg
    // Serialize message field [voltage]
    bufferOffset = _serializer.float32(obj.voltage, buffer, bufferOffset);
    // Serialize message field [current]
    bufferOffset = _serializer.float32(obj.current, buffer, bufferOffset);
    // Serialize message field [resistance]
    bufferOffset = _serializer.float32(obj.resistance, buffer, bufferOffset);
    // Serialize message field [watt]
    bufferOffset = _serializer.float32(obj.watt, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type watt_msg
    let len;
    let data = new watt_msg(null);
    // Deserialize message field [voltage]
    data.voltage = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [current]
    data.current = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [resistance]
    data.resistance = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [watt]
    data.watt = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sensor/watt_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '136cc9f95f5d86898b1dfcc8b32f4a40';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # 定义一个4维向量用于传输功率的数据
    float32 voltage
    float32 current
    float32 resistance
    float32 watt
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new watt_msg(null);
    if (msg.voltage !== undefined) {
      resolved.voltage = msg.voltage;
    }
    else {
      resolved.voltage = 0.0
    }

    if (msg.current !== undefined) {
      resolved.current = msg.current;
    }
    else {
      resolved.current = 0.0
    }

    if (msg.resistance !== undefined) {
      resolved.resistance = msg.resistance;
    }
    else {
      resolved.resistance = 0.0
    }

    if (msg.watt !== undefined) {
      resolved.watt = msg.watt;
    }
    else {
      resolved.watt = 0.0
    }

    return resolved;
    }
};

module.exports = watt_msg;
