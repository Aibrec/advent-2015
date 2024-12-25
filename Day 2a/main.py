import time
import itertools
import math

file_path = 'input.txt'

start = time.perf_counter()
with open(file_path, 'r') as file:
    input = []
    for line in file:
        input.append(tuple([int(n) for n in line.strip().split('x')]))

def warp(dimensions):
    side_areas = list(math.prod(c) for c in itertools.combinations(dimensions, 2))
    smallest_side = min(side_areas)
    total_area = smallest_side + (2 * sum(side_areas))
    return total_area

paper = 0
for present in input:
    paper += warp(present)

end = time.perf_counter()
print(f"paper {paper}")

time_in_microseconds = (end-start) * 1000000
print(f"took {time_in_microseconds:.2f}μs")