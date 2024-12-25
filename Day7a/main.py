import time
import networkx as nx
import itertools

file_path = 'input.txt'

start_time = time.perf_counter()
with open(file_path, 'r') as file:
    wires = {}
    operations = []
    for line in file:
        (operation, output) = line.strip().split(' -> ')
        if ' ' not in operation:
            try:
                initial_value = int(operation)
                wires[output] = initial_value
                continue
            except:
                pass

            operations.append((operation, None, 'ASSIGN', output))
        elif operation.startswith('NOT'):
            (op, left) = operation.split(' ')
            operations.append((left, None, op, output))
        else:
            (left, op, right) = operation.split(' ')
            operations.append((left, right, op, output))

for i in range(10):
    wires[str(i)] = i

remaining_operations = []
while operations:
    for i, operation in enumerate(operations):
        (left, right, op, output) = operation
        if op in {'ASSIGN', 'NOT', 'LSHIFT', 'RSHIFT'}:
            if left in wires:
                match op:
                    case 'ASSIGN':
                        wires[output] = wires[left]
                    case 'NOT':
                        wires[output] = ~wires[left]
                    case 'LSHIFT':
                        wires[output] = wires[left] << int(right)
                    case 'RSHIFT':
                        wires[output] = wires[left] >> int(right)
                    case _:
                        raise Exception('Unknown operation')
            else:
                remaining_operations.append(operation)
        else:
            if left in wires and right in wires:
                match op:
                    case 'AND':
                        wires[output] = wires[left] & wires[right]
                    case 'OR':
                        wires[output] = wires[left] | wires[right]
                    case _:
                        raise Exception('Unknown operation')
            else:
                remaining_operations.append(operation)
    operations = remaining_operations
    remaining_operations = []
    #print(f"Done with {len(operations)} remaining")

end_time = time.perf_counter()
print(f"A wire: {wires['a']}")

# for wire in sorted(wires.keys()):
#     print(f"{wire}: {wires[wire]}")

time_in_microseconds = (end_time-start_time) * 1000000
print(f"took {time_in_microseconds:.0f}μs")
