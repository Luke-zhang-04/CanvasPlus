"""Defines methods for placing widgets on the canvas."""
"""Luke-zhang-04
CanvasPlus (https://github.com/Luke-zhang-04/CanvasPlus)
Copyright (C) 2020 Luke Zhang
"""
# tkinter
from tkinter import (
    Button,
    Checkbutton,
    Entry,
    Frame,
    Label,
    LabelFrame,
    Listbox,
    PanedWindow,
    Radiobutton,
    Scale,
    Scrollbar,
    Spinbox,
)

# typing
from typing import Tuple
from numbers import Real


class WidgetWindows:
    """Class for createing widgets as windows within the canvas."""

    windowProperties = ["anchor", "height", "state", "tags", "width", "window"]

    def _create_widget(self, x, y, widget, **kwargs):
        """internal function: creates widget of widget type and puts it onto the canvas."""
        widgetKwargs = {}
        windowKwargs = {}
        for key, val in kwargs.items():
            if key in self.windowProperties:
                windowKwargs[key] = val
            else:
                widgetKwargs[key] = val

        newWidget = widget(self, **widgetKwargs)
        if "window" not in windowKwargs:
            windowKwargs["window"] = newWidget
        return self.create_window(x, y, **windowKwargs), newWidget

    def create_button(self, x: Real, y: Real, **kwargs) -> Tuple[int, Button]:
        """create button with cordinates x y.

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Button widget while "anchor" will be allocated to the window creation
        """
        return self._create_widget(x, y, Button, **kwargs)

    def create_checkbutton(self, x: Real, y: Real, **kwargs) -> Tuple[int, Checkbutton]:
        """create checkbutton with cordinates x y.

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Checkbutton widget while "anchor" will be allocated to the window creation
        """
        return self._create_widget(x, y, Checkbutton, **kwargs)

    def create_entry(self, x: Real, y: Real, **kwargs) -> Tuple[int, Entry]:
        """create text entry box with cordinates x y.

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Entry widget while "anchor" will be allocated to the window creation
        """
        return self._create_widget(x, y, Entry, **kwargs)

    def create_frame(self, x: Real, y: Real, **kwargs) -> Tuple[int, Frame]:
        """create frame with cordinates x y.

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Frame widget while "anchor" will be allocated to the window creation
        """
        return self._create_widget(x, y, Frame, **kwargs)

    def create_label(self, x: Real, y: Real, **kwargs) -> Tuple[int, Label]:
        """create label with cordinates x y.

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Label widget while "anchor" will be allocated to the window creation
        """
        return self._create_widget(x, y, Label, **kwargs)

    def create_labelframe(self, x: Real, y: Real, **kwargs) -> Tuple[int, LabelFrame]:
        """create label with cordinates x y.

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the LabelFrame widget while "anchor" will be allocated to the window creation
        """
        return self._create_widget(x, y, LabelFrame, **kwargs)

    def create_listbox(self, x: Real, y: Real, **kwargs) -> Tuple[int, Listbox]:
        """create listbox with cordinates x y.

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Listbox widget while "anchor" will be allocated to the window creation
        """
        return self._create_widget(x, y, Listbox, **kwargs)

    def create_panedwindow(self, x: Real, y: Real, **kwargs) -> Tuple[int, PanedWindow]:
        """create panned window with cordinates x y.

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the PanedWindow widget while "anchor" will be allocated to the window creation
        """
        return self._create_widget(x, y, PanedWindow, **kwargs)

    def create_radiobutton(self, x: Real, y: Real, **kwargs) -> Tuple[int, Radiobutton]:
        """create radiobutton with cordinates x y.

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Radiobutton widget while "anchor" will be allocated to the window creation
        """
        return self._create_widget(x, y, Radiobutton, **kwargs)

    def create_scale(self, x: Real, y: Real, **kwargs) -> Tuple[int, Scale]:
        """create scale with cordinates x y.

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Scale widget while "anchor" will be allocated to the window creation
        """
        return self._create_widget(x, y, Scale, **kwargs)

    def create_scrollbar(self, x: Real, y: Real, **kwargs) -> Tuple[int, Scrollbar]:
        """create scrollbar with cordinates x y.

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Scrollbar widget while "anchor" will be allocated to the window creation
        """
        return self._create_widget(x, y, Scrollbar, **kwargs)

    def create_spinbox(self, x: Real, y: Real, **kwargs) -> Tuple[int, Spinbox]:
        """create spinbox with cordinates x y.

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Spinbox widget while "anchor" will be allocated to the window creation
        """
        return self._create_widget(x, y, Spinbox, **kwargs)
