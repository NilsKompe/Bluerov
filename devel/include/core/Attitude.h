// Generated by gencpp from file core/Attitude.msg
// DO NOT EDIT!


#ifndef CORE_MESSAGE_ATTITUDE_H
#define CORE_MESSAGE_ATTITUDE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace core
{
template <class ContainerAllocator>
struct Attitude_
{
  typedef Attitude_<ContainerAllocator> Type;

  Attitude_()
    : header()
    , time_boot_ms(0)
    , roll(0.0)
    , pitch(0.0)
    , yaw(0.0)
    , rollspeed(0.0)
    , pitchspeed(0.0)
    , yawspeed(0.0)  {
    }
  Attitude_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , time_boot_ms(0)
    , roll(0.0)
    , pitch(0.0)
    , yaw(0.0)
    , rollspeed(0.0)
    , pitchspeed(0.0)
    , yawspeed(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint32_t _time_boot_ms_type;
  _time_boot_ms_type time_boot_ms;

   typedef double _roll_type;
  _roll_type roll;

   typedef double _pitch_type;
  _pitch_type pitch;

   typedef double _yaw_type;
  _yaw_type yaw;

   typedef double _rollspeed_type;
  _rollspeed_type rollspeed;

   typedef double _pitchspeed_type;
  _pitchspeed_type pitchspeed;

   typedef double _yawspeed_type;
  _yawspeed_type yawspeed;





  typedef boost::shared_ptr< ::core::Attitude_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::core::Attitude_<ContainerAllocator> const> ConstPtr;

}; // struct Attitude_

typedef ::core::Attitude_<std::allocator<void> > Attitude;

typedef boost::shared_ptr< ::core::Attitude > AttitudePtr;
typedef boost::shared_ptr< ::core::Attitude const> AttitudeConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::core::Attitude_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::core::Attitude_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::core::Attitude_<ContainerAllocator1> & lhs, const ::core::Attitude_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.time_boot_ms == rhs.time_boot_ms &&
    lhs.roll == rhs.roll &&
    lhs.pitch == rhs.pitch &&
    lhs.yaw == rhs.yaw &&
    lhs.rollspeed == rhs.rollspeed &&
    lhs.pitchspeed == rhs.pitchspeed &&
    lhs.yawspeed == rhs.yawspeed;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::core::Attitude_<ContainerAllocator1> & lhs, const ::core::Attitude_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace core

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::core::Attitude_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::core::Attitude_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::core::Attitude_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::core::Attitude_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::core::Attitude_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::core::Attitude_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::core::Attitude_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b9624dfb707d17cb5b1412fbdd4f2b55";
  }

  static const char* value(const ::core::Attitude_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb9624dfb707d17cbULL;
  static const uint64_t static_value2 = 0x5b1412fbdd4f2b55ULL;
};

template<class ContainerAllocator>
struct DataType< ::core::Attitude_<ContainerAllocator> >
{
  static const char* value()
  {
    return "core/Attitude";
  }

  static const char* value(const ::core::Attitude_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::core::Attitude_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"uint32 time_boot_ms\n"
"float64 roll\n"
"float64 pitch\n"
"float64 yaw\n"
"float64 rollspeed\n"
"float64 pitchspeed\n"
"float64 yawspeed\n"
"\n"
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

  static const char* value(const ::core::Attitude_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::core::Attitude_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.time_boot_ms);
      stream.next(m.roll);
      stream.next(m.pitch);
      stream.next(m.yaw);
      stream.next(m.rollspeed);
      stream.next(m.pitchspeed);
      stream.next(m.yawspeed);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Attitude_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::core::Attitude_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::core::Attitude_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "time_boot_ms: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.time_boot_ms);
    s << indent << "roll: ";
    Printer<double>::stream(s, indent + "  ", v.roll);
    s << indent << "pitch: ";
    Printer<double>::stream(s, indent + "  ", v.pitch);
    s << indent << "yaw: ";
    Printer<double>::stream(s, indent + "  ", v.yaw);
    s << indent << "rollspeed: ";
    Printer<double>::stream(s, indent + "  ", v.rollspeed);
    s << indent << "pitchspeed: ";
    Printer<double>::stream(s, indent + "  ", v.pitchspeed);
    s << indent << "yawspeed: ";
    Printer<double>::stream(s, indent + "  ", v.yawspeed);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CORE_MESSAGE_ATTITUDE_H
