# -*- coding: utf-8 -*-

import pytest
from udacity_course.skeleton import fib

__author__ = "Aravind Kumar Murugaiyan"
__copyright__ = "Aravind Kumar Murugaiyan"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
