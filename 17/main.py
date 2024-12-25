from pathlib import Path

def find_fitting(already_filled, remaining_containers, total_liters, containers_used):
    if already_filled==total_liters:
        return 1, [containers_used]
    total = 0
    used_container = []
    for i, container in enumerate(remaining_containers):
        if already_filled+container<=total_liters:
            t,c = find_fitting(already_filled+container, remaining_containers[i+1:], total_liters, containers_used+1)
            total += t
            used_container.extend(c)
    return total,  used_container


def do_main(debug_mode=False):
    with open(Path('17/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('17/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    containers = []
    total_liters = 150

    for line_index, line in enumerate(lines):
        containers.append(int(line))

    total, used_containers = find_fitting(0, containers, total_liters, 0)
    print(total)
    min_used = min(used_containers)
    print(used_containers.count(min_used))


if __name__ == '__main__':
    do_main(False)