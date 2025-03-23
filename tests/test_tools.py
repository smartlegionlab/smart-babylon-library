# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import time
from smart_babylon_library.tools import timeit


@timeit
def dummy_function():
    time.sleep(0.1)
    return "done"


def test_timeit_decorator(capsys):
    result = dummy_function()
    captured = capsys.readouterr()
    assert "Execution time:" in captured.out
    assert result == "done"
