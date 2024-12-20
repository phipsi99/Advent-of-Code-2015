from pathlib import Path

class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.distance = 0
        self.time_left = self.fly_time
        self.flying = True
        self.points = 0

def do_main(debug_mode=False):
    with open(Path('14/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('14/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    reindeers =  []

    for line_index, line in enumerate(lines):
        name = line.split(' ')[0] 
        speed = int(line.split(' ')[3])
        fly_time = int(line.split(' ')[6])
        rest_time = int(line.split(' ')[13])
        distance = 0
        reindeers.append(Reindeer(name, speed, fly_time, rest_time))

    for i in range(2503):
        for reindeer in reindeers:
            if reindeer.time_left > 0:
                if reindeer.flying:
                    reindeer.distance += reindeer.speed
                    reindeer.time_left -= 1
                    if reindeer.time_left == 0: 
                        reindeer.flying = False
                        reindeer.time_left = reindeer.rest_time
                else:
                    reindeer.time_left -= 1
                    if reindeer.time_left == 0: 
                        reindeer.flying = True
                        reindeer.time_left = reindeer.fly_time
        current_max = 0
        for reindeer in reindeers:
            if reindeer.distance > current_max:
                current_max = reindeer.distance
        for rindeer in reindeers:
            if rindeer.distance == current_max:
                rindeer.points += 1

    print(max([reindeer.distance for reindeer in reindeers]))
    print(max([reindeer.points for reindeer in reindeers]))



if __name__ == '__main__':
    do_main(False)