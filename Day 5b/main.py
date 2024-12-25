import time
import re

file_path = 'input.txt'

start = time.perf_counter()
with open(file_path, 'r') as file:
    input = []
    for line in file:
        input.append(line.strip())

def judge(line):
    # Repeat with exactly one letter between them
    one_seperate = re.search(r'(\w).\1', line)

    # Pair that appears twice
    pair_twice = re.search(r'(\w{2}).*\1', line)

    return pair_twice and one_seperate

score = 0
for line in input:
    if judge(line):
        score += 1

end = time.perf_counter()
print(f"score {score}")

time_in_microseconds = (end-start) * 1000000
print(f"took {time_in_microseconds:.2f}μs")