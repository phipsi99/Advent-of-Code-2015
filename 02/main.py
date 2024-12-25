from pathlib import Path

def do_main(debug_mode=False):
    with open(Path('02/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('02/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    point_sum2 = 0

    for line_index, line in enumerate(lines):
        r = [int(i) for i in line.split("x")]
        mins = r[:]
        mins.remove(max(r))
        slack = mins[0] * mins[1]
        box = 2*r[0]*r[1] + 2*r[1]*r[2]+ 2*r[0]*r[2]
        point_sum += (box + slack)

        ribbon = sum(mins*2)
        bow = r[0]*r[1]*r[2]
        point_sum2 += (ribbon + bow)



    print(point_sum)
    print(point_sum2)
if __name__ == '__main__':
    do_main(False)