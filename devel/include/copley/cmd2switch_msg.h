// Generated by gencpp from file copley/cmd2switch_msg.msg
// DO NOT EDIT!


#ifndef COPLEY_MESSAGE_CMD2SWITCH_MSG_H
#define COPLEY_MESSAGE_CMD2SWITCH_MSG_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <copley/motor_msg.h>
#include <copley/motor_msg.h>

namespace copley
{
template <class ContainerAllocator>
struct cmd2switch_msg_
{
  typedef cmd2switch_msg_<ContainerAllocator> Type;

  cmd2switch_msg_()
    : header()
    , adjust_left(0)
    , adjust_right(0)
    , enc_wing(false)
    , enc_sting(false)
    , wing()
    , sting()  {
    }
  cmd2switch_msg_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , adjust_left(0)
    , adjust_right(0)
    , enc_wing(false)
    , enc_sting(false)
    , wing(_alloc)
    , sting(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int8_t _adjust_left_type;
  _adjust_left_type adjust_left;

   typedef int8_t _adjust_right_type;
  _adjust_right_type adjust_right;

   typedef uint8_t _enc_wing_type;
  _enc_wing_type enc_wing;

   typedef uint8_t _enc_sting_type;
  _enc_sting_type enc_sting;

   typedef  ::copley::motor_msg_<ContainerAllocator>  _wing_type;
  _wing_type wing;

   typedef  ::copley::motor_msg_<ContainerAllocator>  _sting_type;
  _sting_type sting;





  typedef boost::shared_ptr< ::copley::cmd2switch_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::copley::cmd2switch_msg_<ContainerAllocator> const> ConstPtr;

}; // struct cmd2switch_msg_

typedef ::copley::cmd2switch_msg_<std::allocator<void> > cmd2switch_msg;

typedef boost::shared_ptr< ::copley::cmd2switch_msg > cmd2switch_msgPtr;
typedef boost::shared_ptr< ::copley::cmd2switch_msg const> cmd2switch_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::copley::cmd2switch_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::copley::cmd2switch_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::copley::cmd2switch_msg_<ContainerAllocator1> & lhs, const ::copley::cmd2switch_msg_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.adjust_left == rhs.adjust_left &&
    lhs.adjust_right == rhs.adjust_right &&
    lhs.enc_wing == rhs.enc_wing &&
    lhs.enc_sting == rhs.enc_sting &&
    lhs.wing == rhs.wing &&
    lhs.sting == rhs.sting;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::copley::cmd2switch_msg_<ContainerAllocator1> & lhs, const ::copley::cmd2switch_msg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace copley

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::copley::cmd2switch_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::copley::cmd2switch_msg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::copley::cmd2switch_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::copley::cmd2switch_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::copley::cmd2switch_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::copley::cmd2switch_msg_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::copley::cmd2switch_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "19a90ae0a917ebed802b29fa446ac872";
  }

  static const char* value(const ::copley::cmd2switch_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x19a90ae0a917ebedULL;
  static const uint64_t static_value2 = 0x802b29fa446ac872ULL;
};

template<class ContainerAllocator>
struct DataType< ::copley::cmd2switch_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "copley/cmd2switch_msg";
  }

  static const char* value(const ::copley::cmd2switch_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::copley::cmd2switch_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# -*- coding:utf-8 -*-\n"
"# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"\n"
"# 用于控制钩刺机构和推拉机构的运动\n"
"# Header\n"
"Header header\n"
"# Switch\n"
"int8 adjust_left\n"
"int8 adjust_right\n"
"bool enc_wing\n"
"bool enc_sting\n"
"copley/motor_msg wing\n"
"copley/motor_msg sting\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: copley/motor_msg\n"
"# -*- coding:utf-8 -*-\n"
"# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"\n"
"\n"
"# Control\n"
"float32 motor_l\n"
"float32 motor_r\n"
;
  }

  static const char* value(const ::copley::cmd2switch_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::copley::cmd2switch_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.adjust_left);
      stream.next(m.adjust_right);
      stream.next(m.enc_wing);
      stream.next(m.enc_sting);
      stream.next(m.wing);
      stream.next(m.sting);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct cmd2switch_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::copley::cmd2switch_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::copley::cmd2switch_msg_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "adjust_left: ";
    Printer<int8_t>::stream(s, indent + "  ", v.adjust_left);
    s << indent << "adjust_right: ";
    Printer<int8_t>::stream(s, indent + "  ", v.adjust_right);
    s << indent << "enc_wing: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.enc_wing);
    s << indent << "enc_sting: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.enc_sting);
    s << indent << "wing: ";
    s << std::endl;
    Printer< ::copley::motor_msg_<ContainerAllocator> >::stream(s, indent + "  ", v.wing);
    s << indent << "sting: ";
    s << std::endl;
    Printer< ::copley::motor_msg_<ContainerAllocator> >::stream(s, indent + "  ", v.sting);
  }
};

} // namespace message_operations
} // namespace ros

#endif // COPLEY_MESSAGE_CMD2SWITCH_MSG_H
