# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "copley: 8 messages, 0 services")

set(MSG_I_FLAGS "-Icopley:/home/ubuntu/catkin_ws/src/copley/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(copley_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg" NAME_WE)
add_custom_target(_copley_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "copley" "/home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg" NAME_WE)
add_custom_target(_copley_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "copley" "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg" "copley/motor_msg"
)

get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg" NAME_WE)
add_custom_target(_copley_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "copley" "/home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg" "copley/motor_msg:std_msgs/Header"
)

get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg" NAME_WE)
add_custom_target(_copley_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "copley" "/home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg" "copley/motors_msg:copley/motor_msg:std_msgs/Header"
)

get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg" NAME_WE)
add_custom_target(_copley_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "copley" "/home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg" ""
)

get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg" NAME_WE)
add_custom_target(_copley_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "copley" "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg" ""
)

get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg" NAME_WE)
add_custom_target(_copley_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "copley" "/home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg" "copley/motor_msg:std_msgs/Header"
)

get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg" NAME_WE)
add_custom_target(_copley_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "copley" "/home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/copley
)
_generate_msg_cpp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/copley
)
_generate_msg_cpp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/copley
)
_generate_msg_cpp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg;/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/copley
)
_generate_msg_cpp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/copley
)
_generate_msg_cpp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/copley
)
_generate_msg_cpp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/copley
)
_generate_msg_cpp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/copley
)

### Generating Services

### Generating Module File
_generate_module_cpp(copley
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/copley
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(copley_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(copley_generate_messages copley_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_cpp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_cpp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_cpp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_cpp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_cpp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_cpp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_cpp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_cpp _copley_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(copley_gencpp)
add_dependencies(copley_gencpp copley_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS copley_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/copley
)
_generate_msg_eus(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/copley
)
_generate_msg_eus(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/copley
)
_generate_msg_eus(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg;/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/copley
)
_generate_msg_eus(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/copley
)
_generate_msg_eus(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/copley
)
_generate_msg_eus(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/copley
)
_generate_msg_eus(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/copley
)

### Generating Services

### Generating Module File
_generate_module_eus(copley
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/copley
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(copley_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(copley_generate_messages copley_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_eus _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_eus _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_eus _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_eus _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_eus _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_eus _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_eus _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_eus _copley_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(copley_geneus)
add_dependencies(copley_geneus copley_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS copley_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/copley
)
_generate_msg_lisp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/copley
)
_generate_msg_lisp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/copley
)
_generate_msg_lisp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg;/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/copley
)
_generate_msg_lisp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/copley
)
_generate_msg_lisp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/copley
)
_generate_msg_lisp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/copley
)
_generate_msg_lisp(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/copley
)

### Generating Services

### Generating Module File
_generate_module_lisp(copley
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/copley
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(copley_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(copley_generate_messages copley_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_lisp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_lisp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_lisp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_lisp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_lisp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_lisp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_lisp _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_lisp _copley_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(copley_genlisp)
add_dependencies(copley_genlisp copley_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS copley_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/copley
)
_generate_msg_nodejs(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/copley
)
_generate_msg_nodejs(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/copley
)
_generate_msg_nodejs(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg;/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/copley
)
_generate_msg_nodejs(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/copley
)
_generate_msg_nodejs(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/copley
)
_generate_msg_nodejs(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/copley
)
_generate_msg_nodejs(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/copley
)

### Generating Services

### Generating Module File
_generate_module_nodejs(copley
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/copley
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(copley_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(copley_generate_messages copley_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_nodejs _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_nodejs _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_nodejs _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_nodejs _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_nodejs _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_nodejs _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_nodejs _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_nodejs _copley_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(copley_gennodejs)
add_dependencies(copley_gennodejs copley_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS copley_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/copley
)
_generate_msg_py(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/copley
)
_generate_msg_py(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/copley
)
_generate_msg_py(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg;/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/copley
)
_generate_msg_py(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/copley
)
_generate_msg_py(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/copley
)
_generate_msg_py(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg"
  "${MSG_I_FLAGS}"
  "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/copley
)
_generate_msg_py(copley
  "/home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/copley
)

### Generating Services

### Generating Module File
_generate_module_py(copley
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/copley
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(copley_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(copley_generate_messages copley_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_py _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_py _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_py _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_py _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_py _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_py _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_py _copley_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg" NAME_WE)
add_dependencies(copley_generate_messages_py _copley_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(copley_genpy)
add_dependencies(copley_genpy copley_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS copley_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/copley)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/copley
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(copley_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(copley_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/copley)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/copley
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(copley_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(copley_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/copley)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/copley
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(copley_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(copley_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/copley)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/copley
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(copley_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(copley_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/copley)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/copley\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/copley
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(copley_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(copley_generate_messages_py geometry_msgs_generate_messages_py)
endif()
