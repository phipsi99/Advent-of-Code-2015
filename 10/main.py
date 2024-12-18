from pathlib import Path

def group_consecutive_same_numbers(number_str):
    result = []
    current_group = [number_str[0]]
    for i in range(1, len(number_str)):
        if number_str[i] == number_str[i - 1]:
            current_group.append(number_str[i])
        else:
            result.append(tuple(current_group))
            current_group = [number_str[i]]
    result.append(tuple(current_group))
    return result

def do_main(debug_mode=False):
    with open(Path('10/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('10/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    for line_index, line in enumerate(lines):
        s = line
        for i in range(50):
            n = group_consecutive_same_numbers(s)
            new_s = ''
            for group in n:
                new_s += str(len(group)) + group[0]
            s = new_s
    
    print(len(s))




if __name__ == '__main__':
    do_main(False)