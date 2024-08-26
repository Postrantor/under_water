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

class ms5837 {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.psr_atm = null;
      this.psr_Torr = null;
      this.psr_psi = null;
      this.temp_C = null;
      this.temp_F = null;
      this.temp_K = null;
      this.freshDepth = null;
      this.saltDepth = null;
      this.altitude = null;
    }
    else {
      if (initObj.hasOwnProperty('psr_atm')) {
        this.psr_atm = initObj.psr_atm
      }
      else {
        this.psr_atm = 0.0;
      }
      if (initObj.hasOwnProperty('psr_Torr')) {
        this.psr_Torr = initObj.psr_Torr
      }
      else {
        this.psr_Torr = 0.0;
      }
      if (initObj.hasOwnProperty('psr_psi')) {
        this.psr_psi = initObj.psr_psi
      }
      else {
        this.psr_psi = 0.0;
      }
      if (initObj.hasOwnProperty('temp_C')) {
        this.temp_C = initObj.temp_C
      }
      else {
        this.temp_C = 0.0;
      }
      if (initObj.hasOwnProperty('temp_F')) {
        this.temp_F = initObj.temp_F
      }
      else {
        this.temp_F = 0.0;
      }
      if (initObj.hasOwnProperty('temp_K')) {
        this.temp_K = initObj.temp_K
      }
      else {
        this.temp_K = 0.0;
      }
      if (initObj.hasOwnProperty('freshDepth')) {
        this.freshDepth = initObj.freshDepth
      }
      else {
        this.freshDepth = 0.0;
      }
      if (initObj.hasOwnProperty('saltDepth')) {
        this.saltDepth = initObj.saltDepth
      }
      else {
        this.saltDepth = 0.0;
      }
      if (initObj.hasOwnProperty('altitude')) {
        this.altitude = initObj.altitude
      }
      else {
        this.altitude = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ms5837
    // Serialize message field [psr_atm]
    bufferOffset = _serializer.float32(obj.psr_atm, buffer, bufferOffset);
    // Serialize message field [psr_Torr]
    bufferOffset = _serializer.float32(obj.psr_Torr, buffer, bufferOffset);
    // Serialize message field [psr_psi]
    bufferOffset = _serializer.float32(obj.psr_psi, buffer, bufferOffset);
    // Serialize message field [temp_C]
    bufferOffset = _serializer.float32(obj.temp_C, buffer, bufferOffset);
    // Serialize message field [temp_F]
    bufferOffset = _serializer.float32(obj.temp_F, buffer, bufferOffset);
    // Serialize message field [temp_K]
    bufferOffset = _serializer.float32(obj.temp_K, buffer, bufferOffset);
    // Serialize message field [freshDepth]
    bufferOffset = _serializer.float32(obj.freshDepth, buffer, bufferOffset);
    // Serialize message field [saltDepth]
    bufferOffset = _serializer.float32(obj.saltDepth, buffer, bufferOffset);
    // Serialize message field [altitude]
    bufferOffset = _serializer.float32(obj.altitude, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ms5837
    let len;
    let data = new ms5837(null);
    // Deserialize message field [psr_atm]
    data.psr_atm = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [psr_Torr]
    data.psr_Torr = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [psr_psi]
    data.psr_psi = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [temp_C]
    data.temp_C = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [temp_F]
    data.temp_F = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [temp_K]
    data.temp_K = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [freshDepth]
    data.freshDepth = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [saltDepth]
    data.saltDepth = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [altitude]
    data.altitude = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 36;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sensor/ms5837';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b7b0b58529fcdad3a20813b27c552e2d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # define deep sensor MS5837_30B message format
    # Pressure
    float32 psr_atm
    float32 psr_Torr
    float32 psr_psi
    # temperature
    float32 temp_C
    float32 temp_F
    float32 temp_K
    # depth
    float32 freshDepth
    float32 saltDepth
    # altitude
    float32 altitude
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ms5837(null);
    if (msg.psr_atm !== undefined) {
      resolved.psr_atm = msg.psr_atm;
    }
    else {
      resolved.psr_atm = 0.0
    }

    if (msg.psr_Torr !== undefined) {
      resolved.psr_Torr = msg.psr_Torr;
    }
    else {
      resolved.psr_Torr = 0.0
    }

    if (msg.psr_psi !== undefined) {
      resolved.psr_psi = msg.psr_psi;
    }
    else {
      resolved.psr_psi = 0.0
    }

    if (msg.temp_C !== undefined) {
      resolved.temp_C = msg.temp_C;
    }
    else {
      resolved.temp_C = 0.0
    }

    if (msg.temp_F !== undefined) {
      resolved.temp_F = msg.temp_F;
    }
    else {
      resolved.temp_F = 0.0
    }

    if (msg.temp_K !== undefined) {
      resolved.temp_K = msg.temp_K;
    }
    else {
      resolved.temp_K = 0.0
    }

    if (msg.freshDepth !== undefined) {
      resolved.freshDepth = msg.freshDepth;
    }
    else {
      resolved.freshDepth = 0.0
    }

    if (msg.saltDepth !== undefined) {
      resolved.saltDepth = msg.saltDepth;
    }
    else {
      resolved.saltDepth = 0.0
    }

    if (msg.altitude !== undefined) {
      resolved.altitude = msg.altitude;
    }
    else {
      resolved.altitude = 0.0
    }

    return resolved;
    }
};

module.exports = ms5837;
