# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 05 (numbers: sine series)
# PROBLEM NUMBER: 1

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_function

FILENAME = 'series.py'
POINTS = 1

@pytest.mark.parametrize(("args", "kwargs", "reference"),
                         list(zip([[0]], [{'eps': 1e-16}], [[0, 1]])))
def test_sin_zero(args, kwargs, reference):
    return _test_function("sin_recursive",
                          args,     # tuple or list
                          kwargs,   # dict
                          reference,
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )

