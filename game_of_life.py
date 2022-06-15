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
                if i_row!=None and i_col!=None:
                    result.add((i_row, i_col))
        
        result.remove((idx_row, idx_col))

        return result

    def action(self, idx):
        prev_val = self.grid[idx[0], idx[1]]
        if prev_val == 0:
            self.grid[idx[0], idx[1]] = 1
        else:
            self.grid[idx[0], idx[1]] = 0

    def get_nn_number(self, array_idx):
        return len(self.get_nn_idx_set(array_idx))

    def get_nn_number_live(self, array_idx):
        nn_idx_set = self.get_nn_idx_set(array_idx)
        result = 0
        for nn_idx in nn_idx_set:
            stat = self.grid[nn_idx[0], nn_idx[1]]
            if stat == 1:
                result+=1
        return result

if __name__ == "__main__":
    gol = GoL()
    nn_idx_set = gol.get_nn_idx_set((0,1))

