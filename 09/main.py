from collections import deque
from pathlib import Path


def travel_to_all_min(cities, routes):
    min_cost = float('inf')
    best_path = []
    for city in cities:
        queue = deque([([city], 0)])
        while len(queue) > 0:
            path, cost = queue.popleft()
            if len(path) == len(cities):
                if cost < min_cost:
                    min_cost = cost
                    best_path = path
            else:
                if path[-1] in routes:
                    for next_city, cost_to_next_city in routes[path[-1]]:
                        if next_city not in path:
                            queue.append((path + [next_city], cost + cost_to_next_city))
    return min_cost, best_path
    

def travel_to_all_max(cities, routes):
    max_cost = 0
    best_path = []
    for city in cities:
        queue = deque([([city], 0)])
        while len(queue) > 0:
            path, cost = queue.popleft()
            if len(path) == len(cities):
                if cost > max_cost:
                    max_cost = cost
                    best_path = path
            else:
                if path[-1] in routes:
                    for next_city, cost_to_next_city in routes[path[-1]]:
                        if next_city not in path:
                            queue.append((path + [next_city], cost + cost_to_next_city))
    return max_cost, best_path


def do_main(debug_mode=False):
    with open(Path('09/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('09/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    routes = {}
    cities = set()

    for line_index, line in enumerate(lines):
        city1 = line.split(' to ')[0].strip()
        city2 = line.split(' to ')[1].split(' = ')[0].strip()
        distance = int(line.split(' = ')[1].strip())
        cities.add(city1)
        cities.add(city2)
    
        if city1 not in routes:
            routes[city1] = []
        if city2 not in routes:
            routes[city2] = []
        routes[city1].append((city2, distance))
        routes[city2].append((city1, distance))

    print(travel_to_all_min(cities, routes))
    print(travel_to_all_max(cities, routes))
    

if __name__ == '__main__':
    do_main(False)