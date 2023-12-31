# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from core/State.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class State(genpy.Message):
  _md5sum = "0d689844bfa2e5cd74a8f2a60b1a7770"
  _type = "core/State"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool arm
int16 rc1
int16 rc2
int16 rc3
int16 rc4
int16 rc5
int16 rc6
float64 light
float64 camera
string mode

"""
  __slots__ = ['arm','rc1','rc2','rc3','rc4','rc5','rc6','light','camera','mode']
  _slot_types = ['bool','int16','int16','int16','int16','int16','int16','float64','float64','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       arm,rc1,rc2,rc3,rc4,rc5,rc6,light,camera,mode

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(State, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.arm is None:
        self.arm = False
      if self.rc1 is None:
        self.rc1 = 0
      if self.rc2 is None:
        self.rc2 = 0
      if self.rc3 is None:
        self.rc3 = 0
      if self.rc4 is None:
        self.rc4 = 0
      if self.rc5 is None:
        self.rc5 = 0
      if self.rc6 is None:
        self.rc6 = 0
      if self.light is None:
        self.light = 0.
      if self.camera is None:
        self.camera = 0.
      if self.mode is None:
        self.mode = ''
    else:
      self.arm = False
      self.rc1 = 0
      self.rc2 = 0
      self.rc3 = 0
      self.rc4 = 0
      self.rc5 = 0
      self.rc6 = 0
      self.light = 0.
      self.camera = 0.
      self.mode = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_B6h2d().pack(_x.arm, _x.rc1, _x.rc2, _x.rc3, _x.rc4, _x.rc5, _x.rc6, _x.light, _x.camera))
      _x = self.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 29
      (_x.arm, _x.rc1, _x.rc2, _x.rc3, _x.rc4, _x.rc5, _x.rc6, _x.light, _x.camera,) = _get_struct_B6h2d().unpack(str[start:end])
      self.arm = bool(self.arm)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.mode = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_B6h2d().pack(_x.arm, _x.rc1, _x.rc2, _x.rc3, _x.rc4, _x.rc5, _x.rc6, _x.light, _x.camera))
      _x = self.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 29
      (_x.arm, _x.rc1, _x.rc2, _x.rc3, _x.rc4, _x.rc5, _x.rc6, _x.light, _x.camera,) = _get_struct_B6h2d().unpack(str[start:end])
      self.arm = bool(self.arm)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.mode = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B6h2d = None
def _get_struct_B6h2d():
    global _struct_B6h2d
    if _struct_B6h2d is None:
        _struct_B6h2d = struct.Struct("<B6h2d")
    return _struct_B6h2d
