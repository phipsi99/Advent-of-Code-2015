from collections import defaultdict, deque
import copy
from pathlib import Path
from random import shuffle
import re

def find_molecules(replacements, elements, index):
    queue = deque([replacements])
    found_molecules = set()

    while queue:
        current_replacement = queue.popleft()
        



def do_main(debug_mode=False):
    with open(Path('19/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('19/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    replacements = defaultdict(list)

    #start_str = "HOHOHO"
    start_str = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"

    elements = re.findall(r'[A-Z][a-z]?', start_str)

    for line_index, line in enumerate(lines):
        key = line.split(" => ")[0]
        value = line.split(" => ")[1]
        replacements[key].append(value)

    found_molecules = set()
    for before, after_list in replacements.items():
        for after in after_list:
            indexes = [i for i, element in enumerate(elements) if element == before]
            for i in indexes:
                new_molecule = copy.deepcopy(elements)
                new_molecule[i] = after
                found_molecules.add("".join(new_molecule))
    print(len(found_molecules))

    replacements = []
    for line in lines:
        key, value = line.split(" => ")
        replacements.append((value, key))

    molecule = start_str

    cnt = 0
    while molecule != 'e':
        cnt_before = cnt
        for after, before in replacements:
            if after in molecule:
                cnt += 1
                molecule = molecule.replace(after, before, 1)
        if cnt_before == cnt:
            shuffle(replacements)
            cnt = 0
            molecule = start_str
    print(cnt)
                

if __name__ == '__main__':
    do_main(False)