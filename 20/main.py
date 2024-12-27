import functools
import numpy as np
import tqdm


@functools.cache
def sieve(maxi):
    divisors = np.empty(maxi, dtype=object)
    for i in range(maxi):
        divisors[i] = []
    for i in tqdm.tqdm(range(1, maxi)):
        for j in range(i, maxi, i):
            divisors[j].append(i)
    return divisors


def findNFactors(divisor, n):
    total_sum = 0
    for divi in divisor[n]:
        total_sum += divi
    return total_sum


def find50Factors(divisor, n):
    total_sum = 0
    d = []
    for dd in divisor[n]:
        if n // dd > 50:
            continue
        d.append(dd)
    return sum(d)


def find_x_for_y(y):
    test = 1000000
    target_sum = y // 10
    divisor = sieve(test)
    for x in tqdm.tqdm(range(test)):
        if findNFactors(divisor, x) >= target_sum:
            return x
    return None


def find_x_for_y2(y):
    test = 1000000
    target_sum = y // 11
    divisor = sieve(test)
    for x in tqdm.tqdm(range(test)):
        if find50Factors(divisor, x) >= target_sum:
            return x
    return None


@functools.cache
def calc_val_for_house(house_num):
    return sum(i * 10 for i in range(1, house_num + 1) if house_num % i == 0)


def do_main(debug_mode=False):
    val = 36000000
    house = find_x_for_y(val)
    print(house)
    house = find_x_for_y2(val)
    print(house)


if __name__ == "__main__":
    do_main(False)
