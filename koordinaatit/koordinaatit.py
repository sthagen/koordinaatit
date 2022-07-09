# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""Coordinates API."""
import math
import os
import sys
from enum import Enum, auto
from typing import List, Union

DEBUG_VAR = 'KOORDINAATIT_DEBUG'
DEBUG = os.getenv(DEBUG_VAR)

ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'


class Dimension(Enum):
    LAT = auto()
    LON = auto()
    ALT = auto()


class Unit(Enum):
    DEGREE = auto()
    RADIAN = auto()
    METER = auto()
    FEET = auto()


class Length:
    """Provide conversions between meter and feet.

    Internal representation of unit is meter.
    """

    WUN_METER = 0.3048  # feet

    def __init__(self, value: Union[int, float], unit: Unit):
        self.base_value = value
        self.unit = unit
        if self.unit is not Unit.METER and self.unit is not Unit.FEET:
            raise ValueError('length unit neither meter nor feet')

        if self.unit is Unit.FEET:
            self.base_value /= Length.WUN_METER


class Koordinaatit:
    """Coordinate representations require handling.

    Internal representation of value is as float.
    """

    def __init__(self, dimension: Dimension, value: Union[int, float, str], unit: Unit):
        self.sexagesimal = None
        self.decimal = None
        self.na = math.nan
        self.dimension = dimension
        self.value = math.nan
        self.unit = unit
        if not self.unit_valid_for_dimension():
            raise ValueError('unit not valid for dimension')

        self.unit_label = self.label_unit()
        self.what = self.label_dimension()

    def is_latitide(self) -> bool:
        """Service maybe YAGNI."""
        return self.dimension is Dimension.LAT

    def is_longitude(self) -> bool:
        """Service maybe YAGNI."""
        return self.dimension is Dimension.LON

    def is_altitude(self) -> bool:
        """Service maybe YAGNI."""
        return self.dimension is Dimension.ALT

    def label_dimension(self) -> str:
        """Delegate labeling of dimension to the enumeration type."""
        return self.dimension.name

    def label_unit(self) -> str:
        """Delegate labeling of unit to the enumeration type."""
        return self.unit.name

    def unit_valid_for_dimension(self) -> bool:
        """Latitudes and altitude units must be degree or radian, altitudes meter or feet."""
        if self.dimension is Dimension.ALT:
            return self.unit is Unit.METER or self.unit is Unit.FEET

        return self.unit is Unit.DEGREE or self.unit is Unit.RADIAN


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the coordination."""
    argv = argv if argv else sys.argv[1:]
    if not argv:
        print('ERROR arguments expected.', file=sys.stderr)
        return 2

    return 0
