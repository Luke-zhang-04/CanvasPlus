'''
Canvas Plus v1.1.0 (https://github.com/Luke-zhang-04/CanvasPlus)
Licensed under GPL-3.0 (https://github.com/Luke-zhang-04/CanvasPlus/blob/master/LICENSE)
'''

#tkinter
from tkinter import (
    Canvas, Button, Checkbutton, Entry, Frame, Label, LabelFrame, Listbox,
    Menu, PanedWindow, Radiobutton, Scale, Scrollbar, Spinbox, Text, Toplevel
)

#complex numbers and stuff
import cmath, math

#stuff for typing hints
from numbers import Real

#typing
from typing import Tuple

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

class WidgetWindows:
    '''Class for createing widgets as windows within the canvas'''

    windowProperties = ["anchor", "height", "state", "tags", "width", "window"]

    def _create_widget(self, x, y, widget, **kwargs):
        '''internal function: creates widget of widget type and puts it onto the canvas'''
        widgetKwargs = {}
        windowKwargs = {}
        for key, val in kwargs.items():
            if key in self.windowProperties:
                windowKwargs[key] = val
            else:
                widgetKwargs[key] = val

        newWidget = widget(self, **widgetKwargs)
        if "window" not in windowKwargs: windowKwargs["window"] = newWidget
        return self.create_window(x, y, **windowKwargs), newWidget
    
    def create_button(self, x: Real, y: Real, **kwargs) -> Tuple[int, Button]:
        '''
        create button with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Button widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Button, **kwargs)
        
    def create_checkbutton(self, x: Real, y: Real, **kwargs) -> Tuple[int, Checkbutton]:
        '''
        create checkbutton with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Checkbutton widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Checkbutton, **kwargs)

    def create_entry(self, x: Real, y: Real, **kwargs) -> Tuple[int, Entry]:
        '''
        create text entry box with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Entry widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Entry, **kwargs)
    
    def create_frame(self, x: Real, y: Real, **kwargs) -> Tuple[int, Frame]:
        '''
        create frame with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Frame widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Button, **kwargs)

    def create_label(self, x: Real, y: Real, **kwargs) -> Tuple[int, Label]:
        '''
        create label with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Label widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Label, **kwargs)

    def create_labelframe(self, x: Real, y: Real, **kwargs) -> Tuple[int, LabelFrame]:
        '''
        create label with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the LabelFrame widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, LabelFrame, **kwargs)

    def create_listbox(self, x: Real, y: Real, **kwargs) -> Tuple[int, Listbox]:
        '''
        create listbox with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Listbox widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Listbox, **kwargs)

    def create_menu(self, x: Real, y: Real, **kwargs) -> Tuple[int, Menu]:
        '''
        create menu with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Menu widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Menu, **kwargs)

    def create_pannedwindow(self, x: Real, y: Real, **kwargs) -> Tuple[int, PanedWindow]:
        '''
        create panned window with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the PanedWindow widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, PanedWindow, **kwargs)

    def create_radiobutton(self, x: Real, y: Real, **kwargs) -> Tuple[int, Radiobutton]:
        '''
        create radiobutton with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Radiobutton widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Radiobutton, **kwargs)
    
    def create_scale(self, x: Real, y: Real, **kwargs) -> Tuple[int, Scale]:
        '''
        create scale with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Scale widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Scale, **kwargs)
    
    def create_scale(self, x: Real, y: Real, **kwargs) -> Tuple[int, Scrollbar]:
        '''
        create scrollbar with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Scrollbar widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Scrollbar, **kwargs)

    def create_spinbox(self, x: Real, y: Real, **kwargs) -> Tuple[int, Spinbox]:
        '''
        create spinbox with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Spinbox widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Spinbox, **kwargs)

    def create_text_widget(self, x: Real, y: Real, **kwargs) -> Tuple[int, Text]:
        '''
        create text with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Text widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Text, **kwargs)

    def create_toplevel(self, x: Real, y: Real, **kwargs) -> Tuple[int, Toplevel]:
        '''
        create toplevel with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Toplevel widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Toplevel, **kwargs)


class CanvasPlus(Canvas, WidgetWindows):
    '''Improved Canvas widget with more functionality to display graphical elements like lines or text.'''

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

    def create_circle(self, x: Real, y: Real, radius: Real, **kwargs) -> int:
        '''Create circle with coordinates x, y, radius'''
        return self._create('oval', [x+radius, y+radius, x-radius, y-radius], kwargs)

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

def _test():
    from tkinter import Tk, StringVar
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

    strVar = StringVar()
    canvas.create_entry(0, 0, anchor = "nw", textvariable=strVar)
    strVar.set("a default value")

    canvas.update()
    canvas.mainloop()

if __name__ == "__main__":
    _test()

'''
Canvas Plus v1.0.1 (https://github.com/Luke-zhang-04/CanvasPlus)
Licensed under GPL-3.0 (https://github.com/Luke-zhang-04/CanvasPlus/blob/master/LICENSE)
'''