from pathlib import Path
import json
import re

def get_all_childs(json_obj):
    if isinstance(json_obj, dict):
        if "red" in json_obj.values():
            return 0
        return sum(get_all_childs(value) for value in json_obj.values())
    elif isinstance(json_obj, list):
        return sum(get_all_childs(value) for value in json_obj)
    elif isinstance(json_obj, int):
        return json_obj
    return 0
def do_main(debug_mode=False):
    with open(Path('12/input.json')) as file:
        text = file.read()
    
    if debug_mode:
        with open(Path('12/test.json')) as file:
            text = file.read()

    point_sum = 0

    numbers = re.findall(r"(-?\d+)", text)
    print(sum([int(i) for i in numbers]))
    json_input = json.loads(text)
    test = get_all_childs(json_input)
    print(test)

if __name__ == '__main__':
    do_main(True)