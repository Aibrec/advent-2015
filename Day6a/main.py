import time
import re
from collections import defaultdict

file_path = 'input.txt'

start = time.perf_counter()
with open(file_path, 'r') as file:
    input = []
    for line in file:
        line = line.strip()

        if line.startswith('toggle '):
            command = 'toggle'
            line = line[len('toggle '):]
        else:
            if line.startswith('turn off '):
                command = 'off'
                line = line[len('turn off '):]
            else:
                command = 'on'
                line = line[len('turn on '):]

        corners = line.split(' through ')
        corners = tuple(tuple(int(val) for val in corner.split(',')) for corner in corners)
        input.append((command, corners))

lights = defaultdict(bool)
for (command, ((x1, y1), (x2, y2))) in input:
    (x1, x2) = sorted((x1, x2))
    (y1, y2) = sorted((y1, y2))
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if command == 'toggle':
                lights[(x, y)] = not lights[(x, y)]
            elif command == 'on':
                lights[(x, y)] = True
            else:
                lights[(x, y)] = False

lights_on = sum(lights.values())

end = time.perf_counter()
print(f"score {lights_on}")

time_in_microseconds = (end-start) * 1000000
print(f"took {time_in_microseconds:.2f}μs")