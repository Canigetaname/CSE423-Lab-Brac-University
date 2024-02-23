'''OpenGL extension OES.viewport_array

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.viewport_array to provide a more 
Python-friendly API

Overview (from the spec)
	
	OpenGL ES is modeled on a pipeline of operations. The final stage in this
	pipeline before rasterization is the viewport transformation. This stage
	transforms vertices from view space into window coordinates and allows the
	application to specify a rectangular region of screen space into which
	OpenGL ES should draw primitives. Unextended OpenGL ES implementations provide a
	single viewport per context. In order to draw primitives into multiple
	viewports, the OpenGL ES viewport may be changed between several draw calls.
	With the advent of Geometry Shaders, it has become possible for an
	application to amplify geometry and produce multiple output primitives
	for each primitive input to the Geometry Shader. It is possible to direct
	these primitives to render into a selected render target. However, all
	render targets share the same, global OpenGL ES viewport.
	
	This extension enhances OpenGL ES by providing a mechanism to expose multiple
	viewports. Each viewport is specified as a rectangle. The destination
	viewport may be selected per-primitive by the geometry shader. This allows
	the Geometry Shader to produce different versions of primitives destined
	for separate viewport rectangles on the same surface. Additionally, when
	combined with multiple framebuffer attachments, it allows a different
	viewport rectangle to be selected for each. This extension also exposes a
	separate scissor rectangle for each viewport. Finally, the viewport bounds
	are now floating point quantities allowing fractional pixel offsets to be
	applied during the viewport transform.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/viewport_array.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.OES.viewport_array import *
from OpenGL.raw.GLES2.OES.viewport_array import _EXTENSION_NAME

def glInitViewportArrayOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glViewportArrayvOES.v size not checked against 'count'
glViewportArrayvOES=wrapper.wrapper(glViewportArrayvOES).setInputArraySize(
    'v', None
)
glViewportIndexedfvOES=wrapper.wrapper(glViewportIndexedfvOES).setInputArraySize(
    'v', 4
)
# INPUT glScissorArrayvOES.v size not checked against 'count'
glScissorArrayvOES=wrapper.wrapper(glScissorArrayvOES).setInputArraySize(
    'v', None
)
glScissorIndexedvOES=wrapper.wrapper(glScissorIndexedvOES).setInputArraySize(
    'v', 4
)
# INPUT glGetFloati_vOES.data size not checked against 'target'
glGetFloati_vOES=wrapper.wrapper(glGetFloati_vOES).setInputArraySize(
    'data', None
)
### END AUTOGENERATED SECTION