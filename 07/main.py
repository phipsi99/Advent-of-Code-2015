from collections import deque
from pathlib import Path
import re

import numpy as np

def do_main(debug_mode=False):
    with open(Path('07/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('07/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    db = {}
    queue = deque(lines)
    selected_item = None

    while len(queue) > 0:
        for item in queue:
            not_all_inputs = False
            li = re.findall(r'[a-z]{1,2}', item.split("->")[0])
            for c in li:
                if c not in db:
                    not_all_inputs = True
                    break
            if not_all_inputs:
                continue
            selected_item = item
            break
        if selected_item.split("->")[1].strip() == "b" and selected_item != "956 -> b":
            queue.remove(selected_item)
            continue
        queue.remove(selected_item)
        line = selected_item
        if "AND" in line:
            x = line.split("->")[0].split("AND")[0].strip()
            xx = line.split("->")[0].split("AND")[1].strip()
            if x.isnumeric():
                x = np.uint16(x)
            if xx.isnumeric():
                xx = np.uint16(xx)
            xxx = line.split("->")[1].strip()
            if isinstance(x, str):
                db[xxx] = db[x] & db[xx]
            else:
                db[xxx] = x & db[xx]
        elif "OR" in line:
            x = line.split("->")[0].split("OR")[0].strip()
            xx = line.split("->")[0].split("OR")[1].strip()
            if x.isnumeric():
                x = np.uint16(x)
            if xx.isnumeric():
                xx = np.uint16(xx)
            xxx = line.split("->")[1].strip()
            db[xxx] = db[x] | db[xx]
        elif "NOT" in line:
            x = re.findall(r'[a-z]{1,2}', line)[0]
            xx = re.findall(r'[a-z]{1,2}', line)[1]
            db[xx] = ~db[x]
        elif "LSHIFT" in line:
            x = re.findall(r'[a-z]{1,2}', line)[0]
            xx = np.uint16(re.findall(r'[0-9]+', line)[0])
            xxx = re.findall(r'[a-z]{1,2}', line)[1]
            db[xxx] = db[x] << xx   
        elif "RSHIFT" in line:
            x = re.findall(r'[a-z]{1,2}', line)[0]
            xx = np.uint16(re.findall(r'[0-9]+', line)[0])
            xxx = re.findall(r'[a-z]{1,2}', line)[1]
            db[xxx] = db[x] >> xx   
        else:
            x = line.split("->")[0].strip()
            xx = line.split("->")[1].strip()
            if x.isnumeric():
                x = np.uint16(x)
            else:
                if x not in db:
                    continue
                x = np.uint16(db[x])
            db[xx] = x
    print(db)
    print(db["a"])

if __name__ == '__main__':
    do_main(False)