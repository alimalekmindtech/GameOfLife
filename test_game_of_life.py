import pytest
from game_of_life import GoL
import numpy as np

# def foo(a, b):
#     return a + 1, b + 1

# @pytest.mark.parametrize("a,b", [(1, 2, 3), (-1, -2), (-1, -4), (4, 2)])
# def test_foo(a, b):
#     # check that foo runs correctly and that the result is a tuple. 
#     assert isinstance(foo(a, b), tuple)

class TestGoL:
    def setup_method(self):
        self.gol = GoL()

    def test_SizeofGrid(self):
        size = self.gol.grid.shape
        assert size == (100, 100)

    def test_GridMembers(self):
        grid_elements =set(np.unique(self.gol.grid))
        assert grid_elements.issubset({0,1})
