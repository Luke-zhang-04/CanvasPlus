def _test():
    # Imports
    from tkinter import Tk, StringVar
    from CanvasPlus import CanvasPlus, _canvasPlusVersion
    import math  # already imported

    # set up canvas
    root = Tk()
    canvas = CanvasPlus(root, width=800, height=800, background="white")
    canvas.pack()
    # create circle function
    canvas.create_circle(300, 600, 100, fill="black", outline="green", width=3)

    # create rounded rectangle function
    canvas.create_round_rectangle(
        400, 550, 500, 650, radius=75, fill="blue", outline="orange", width=5
    )

    # create arrow function and rotate it to by 310 degrees clockwise
    arrow = canvas.create_arrow(600, 600, 50, 50, 150, 20, fill="grey", outline="black")
    canvas.rotate(arrow, 600, 600, 310, unit="deg")

    # create a rectangle and convert it to a polygon; then rotate it by pi/4 radians (45 degrees)
    rect = canvas.create_rectangle(100, 550, 200, 650, fill="#f7a8c6", width=0)
    canvas.clone(rect)
    rect = canvas.poly(rect)
    canvas.rotate(rect, 150, 600, math.pi / 4)

    # create an entry and set it's default value
    content = StringVar()
    canvas.create_entry(0, 0, anchor="nw", textvariable=content, fg="blue", bg="gold")
    content.set("This is CanvasPlus %s" % _canvasPlusVersion)

    # create button to print the value in the previously cretaed entry
    canvas.create_button(
        5,
        25,
        anchor="nw",
        text="button",
        width=50,
        highlightbackground="red",
        command=lambda e=content: print(e.get()),
    )

    # create checkbutton and toggle it
    _, checkbutton = canvas.create_checkbutton(
        5, 50, anchor="nw", bg="brown", fg="white", text="My Checkbutton"
    )
    checkbutton.toggle()

    # create a label
    canvas.create_label(
        5,
        75,
        font=("Times", "24"),
        fg="black",
        bg="green",
        text="By Luke-zhang-04",
        anchor="nw",
    )

    # flip example
    aPrime = canvas.create_polygon(
        500, 10, 500, 20, 550, 25, 600, 20, 600, 10, fill="yellow", outline="black"
    )
    a = canvas.clone(aPrime)
    canvas.flip(a, m=0.5, b=-200)

    canvas.update()
    canvas.mainloop()


if __name__ == "__main__":
    _test()
