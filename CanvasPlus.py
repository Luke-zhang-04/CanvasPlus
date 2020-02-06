from tkinter import Canvas

class CanvasPlus(Canvas):
    '''Improved Canvas widget with more functionality to display graphical elements like lines or text.'''

    def create_circle(self, x, y, radius, **kwargs):
        '''Create circle with coordinates x, y, radius'''
        return self.create_oval(x+radius, y+radius, x-radius, y-radius, **kwargs)

    def create_round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        '''Create circle with coordinates x1, y1, x2, y2, radius = var (default 25)'''

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

        return self.create_polygon(*points, smooth=True, **kwargs)


def _test():
    from tkinter import Tk
    root = Tk()
    canvas = CanvasPlus(root, width=800, height=800, background = "white")
    canvas.pack()

    canvas.create_circle(300, 300, 100, fill = "black", outline = "green", width = 3)
    canvas.create_round_rectangle(400, 400, 500, 500, radius = 50, fill = "blue", outline = "orange", width = 5)

    canvas.update()
    canvas.mainloop()

if __name__ == "__main__":
    _test()