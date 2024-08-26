// Auto-generated. Do not edit!

// (in-package sensor.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class bme280_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.chip_id = null;
      this.chip_version = null;
      this.temperature = null;
      this.pressure = null;
      this.humidity = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
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
    // Serializes a message object of type bme280_msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
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
    //deserializes a message object of type bme280_msg
    let len;
    let data = new bme280_msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
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
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 14;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sensor/bme280_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '84b020ec127ee4e3c9286c9437c22c11';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # defain environment sensor bme280 message format
    # Header
    Header header
    # ID
    int8 chip_id
    int8 chip_version
    # temperature
    float32 temperature
    # air pressure
    float32 pressure
    # humidity
    float32 humidity
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new bme280_msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

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

module.exports = bme280_msg;
