from pathlib import Path
import re

def do_main(debug_mode=False):
    with open(Path('08/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('08/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum_code = 0
    point_sum_mem = 0

    for line_index, line in enumerate(lines):
        code = 0
        for char_index, char in enumerate(line):
            if not char.strip() == "":
                code += 1
        point_sum_code += code
        test = re.sub(r'\\\\', 'a', line[1:-1].strip())  # Replace escaped backslashes
        test = re.sub(r'\\\"', 'a', test)               # Replace escaped quotes
        test = re.sub(r'\\x[0-9a-fA-F]{2}', 'a', test)  # Replace hex escapes

        a = len(test)
        point_sum_mem += a

    print(point_sum_code - point_sum_mem)

    point_sum_code = 0
    point_sum_mem = 0

    for line_index, line in enumerate(lines):
        code = 0
        for char_index, char in enumerate(line):
            if not char.strip() == "":
                code += 1
        point_sum_code += code

        
        test = line.replace('\\', '\\\\')  # Replace backslash with double backslash
        test = test.replace('"', '\\"') 

        a = len(test) + 2
        point_sum_mem += a

    print(point_sum_mem - point_sum_code)


if __name__ == '__main__':
    do_main(False)