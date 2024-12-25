import time

file_path = 'input.txt'

start = time.perf_counter()
with open(file_path, 'r') as file:
    input = ""
    for line in file:
        input = line.strip()

floor = 0
for i, char in enumerate(line):
    match char:
        case '(':
            floor += 1
        case ')':
            floor -= 1
    if floor < 0:
        break

end = time.perf_counter()
print(f"Basement at char {i+1}")

time_in_microseconds = (end-start) * 1000000
print(f"took {time_in_microseconds:.2f}μs")