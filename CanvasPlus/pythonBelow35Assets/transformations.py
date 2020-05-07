"""Defines methods for transforming canvas objects"""
"""Luke-zhang-04
CanvasPlus (https://github.com/Luke-zhang-04/CanvasPlus)
Copyright (C) 2020 Luke Zhang
"""

import warnings
import math, cmath
from CanvasPlus._errors import InvalidUnitError, InvalidEquation, UnsupportedObjectType


class AnalyticGeometry:
    """perform basic analytic geometry."""

    @staticmethod
    def make_eqn(slope, *pt):
        """gets the parts of an equation."""
        properties = {}
        if slope == None:  # got errors becase 0 evaulates to False
            properties = {"m": None, "x": pt[0]}

        elif slope == 0:
            properties = {"m": 0, "y": pt[1]}

        else:
            properties = {"m": slope, "b": pt[1] - slope * pt[0]}

        return properties

    @staticmethod
    def perpendicular_slope(eqn):
        """gets the perpendicular slope of an equation."""
        if "m" not in eqn or not eqn["m"]:
            if "y" in eqn:
                perpendicular = None
            elif "x" in eqn:
                perpendicular = 0
        else:
            if float(eqn["m"]) == 0:
                perpendicular = None
            else:
                perpendicular = -(1 / float(eqn["m"]))
        return perpendicular

    @staticmethod
    def get_poi(eqn1, eqn2):
        """gets the point of intersection between two lines."""
        poi = ()

        flat = False
        if "x" in eqn1:
            flat = eqn1["m"] in (None, 0) and eqn2["m"] in (None, 0)
        elif "y" in eqn1:
            flat = eqn2["m"] in (None, 0) and eqn1["m"] in (None, 0)

        if flat:
            if "x" in eqn1:
                poi = float(eqn1["x"]), float(eqn2["y"])
            else:
                poi = float(eqn2["x"]), float(eqn1["y"])
        else:
            if "b" not in eqn1:
                eqn1["b"] = 0
            if "b" not in eqn2:
                eqn2["b"] = 0
            x = (float(eqn1["b"]) - float(eqn2["b"])) / (
                float(eqn2["m"]) - float(eqn1["m"])
            )
            y = float(eqn1["m"]) * x + float(eqn1["b"])
            poi = (x, y)

        return poi


class Transformations:
    """define transformation methods."""

    def flip(self, tagOrId, **eqn):
        """flips tagOrId on line eqn. eqn should be either {y: val}, {x: val}, or {m: val, b: val} m being slope and b being y-intercept."""
        if len(eqn) == 0:
            raise InvalidEquation("Empty equation")

        for key, _ in eqn.items():
            if key != "x":
                eqn[key] = float(eqn[key]) * -1

        if "x" in eqn and "m" not in eqn:
            eqn["m"] = None
        elif "y" in eqn and "m" not in eqn:
            eqn["m"] = 0

        all_cords = self.coords(tagOrId)
        cords = [(all_cords[i], all_cords[i + 1]) for i in range(0, len(all_cords), 2)]

        # perpendicular slope
        perSlope = AnalyticGeometry.perpendicular_slope(eqn)

        # perpendicular eqnations
        perEqns = [AnalyticGeometry.make_eqn(perSlope, i[0], -i[1]) for i in cords]

        # Points of intersect
        POIs = [AnalyticGeometry.get_poi(eqn, i) for i in perEqns]

        newPts = []  # new points

        for i, _ in enumerate(POIs):  # get new points
            newPts.append(
                (
                    POIs[i][0] - (cords[i][0] - POIs[i][0]),
                    (-(POIs[i][1]) - cords[i][1]) - POIs[i][1],
                )
            )

        newCords = []
        for i in newPts:
            newCords.append(i[0])
            newCords.append(i[1])

        self.coords(tagOrId, *newCords)
        return newPts

    reflect = flip

    def resize(self, tagOrId, scale, x, y):
        """Resizes tagOrId by scale with point x, y."""
        vals = self.coords(tagOrId)
        coords = [(vals[i], vals[i + 1]) for i in range(0, len(vals), 2)]
        newCoords = []

        if scale < 1:
            for x1, y1 in coords:
                newCoords.append(x1 + (x - x1) * scale)
                newCoords.append(y1 - (y1 - y) * scale)
        elif scale > 1:
            for x1, y1 in coords:
                newCoords.append(x - (x - x1) * scale)
                newCoords.append(y - (y - y1) * scale)

        self.coords(tagOrId, *newCoords)
        return newCoords

    def rotate(self, tagOrId, x, y, amount, unit="rad", warn=True):
        """rotate obj on axis x, y by amount in degrees or radians clockwise."""
        if unit in ("d", "deg", "degree", "degrees"):
            amount *= math.pi / 180  # convert to radians
        elif unit in ("r", "rad", "radian", "radians"):
            pass
        else:
            raise InvalidUnitError('Invalid unit "' + unit + '"')

        angle = cmath.exp(amount * 1j)
        offset = complex(x, y)
        newCords = []
        cords = [
            (self.coords(tagOrId)[i], self.coords(tagOrId)[i + 1])
            for i in range(0, len(self.coords(tagOrId)), 2)
        ]
        for xPt, yPt in cords:
            num = angle * (complex(xPt, yPt) - offset) + offset
            newCords.append(num.real)
            newCords.append(num.imag)

        objType = self.tk.call(self._w, "type", tagOrId)
        if objType == "polygon":
            self.coords(tagOrId, *newCords)
        else:
            if warn:
                warnings.warn(
                    "WARNING! Canvas element of type "
                    + objType
                    + " is not supported. Rotation may not look as expected. "
                    + "Use the to_polygon() method to turn the "
                    + objType
                    + " into a polygon.",
                    UnsupportedObjectType,
                )
            self.coords(tagOrId, *newCords)
        return newCords
