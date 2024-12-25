import time

file_path = 'input.txt'
start_time = time.perf_counter()

with open(file_path, 'r') as file:
    string = None
    for line in file:
        string = line.strip()

def look_say(line):
    parts = []
    current_char = line[0]
    current_count = 1
    for char in line[1:]:
        if char == current_char:
            current_count += 1
        else:
            parts.append(f"{current_count}{current_char}")
            current_char = char
            current_count = 1
    parts.append(f"{current_count}{current_char}")
    return ''.join(parts)

for i in range(50):
    next_string = look_say(string)
    string = next_string

end_time = time.perf_counter()
print(f"Cost: {len(string)}")

time_in_microseconds = (end_time-start_time) * 1000000
print(f"took {time_in_microseconds:.0f}μs")
