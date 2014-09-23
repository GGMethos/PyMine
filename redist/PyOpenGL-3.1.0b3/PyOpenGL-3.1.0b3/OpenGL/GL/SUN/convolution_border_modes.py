'''OpenGL extension SUN.convolution_border_modes

This module customises the behaviour of the 
OpenGL.raw.GL.SUN.convolution_border_modes to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides an additional border mode for the
	EXT_convolution extension.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SUN/convolution_border_modes.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.SUN.convolution_border_modes import *
from OpenGL.raw.GL.SUN.convolution_border_modes import _EXTENSION_NAME

def glInitConvolutionBorderModesSUN():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION