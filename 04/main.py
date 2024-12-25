from pathlib import Path
import hashlib

def do_main(debug_mode=False):
    with open(Path('04/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('04/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    for line_index, line in enumerate(lines):
        i = 0
        while True:
            i += 1
            str2hash = line + str(i)
            result = hashlib.md5(str2hash.encode())
            if result.hexdigest().startswith("000000"):
                print(i)
                break
            

if __name__ == '__main__':
    do_main(False)