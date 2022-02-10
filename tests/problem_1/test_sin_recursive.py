import pytest

import numpy as np
from numpy.testing import assert_almost_equal

from ..tst import import_file


class TestSinRecursive:
    def _test_sin(self, x):
        series = import_file("series.py")
        y, nmax = series.sin_recursive(x)
        y0 = np.sin(x)
        assert_almost_equal(y, y0)

    @pytest.mark.parametrize("x", np.pi*np.arange(-1, 1.2, 0.2))
    def test_sin_floats(self, x):
        self._test_sin(x)

    @pytest.mark.parametrize("x", np.pi*np.linspace(-2, 2, 9))
    def test_sin(self, x):
        self._test_sin(x)

    @pytest.mark.xfail
    @pytest.mark.parametrize("x", np.pi*np.linspace(-50, 50, 4))
    def test_sin_large_range(self, x):
        self._test_sin(x)

