# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""Coordinates API."""
import os
import sys
from typing import List, Union


DEBUG_VAR = 'KOORDINAATI_DEBUG'
DEBUG = os.getenv(DEBUG_VAR)

ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'


class Koordinaati:
    """Coordinate representations require handling."""
    def __init__(self, unit, value, what):
        self.sexagesimal = None
        self.decimal = None
        self.na = True
        self.unit = unit
        self.value = value
        self.what = what


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the coordination."""
    argv = argv if argv else sys.argv[1:]
    if not argv:
        print('ERROR arguments expected.', file=sys.stderr)
        return 2
    
    return 0
