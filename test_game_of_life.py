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

    @pytest.mark.parametrize("idx", [(88,78), (56,67)])
    def test_action(self, idx):
        prev_val = self.gol.grid[idx[0], idx[1]]
        self.gol.action(idx)
        curr_val = self.gol.grid[idx[0], idx[1]]
        if prev_val == 0:
            assert curr_val == 1

        elif prev_val == 1:
            assert curr_val == 0

    @pytest.mark.parametrize("array_idx, len_nn ", [((2,2), 8), ((99,99), 3)])
    def test_nn_number(self, array_idx, len_nn):
        nn_num = self.gol.get_nn_number(array_idx)
        assert nn_num == len_nn