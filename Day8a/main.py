import time
import re

file_path = 'input.txt'

start_time = time.perf_counter()
with open(file_path, 'r') as file:
    lines = []
    for line in file:
        line = line.strip()
        lines.append(line)

def replace_escape_sequences(line):
    line = line[1:-1]
    line = line.replace('\\"', '"')
    line = re.sub(r'\\x[0-9a-f]{2}', 'Z', line)
    line =  line.replace('\\\\', '\\')
    return line

score = 0
for i, line in enumerate(lines):
    subbed_line = replace_escape_sequences(line)
    score += len(line) - len(subbed_line)
    print(f"{line}: {subbed_line}")

end_time = time.perf_counter()
print(f"Score: {score}")

time_in_microseconds = (end_time-start_time) * 1000000
print(f"took {time_in_microseconds:.0f}μs")
