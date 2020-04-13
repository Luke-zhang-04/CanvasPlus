import sys
    
try: from CanvasPlus.canvasplus import CanvasPlus
except:
    print("Your python verision %s is not compatible with canvasplus. For compatibility, another file is being imported." % sys.version)
    from CanvasPlus.pythonBelow35 import CanvasPlus