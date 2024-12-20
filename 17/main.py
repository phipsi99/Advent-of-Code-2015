from pathlib import Path

def find_fitting(already_filled, remaining_containers, total_liters, total):
    if already_filled==total_liters:
        return 1
    for container in remaining_containers:
        if already_filled+container<=total_liters:
            total += find_fitting(already_filled+container, remaining_containers[1:], total_liters, total)
    return total


def do_main(debug_mode=False):
    with open(Path('17/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('17/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    containers = []
    total_liters = 25

    for line_index, line in enumerate(lines):
        containers.append(int(line))

    print(find_fitting(0, containers, total_liters, 0))

if __name__ == '__main__':
    do_main(True)