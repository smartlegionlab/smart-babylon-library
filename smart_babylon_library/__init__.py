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
from .babylon_lib_with_books import BabylonLibraryWithBooks

__version__ = '0.4.1'
__author__ = 'A.A. Suvorov'
__all__ = [
    "LibraryStructure",
    "TextEncoder",
    "timeit",
    "BabylonLibrary",
    "BabylonLibraryWithBooks",
    "BabylonLibraryIterator"
]
