from pathlib import Path

# hlf r sets register r to half its current value, then continues with the next instruction.
# tpl r sets register r to triple its current value, then continues with the next instruction.
# inc r increments register r, adding 1 to it, then continues with the next instruction.
# jmp offset is a jump; it continues with the instruction offset away relative to itself.
# jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
# jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

def execute_programm(lines):
    registers = {"a": 1, "b": 0}
    pointer = 0
    while pointer < len(lines):
        line = lines[pointer]
        if line.startswith("hlf"):
            registers[line[4]] //= 2
            pointer +=1
        elif line.startswith("tpl"):
            registers[line[4]] *= 3
            pointer +=1
        elif line.startswith("inc"):
            registers[line[4]] += 1
            pointer +=1
        elif line.startswith("jmp"):
            pointer += int(line.split(" ")[1])
        elif line.startswith("jie"):
            if registers[line[4]] % 2 == 0:
                pointer += int(line.split(" ")[2])
            else:
                pointer +=1
        elif line.startswith("jio"):
            if registers[line[4]] == 1:
                pointer += int(line.split(" ")[2])
            else:
                pointer +=1
    return registers

def do_main(debug_mode=False):
    with open(Path('23/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('23/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    registers = execute_programm(lines)
    print(registers)

if __name__ == '__main__':
    do_main(False)