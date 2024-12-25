import time
import re

file_path = 'input.txt'

start_time = time.perf_counter()
with open(file_path, 'r') as file:
    lines = []
    for line in file:
        line = line.strip()
        lines.append(line)

def apply_escape_sequences(line):
    line = line.replace('\\', '\\\\')
    line = line.replace('"', '\\"')
    line = f'"{line}"'
    return line

score = 0
for i, line in enumerate(lines):
    subbed_line = apply_escape_sequences(line)
    score += len(subbed_line) - len(line)
    print(f"{line}: {subbed_line}")

end_time = time.perf_counter()
print(f"Score: {score}")

time_in_microseconds = (end_time-start_time) * 1000000
print(f"took {time_in_microseconds:.0f}μs")
