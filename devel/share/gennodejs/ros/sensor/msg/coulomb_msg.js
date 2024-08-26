// Auto-generated. Do not edit!

// (in-package sensor.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let watt_msg = require('./watt_msg.js');
let power_msg = require('./power_msg.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class coulomb_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.watt = null;
      this.power = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('watt')) {
        this.watt = initObj.watt
      }
      else {
        this.watt = new watt_msg();
      }
      if (initObj.hasOwnProperty('power')) {
        this.power = initObj.power
      }
      else {
        this.power = new power_msg();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type coulomb_msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [watt]
    bufferOffset = watt_msg.serialize(obj.watt, buffer, bufferOffset);
    // Serialize message field [power]
    bufferOffset = power_msg.serialize(obj.power, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type coulomb_msg
    let len;
    let data = new coulomb_msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [watt]
    data.watt = watt_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [power]
    data.power = power_msg.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 30;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sensor/coulomb_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c5cd7058055ef3a00c048e9d3583364c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # define coulomb sensor XLDN_1602 message format
    # Header
    Header header
    # Watt
    sensor/watt_msg watt
    # Power
    sensor/power_msg power
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
    
    ================================================================================
    MSG: sensor/watt_msg
    # 定义一个4维向量用于传输功率的数据
    float32 voltage
    float32 current
    float32 resistance
    float32 watt
    ================================================================================
    MSG: sensor/power_msg
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
    const resolved = new coulomb_msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.watt !== undefined) {
      resolved.watt = watt_msg.Resolve(msg.watt)
    }
    else {
      resolved.watt = new watt_msg()
    }

    if (msg.power !== undefined) {
      resolved.power = power_msg.Resolve(msg.power)
    }
    else {
      resolved.power = new power_msg()
    }

    return resolved;
    }
};

module.exports = coulomb_msg;
