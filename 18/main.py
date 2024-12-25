import copy
from pathlib import Path

def get_neighbors(x, y, grid):
    pos = [(x+dx, y+dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx != 0 or dy != 0]
    result = []
    for p in pos:
        if p[0] < 0 or p[0] >= len(grid[0]) or p[1] < 0 or p[1] >= len(grid):
            continue
        result.append(p)
    return result


def turn_on_off(x, y, grid):
    cnt = 0
    for neighbour in get_neighbors(x, y, grid):
        if grid[neighbour[1]][neighbour[0]] == "#":
            cnt += 1
    if grid[y][x] == "#":
        if cnt == 2 or cnt == 3:
            return("#")
        else: 
            return(".")
    else:
        if cnt == 3:
            return("#")
        else:
            return(".")



def do_main(debug_mode=False):
    with open(Path('18/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('18/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    grid = [list(line) for line in lines]
    height, width = len(grid), len(grid[0])

    for _ in range(100):
        new_grid = copy.deepcopy(grid) 
        for y in range(height):
            for x in range(width):
                new_grid[y][x] = turn_on_off(x, y, grid)
        grid = new_grid  

    point_sum = sum(1 for row in grid for cell in row if cell == "#")
    print(point_sum)
    

    point_sum = 0

    grid = [list(line) for line in lines]
    height, width = len(grid), len(grid[0])
    grid[0][0] = "#"
    grid[0][width-1] = "#"
    grid[height-1][0] = "#"
    grid[height-1][width-1] = "#"

    for _ in range(100):
        new_grid = copy.deepcopy(grid) 
        for y in range(height):
            for x in range(width):
                if x == 0 and y == 0 or x == width-1 and y == height-1:
                    continue
                elif x == 0 and y==height-1 or y==0 and x==width-1:
                    continue
                new_grid[y][x] = turn_on_off(x, y, grid)
        grid = new_grid  

    point_sum = sum(1 for row in grid for cell in row if cell == "#")
    print(point_sum)

if __name__ == '__main__':
    do_main(False)