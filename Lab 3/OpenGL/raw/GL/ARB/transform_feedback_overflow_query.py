'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_transform_feedback_overflow_query'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_transform_feedback_overflow_query',error_checker=_errors._error_checker)
GL_TRANSFORM_FEEDBACK_OVERFLOW_ARB=_C('GL_TRANSFORM_FEEDBACK_OVERFLOW_ARB',0x82EC)
GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW_ARB=_C('GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW_ARB',0x82ED)

