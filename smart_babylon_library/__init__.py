# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Smart Babylon Library"""
from .library_structure import LibraryStructure
from .text_encoder import TextEncoder
from .tools import timeit
from .babylon_library import BabylonLibrary, BabylonLibraryIterator
from .smart_babylon_library import SmartBabylonLibrary, SmartBabylonLibraryIterator
from .config import *

__version__ = '0.6.1'
__author__ = 'A.A. Suvorov'
__all__ = [
    "LibraryStructure",
    "TextEncoder",
    "timeit",
    "BabylonLibrary",
    "SmartBabylonLibrary",
    "BabylonLibraryIterator",
    'SmartBabylonLibraryIterator',
]
