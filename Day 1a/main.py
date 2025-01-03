import time

file_path = 'input.txt'

start = time.perf_counter()
with open(file_path, 'r') as file:
    input = ""
    for line in file:
        input = line.strip()

floor = 0
for char in line:
    match char:
        case '(':
            floor += 1
        case ')':
            floor -= 1

end = time.perf_counter()
print(f"Floor is {floor}")

time_in_microseconds = (end-start) * 1000000
print(f"took {time_in_microseconds:.2f}μs")