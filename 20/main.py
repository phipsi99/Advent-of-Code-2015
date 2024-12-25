
import functools


@functools.cache
def calc_val_for_house(house_num):
    return sum(i*10 for i in range(1, house_num+1) if house_num % i == 0)

def do_main(debug_mode=False):
    
    print(calc_val_for_house(2000000))
    house_num = 0
    val = 0
    while val < 36000000:
        house_num += 1
        val = calc_val_for_house(house_num)
    print(house_num)

if __name__ == '__main__':
    do_main(False)