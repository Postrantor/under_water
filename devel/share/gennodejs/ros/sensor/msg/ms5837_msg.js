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

class ms5837_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.psr_mbar = null;
      this.psr_atm = null;
      this.psr_Pa = null;
      this.temp_C = null;
      this.temp_F = null;
      this.temp_K = null;
      this.depth_fresh = null;
      this.depth_salt = null;
      this.altitude = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('psr_mbar')) {
        this.psr_mbar = initObj.psr_mbar
      }
      else {
        this.psr_mbar = 0.0;
      }
      if (initObj.hasOwnProperty('psr_atm')) {
        this.psr_atm = initObj.psr_atm
      }
      else {
        this.psr_atm = 0.0;
      }
      if (initObj.hasOwnProperty('psr_Pa')) {
        this.psr_Pa = initObj.psr_Pa
      }
      else {
        this.psr_Pa = 0.0;
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
      if (initObj.hasOwnProperty('depth_fresh')) {
        this.depth_fresh = initObj.depth_fresh
      }
      else {
        this.depth_fresh = 0.0;
      }
      if (initObj.hasOwnProperty('depth_salt')) {
        this.depth_salt = initObj.depth_salt
      }
      else {
        this.depth_salt = 0.0;
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
    // Serializes a message object of type ms5837_msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [psr_mbar]
    bufferOffset = _serializer.float32(obj.psr_mbar, buffer, bufferOffset);
    // Serialize message field [psr_atm]
    bufferOffset = _serializer.float32(obj.psr_atm, buffer, bufferOffset);
    // Serialize message field [psr_Pa]
    bufferOffset = _serializer.float32(obj.psr_Pa, buffer, bufferOffset);
    // Serialize message field [temp_C]
    bufferOffset = _serializer.float32(obj.temp_C, buffer, bufferOffset);
    // Serialize message field [temp_F]
    bufferOffset = _serializer.float32(obj.temp_F, buffer, bufferOffset);
    // Serialize message field [temp_K]
    bufferOffset = _serializer.float32(obj.temp_K, buffer, bufferOffset);
    // Serialize message field [depth_fresh]
    bufferOffset = _serializer.float32(obj.depth_fresh, buffer, bufferOffset);
    // Serialize message field [depth_salt]
    bufferOffset = _serializer.float32(obj.depth_salt, buffer, bufferOffset);
    // Serialize message field [altitude]
    bufferOffset = _serializer.float32(obj.altitude, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ms5837_msg
    let len;
    let data = new ms5837_msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [psr_mbar]
    data.psr_mbar = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [psr_atm]
    data.psr_atm = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [psr_Pa]
    data.psr_Pa = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [temp_C]
    data.temp_C = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [temp_F]
    data.temp_F = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [temp_K]
    data.temp_K = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [depth_fresh]
    data.depth_fresh = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [depth_salt]
    data.depth_salt = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [altitude]
    data.altitude = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 36;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sensor/ms5837_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2465bb52020c0c434b014d6184497bf3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # define deep sensor MS5837_30B message format
    # Header
    Header header
    # Pressure
    float32 psr_mbar
    float32 psr_atm
    float32 psr_Pa
    # temperature
    float32 temp_C
    float32 temp_F
    float32 temp_K
    # depth
    float32 depth_fresh
    float32 depth_salt
    # altitude
    float32 altitude
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
    const resolved = new ms5837_msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.psr_mbar !== undefined) {
      resolved.psr_mbar = msg.psr_mbar;
    }
    else {
      resolved.psr_mbar = 0.0
    }

    if (msg.psr_atm !== undefined) {
      resolved.psr_atm = msg.psr_atm;
    }
    else {
      resolved.psr_atm = 0.0
    }

    if (msg.psr_Pa !== undefined) {
      resolved.psr_Pa = msg.psr_Pa;
    }
    else {
      resolved.psr_Pa = 0.0
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

    if (msg.depth_fresh !== undefined) {
      resolved.depth_fresh = msg.depth_fresh;
    }
    else {
      resolved.depth_fresh = 0.0
    }

    if (msg.depth_salt !== undefined) {
      resolved.depth_salt = msg.depth_salt;
    }
    else {
      resolved.depth_salt = 0.0
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

module.exports = ms5837_msg;
