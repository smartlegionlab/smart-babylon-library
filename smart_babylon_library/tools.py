# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import shutil
import time
from functools import wraps


def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        console_width = shutil.get_terminal_size().columns
        separator = '-' * console_width
        print(separator)
        print(f"'{func.__name__}' - Execution time: {end_time - start_time:.6f} seconds")
        print(separator)
        return result
    return wrapper
