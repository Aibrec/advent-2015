import time
import itertools
import math
import hashlib

file_path = 'input.txt'

start = time.perf_counter()
with open(file_path, 'r') as file:
    input = []
    for line in file:
        input.append(line.strip())

def judge(line):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    double_letter = False
    for i, char in enumerate(line):
        if vowel_count < 3 and char in vowels:
            vowel_count += 1

        if not double_letter and i != 0 and line[i-1] == char:
            double_letter = True

        if i != 0 and line[i-1:i+1] in {'ab', 'cd', 'pq', 'xy'}:
            return False

    if vowel_count >= 3 and double_letter:
        return True
    else:
        return False

score = 0
for line in input:
    if judge(line):
        score += 1

end = time.perf_counter()
print(f"score {score}")

time_in_microseconds = (end-start) * 1000000
print(f"took {time_in_microseconds:.2f}μs")