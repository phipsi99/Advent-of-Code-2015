from pathlib import Path
import re

def is_password_valid(password):
    rule1 = False
    for i in range(len(password) - 2):
        if ord(password[i]) - ord(password[i + 1]) == -1 and ord(password[i+1]) - ord(password[i + 2]) == -1:
            rule1 = True
            break
    if not rule1:
        return False
    pairs = re.findall(r'([a-z])\1', password)
    if pairs and len(pairs) > 1:
        a = set(pairs[0])
        for pair in pairs:
            a.add(pair)
        if len(a) < 2:
            return False
    else:
        return False
    
    if "i" in password or "o" in password or "l" in password:
        return False
    return True
    
def string_to_base26(s):
    result = 0
    for i, char in enumerate(s):
        value = ord(char) - ord('a') +1 # Now 'a' = 1, 'b' = 2, ..., 'z' = 26
        result = result * 26 + value  # Shift previous digits and add the new one
    return result-1

def base26_to_string(n):
    result = []
    while n >= 0:
        remainder = n % 26
        result.append(chr(remainder + ord('a')))  # Convert the remainder to a letter
        n = n // 26 - 1  # Adjust for next "digit", and fix the base-26 overflow
        
        # Once n becomes negative, we're done.
        if n < 0:
            break
    return ''.join(result[::-1])  # Reverse to get the correct order


def find_next_pw(input_str):
    b26_repr = string_to_base26(input_str)
    while not is_password_valid(base26_to_string(b26_repr)):
        stri = base26_to_string(b26_repr)
        if "i" in stri:
            ss = stri[:stri.index("i")] + "j" + "a" * len(stri[stri.index("i")+1:])
            b26_repr = string_to_base26(ss)
        if "o" in stri:
            ss = stri[:stri.index("o")] + "p" + "a" * len(stri[stri.index("o")+1:])
            b26_repr = string_to_base26(ss)
        if "l" in stri:
            ss = stri[:stri.index("l")] + "m" + "a" * len(stri[stri.index("l")+1:])
            b26_repr = string_to_base26(ss)

        b26_repr += 1
    return base26_to_string(b26_repr)


def do_main(debug_mode=False):
    with open(Path('11/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    if debug_mode:
        with open(Path('11/test.txt')) as file:
            lines = [line.rstrip() for line in file]
    point_sum = 0
    input = "hepxcrrq"
    result1 = find_next_pw(input)
    print(result1)
    input2 = base26_to_string(string_to_base26(result1) +1 )
    result2 = find_next_pw(input2)
    print(result2)


if __name__ == '__main__':
    do_main(False)