import pytest
from game_of_life import GoL
import numpy as np


class TestGoL:
    def setup_method(self):
        self.gol = GoL()

    def test_SizeofGrid(self):
        size = self.gol.grid.shape
        assert size == (100, 100)

    def test_GridMembers(self):
        grid_elements =set(np.unique(self.gol.grid))
        assert grid_elements.issubset({0,1})

    @pytest.mark.parametrize("array_idx, nn_idx_set", [
        ((2,2), {(1, 3), (2, 3), (3, 3), (1, 2), (3, 2), (1, 1), (2, 1), (3, 1)}),
        ((99, 99), {(98, 98), (98, 99), (99, 98)}),
        
    ])
    def test_NN_idx(self, array_idx, nn_idx_set):
        assert self.gol.get_nn_idx_set(array_idx)==nn_idx_set
