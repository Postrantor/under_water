
"use strict";

let motor_msg = require('./motor_msg.js');
let joy2switch_msg = require('./joy2switch_msg.js');
let cmd2drive_msg = require('./cmd2drive_msg.js');
let motors_msg = require('./motors_msg.js');
let cmd2switch_msg = require('./cmd2switch_msg.js');
let ucr_msg = require('./ucr_msg.js');
let cmd2start_msg = require('./cmd2start_msg.js');
let joy2start_msg = require('./joy2start_msg.js');

module.exports = {
  motor_msg: motor_msg,
  joy2switch_msg: joy2switch_msg,
  cmd2drive_msg: cmd2drive_msg,
  motors_msg: motors_msg,
  cmd2switch_msg: cmd2switch_msg,
  ucr_msg: ucr_msg,
  cmd2start_msg: cmd2start_msg,
  joy2start_msg: joy2start_msg,
};
