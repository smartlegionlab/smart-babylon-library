# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import string

MIN_PUNCTUATION = ' ,.'
RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
BABYLON_CHARSET = string.ascii_letters + string.digits + string.punctuation + " " + RU
CHARSET = string.ascii_lowercase + MIN_PUNCTUATION
MAX_PAGE_CONTENT_LENGTH = 3200
NUM_WALLS = 4
NUM_SHELVES = 5
NUM_VOLUMES = 32
NUM_PAGES = 410
HEXAGON_BASE = 36
