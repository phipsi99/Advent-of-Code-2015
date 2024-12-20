from pathlib import Path

def do_main(debug_mode=False):
    with open(Path('16/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('16/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    sues = {}

    for line_index, line in enumerate(lines):
        sues[line_index+1] = {}
        sues[line_index+1][line.split(' ')[2].strip(":")] = int(line.split(' ')[3].strip(","))
        sues[line_index+1][line.split(' ')[4].strip(":")] = int(line.split(' ')[5].strip(","))
        sues[line_index+1][line.split(' ')[6].strip(":")] = int(line.split(' ')[7].strip(","))
    
    for index, sue in sues.items():
        right_sue = True
        for key, value in sue.items():
            if key == "children" and value != 3:
                right_sue = False
            elif key == "cats" and value < 7:
                right_sue = False
            elif key == "samoyeds" and value != 2:
                right_sue = False
            elif key == "pomeranians" and value > 3:
                right_sue = False
            elif key == "goldfish" and value > 5:
                right_sue = False
            elif key == "trees" and value < 3:
                right_sue = False
            elif key == "cars" and value != 2:
                right_sue = False
            elif key == "perfumes" and value != 1:
                right_sue = False
            elif key == "akitas":
                right_sue = False
            elif key == "vizslas":
                right_sue = False
        if right_sue:
            print(index,sue)

if __name__ == '__main__':
    do_main(False)