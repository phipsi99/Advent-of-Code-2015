from pathlib import Path
import re

def do_main(debug_mode=False):
    with open(Path('05/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('05/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    point_sum2 = 0

    for line_index, line in enumerate(lines):
        if any(x in line for x in ["ab", "cd", "pq", "xy"]):
            continue
        if sum([line.count(x) for x in ["a", "e", "i", "o", "u"]]) <3:
            continue
        for i, c in enumerate(line):
            if i<len(line)-1 and line[i+1] == c:
                point_sum +=1
                break
    
    for line_index, line in enumerate(lines):
        rule1 = False
        rule2 = False
        for i, c in enumerate(line):
            if i<len(line)-1:
                let = line[i:i+2]
                if line.find(let, i+2) != -1:
                    rule1 = True
                    break
        for i, c in enumerate(line):
            if i<len(line)-2 and line[i+2] == c:
                rule2 = True
                break
        if rule1 and rule2:
            point_sum2+=1

    print(point_sum)
    print(point_sum2)

if __name__ == '__main__':
    do_main(False)