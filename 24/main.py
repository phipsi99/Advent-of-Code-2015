from itertools import combinations
from math import prod
from pathlib import Path

def find_candidates(packages):
    candidates = []
    min_l = float ('inf')

    for num_front in range(1, len(packages)):
        combs = combinations(packages, num_front)
        for comb in combs:
            other_packages = packages[:]
            for p in comb:
                other_packages.remove(p)
            packages_2 = []
            packages_3 = []
            if sum(other_packages) % 2 == 0 and sum(other_packages) // 2 == sum(comb):
                target_sum = sum(other_packages) // 2
                found_split = False
                
                for i in range(1, len(other_packages)):
                    for sub_comb in combinations(other_packages, i):
                        if sum(sub_comb) == target_sum:
                            packages_2 = list(sub_comb)
                            packages_3 = [pkg for pkg in other_packages if pkg not in sub_comb]
                            
                            if sum(packages_2) == sum(packages_3):
                                found_split = True
                                break
                    if found_split:
                        break
                
                if found_split:
                    if len(comb) < min_l:
                        min_l = len(comb)
                    elif len(comb) > min_l:
                        return candidates, min_l
                    candidates.append(comb)
                    print(f'{num_front} {comb} {packages_2} {packages_3}')
    return candidates, min_l

def find_candidates2(packages):
    candidates = []
    min_l = float ('inf')

    for num_front in range(1, len(packages)):
        combs = combinations(packages, num_front)
        for comb in combs:
            other_packages = packages[:]
            for p in comb:
                other_packages.remove(p)
            packages_2 = []
            packages_3 = []
            packages_4 = []
            if sum(other_packages) % 3 == 0 and sum(other_packages) // 3 == sum(comb):
                target_sum = sum(other_packages) // 3
                found_split = False
                
                for i in range(1, len(other_packages)):
                    for sub_comb in combinations(other_packages, i):
                        if sum(sub_comb) == target_sum:
                            packages_2 = list(sub_comb)
                            packages_z = [pkg for pkg in other_packages if pkg not in sub_comb]
                            for i in range(1, len(packages_z)):
                                for subsub_comb in combinations(packages_z, i):
                                    if sum(subsub_comb) == target_sum:
                                        packages_3 = list(subsub_comb)
                                        packages_4 = [pkg for pkg in packages_z if pkg not in subsub_comb]
                            if sum(packages_2) == sum(packages_3) == sum(packages_4):
                                found_split = True
                                break
                    if found_split:
                        break
                
                if found_split:
                    if len(comb) < min_l:
                        min_l = len(comb)
                    elif len(comb) > min_l:
                        return candidates, min_l
                    candidates.append(comb)
                    print(f'{num_front} {comb} {packages_2} {packages_3} {packages_4}')
    return candidates, min_l

def do_main(debug_mode=False):
    with open(Path('24/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('24/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    packages = [int(p) for p in lines]
    packages.sort(reverse=True)

    candidates, min_l = find_candidates(packages)
    candidates2, min_l2 = find_candidates2(packages)

    min_q = float('inf')
    for candidate in candidates:
        if len(candidate) == min_l:
            q = prod(candidate)
            if q < min_q:
                min_q = q
    print(min_q)

    min_q = float('inf')
    for candidate in candidates2:
        if len(candidate) == min_l2:
            q = prod(candidate)
            if q < min_q:
                min_q = q
    print(min_q)

if __name__ == '__main__':
    do_main(False)