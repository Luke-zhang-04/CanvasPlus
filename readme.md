# Canvas Plus #
## V1.1.0 ##
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/CanvasPlus.svg)](https://pypi.python.org/pypi/CanvasPlus/)
[![GitHub release](https://img.shields.io/github/release/Luke-zhang-04/CanvasPlus)](https://GitHub.com/Luke-zhang-04/CanvasPlus/releases/)
[![GitHub license](https://img.shields.io/github/license/Luke-zhang-04/CanvasPlus)](https://github.com/Luke-zhang-04/CanvasPlus/blob/master/LICENSE)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/CanvasPlus.svg)](https://pypi.python.org/pypi/CanvasPlus/)


An improved Canvas widget for tkinter with more functionality to display graphical elements like lines or text. 

Tkinter's Canvas widget has some limitations which are adressed in this package.

Simmilar to the default tkinter Canvas widget, e.g canvas.create_rectangle, other canvas objects can be created.

## Usage ##
Usage is very simple, especially for those with experience using tkinter canvas.

### Example: ###
```python

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
```

![Screen Shot 2020-03-30 at 7 21 45 PM](https://user-images.githubusercontent.com/55749227/77971056-c18e4a00-72bb-11ea-87a7-98bcb56ea037.png)

For more information, head over the [the wiki](https://github.com/Luke-zhang-04/CanvasPlus/wiki)


## Availability ##
### Option 1: Pip ###
Pip install this package
```
pip install CanvasPlus
```
### Option 2: Github ###
Download a zip file containing all files.
```
git clone https://github.com/Luke-zhang-04/CanvasPlus.git
```