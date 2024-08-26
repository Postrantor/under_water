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

class bme280 {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.chip_id = null;
      this.chip_version = null;
      this.temperature = null;
      this.pressure = null;
      this.humidity = null;
    }
    else {
      if (initObj.hasOwnProperty('chip_id')) {
        this.chip_id = initObj.chip_id
      }
      else {
        this.chip_id = 0;
      }
      if (initObj.hasOwnProperty('chip_version')) {
        this.chip_version = initObj.chip_version
      }
      else {
        this.chip_version = 0;
      }
      if (initObj.hasOwnProperty('temperature')) {
        this.temperature = initObj.temperature
      }
      else {
        this.temperature = 0.0;
      }
      if (initObj.hasOwnProperty('pressure')) {
        this.pressure = initObj.pressure
      }
      else {
        this.pressure = 0.0;
      }
      if (initObj.hasOwnProperty('humidity')) {
        this.humidity = initObj.humidity
      }
      else {
        this.humidity = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type bme280
    // Serialize message field [chip_id]
    bufferOffset = _serializer.int8(obj.chip_id, buffer, bufferOffset);
    // Serialize message field [chip_version]
    bufferOffset = _serializer.int8(obj.chip_version, buffer, bufferOffset);
    // Serialize message field [temperature]
    bufferOffset = _serializer.float32(obj.temperature, buffer, bufferOffset);
    // Serialize message field [pressure]
    bufferOffset = _serializer.float32(obj.pressure, buffer, bufferOffset);
    // Serialize message field [humidity]
    bufferOffset = _serializer.float32(obj.humidity, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type bme280
    let len;
    let data = new bme280(null);
    // Deserialize message field [chip_id]
    data.chip_id = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [chip_version]
    data.chip_version = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [temperature]
    data.temperature = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [pressure]
    data.pressure = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [humidity]
    data.humidity = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 14;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sensor/bme280';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'cf334dd156db771a2125cf250be13097';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # defain environment sensor bme280 message format
    # ID
    int8 chip_id
    int8 chip_version
    # temperature
    float32 temperature
    # air pressure
    float32 pressure
    # humidity
    float32 humidity
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new bme280(null);
    if (msg.chip_id !== undefined) {
      resolved.chip_id = msg.chip_id;
    }
    else {
      resolved.chip_id = 0
    }

    if (msg.chip_version !== undefined) {
      resolved.chip_version = msg.chip_version;
    }
    else {
      resolved.chip_version = 0
    }

    if (msg.temperature !== undefined) {
      resolved.temperature = msg.temperature;
    }
    else {
      resolved.temperature = 0.0
    }

    if (msg.pressure !== undefined) {
      resolved.pressure = msg.pressure;
    }
    else {
      resolved.pressure = 0.0
    }

    if (msg.humidity !== undefined) {
      resolved.humidity = msg.humidity;
    }
    else {
      resolved.humidity = 0.0
    }

    return resolved;
    }
};

module.exports = bme280;
