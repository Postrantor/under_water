# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ubuntu/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ubuntu/catkin_ws/build

# Utility rule file for copley_generate_messages_cpp.

# Include the progress variables for this target.
include copley/CMakeFiles/copley_generate_messages_cpp.dir/progress.make

copley/CMakeFiles/copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/cmd2start_msg.h
copley/CMakeFiles/copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/motors_msg.h
copley/CMakeFiles/copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/cmd2switch_msg.h
copley/CMakeFiles/copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/ucr_msg.h
copley/CMakeFiles/copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/joy2start_msg.h
copley/CMakeFiles/copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/motor_msg.h
copley/CMakeFiles/copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/cmd2drive_msg.h
copley/CMakeFiles/copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/joy2switch_msg.h


/home/ubuntu/catkin_ws/devel/include/copley/cmd2start_msg.h: /opt/ros/melodic/lib/gencpp/gen_cpp.py
/home/ubuntu/catkin_ws/devel/include/copley/cmd2start_msg.h: /home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg
/home/ubuntu/catkin_ws/devel/include/copley/cmd2start_msg.h: /opt/ros/melodic/share/std_msgs/msg/Header.msg
/home/ubuntu/catkin_ws/devel/include/copley/cmd2start_msg.h: /opt/ros/melodic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ubuntu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating C++ code from copley/cmd2start_msg.msg"
	cd /home/ubuntu/catkin_ws/src/copley && /home/ubuntu/catkin_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/ubuntu/catkin_ws/src/copley/msg/cmd2start_msg.msg -Icopley:/home/ubuntu/catkin_ws/src/copley/msg -Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg -Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg -p copley -o /home/ubuntu/catkin_ws/devel/include/copley -e /opt/ros/melodic/share/gencpp/cmake/..

/home/ubuntu/catkin_ws/devel/include/copley/motors_msg.h: /opt/ros/melodic/lib/gencpp/gen_cpp.py
/home/ubuntu/catkin_ws/devel/include/copley/motors_msg.h: /home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg
/home/ubuntu/catkin_ws/devel/include/copley/motors_msg.h: /home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg
/home/ubuntu/catkin_ws/devel/include/copley/motors_msg.h: /opt/ros/melodic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ubuntu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating C++ code from copley/motors_msg.msg"
	cd /home/ubuntu/catkin_ws/src/copley && /home/ubuntu/catkin_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg -Icopley:/home/ubuntu/catkin_ws/src/copley/msg -Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg -Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg -p copley -o /home/ubuntu/catkin_ws/devel/include/copley -e /opt/ros/melodic/share/gencpp/cmake/..

/home/ubuntu/catkin_ws/devel/include/copley/cmd2switch_msg.h: /opt/ros/melodic/lib/gencpp/gen_cpp.py
/home/ubuntu/catkin_ws/devel/include/copley/cmd2switch_msg.h: /home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg
/home/ubuntu/catkin_ws/devel/include/copley/cmd2switch_msg.h: /home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg
/home/ubuntu/catkin_ws/devel/include/copley/cmd2switch_msg.h: /opt/ros/melodic/share/std_msgs/msg/Header.msg
/home/ubuntu/catkin_ws/devel/include/copley/cmd2switch_msg.h: /opt/ros/melodic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ubuntu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Generating C++ code from copley/cmd2switch_msg.msg"
	cd /home/ubuntu/catkin_ws/src/copley && /home/ubuntu/catkin_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/ubuntu/catkin_ws/src/copley/msg/cmd2switch_msg.msg -Icopley:/home/ubuntu/catkin_ws/src/copley/msg -Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg -Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg -p copley -o /home/ubuntu/catkin_ws/devel/include/copley -e /opt/ros/melodic/share/gencpp/cmake/..

/home/ubuntu/catkin_ws/devel/include/copley/ucr_msg.h: /opt/ros/melodic/lib/gencpp/gen_cpp.py
/home/ubuntu/catkin_ws/devel/include/copley/ucr_msg.h: /home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg
/home/ubuntu/catkin_ws/devel/include/copley/ucr_msg.h: /home/ubuntu/catkin_ws/src/copley/msg/motors_msg.msg
/home/ubuntu/catkin_ws/devel/include/copley/ucr_msg.h: /home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg
/home/ubuntu/catkin_ws/devel/include/copley/ucr_msg.h: /opt/ros/melodic/share/std_msgs/msg/Header.msg
/home/ubuntu/catkin_ws/devel/include/copley/ucr_msg.h: /opt/ros/melodic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ubuntu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Generating C++ code from copley/ucr_msg.msg"
	cd /home/ubuntu/catkin_ws/src/copley && /home/ubuntu/catkin_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/ubuntu/catkin_ws/src/copley/msg/ucr_msg.msg -Icopley:/home/ubuntu/catkin_ws/src/copley/msg -Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg -Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg -p copley -o /home/ubuntu/catkin_ws/devel/include/copley -e /opt/ros/melodic/share/gencpp/cmake/..

/home/ubuntu/catkin_ws/devel/include/copley/joy2start_msg.h: /opt/ros/melodic/lib/gencpp/gen_cpp.py
/home/ubuntu/catkin_ws/devel/include/copley/joy2start_msg.h: /home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg
/home/ubuntu/catkin_ws/devel/include/copley/joy2start_msg.h: /opt/ros/melodic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ubuntu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Generating C++ code from copley/joy2start_msg.msg"
	cd /home/ubuntu/catkin_ws/src/copley && /home/ubuntu/catkin_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/ubuntu/catkin_ws/src/copley/msg/joy2start_msg.msg -Icopley:/home/ubuntu/catkin_ws/src/copley/msg -Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg -Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg -p copley -o /home/ubuntu/catkin_ws/devel/include/copley -e /opt/ros/melodic/share/gencpp/cmake/..

/home/ubuntu/catkin_ws/devel/include/copley/motor_msg.h: /opt/ros/melodic/lib/gencpp/gen_cpp.py
/home/ubuntu/catkin_ws/devel/include/copley/motor_msg.h: /home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg
/home/ubuntu/catkin_ws/devel/include/copley/motor_msg.h: /opt/ros/melodic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ubuntu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Generating C++ code from copley/motor_msg.msg"
	cd /home/ubuntu/catkin_ws/src/copley && /home/ubuntu/catkin_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg -Icopley:/home/ubuntu/catkin_ws/src/copley/msg -Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg -Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg -p copley -o /home/ubuntu/catkin_ws/devel/include/copley -e /opt/ros/melodic/share/gencpp/cmake/..

/home/ubuntu/catkin_ws/devel/include/copley/cmd2drive_msg.h: /opt/ros/melodic/lib/gencpp/gen_cpp.py
/home/ubuntu/catkin_ws/devel/include/copley/cmd2drive_msg.h: /home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg
/home/ubuntu/catkin_ws/devel/include/copley/cmd2drive_msg.h: /home/ubuntu/catkin_ws/src/copley/msg/motor_msg.msg
/home/ubuntu/catkin_ws/devel/include/copley/cmd2drive_msg.h: /opt/ros/melodic/share/std_msgs/msg/Header.msg
/home/ubuntu/catkin_ws/devel/include/copley/cmd2drive_msg.h: /opt/ros/melodic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ubuntu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Generating C++ code from copley/cmd2drive_msg.msg"
	cd /home/ubuntu/catkin_ws/src/copley && /home/ubuntu/catkin_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/ubuntu/catkin_ws/src/copley/msg/cmd2drive_msg.msg -Icopley:/home/ubuntu/catkin_ws/src/copley/msg -Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg -Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg -p copley -o /home/ubuntu/catkin_ws/devel/include/copley -e /opt/ros/melodic/share/gencpp/cmake/..

/home/ubuntu/catkin_ws/devel/include/copley/joy2switch_msg.h: /opt/ros/melodic/lib/gencpp/gen_cpp.py
/home/ubuntu/catkin_ws/devel/include/copley/joy2switch_msg.h: /home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg
/home/ubuntu/catkin_ws/devel/include/copley/joy2switch_msg.h: /opt/ros/melodic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ubuntu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Generating C++ code from copley/joy2switch_msg.msg"
	cd /home/ubuntu/catkin_ws/src/copley && /home/ubuntu/catkin_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/ubuntu/catkin_ws/src/copley/msg/joy2switch_msg.msg -Icopley:/home/ubuntu/catkin_ws/src/copley/msg -Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg -Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg -p copley -o /home/ubuntu/catkin_ws/devel/include/copley -e /opt/ros/melodic/share/gencpp/cmake/..

copley_generate_messages_cpp: copley/CMakeFiles/copley_generate_messages_cpp
copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/cmd2start_msg.h
copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/motors_msg.h
copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/cmd2switch_msg.h
copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/ucr_msg.h
copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/joy2start_msg.h
copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/motor_msg.h
copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/cmd2drive_msg.h
copley_generate_messages_cpp: /home/ubuntu/catkin_ws/devel/include/copley/joy2switch_msg.h
copley_generate_messages_cpp: copley/CMakeFiles/copley_generate_messages_cpp.dir/build.make

.PHONY : copley_generate_messages_cpp

# Rule to build all files generated by this target.
copley/CMakeFiles/copley_generate_messages_cpp.dir/build: copley_generate_messages_cpp

.PHONY : copley/CMakeFiles/copley_generate_messages_cpp.dir/build

copley/CMakeFiles/copley_generate_messages_cpp.dir/clean:
	cd /home/ubuntu/catkin_ws/build/copley && $(CMAKE_COMMAND) -P CMakeFiles/copley_generate_messages_cpp.dir/cmake_clean.cmake
.PHONY : copley/CMakeFiles/copley_generate_messages_cpp.dir/clean

copley/CMakeFiles/copley_generate_messages_cpp.dir/depend:
	cd /home/ubuntu/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/catkin_ws/src /home/ubuntu/catkin_ws/src/copley /home/ubuntu/catkin_ws/build /home/ubuntu/catkin_ws/build/copley /home/ubuntu/catkin_ws/build/copley/CMakeFiles/copley_generate_messages_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : copley/CMakeFiles/copley_generate_messages_cpp.dir/depend

