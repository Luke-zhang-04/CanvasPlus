"""The CanvasPlus package, version 1.3.2."""
"""Luke-zhang-04
CanvasPlus (https://github.com/Luke-zhang-04/CanvasPlus)
Copyright (C) 2020 Luke Zhang
Licensed under the MIT License
"""

# This file is compatible with Python 3.5 and above. For python 3.4 and below, use the code in pythonBelow3.5

from tkinter import Canvas
from numbers import Real
from typing import Tuple, Union, List, Callable, Dict

if __name__ != "__main__":
    from CanvasPlus._errors import *
    from CanvasPlus.templates import Template
    from CanvasPlus.assets import WidgetWindows, AsyncTransformations, Transformations
else:
    from _errors import *
    from templates import Template
    from assets import WidgetWindows, AsyncTransformations, Transformations

_canvasPlusVersion = "v1.4.1"

print("This is CanvasPlus %s" % _canvasPlusVersion)


class CanvasPlus(Canvas, WidgetWindows, Transformations, AsyncTransformations):
    """Improved Canvas widget with more functionality to display graphical elements like lines or text."""

    def clone(self, tagOrId: Union[int, str], *args: List[int]) -> int:
        """clones tagOrId and places is at optional coordinates, or places is on top of the first object."""
        if len(args) == 0:
            args = self.coords(tagOrId)

        output = self.get_attributes(tagOrId)

        return self._create(self.tk.call(self._w, "type", tagOrId), args, output)

    def create_arrow(
        self,
        x1: Real,
        y1: Real,
        headLength: Real,
        headWidth: Real,
        bodyLength: Real,
        bodyWidth: Real,
        **kwargs
    ) -> int:
        """Create arrow with x1, y1 as the tip; headWith, headLengh as the length and width of the arrowhead; and bodyLength, bodyWidth as the length and width of the arrow body, as well as direction = val (0 by default)."""

        points = [
            x1,
            y1,
            x1 - headWidth // 2,
            y1 + headLength,
            x1 - bodyWidth // 2,
            y1 + headLength,
            x1 - bodyWidth // 2,
            y1 + bodyLength,
            x1 + bodyWidth // 2,
            y1 + bodyLength,
            x1 + bodyWidth // 2,
            y1 + headLength,
            x1 + headWidth // 2,
            y1 + headLength,
        ]

        return self._create("polygon", points, kwargs)

    def create_circle(self, x: Real, y: Real, radius: Real, **kwargs) -> int:
        """Create circle with coordinates x, y, radius."""
        return self._create(
            "oval", [x + radius, y + radius, x - radius, y - radius], kwargs
        )

    def create_round_rectangle(
        self, x1: Real, y1: Real, x2: Real, y2: Real, radius: Real = 25, **kwargs
    ) -> int:
        """Create circle with coordinates x1, y1, x2, y2, radius = val (default 25)."""
        points = [
            x1 + radius,
            y1,
            x1 + radius,
            y1,
            x2 - radius,
            y1,
            x2 - radius,
            y1,
            x2,
            y1,
            x2,
            y1 + radius,
            x2,
            y1 + radius,
            x2,
            y2 - radius,
            x2,
            y2 - radius,
            x2,
            y2,
            x2 - radius,
            y2,
            x2 - radius,
            y2,
            x1 + radius,
            y2,
            x1 + radius,
            y2,
            x1,
            y2,
            x1,
            y2 - radius,
            x1,
            y2 - radius,
            x1,
            y1 + radius,
            x1,
            y1 + radius,
            x1,
            y1,
        ]

        kwargs["smooth"] = True
        return self._create("polygon", points, kwargs)

    def get_attributes(self, tagOrId: Union[int, str]) -> Dict:
        """Returns all properties of tagOrId."""
        properties = self.itemconfig(tagOrId)
        return {key: properties[key][-1] for key in properties}

    get_attr = get_attributes

    def __iter__(self) -> iter:
        """Creates iterator of everything on the canvas."""
        return iter(self.find_all())

    def to_polygon(self, tagOrId: Union[int, str]) -> int:
        """converts rectangle to polygon."""
        output = self.get_attributes(tagOrId)

        cords = [
            self.tk.getdouble(x)
            for x in self.tk.splitlist(
                self.tk.call((self._w, "coords") + tuple([tagOrId]))
            )
        ]

        if output["width"] == "0.0":
            output["outline"] = ""

        if self.tk.call(self._w, "type", tagOrId) == "rectangle":
            newCords = [
                cords[0],
                cords[1],
                cords[2],
                cords[1],
                cords[2],
                cords[3],
                cords[0],
                cords[3],
            ]
        else:
            raise InvalidObjectType(
                'Invalid canvas element "'
                + self.tk.call(self._w, "type", tagOrId)
                + '"'
            )

        self.tk.call((self._w, "delete") + tuple([tagOrId]))

        return self._create("polygon", newCords, output)

    poly = to_polygon

    def tags_bind(
        self,
        tagsOrIds: Union[int, str, Tuple],
        sequences: Union[str, Tuple] = None,
        funcs=Union[Callable, Tuple],
        add: bool = None,
    ) -> Union[str, List[str]]:
        """Binds either multiple tags to one function, or multiple tags to multiple functions with matching indicies in one function.
        
        i.e (tag1, tag2, tag3), func1 will bind tag1, tag2, tag3 into fun1, while (tag1, tag2, tag3), (func1, func2, func3) will bind tag1 to func1, tag2 to func2, tag3 to func3.
        """
        if type(tagsOrIds) == int and callable(funcs):  # normal tag_bind
            return self._bind((self._w, "bind", tagsOrIds), sequences, funcs, add)
        else:
            bindings = []
            if type(funcs) not in [list, tuple]:
                funcs = tuple([funcs])
            if type(sequences) not in [list, tuple]:
                sequences = tuple([sequences])

            for index, obj in enumerate(tagsOrIds):
                bindings.append(
                    self._bind(
                        (self._w, "bind", obj),
                        sequences[index % len(sequences)],
                        funcs[index % len(funcs)],
                        add,
                    )
                )
            return bindings

    def render_template(self, template: Template, *args, **kwargs):
        """Renders a template from the template class."""
        coords = args if len(template.coords) == 0 else template.coords

        properties = template.properties
        for i in kwargs:
            properties[i] = kwargs[i]

        shape = self._create(template.type, coords, properties)

        if template.onRender:
            template.onRender(shape)

        return shape
