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
