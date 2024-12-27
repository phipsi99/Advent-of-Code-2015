from pathlib import Path

import numpy as np
import tqdm

def calc_index(row, col):
    row_result = 1
    for i in range(1, row):
        row_result += i
    col_result = row_result
    for i in range(1, col):
        col_result += row + i
    return col_result-1

def do_main(debug_mode=False):
    with open(Path('25/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('25/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    grid_size = 50000000
    code_grid = np.zeros((grid_size), dtype=int)

    last_val = 20151125
    for i in tqdm.tqdm (range(1, grid_size)):
        code_grid[i] = (last_val * 252533) % 33554393
        last_val = code_grid[i]

    print(code_grid[calc_index(3010, 3019)])


if __name__ == '__main__':
    do_main(False)