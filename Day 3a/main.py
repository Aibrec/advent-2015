import time
import itertools
import math

file_path = 'input.txt'

start = time.perf_counter()
with open(file_path, 'r') as file:
    input = None
    for line in file:
        input = line.strip()

def get_dir(char):
    match char:
        case '<':
            dir = (0, -1)
        case '^':
            dir = (-1, 0)
        case '>':
            dir = (0, 1)
        case 'v':
            dir = (1, 0)
        case _:
            raise ValueError(char)
    return dir

def warp(dimensions):
    min_perimeter = min(sum(c) for c in itertools.combinations(dimensions, 2))
    volume = math.prod(dimensions)
    return volume + 2*min_perimeter

location = (0,0)
seen_locations = {location}
for i, char in enumerate(input):
    dir = get_dir(char)
    location = (location[0] + dir[0], location[1] + dir[1])
    seen_locations.add(location)

end = time.perf_counter()
print(f"score {len(seen_locations)}")

time_in_microseconds = (end-start) * 1000000
print(f"took {time_in_microseconds:.2f}μs")