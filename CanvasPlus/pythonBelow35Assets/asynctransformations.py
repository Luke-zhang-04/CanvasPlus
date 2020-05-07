"""Defines asynchronus transformations."""
"""Luke-zhang-04
CanvasPlus v1.3.0 (https://github.com/Luke-zhang-04/CanvasPlus)
Copyright (C) 2020 Luke Zhang
"""

import warnings
import cmath, math

try:
    import asyncio
except ImportError:
    print(
        "Library Asyncio not found. You have four options\n1. use python 3.7 or higher\n2. install asyncio with pip (pip install asyncio)\n3. Download CanvasPlus version 1.2.2 which does not use asyncio, but loose async features\n4. Download the asyncio library from GitHub https://www.google.com/search?client=firefox-b-d&q=asyncio+github"
    )

from CanvasPlus._errors import InvalidUnitError, UnsupportedObjectType, MorphError


class AsyncTransformations:
    """define asynchronus transformation methodsscreen.update()"""

    async def async_morph(self, tagOrId, time, *coords, fps=24, update=True):
        """Asynchronously morph tagOrId into *coords.
        fps: frames per second, time: specify the amount of time the animation shall take to complete, update: call update() method within loop
        """
        if len(self.coords(tagOrId)) != len(coords):
            raise MorphError(
                "*coords must be the same length as the coords of the original shape"
            )

        oldCoords = self.coords(tagOrId)

        timeIncrement = 1 / fps

        counter = 0
        while time * fps > counter * timeIncrement * fps:
            counter += 1

            newCoords = []
            for i in range(0, len(oldCoords), 2):
                newCoords.append(
                    oldCoords[i] + (coords[i] - oldCoords[i]) / time / fps * counter
                )
                newCoords.append(
                    oldCoords[i + 1]
                    + (coords[i + 1] - oldCoords[i + 1]) / time / fps * counter
                )

            self.coords(tagOrId, *newCoords)

            if update:
                self.tk.call("update")
            await asyncio.sleep(timeIncrement)

    async def async_move(self, tagOrId, xDist, yDist, time, fps=24, update=True):
        """Asynchronously move tagOrId by xDist and yDist (x distance, y distance).

        fps: frames per second, time: specify the amount of time the animation shall take to complete, update: call update() method within loop
        """
        timeIncrement, moveIncrement = (
            1 / fps,
            (xDist / time / fps, yDist / time / fps),
        )

        counter = 0
        while time * fps > counter * timeIncrement * fps:
            counter += 1

            self.tk.call(
                (self._w, "move") + (tagOrId, moveIncrement[0], moveIncrement[1])
            )

            if update:
                self.tk.call("update")
            await asyncio.sleep(timeIncrement)

    async def async_resize(self, tagOrId, scale, x, y, time, fps=24, update=True):
        """Asynchronously resize tagOrId with point x, y and scale.

        fps: frames per second, time: specify the amount of time the animation shall take to complete, update: call update() method within loop
        """
        scale *= -1
        timeIncrement, moveIncrement = 1 / fps, scale / time / fps

        counter = 0
        while time * fps > counter * timeIncrement * fps:
            counter += 1

            self.resize(tagOrId, moveIncrement, x, y)

            if update:
                self.tk.call("update")
            await asyncio.sleep(timeIncrement)

    async def async_rotate(
        self, tagOrId, x, y, time, amount, unit="rad", warn=True, fps=24, update=True,
    ):
        """Asynchronously rotate tagOrId on axis x, y by amount in degrees or radians clockwise (use negaitves for counter-clockwise).
        
        fps: frames per second, time: specify the amount of time the animation shall take to complete, update: call update() method within loop
        """
        if unit in ("d", "deg", "degree", "degrees"):
            amount *= math.pi / 180  # convert to radians
        elif unit in ("r", "rad", "radian", "radians"):
            pass
        else:
            raise InvalidUnitError('Invalid unit "' + unit + '"')

        if self.tk.call(self._w, "type", tagOrId) != "polygon" and warn:
            warnings.warn(
                "WARNING! Canvas element of type "
                + self.tk.call(self._w, "type", tagOrId)
                + " is not supported. Rotation may not look as expected. "
                + "Use the to_polygon() method to turn the "
                + self.tk.call(self._w, "type", tagOrId)
                + " into a polygon.",
                UnsupportedObjectType,
            )

        timeIncrement, moveIncrement = 1 / fps, amount / time / fps

        counter = 0
        while (
            time * fps > counter * timeIncrement * fps
        ):  # use while loop in case of float
            counter += 1
            self.rotate(tagOrId, x, y, moveIncrement, unit="r", warn=False)

            if update:
                self.tk.call("update")
            await asyncio.sleep(timeIncrement)
