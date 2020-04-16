"""The CanvasPlus package, version 1.3.0-a"""
"""
Luke-zhang-04
CanvasPlus v1.3.0-a (https://github.com/Luke-zhang-04/CanvasPlus)
Copyright (C) 2020 Luke Zhang
"""

try: from CanvasPlus.canvasplus import CanvasPlus
except:
    import sys
    print("Your python version %s is not compatible with the standard canvasplus library. For compatibility, another file is being imported." % sys.version)
    from CanvasPlus.pythonBelow35 import CanvasPlus