#tkinter
from tkinter import Canvas

#complex numbers and stuff
import cmath, math

#stuff for typing hints
from numbers import Real

#warnings
import warnings

class Error(Exception):
   '''Base class for other exceptions'''
   pass

class InvalidUnitError(Error):
    '''Raised when unit is not recognised'''
    pass

class UnsupportedObjectType(UserWarning):
    '''raised when object type is not supported'''
    pass

class InvalidObjectType(Error):
    '''raised when object type not supported'''
    pass

class CanvasPlus(Canvas):
    '''Improved Canvas widget with more functionality to display graphical elements like lines or text.'''

    def create_circle(self, x: Real, y: Real, radius: Real, **kwargs) -> int:
        '''Create circle with coordinates x, y, radius'''
        return self._create('oval', [x+radius, y+radius, x-radius, y-radius], kwargs)

    def create_round_rectangle(self, x1: Real, y1: Real, x2: Real, y2: Real, radius: Real = 25, **kwargs) -> int:
        '''Create circle with coordinates x1, y1, x2, y2, radius = val (default 25)'''
        points = [
            x1+radius, y1,
            x1+radius, y1,
            x2-radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y1+radius,
            x2, y2-radius,
            x2, y2-radius,
            x2, y2,
            x2-radius, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1+radius, y2,
            x1, y2, 
            x1, y2-radius, 
            x1, y2-radius, 
            x1, y1+radius,
            x1, y1+radius, 
            x1, y1
        ]

        kwargs["smooth"] = True
        return self._create('polygon', points, kwargs)

    def create_arrow(self, x1: Real, y1: Real, headLength: Real, headWidth: Real, bodyLength: Real, bodyWidth: Real, **kwargs) -> int:
        '''Create arrow with x1, y1 as the tip; headWith, headLengh as the length and width of the arrowhead; and bodyLength, bodyWidth as the length and width of the arrow body, as well as direction = val (0 by default)'''
        
        points = [
            x1, y1,
            x1-headWidth//2, y1+headLength,
            x1-bodyWidth//2, y1+headLength,
            x1-bodyWidth//2, y1+bodyLength,
            x1+bodyWidth//2, y1+bodyLength,
            x1+bodyWidth//2, y1+headLength,
            x1+headWidth//2, y1+headLength
        ]
        
        return self._create('polygon', points, kwargs)

    def to_polygon(self, obj:int) -> int:
        '''converts rectangle to polygon'''
        properties = self.itemconfig(obj)
        output = {
            key: properties[key][-1] for key in properties
        }
        
        cords = [self.tk.getdouble(x) for x in self.tk.splitlist(self.tk.call((self._w, 'coords') + tuple([obj])))]

        if output["width"] == '0.0':
            output["outline"] = ''

        if self.tk.call(self._w, 'type', obj) == "rectangle":
            newCords = [
                cords[0], cords[1],
                cords[1], cords[2],
                cords[2], cords[3],
                cords[3], cords[0]
            ]
        else:
            raise InvalidObjectType("Invalid canvas element \"" + self.tk.call(self._w, 'type', obj) + "\"")

        self.tk.call((self._w, 'delete') + tuple([obj]))

        return self._create('polygon', newCords, output)

    poly = to_polygon

    def rotate(self, obj: int, x: Real, y: Real, amount: Real, unit: str = "rad") -> None:
        '''rotate obj on axis x, y by amount in degrees or radians clockwise'''
        if unit in ("d", "deg", "degree", "degrees"):
            amount *= math.pi/180 #convert to radians
        elif unit in ("r", "rad", "radian", "radians"):
            pass
        else:
            raise InvalidUnitError("Invalid unit \"" + unit + "\"")
        
        angle = cmath.exp(amount*1j)
        offset = complex(x, y)
        newCords = []
        cords = [
            (self.coords(obj)[i], self.coords(obj)[i+1]) for i in range(0, len(self.coords(obj)), 2)
        ]
        for xPt, yPt in cords:
            num = angle * (complex(xPt, yPt) - offset) + offset
            newCords.append(num.real)
            newCords.append(num.imag)
        
        objType = self.tk.call(self._w, 'type', obj)
        if objType == "polygon":
            self.coords(obj, *newCords)
        else:
            warnings.warn("WARNING! Canvas element of type " + objType + " is not supported. Rotation may not look as expected.", UnsupportedObjectType)
            self.coords(obj, *newCords)
        

def _test():
    from tkinter import Tk
    import math

    root = Tk()
    canvas = CanvasPlus(root, width=800, height=800, background = "white")
    canvas.pack()

    canvas.create_circle(300, 300, 100, fill = "black", outline = "green", width = 3)
    
    canvas.create_round_rectangle(400, 400, 500, 500, radius = 75, fill = "blue", outline = "orange", width = 5)

    arrow = canvas.create_arrow(600, 600, 50, 50, 150, 20, fill = "grey", outline = "black")
    canvas.rotate(arrow, 600, 600, 310, unit="deg")

    rect = canvas.create_rectangle(100, 100, 200, 200, fill = "#f7a8c6", width = 0)
    rect = canvas.poly(rect)
    canvas.rotate(rect, 150, 150, math.pi/4)

    canvas.update()
    canvas.mainloop()

if __name__ == "__main__":
    _test()
