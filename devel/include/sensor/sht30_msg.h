// Generated by gencpp from file sensor/sht30_msg.msg
// DO NOT EDIT!


#ifndef SENSOR_MESSAGE_SHT30_MSG_H
#define SENSOR_MESSAGE_SHT30_MSG_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace sensor
{
template <class ContainerAllocator>
struct sht30_msg_
{
  typedef sht30_msg_<ContainerAllocator> Type;

  sht30_msg_()
    : header()
    , temperature(0.0)
    , humidity(0.0)  {
    }
  sht30_msg_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , temperature(0.0)
    , humidity(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef float _temperature_type;
  _temperature_type temperature;

   typedef float _humidity_type;
  _humidity_type humidity;





  typedef boost::shared_ptr< ::sensor::sht30_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sensor::sht30_msg_<ContainerAllocator> const> ConstPtr;

}; // struct sht30_msg_

typedef ::sensor::sht30_msg_<std::allocator<void> > sht30_msg;

typedef boost::shared_ptr< ::sensor::sht30_msg > sht30_msgPtr;
typedef boost::shared_ptr< ::sensor::sht30_msg const> sht30_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sensor::sht30_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sensor::sht30_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sensor::sht30_msg_<ContainerAllocator1> & lhs, const ::sensor::sht30_msg_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.temperature == rhs.temperature &&
    lhs.humidity == rhs.humidity;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sensor::sht30_msg_<ContainerAllocator1> & lhs, const ::sensor::sht30_msg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sensor

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::sensor::sht30_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sensor::sht30_msg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sensor::sht30_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sensor::sht30_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sensor::sht30_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sensor::sht30_msg_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sensor::sht30_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "894330594d2fa263a3df4bb6c44bb2ed";
  }

  static const char* value(const ::sensor::sht30_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x894330594d2fa263ULL;
  static const uint64_t static_value2 = 0xa3df4bb6c44bb2edULL;
};

template<class ContainerAllocator>
struct DataType< ::sensor::sht30_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sensor/sht30_msg";
  }

  static const char* value(const ::sensor::sht30_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sensor::sht30_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# defain environment sensor sht30 message format\n"
"# Header\n"
"Header header\n"
"# temperature\n"
"float32 temperature\n"
"# humidity\n"
"float32 humidity\n"
"\n"
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

  static const char* value(const ::sensor::sht30_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sensor::sht30_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.temperature);
      stream.next(m.humidity);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct sht30_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sensor::sht30_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sensor::sht30_msg_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "temperature: ";
    Printer<float>::stream(s, indent + "  ", v.temperature);
    s << indent << "humidity: ";
    Printer<float>::stream(s, indent + "  ", v.humidity);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SENSOR_MESSAGE_SHT30_MSG_H
