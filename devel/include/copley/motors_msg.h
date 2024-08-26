// Generated by gencpp from file copley/motors_msg.msg
// DO NOT EDIT!


#ifndef COPLEY_MESSAGE_MOTORS_MSG_H
#define COPLEY_MESSAGE_MOTORS_MSG_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <copley/motor_msg.h>
#include <copley/motor_msg.h>
#include <copley/motor_msg.h>

namespace copley
{
template <class ContainerAllocator>
struct motors_msg_
{
  typedef motors_msg_<ContainerAllocator> Type;

  motors_msg_()
    : drive()
    , wing()
    , sting()  {
    }
  motors_msg_(const ContainerAllocator& _alloc)
    : drive(_alloc)
    , wing(_alloc)
    , sting(_alloc)  {
  (void)_alloc;
    }



   typedef  ::copley::motor_msg_<ContainerAllocator>  _drive_type;
  _drive_type drive;

   typedef  ::copley::motor_msg_<ContainerAllocator>  _wing_type;
  _wing_type wing;

   typedef  ::copley::motor_msg_<ContainerAllocator>  _sting_type;
  _sting_type sting;





  typedef boost::shared_ptr< ::copley::motors_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::copley::motors_msg_<ContainerAllocator> const> ConstPtr;

}; // struct motors_msg_

typedef ::copley::motors_msg_<std::allocator<void> > motors_msg;

typedef boost::shared_ptr< ::copley::motors_msg > motors_msgPtr;
typedef boost::shared_ptr< ::copley::motors_msg const> motors_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::copley::motors_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::copley::motors_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::copley::motors_msg_<ContainerAllocator1> & lhs, const ::copley::motors_msg_<ContainerAllocator2> & rhs)
{
  return lhs.drive == rhs.drive &&
    lhs.wing == rhs.wing &&
    lhs.sting == rhs.sting;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::copley::motors_msg_<ContainerAllocator1> & lhs, const ::copley::motors_msg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace copley

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::copley::motors_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::copley::motors_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::copley::motors_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::copley::motors_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::copley::motors_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::copley::motors_msg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::copley::motors_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e82ee222b0e96a1635070adf737cc004";
  }

  static const char* value(const ::copley::motors_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe82ee222b0e96a16ULL;
  static const uint64_t static_value2 = 0x35070adf737cc004ULL;
};

template<class ContainerAllocator>
struct DataType< ::copley::motors_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "copley/motors_msg";
  }

  static const char* value(const ::copley::motors_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::copley::motors_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# -*- coding:utf-8 -*-\n"
"# $ catkin_make -DCATKIN_WHITELIST_PACKAGES=\"copley\"\n"
"\n"
"copley/motor_msg drive\n"
"copley/motor_msg wing\n"
"copley/motor_msg sting\n"
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

  static const char* value(const ::copley::motors_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::copley::motors_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.drive);
      stream.next(m.wing);
      stream.next(m.sting);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct motors_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::copley::motors_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::copley::motors_msg_<ContainerAllocator>& v)
  {
    s << indent << "drive: ";
    s << std::endl;
    Printer< ::copley::motor_msg_<ContainerAllocator> >::stream(s, indent + "  ", v.drive);
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

#endif // COPLEY_MESSAGE_MOTORS_MSG_H
