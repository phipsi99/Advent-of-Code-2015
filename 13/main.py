from collections import deque
from pathlib import Path


def find_max_happiness_bfs(happinesses):
    queue = deque([("Alice", ["Alice"], 0)])
    max_happiness = 0
    while queue:
        name, path, happiness = queue.popleft()
        if len(path) == len(happinesses) + 1:
            if happiness > max_happiness:
                max_happiness = happiness
        else:
            for other_name in happinesses.keys():
                if other_name == name and len(path) == len(happinesses):
                    queue.append(
                        (
                            name,
                            path + [other_name],
                            happiness
                            + happinesses[other_name][path[-1]]
                            + happinesses[path[-1]][other_name],
                        )
                    )
                if other_name not in path:
                    queue.append(
                        (
                            name,
                            path + [other_name],
                            happiness
                            + happinesses[other_name][path[-1]]
                            + happinesses[path[-1]][other_name],
                        )
                    )
    return max_happiness


def do_main(debug_mode=False):
    with open(Path("13/input.txt")) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path("13/test.txt")) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    happinesses = {}

    for line_index, line in enumerate(lines):
        name1 = line.split(" ")[0]
        name2 = line.split(" ")[-1].rstrip(".")
        happiness = int(line.split(" ")[3])
        if line.split(" ")[2] == "lose":
            happiness *= -1
        if name1 not in happinesses:
            happinesses[name1] = {}
        happinesses[name1][name2] = happiness

    print(find_max_happiness_bfs(happinesses))

    happinesses["Philipp"] = {}    
    for name in happinesses:
        happinesses[name]["Philipp"] = 0
        happinesses["Philipp"][name] = 0

    print(find_max_happiness_bfs(happinesses))



if __name__ == "__main__":
    do_main(False)
