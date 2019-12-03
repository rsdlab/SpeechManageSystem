# Python stubs generated by omniidl from idl/BasicDataType.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "RTC"
#
__name__ = "RTC"
_0_RTC = omniORB.openModule("RTC", r"idl/BasicDataType.idl")
_0_RTC__POA = omniORB.openModule("RTC__POA", r"idl/BasicDataType.idl")


# struct Time
_0_RTC.Time = omniORB.newEmptyClass()
class Time (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/Time:1.0"

    def __init__(self, sec, nsec):
        self.sec = sec
        self.nsec = nsec

_0_RTC.Time = Time
_0_RTC._d_Time  = (omniORB.tcInternal.tv_struct, Time, Time._NP_RepositoryId, "Time", "sec", omniORB.tcInternal.tv_ulong, "nsec", omniORB.tcInternal.tv_ulong)
_0_RTC._tc_Time = omniORB.tcInternal.createTypeCode(_0_RTC._d_Time)
omniORB.registerType(Time._NP_RepositoryId, _0_RTC._d_Time, _0_RTC._tc_Time)
del Time

# struct TimedState
_0_RTC.TimedState = omniORB.newEmptyClass()
class TimedState (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedState:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedState = TimedState
_0_RTC._d_TimedState  = (omniORB.tcInternal.tv_struct, TimedState, TimedState._NP_RepositoryId, "TimedState", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", omniORB.tcInternal.tv_short)
_0_RTC._tc_TimedState = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedState)
omniORB.registerType(TimedState._NP_RepositoryId, _0_RTC._d_TimedState, _0_RTC._tc_TimedState)
del TimedState

# struct TimedShort
_0_RTC.TimedShort = omniORB.newEmptyClass()
class TimedShort (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedShort:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedShort = TimedShort
_0_RTC._d_TimedShort  = (omniORB.tcInternal.tv_struct, TimedShort, TimedShort._NP_RepositoryId, "TimedShort", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", omniORB.tcInternal.tv_short)
_0_RTC._tc_TimedShort = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedShort)
omniORB.registerType(TimedShort._NP_RepositoryId, _0_RTC._d_TimedShort, _0_RTC._tc_TimedShort)
del TimedShort

# struct TimedLong
_0_RTC.TimedLong = omniORB.newEmptyClass()
class TimedLong (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedLong:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedLong = TimedLong
_0_RTC._d_TimedLong  = (omniORB.tcInternal.tv_struct, TimedLong, TimedLong._NP_RepositoryId, "TimedLong", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", omniORB.tcInternal.tv_long)
_0_RTC._tc_TimedLong = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedLong)
omniORB.registerType(TimedLong._NP_RepositoryId, _0_RTC._d_TimedLong, _0_RTC._tc_TimedLong)
del TimedLong

# struct TimedUShort
_0_RTC.TimedUShort = omniORB.newEmptyClass()
class TimedUShort (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedUShort:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedUShort = TimedUShort
_0_RTC._d_TimedUShort  = (omniORB.tcInternal.tv_struct, TimedUShort, TimedUShort._NP_RepositoryId, "TimedUShort", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", omniORB.tcInternal.tv_ushort)
_0_RTC._tc_TimedUShort = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedUShort)
omniORB.registerType(TimedUShort._NP_RepositoryId, _0_RTC._d_TimedUShort, _0_RTC._tc_TimedUShort)
del TimedUShort

# struct TimedULong
_0_RTC.TimedULong = omniORB.newEmptyClass()
class TimedULong (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedULong:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedULong = TimedULong
_0_RTC._d_TimedULong  = (omniORB.tcInternal.tv_struct, TimedULong, TimedULong._NP_RepositoryId, "TimedULong", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", omniORB.tcInternal.tv_ulong)
_0_RTC._tc_TimedULong = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedULong)
omniORB.registerType(TimedULong._NP_RepositoryId, _0_RTC._d_TimedULong, _0_RTC._tc_TimedULong)
del TimedULong

# struct TimedFloat
_0_RTC.TimedFloat = omniORB.newEmptyClass()
class TimedFloat (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedFloat:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedFloat = TimedFloat
_0_RTC._d_TimedFloat  = (omniORB.tcInternal.tv_struct, TimedFloat, TimedFloat._NP_RepositoryId, "TimedFloat", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", omniORB.tcInternal.tv_float)
_0_RTC._tc_TimedFloat = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedFloat)
omniORB.registerType(TimedFloat._NP_RepositoryId, _0_RTC._d_TimedFloat, _0_RTC._tc_TimedFloat)
del TimedFloat

# struct TimedDouble
_0_RTC.TimedDouble = omniORB.newEmptyClass()
class TimedDouble (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedDouble:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedDouble = TimedDouble
_0_RTC._d_TimedDouble  = (omniORB.tcInternal.tv_struct, TimedDouble, TimedDouble._NP_RepositoryId, "TimedDouble", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", omniORB.tcInternal.tv_double)
_0_RTC._tc_TimedDouble = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedDouble)
omniORB.registerType(TimedDouble._NP_RepositoryId, _0_RTC._d_TimedDouble, _0_RTC._tc_TimedDouble)
del TimedDouble

# struct TimedChar
_0_RTC.TimedChar = omniORB.newEmptyClass()
class TimedChar (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedChar:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedChar = TimedChar
_0_RTC._d_TimedChar  = (omniORB.tcInternal.tv_struct, TimedChar, TimedChar._NP_RepositoryId, "TimedChar", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", omniORB.tcInternal.tv_char)
_0_RTC._tc_TimedChar = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedChar)
omniORB.registerType(TimedChar._NP_RepositoryId, _0_RTC._d_TimedChar, _0_RTC._tc_TimedChar)
del TimedChar

# struct TimedWChar
_0_RTC.TimedWChar = omniORB.newEmptyClass()
class TimedWChar (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedWChar:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedWChar = TimedWChar
_0_RTC._d_TimedWChar  = (omniORB.tcInternal.tv_struct, TimedWChar, TimedWChar._NP_RepositoryId, "TimedWChar", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", omniORB.tcInternal.tv_wchar)
_0_RTC._tc_TimedWChar = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedWChar)
omniORB.registerType(TimedWChar._NP_RepositoryId, _0_RTC._d_TimedWChar, _0_RTC._tc_TimedWChar)
del TimedWChar

# struct TimedBoolean
_0_RTC.TimedBoolean = omniORB.newEmptyClass()
class TimedBoolean (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedBoolean:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedBoolean = TimedBoolean
_0_RTC._d_TimedBoolean  = (omniORB.tcInternal.tv_struct, TimedBoolean, TimedBoolean._NP_RepositoryId, "TimedBoolean", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", omniORB.tcInternal.tv_boolean)
_0_RTC._tc_TimedBoolean = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedBoolean)
omniORB.registerType(TimedBoolean._NP_RepositoryId, _0_RTC._d_TimedBoolean, _0_RTC._tc_TimedBoolean)
del TimedBoolean

# struct TimedOctet
_0_RTC.TimedOctet = omniORB.newEmptyClass()
class TimedOctet (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedOctet:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedOctet = TimedOctet
_0_RTC._d_TimedOctet  = (omniORB.tcInternal.tv_struct, TimedOctet, TimedOctet._NP_RepositoryId, "TimedOctet", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", omniORB.tcInternal.tv_octet)
_0_RTC._tc_TimedOctet = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedOctet)
omniORB.registerType(TimedOctet._NP_RepositoryId, _0_RTC._d_TimedOctet, _0_RTC._tc_TimedOctet)
del TimedOctet

# struct TimedString
_0_RTC.TimedString = omniORB.newEmptyClass()
class TimedString (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedString:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedString = TimedString
_0_RTC._d_TimedString  = (omniORB.tcInternal.tv_struct, TimedString, TimedString._NP_RepositoryId, "TimedString", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_string,0))
_0_RTC._tc_TimedString = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedString)
omniORB.registerType(TimedString._NP_RepositoryId, _0_RTC._d_TimedString, _0_RTC._tc_TimedString)
del TimedString

# struct TimedWString
_0_RTC.TimedWString = omniORB.newEmptyClass()
class TimedWString (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedWString:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedWString = TimedWString
_0_RTC._d_TimedWString  = (omniORB.tcInternal.tv_struct, TimedWString, TimedWString._NP_RepositoryId, "TimedWString", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_wstring,0))
_0_RTC._tc_TimedWString = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedWString)
omniORB.registerType(TimedWString._NP_RepositoryId, _0_RTC._d_TimedWString, _0_RTC._tc_TimedWString)
del TimedWString

# struct TimedShortSeq
_0_RTC.TimedShortSeq = omniORB.newEmptyClass()
class TimedShortSeq (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedShortSeq:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedShortSeq = TimedShortSeq
_0_RTC._d_TimedShortSeq  = (omniORB.tcInternal.tv_struct, TimedShortSeq, TimedShortSeq._NP_RepositoryId, "TimedShortSeq", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_short, 0))
_0_RTC._tc_TimedShortSeq = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedShortSeq)
omniORB.registerType(TimedShortSeq._NP_RepositoryId, _0_RTC._d_TimedShortSeq, _0_RTC._tc_TimedShortSeq)
del TimedShortSeq

# struct TimedLongSeq
_0_RTC.TimedLongSeq = omniORB.newEmptyClass()
class TimedLongSeq (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedLongSeq:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedLongSeq = TimedLongSeq
_0_RTC._d_TimedLongSeq  = (omniORB.tcInternal.tv_struct, TimedLongSeq, TimedLongSeq._NP_RepositoryId, "TimedLongSeq", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_long, 0))
_0_RTC._tc_TimedLongSeq = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedLongSeq)
omniORB.registerType(TimedLongSeq._NP_RepositoryId, _0_RTC._d_TimedLongSeq, _0_RTC._tc_TimedLongSeq)
del TimedLongSeq

# struct TimedUShortSeq
_0_RTC.TimedUShortSeq = omniORB.newEmptyClass()
class TimedUShortSeq (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedUShortSeq:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedUShortSeq = TimedUShortSeq
_0_RTC._d_TimedUShortSeq  = (omniORB.tcInternal.tv_struct, TimedUShortSeq, TimedUShortSeq._NP_RepositoryId, "TimedUShortSeq", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_ushort, 0))
_0_RTC._tc_TimedUShortSeq = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedUShortSeq)
omniORB.registerType(TimedUShortSeq._NP_RepositoryId, _0_RTC._d_TimedUShortSeq, _0_RTC._tc_TimedUShortSeq)
del TimedUShortSeq

# struct TimedULongSeq
_0_RTC.TimedULongSeq = omniORB.newEmptyClass()
class TimedULongSeq (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedULongSeq:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedULongSeq = TimedULongSeq
_0_RTC._d_TimedULongSeq  = (omniORB.tcInternal.tv_struct, TimedULongSeq, TimedULongSeq._NP_RepositoryId, "TimedULongSeq", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_ulong, 0))
_0_RTC._tc_TimedULongSeq = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedULongSeq)
omniORB.registerType(TimedULongSeq._NP_RepositoryId, _0_RTC._d_TimedULongSeq, _0_RTC._tc_TimedULongSeq)
del TimedULongSeq

# struct TimedFloatSeq
_0_RTC.TimedFloatSeq = omniORB.newEmptyClass()
class TimedFloatSeq (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedFloatSeq:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedFloatSeq = TimedFloatSeq
_0_RTC._d_TimedFloatSeq  = (omniORB.tcInternal.tv_struct, TimedFloatSeq, TimedFloatSeq._NP_RepositoryId, "TimedFloatSeq", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_float, 0))
_0_RTC._tc_TimedFloatSeq = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedFloatSeq)
omniORB.registerType(TimedFloatSeq._NP_RepositoryId, _0_RTC._d_TimedFloatSeq, _0_RTC._tc_TimedFloatSeq)
del TimedFloatSeq

# struct TimedDoubleSeq
_0_RTC.TimedDoubleSeq = omniORB.newEmptyClass()
class TimedDoubleSeq (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedDoubleSeq:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedDoubleSeq = TimedDoubleSeq
_0_RTC._d_TimedDoubleSeq  = (omniORB.tcInternal.tv_struct, TimedDoubleSeq, TimedDoubleSeq._NP_RepositoryId, "TimedDoubleSeq", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_double, 0))
_0_RTC._tc_TimedDoubleSeq = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedDoubleSeq)
omniORB.registerType(TimedDoubleSeq._NP_RepositoryId, _0_RTC._d_TimedDoubleSeq, _0_RTC._tc_TimedDoubleSeq)
del TimedDoubleSeq

# struct TimedCharSeq
_0_RTC.TimedCharSeq = omniORB.newEmptyClass()
class TimedCharSeq (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedCharSeq:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedCharSeq = TimedCharSeq
_0_RTC._d_TimedCharSeq  = (omniORB.tcInternal.tv_struct, TimedCharSeq, TimedCharSeq._NP_RepositoryId, "TimedCharSeq", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_char, 0))
_0_RTC._tc_TimedCharSeq = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedCharSeq)
omniORB.registerType(TimedCharSeq._NP_RepositoryId, _0_RTC._d_TimedCharSeq, _0_RTC._tc_TimedCharSeq)
del TimedCharSeq

# struct TimedWCharSeq
_0_RTC.TimedWCharSeq = omniORB.newEmptyClass()
class TimedWCharSeq (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedWCharSeq:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedWCharSeq = TimedWCharSeq
_0_RTC._d_TimedWCharSeq  = (omniORB.tcInternal.tv_struct, TimedWCharSeq, TimedWCharSeq._NP_RepositoryId, "TimedWCharSeq", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_wchar, 0))
_0_RTC._tc_TimedWCharSeq = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedWCharSeq)
omniORB.registerType(TimedWCharSeq._NP_RepositoryId, _0_RTC._d_TimedWCharSeq, _0_RTC._tc_TimedWCharSeq)
del TimedWCharSeq

# struct TimedBooleanSeq
_0_RTC.TimedBooleanSeq = omniORB.newEmptyClass()
class TimedBooleanSeq (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedBooleanSeq:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedBooleanSeq = TimedBooleanSeq
_0_RTC._d_TimedBooleanSeq  = (omniORB.tcInternal.tv_struct, TimedBooleanSeq, TimedBooleanSeq._NP_RepositoryId, "TimedBooleanSeq", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_boolean, 0))
_0_RTC._tc_TimedBooleanSeq = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedBooleanSeq)
omniORB.registerType(TimedBooleanSeq._NP_RepositoryId, _0_RTC._d_TimedBooleanSeq, _0_RTC._tc_TimedBooleanSeq)
del TimedBooleanSeq

# struct TimedOctetSeq
_0_RTC.TimedOctetSeq = omniORB.newEmptyClass()
class TimedOctetSeq (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedOctetSeq:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedOctetSeq = TimedOctetSeq
_0_RTC._d_TimedOctetSeq  = (omniORB.tcInternal.tv_struct, TimedOctetSeq, TimedOctetSeq._NP_RepositoryId, "TimedOctetSeq", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_octet, 0))
_0_RTC._tc_TimedOctetSeq = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedOctetSeq)
omniORB.registerType(TimedOctetSeq._NP_RepositoryId, _0_RTC._d_TimedOctetSeq, _0_RTC._tc_TimedOctetSeq)
del TimedOctetSeq

# struct TimedStringSeq
_0_RTC.TimedStringSeq = omniORB.newEmptyClass()
class TimedStringSeq (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedStringSeq:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedStringSeq = TimedStringSeq
_0_RTC._d_TimedStringSeq  = (omniORB.tcInternal.tv_struct, TimedStringSeq, TimedStringSeq._NP_RepositoryId, "TimedStringSeq", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0))
_0_RTC._tc_TimedStringSeq = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedStringSeq)
omniORB.registerType(TimedStringSeq._NP_RepositoryId, _0_RTC._d_TimedStringSeq, _0_RTC._tc_TimedStringSeq)
del TimedStringSeq

# struct TimedWStringSeq
_0_RTC.TimedWStringSeq = omniORB.newEmptyClass()
class TimedWStringSeq (omniORB.StructBase):
    _NP_RepositoryId = "IDL:RTC/TimedWStringSeq:1.0"

    def __init__(self, tm, data):
        self.tm = tm
        self.data = data

_0_RTC.TimedWStringSeq = TimedWStringSeq
_0_RTC._d_TimedWStringSeq  = (omniORB.tcInternal.tv_struct, TimedWStringSeq, TimedWStringSeq._NP_RepositoryId, "TimedWStringSeq", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "data", (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_wstring,0), 0))
_0_RTC._tc_TimedWStringSeq = omniORB.tcInternal.createTypeCode(_0_RTC._d_TimedWStringSeq)
omniORB.registerType(TimedWStringSeq._NP_RepositoryId, _0_RTC._d_TimedWStringSeq, _0_RTC._tc_TimedWStringSeq)
del TimedWStringSeq

#
# End of module "RTC"
#
__name__ = "BasicDataType_idl"

_exported_modules = ( "RTC", )

# The end.
