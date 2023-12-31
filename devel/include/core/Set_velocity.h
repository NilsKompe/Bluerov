// Generated by gencpp from file core/Set_velocity.msg
// DO NOT EDIT!


#ifndef CORE_MESSAGE_SET_VELOCITY_H
#define CORE_MESSAGE_SET_VELOCITY_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace core
{
template <class ContainerAllocator>
struct Set_velocity_
{
  typedef Set_velocity_<ContainerAllocator> Type;

  Set_velocity_()
    : enable_velocity_ctrl(false)
    , pwm_max(0)
    , KP(0)
    , KD(0)  {
    }
  Set_velocity_(const ContainerAllocator& _alloc)
    : enable_velocity_ctrl(false)
    , pwm_max(0)
    , KP(0)
    , KD(0)  {
  (void)_alloc;
    }



   typedef uint8_t _enable_velocity_ctrl_type;
  _enable_velocity_ctrl_type enable_velocity_ctrl;

   typedef uint16_t _pwm_max_type;
  _pwm_max_type pwm_max;

   typedef uint32_t _KP_type;
  _KP_type KP;

   typedef uint32_t _KD_type;
  _KD_type KD;





  typedef boost::shared_ptr< ::core::Set_velocity_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::core::Set_velocity_<ContainerAllocator> const> ConstPtr;

}; // struct Set_velocity_

typedef ::core::Set_velocity_<std::allocator<void> > Set_velocity;

typedef boost::shared_ptr< ::core::Set_velocity > Set_velocityPtr;
typedef boost::shared_ptr< ::core::Set_velocity const> Set_velocityConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::core::Set_velocity_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::core::Set_velocity_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::core::Set_velocity_<ContainerAllocator1> & lhs, const ::core::Set_velocity_<ContainerAllocator2> & rhs)
{
  return lhs.enable_velocity_ctrl == rhs.enable_velocity_ctrl &&
    lhs.pwm_max == rhs.pwm_max &&
    lhs.KP == rhs.KP &&
    lhs.KD == rhs.KD;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::core::Set_velocity_<ContainerAllocator1> & lhs, const ::core::Set_velocity_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace core

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::core::Set_velocity_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::core::Set_velocity_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::core::Set_velocity_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::core::Set_velocity_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::core::Set_velocity_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::core::Set_velocity_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::core::Set_velocity_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c4803dc7cecc9ba43456f9905c6d9e6c";
  }

  static const char* value(const ::core::Set_velocity_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc4803dc7cecc9ba4ULL;
  static const uint64_t static_value2 = 0x3456f9905c6d9e6cULL;
};

template<class ContainerAllocator>
struct DataType< ::core::Set_velocity_<ContainerAllocator> >
{
  static const char* value()
  {
    return "core/Set_velocity";
  }

  static const char* value(const ::core::Set_velocity_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::core::Set_velocity_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool enable_velocity_ctrl\n"
"uint16 pwm_max \n"
"uint32 KP\n"
"uint32 KD\n"
;
  }

  static const char* value(const ::core::Set_velocity_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::core::Set_velocity_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.enable_velocity_ctrl);
      stream.next(m.pwm_max);
      stream.next(m.KP);
      stream.next(m.KD);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Set_velocity_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::core::Set_velocity_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::core::Set_velocity_<ContainerAllocator>& v)
  {
    s << indent << "enable_velocity_ctrl: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.enable_velocity_ctrl);
    s << indent << "pwm_max: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.pwm_max);
    s << indent << "KP: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.KP);
    s << indent << "KD: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.KD);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CORE_MESSAGE_SET_VELOCITY_H
