"""defines errors for canvasplus"""
"""
Luke-zhang-04
CanvasPlus v1.3.0 (https://github.com/Luke-zhang-04/CanvasPlus)
Copyright (C) 2020 Luke Zhang
"""

class Error(Exception):
   """Base class for other exceptions"""
   pass

class InvalidUnitError(Error):
    """Raised when unit is not recognised"""
    pass

class UnsupportedObjectType(UserWarning):
    """raised when object type is not supported"""
    pass

class InvalidObjectType(Error):
    """raised when object type not supported"""
    pass

class InvalidEquation(Error):
    """raised when euqtion of a line is invalid"""
    pass

class MorphError(Error):
    """raised when *coords array in async_morph is not the same size as the coords of the original shape"""
    pass
