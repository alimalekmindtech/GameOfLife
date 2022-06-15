import numpy as np
class GoL:
    def __init__(self):
        self.grid = np.zeros((100, 100), dtype=int)
    
    def get_nn_idx_set(self, array_idx):
        idx_row = array_idx[0]
        idx_col = array_idx[1]
        idx_row_next = idx_row + 1
        if idx_row_next >= 100:
            idx_row_next = None

        idx_row_prev = idx_row - 1
        if idx_row_prev <0:
            idx_row_prev = None

        idx_col_next = idx_col + 1
        if idx_col_next >= 100:
            idx_col_next = None
        idx_col_prev = idx_col - 1
        if idx_col_prev <0:
            idx_col_prev = None

        idx_nn_row = [idx_row, idx_row_next, idx_row_prev]
        idx_nn_col = [idx_col, idx_col_next, idx_col_prev]

        result = set()
        for i_row in idx_nn_row:
            for i_col in idx_nn_col:
                if i_row and i_col:
                    result.add((i_row, i_col))
        
        result.remove((idx_row, idx_col))

        return result