<div align="center"><img alt="logo" src="https://user-images.githubusercontent.com/55749227/81359054-1769c500-90a6-11ea-8d52-541de3f3662d.png" /></div>

<p align="center">
    <a href="https://www.python.org/"><img alt="forthebadge made-with-python" src="http://ForTheBadge.com/images/badges/made-with-python.svg"/></a><br/>
    <a href="https://GitHub.com/Luke-zhang-04/CanvasPlus/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/Luke-zhang-04/CanvasPlus?logo=GitHub"/></a>
    <a href="https://pypi.python.org/pypi/canvasplus"><img alt="PyPI version shields.io" src="https://img.shields.io/pypi/v/canvasplus.svg?logo=pypi&logoColor=white"/></a>
    <a href="https://github.com/Luke-zhang-04/CanvasPlus/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/Luke-zhang-04/CanvasPlus"/></a>
    <a href="https://pypi.python.org/pypi/CanvasPlus/"><img alt="PyPI pyversions" src="https://img.shields.io/pypi/pyversions/CanvasPlus.svg?logo=pypi&logoColor=white"/></a>
    <a href="https://github.com/Luke-zhang-04/CanvasPlus/actions?query=workflow%3APython-package"><img alt="Workflow Status" src="https://github.com/luke-zhang-04/CanvasPLus/workflows/Python-package/badge.svg"/></a>
    <a href="https://github.com/Luke-zhang-04/CanvasPlus/actions?query=workflow%3APython-package"><img alt="Workflow Status" src="https://img.shields.io/github/workflow/status/luke-zhang-04/CanvasPlus/Python-package?logo=python&logoColor=blue"/></a><br/>
    <a href="https://github.com/psf/black"><img alt="code style" src="https://img.shields.io/badge/code%20style-black-000000.svg?logo=python&logoColor=black"/></a>
    <a href="https://app.codacy.com/manual/luke.zhang2004/CanvasPlus?utm_source=github.com&utm_medium=referral&utm_content=Luke-zhang-04/CanvasPlus&utm_campaign=Badge_Grade_Dashboard"><img alt="Codacy Badge" src="https://api.codacy.com/project/badge/Grade/37320c28d7e348a3b378756a6da80e62"/></a>
    <a href="https://codeclimate.com/github/Luke-zhang-04/CanvasPlus"><img alt="code maintainability" src="https://img.shields.io/codeclimate/maintainability-percentage/Luke-zhang-04/CanvasPlus?logo=code-climate"/></a>
</p>

An improved Canvas widget for tkinter with more functionality to display graphical elements like lines or text. 

Tkinter's Canvas widget has some limitations which are adressed in this package.

Simmilar to the default tkinter Canvas widget, e.g canvas.create_rectangle, other canvas objects can be created.

## Availability ##
To start, make sure you have CanvasPlus installed or cloned. You can do this with one of two methods.
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
or<br/>
Clone the latest stable Release<br/>
[![GitHub release](https://img.shields.io/github/release/Luke-zhang-04/CanvasPlus)](https://GitHub.com/Luke-zhang-04/CanvasPlus/releases/)<br/>
[![Screen Shot 2020-04-15 at 11 26 54 PM](https://user-images.githubusercontent.com/55749227/79411325-991b7680-7f70-11ea-9415-84e978fb76ca.png)](https://github.com/Luke-zhang-04/CanvasPlus/releases)
## Importing ##
It is advised that you do not import the entire module.
```python
from CanvasPlus import CanvasPlus
CanvasPlus()
```
```python
import CanvasPlus
CanvasPlus.CanvasPlus()
```

## Usage ##
Usage is very simple, especially for those with experience using tkinter canvas.

For complete documentation, head over the [the wiki](https://github.com/Luke-zhang-04/CanvasPlus/wiki)

### Example: ###
```python
#Imports
from CanvasPlus import CanvasPLus
from tkinter import Tk, StringVar, DoubleVar

#set up canvas
root = Tk()
canvas = CanvasPlus(root, width=800, height=800, background = "white")
canvas.pack()
#create circle function
canvas.create_circle(300, 600, 100, fill = "black", outline = "green", width = 3)

#create rounded rectangle function
canvas.create_round_rectangle(
    400, 550, 500, 650, radius = 75, fill = "blue", outline = "orange", width = 5
)   

#create arrow function and rotate it to by 310 degrees clockwise
arrow = canvas.create_arrow(600, 600, 50, 50, 150, 20, fill = "grey", outline = "black")
canvas.rotate(arrow, 600, 600, 310, unit="deg")

#create a rectangle and convert it to a polygon; then rotate it by pi/4 radians (45 degrees)
rect = canvas.create_rectangle(100, 550, 200, 650, fill = "#f7a8c6", width = 0)
canvas.clone(rect)
rect = canvas.poly(rect)
canvas.rotate(rect, 150, 600, math.pi/4)

#create an entry and set it's default value
content = StringVar()
canvas.create_entry(0, 0, anchor = "nw", textvariable = content, fg = "blue", bg = "gold")
content.set("This is CanvasPlus %s" % _canvasPlusVersion)

#create button to print the value in the previously cretaed entry
canvas.create_button(
    5, 25, anchor = "nw", text = "button", width = 50, highlightbackground = "red",
    command = lambda e = content: print(e.get())
)

#create checkbutton and toggle it
_, checkbutton = canvas.create_checkbutton(
    5, 50, anchor = "nw", bg = "brown", fg = "white", text = "My Checkbutton"
)
checkbutton.toggle()

#create a label
canvas.create_label(
    5, 75, font = ("Times", "24"), fg = "black", bg = "green", text = "By Luke-zhang-04", anchor = "nw"
)

#flip example
aPrime = canvas.create_polygon(500, 10, 500, 20, 550, 25, 600, 20, 600, 10, fill = "yellow", outline = "black")
a = canvas.clone(aPrime)
canvas.flip(a, m = .5, b = -200)

canvas.update()
canvas.mainloop()
```

![demo](https://user-images.githubusercontent.com/55749227/81359089-2a7c9500-90a6-11ea-9910-710de0d39e27.png)