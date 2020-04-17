class Template:
    """Make templates for repeated display"""

    def __init__(self, *args, type = "", onRender = None, **kwargs):
        """
        Make templates for repeated display
        \nargs:
            x and y coordinates for the placement on render; if not given, the coordinates should be given when rendering the template
        \nkwargs: properties of the shape to be drawn
        """
        self.coords, self.onRender, self.properties, self.type = args, onRender, kwargs, type
    
    def copy(self):
        """returns a copy of the template"""
        return Template(
            *self.coords, shapeType = self.type, onRender = self.onRender, **self.properties
        )