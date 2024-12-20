from pathlib import Path
import re

import numpy as np

def do_main(debug_mode=False):
    with open(Path('06/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('06/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    lights = np.full((1000, 1000), 0, dtype=int)

    for line_index, line in enumerate(lines):
        nums = re.findall(r"(\d+),(\d+)",line)
        x = int(nums[0][0])
        y = int(nums[0][1])
        xx = int(nums[1][0])
        yy = int(nums[1][1])
        if "on" in line:
            lights[x:xx+1, y:yy+1] = 1
        elif "off" in line:
            lights[x:xx+1, y:yy+1] = 0
        elif "toggle" in line:
            lights[x:xx+1, y:yy+1] = lights[x:xx+1, y:yy+1] ^ 1
    print(np.count_nonzero(lights == 1))
    lights = np.full((1000, 1000), 0, dtype=int)


    for line_index, line in enumerate(lines):
        nums = re.findall(r"(\d+),(\d+)",line)
        x = int(nums[0][0])
        y = int(nums[0][1])
        xx = int(nums[1][0])
        yy = int(nums[1][1])
        if "on" in line:
            lights[x:xx+1, y:yy+1] += 1
        elif "off" in line:
            lights[x:xx+1, y:yy+1] -=1
            smaller = np.where(lights < 0)
            for i, j in zip(smaller[0], smaller[1]):
                lights[i,j] = 0
        elif "toggle" in line:
            lights[x:xx+1, y:yy+1] += 2
    
    for i in range(1000):
        for j in range(1000):
            point_sum += lights[i, j]
    print(point_sum)


if __name__ == '__main__':
    do_main(False)