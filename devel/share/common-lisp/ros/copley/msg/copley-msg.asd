
(cl:in-package :asdf)

(defsystem "copley-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "cmd2drive_msg" :depends-on ("_package_cmd2drive_msg"))
    (:file "_package_cmd2drive_msg" :depends-on ("_package"))
    (:file "cmd2start_msg" :depends-on ("_package_cmd2start_msg"))
    (:file "_package_cmd2start_msg" :depends-on ("_package"))
    (:file "cmd2switch_msg" :depends-on ("_package_cmd2switch_msg"))
    (:file "_package_cmd2switch_msg" :depends-on ("_package"))
    (:file "joy2start_msg" :depends-on ("_package_joy2start_msg"))
    (:file "_package_joy2start_msg" :depends-on ("_package"))
    (:file "joy2switch_msg" :depends-on ("_package_joy2switch_msg"))
    (:file "_package_joy2switch_msg" :depends-on ("_package"))
    (:file "motor_msg" :depends-on ("_package_motor_msg"))
    (:file "_package_motor_msg" :depends-on ("_package"))
    (:file "motors_msg" :depends-on ("_package_motors_msg"))
    (:file "_package_motors_msg" :depends-on ("_package"))
    (:file "ucr_msg" :depends-on ("_package_ucr_msg"))
    (:file "_package_ucr_msg" :depends-on ("_package"))
  ))