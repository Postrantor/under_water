// Auto-generated. Do not edit!

// (in-package copley.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class cmd2start_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.rpi_host = null;
      this.copley_motor = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('rpi_host')) {
        this.rpi_host = initObj.rpi_host
      }
      else {
        this.rpi_host = 0;
      }
      if (initObj.hasOwnProperty('copley_motor')) {
        this.copley_motor = initObj.copley_motor
      }
      else {
        this.copley_motor = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type cmd2start_msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [rpi_host]
    bufferOffset = _serializer.int16(obj.rpi_host, buffer, bufferOffset);
    // Serialize message field [copley_motor]
    bufferOffset = _serializer.int16(obj.copley_motor, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type cmd2start_msg
    let len;
    let data = new cmd2start_msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [rpi_host]
    data.rpi_host = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [copley_motor]
    data.copley_motor = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'copley/cmd2start_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '111b1a1fda8851b8a4f1107ff12e3c61';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # $ catkin_make -DCATKIN_WHITELIST_PACKAGES="copley"
    
    # Header
    Header header
    # Start_Joy
    int16 rpi_host
    int16 copley_motor # 采用int变量而不是bool，可能再分出第三种情况，如重启
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
    const resolved = new cmd2start_msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.rpi_host !== undefined) {
      resolved.rpi_host = msg.rpi_host;
    }
    else {
      resolved.rpi_host = 0
    }

    if (msg.copley_motor !== undefined) {
      resolved.copley_motor = msg.copley_motor;
    }
    else {
      resolved.copley_motor = 0
    }

    return resolved;
    }
};

module.exports = cmd2start_msg;
