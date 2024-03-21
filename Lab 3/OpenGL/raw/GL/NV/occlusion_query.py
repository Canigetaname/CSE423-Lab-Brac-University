'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_occlusion_query'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_occlusion_query',error_checker=_errors._error_checker)
GL_CURRENT_OCCLUSION_QUERY_ID_NV=_C('GL_CURRENT_OCCLUSION_QUERY_ID_NV',0x8865)
GL_PIXEL_COUNTER_BITS_NV=_C('GL_PIXEL_COUNTER_BITS_NV',0x8864)
GL_PIXEL_COUNT_AVAILABLE_NV=_C('GL_PIXEL_COUNT_AVAILABLE_NV',0x8867)
GL_PIXEL_COUNT_NV=_C('GL_PIXEL_COUNT_NV',0x8866)
@_f
@_p.types(None,_cs.GLuint)
def glBeginOcclusionQueryNV(id):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteOcclusionQueriesNV(n,ids):pass
@_f
@_p.types(None,)
def glEndOcclusionQueryNV():pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenOcclusionQueriesNV(n,ids):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetOcclusionQueryivNV(id,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetOcclusionQueryuivNV(id,pname,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsOcclusionQueryNV(id):pass