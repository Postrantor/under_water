// Auto-generated. Do not edit!

// (in-package copley.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let motors_msg = require('./motors_msg.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class ucr_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.current = null;
      this.velocity = null;
      this.position = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('current')) {
        this.current = initObj.current
      }
      else {
        this.current = new motors_msg();
      }
      if (initObj.hasOwnProperty('velocity')) {
        this.velocity = initObj.velocity
      }
      else {
        this.velocity = new motors_msg();
      }
      if (initObj.hasOwnProperty('position')) {
        this.position = initObj.position
      }
      else {
        this.position = new motors_msg();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ucr_msg
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [current]
    bufferOffset = motors_msg.serialize(obj.current, buffer, bufferOffset);
    // Serialize message field [velocity]
    bufferOffset = motors_msg.serialize(obj.velocity, buffer, bufferOffset);
    // Serialize message field [position]
    bufferOffset = motors_msg.serialize(obj.position, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ucr_msg
    let len;
    let data = new ucr_msg(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [current]
    data.current = motors_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [velocity]
    data.velocity = motors_msg.deserialize(buffer, bufferOffset);
    // Deserialize message field [position]
    data.position = motors_msg.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 72;
  }

  static datatype() {
    // Returns string type for a message object
    return 'copley/ucr_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '697cf9df9ce516a16d261952c472d294';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # -*- coding:utf-8 -*-
    # $ catkin_make -DCATKIN_WHITELIST_PACKAGES="copley"
    
    # Header
    Header header
    # Drive
    copley/motors_msg current
    copley/motors_msg velocity
    copley/motors_msg position
    
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
    MSG: copley/motors_msg
    # -*- coding:utf-8 -*-
    # $ catkin_make -DCATKIN_WHITELIST_PACKAGES="copley"
    
    copley/motor_msg drive
    copley/motor_msg wing
    copley/motor_msg sting
    ================================================================================
    MSG: copley/motor_msg
    # -*- coding:utf-8 -*-
    # $ catkin_make -DCATKIN_WHITELIST_PACKAGES="copley"
    
    # Control
    float32 motor_l
    float32 motor_r
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ucr_msg(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.current !== undefined) {
      resolved.current = motors_msg.Resolve(msg.current)
    }
    else {
      resolved.current = new motors_msg()
    }

    if (msg.velocity !== undefined) {
      resolved.velocity = motors_msg.Resolve(msg.velocity)
    }
    else {
      resolved.velocity = new motors_msg()
    }

    if (msg.position !== undefined) {
      resolved.position = motors_msg.Resolve(msg.position)
    }
    else {
      resolved.position = new motors_msg()
    }

    return resolved;
    }
};

module.exports = ucr_msg;
