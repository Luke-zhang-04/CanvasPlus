"""Defines asynchronus transformations."""
"""Luke-zhang-04
CanvasPlus v1.3.0 (https://github.com/Luke-zhang-04/CanvasPlus)
Copyright (C) 2020 Luke Zhang
"""

from typing import Tuple, Union, List
from numbers import Real
import warnings
import cmath, math

try:
    import asyncio
except ImportError:
    print(
        "Library Asyncio not found. You have four options\n1. use python 3.7 or higher\n2. install asyncio with pip (pip install asyncio)\n3. Download CanvasPlus version 1.2.2 which does not use asyncio, but loose async features\n4. Download the asyncio library from GitHub https://www.google.com/search?client=firefox-b-d&q=asyncio+github"
    )

from CanvasPlus._errors import InvalidUnitError, UnsupportedObjectType


class Error(Exception):
    """Base class for other exceptions."""

    pass


class MorphError(Error):
    """raised when *coords array in async_morph is not the same size as the coords of the original shape."""

    pass


class AsyncTransformations:
    """define asynchronus transformation methods."""

    async def async_morph(
        self,
        tagOrId,
        time: float,
        *coords: List[float],
        fps: int = 24,
        update: bool = True
    ) -> Tuple[Union[float, int]]:
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

    async def async_move(
        self,
        tagOrId: Union[int, str],
        xDist: Real,
        yDist: Real,
        time: float,
        fps: int = 24,
        update: bool = True,
    ) -> Tuple[Union[float, int]]:
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

    async def async_resize(
        self,
        tagOrId: Union[int, str],
        scale: Real,
        x: Real,
        y: Real,
        time: float,
        fps: int = 24,
        update: bool = True,
    ) -> Tuple[Union[float, int]]:
        """Asynchronously resize tagOrId with point x, y and scale.
        
        fps: frames per second, time: specify the amount of time the animation shall take to complete, update: call update() method within loop
        """

        timeIncrement = 1 / fps

        vals = self.coords(tagOrId)
        coords = [(vals[i], vals[i + 1]) for i in range(0, len(vals), 2)]

        if scale < 1:
            scale = 1 - scale

        counter = 0
        while time * fps > counter * timeIncrement * fps:
            counter += 1
            newCoords = []

            if scale < 1:
                for x1, y1 in coords:
                    newCoords.append(x1 + ((x - x1) * scale) / time / fps * counter)
                    newCoords.append(y1 - ((y1 - y) * scale) / time / fps * counter)
            elif scale > 1:
                for x1, y1 in coords:
                    newCoords.append(
                        x1 + ((x1 - x) * (scale - 1)) / time / fps * counter
                    )
                    newCoords.append(
                        y1 - ((y - y1) * (scale - 1)) / time / fps * counter
                    )

            self.coords(tagOrId, *newCoords)

            if update:
                self.tk.call("update")
            await asyncio.sleep(timeIncrement)

    async def async_rotate(
        self,
        tagOrId: Union[int, str],
        x: Real,
        y: Real,
        time: float,
        amount: Real,
        unit: str = "rad",
        warn: bool = True,
        fps: int = 24,
        update: bool = True,
    ) -> Tuple[Union[float, int]]:
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
