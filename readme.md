# Canvas Plus #
Tkinter's Canvas widget has some limitations that I want to try to fix/change with this repository.

Simmilar to the default tkinter Canvas widget, e.g canvas.create_rectangle, other canvas objects can be created. 

## create_circle ##
Canvas.create_circle(x, y, radius, **kwargs)

Creates a circle with the centre x, y, and a radius, rather than create_oval(x1, y1, x2, y2, **kwargs), which can be unintuitive to use in many situations.

## create_round_rectangle ##
Canvas.create_round_rectangle(x1, y1, x2, y2, radius = var, **kwargs)

radius = 25 by default<br>
Creates a rectangle with rounded corners based on radius. Rounded rectangles are hard to make and are useful in many situations.