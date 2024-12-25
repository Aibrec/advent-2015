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
    min_perimeter = min(sum(c) for c in itertools.combinations(dimensions, 2))
    volume = math.prod(dimensions)
    return volume + 2*min_perimeter

ribbon = 0
for present in input:
    ribbon += warp(present)

end = time.perf_counter()
print(f"paper {ribbon}")

time_in_microseconds = (end-start) * 1000000
print(f"took {time_in_microseconds:.2f}μs")