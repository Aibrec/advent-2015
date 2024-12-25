import time
import itertools
import math
import hashlib

file_path = 'input.txt'

start = time.perf_counter()
with open(file_path, 'r') as file:
    input = None
    for line in file:
        input = line.strip()

i = 0
while True:
    hash = hashlib.md5(bytes(f"{input}{i}", encoding="utf-8")).hexdigest()
    if hash.startswith('000000'):
        break
    i += 1

end = time.perf_counter()
print(f"score {i}")

time_in_microseconds = (end-start) * 1000000
print(f"took {time_in_microseconds:.2f}μs")