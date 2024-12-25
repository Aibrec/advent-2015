import time
import networkx as nx
import itertools
import math

file_path = 'input.txt'

start_time = time.perf_counter()
with open(file_path, 'r') as file:
    edges = []
    for line in file:
        locations, price = line.strip().split(' = ')
        left, right = locations.split(' to ')
        edges.append((left, right, int(price)))

party = nx.Graph()
party.add_weighted_edges_from(edges)

possible_paths = itertools.permutations(party.nodes(), len(party.nodes()))
minimum_cost = -math.inf
for path in possible_paths:
    cost = nx.path_weight(party, path, 'weight')
    minimum_cost = max(cost, minimum_cost)

end_time = time.perf_counter()
print(f"Cost: {minimum_cost}")

time_in_microseconds = (end_time-start_time) * 1000000
print(f"took {time_in_microseconds:.0f}μs")
