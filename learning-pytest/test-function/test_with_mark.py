import pytest


@pytest.mark.finished
def test_func1():
    assert 1 == 1


@pytest.mark.unfinished
def test_func2():
    assert 1 != 1

# pytest -m finished learning-pytest/test_with_mark.py
