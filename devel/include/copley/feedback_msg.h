// Generated by gencpp from file copley/feedback_msg.msg
// DO NOT EDIT!


#ifndef COPLEY_MESSAGE_FEEDBACK_MSG_H
#define COPLEY_MESSAGE_FEEDBACK_MSG_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace copley
{
template <class ContainerAllocator>
struct feedback_msg_
{
  typedef feedback_msg_<ContainerAllocator> Type;

  feedback_msg_()
    : header()
    , motor_drive_left(0.0)
    , motor_drive_right(0.0)
    , motor_wing_left(0.0)
    , motor_wing_right(0.0)
    , motor_sting_left(0.0)
    , motor_sting_right(0.0)  {
    }
  feedback_msg_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , motor_drive_left(0.0)
    , motor_drive_right(0.0)
    , motor_wing_left(0.0)
    , motor_wing_right(0.0)
    , motor_sting_left(0.0)
    , motor_sting_right(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef float _motor_drive_left_type;
  _motor_drive_left_type motor_drive_left;

   typedef float _motor_drive_right_type;
  _motor_drive_right_type motor_drive_right;

   typedef float _motor_wing_left_type;
  _motor_wing_left_type motor_wing_left;

   typedef float _motor_wing_right_type;
  _motor_wing_right_type motor_wing_right;

   typedef float _motor_sting_left_type;
  _motor_sting_left_type motor_sting_left;

   typedef float _motor_sting_right_type;
  _motor_sting_right_type motor_sting_right;





  typedef boost::shared_ptr< ::copley::feedback_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::copley::feedback_msg_<ContainerAllocator> const> ConstPtr;

}; // struct feedback_msg_

typedef ::copley::feedback_msg_<std::allocator<void> > feedback_msg;

typedef boost::shared_ptr< ::copley::feedback_msg > feedback_msgPtr;
typedef boost::shared_ptr< ::copley::feedback_msg const> feedback_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::copley::feedback_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::copley::feedback_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::copley::feedback_msg_<ContainerAllocator1> & lhs, const ::copley::feedback_msg_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.motor_drive_left == rhs.motor_drive_left &&
    lhs.motor_drive_right == rhs.motor_drive_right &&
    lhs.motor_wing_left == rhs.motor_wing_left &&
    lhs.motor_wing_right == rhs.motor_wing_right &&
    lhs.motor_sting_left == rhs.motor_sting_left &&
    lhs.motor_sting_right == rhs.motor_sting_right;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::copley::feedback_msg_<ContainerAllocator1> & lhs, const ::copley::feedback_msg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace copley

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::copley::feedback_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::copley::feedback_msg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::copley::feedback_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::copley::feedback_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::copley::feedback_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::copley::feedback_msg_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::copley::feedback_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "14692d936e10ff6e773f574cec4f6e90";
  }

  static const char* value(const ::copley::feedback_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x14692d936e10ff6eULL;
  static const uint64_t static_value2 = 0x773f574cec4f6e90ULL;
};

template<class ContainerAllocator>
struct DataType< ::copley::feedback_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "copley/feedback_msg";
  }

  static const char* value(const ::copley::feedback_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::copley::feedback_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# -*- coding:utf-8 -*-\n"
"# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"\n"
"# 这个是用来读取多个电机的数据，可以是控制指令或者编码器，都用这一个就行，只要实例化不同的对象就可以\n"
"# 主要是为了方便， 暂时写了六个，不一定都用上，留作扩充，就是个数量问题\n"
"# 另外，编号按照node_id来编排\n"
"\n"
"# Header\n"
"Header header\n"
"# Control\n"
"float32 motor_drive_left\n"
"float32 motor_drive_right\n"
"float32 motor_wing_left\n"
"float32 motor_wing_right\n"
"float32 motor_sting_left\n"
"float32 motor_sting_right\n"
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
;
  }

  static const char* value(const ::copley::feedback_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::copley::feedback_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.motor_drive_left);
      stream.next(m.motor_drive_right);
      stream.next(m.motor_wing_left);
      stream.next(m.motor_wing_right);
      stream.next(m.motor_sting_left);
      stream.next(m.motor_sting_right);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct feedback_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::copley::feedback_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::copley::feedback_msg_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "motor_drive_left: ";
    Printer<float>::stream(s, indent + "  ", v.motor_drive_left);
    s << indent << "motor_drive_right: ";
    Printer<float>::stream(s, indent + "  ", v.motor_drive_right);
    s << indent << "motor_wing_left: ";
    Printer<float>::stream(s, indent + "  ", v.motor_wing_left);
    s << indent << "motor_wing_right: ";
    Printer<float>::stream(s, indent + "  ", v.motor_wing_right);
    s << indent << "motor_sting_left: ";
    Printer<float>::stream(s, indent + "  ", v.motor_sting_left);
    s << indent << "motor_sting_right: ";
    Printer<float>::stream(s, indent + "  ", v.motor_sting_right);
  }
};

} // namespace message_operations
} // namespace ros

#endif // COPLEY_MESSAGE_FEEDBACK_MSG_H
