from collections import Counter
from pathlib import Path

def do_main(debug_mode=False):
    with open(Path('03/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('03/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    for line_index, line in enumerate(lines):
        visited = Counter([(0,0)])
        pos = [0,0]
        for c in line:
            if c == ">":
                pos[0] += 1
            elif c == "<":
                pos[0] -= 1
            elif c == "^":
                pos[1] -= 1
            elif c == "v":
                pos[1] += 1
            visited[(pos[0], pos[1])] += 1
        print(len(visited))

        visited = Counter([(0,0)])
        pos = [0,0]
        pos2 = [0,0]
        turn1 = True
        for c in line:
            if turn1:
                if c == ">":
                    pos[0] += 1
                elif c == "<":
                    pos[0] -= 1
                elif c == "^":
                    pos[1] -= 1
                elif c == "v":
                    pos[1] += 1
                visited[(pos[0], pos[1])] += 1
                turn1 = False
            else:
                if c == ">":
                    pos2[0] += 1
                elif c == "<":
                    pos2[0] -= 1
                elif c == "^":
                    pos2[1] -= 1
                elif c == "v":
                    pos2[1] += 1
                visited[(pos2[0], pos2[1])] += 1
                turn1 = True
        print(len(visited))


if __name__ == '__main__':
    do_main(False)