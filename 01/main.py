from pathlib import Path

def do_main(debug_mode=False):
    with open(Path('01/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('01/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum1 = 0
    point_sum2 = 0

    for line_index, line in enumerate(lines):
        point_sum1= line.count("(")-line.count(")")
        floor = 0
        for i, c in enumerate(line):
            if c == "(":
                floor += 1
            else:
                floor -= 1
            if floor < 0:
                point_sum2 = i+1
                break
    print(point_sum1)
    print(point_sum2)


if __name__ == '__main__':
    do_main(False)