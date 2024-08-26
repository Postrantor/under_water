
(cl:in-package :asdf)

(defsystem "sensor-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "bme280_msg" :depends-on ("_package_bme280_msg"))
    (:file "_package_bme280_msg" :depends-on ("_package"))
    (:file "coulomb_msg" :depends-on ("_package_coulomb_msg"))
    (:file "_package_coulomb_msg" :depends-on ("_package"))
    (:file "ms5837_msg" :depends-on ("_package_ms5837_msg"))
    (:file "_package_ms5837_msg" :depends-on ("_package"))
    (:file "pca9685_msg" :depends-on ("_package_pca9685_msg"))
    (:file "_package_pca9685_msg" :depends-on ("_package"))
    (:file "power_msg" :depends-on ("_package_power_msg"))
    (:file "_package_power_msg" :depends-on ("_package"))
    (:file "sht30_msg" :depends-on ("_package_sht30_msg"))
    (:file "_package_sht30_msg" :depends-on ("_package"))
    (:file "watt_msg" :depends-on ("_package_watt_msg"))
    (:file "_package_watt_msg" :depends-on ("_package"))
  ))