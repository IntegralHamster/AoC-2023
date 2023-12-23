with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

adjacency_list = {}

# comment this out for part 1 and just wait a minute for dfs to work
for i in range(len(lines)):
    lines[i] = lines[i].replace('>', '.').replace('<', '.').replace('^', '.').replace('v','.')

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '.':
            coordinates = (x, y)
            adjacent = {}
            if x < len(lines[0]) - 1:
                if lines[y][x + 1] == '.':
                    adjacent[(x + 1, y)] = 1
                elif lines[y][x + 1] == '>':
                    adjacent[(x + 2, y)] = 2
            if x > 0:
                if lines[y][x - 1] == '.':
                    adjacent[(x - 1, y)] = 1
                elif lines[y][x - 1] == '<':
                    adjacent[(x - 2, y)] = 2
            if y < len(lines) - 1:
                if lines[y+1][x] == '.':
                    adjacent[(x, y+1)] = 1
                elif lines[y+1][x] == 'v':
                    adjacent[(x, y+2)] = 2
            if y > 0:
                if lines[y-1][x] == '.':
                    adjacent[(x, y-1)] = 1
                elif lines[y-1][x] == '^':
                    adjacent[(x, y-2)] = 2
            adjacency_list[coordinates] = adjacent

import copy
import sys
sys.setrecursionlimit(5000)


def depthFirst(graph, currentVertex, visited):
    global max_len
    visited.append(currentVertex)
    for vertex in graph[currentVertex].keys():
        if vertex not in visited:
            depthFirst(graph, vertex, copy.deepcopy(visited))
    if finish in visited:
        travel_len = 0
        for i in range(len(visited) - 1):
            travel_len += new_graph[visited[i]][visited[i + 1]]
        if travel_len > max_len:
            max_len = travel_len
            print(max_len)

    visitedList.append(visited)

    return visitedList



start = (1, 0)
finish = (139, 140)
# comment out this part for part 1
new_nodes = [start, finish] # new graph would be intersections, start, finish

for key in adjacency_list.keys():
    if len(adjacency_list[key]) > 2:
        new_nodes.append(key)

def walk_between_nodes (graph, special_nodes, node, visited):
    for vertex in graph[node].keys():
        if vertex not in visited:
            visited.append(vertex)
            if vertex in special_nodes:
                return visited
            else:
                visited = copy.deepcopy(walk_between_nodes(graph, special_nodes, vertex, copy.deepcopy(visited)))
                if set(visited).intersection(special_nodes):
                    return visited

new_graph = {}
for intersection in new_nodes:
    visitedList = []
    for node in adjacency_list[intersection].keys():
        visitedList.append(walk_between_nodes(adjacency_list, new_nodes, node, [intersection, node]))
    adjacent = {}
    for path in visitedList:
        adjacent[path[-1]] = len(path) - 1
    new_graph[intersection] = adjacent

print(len(new_graph))
# end of commented out part for part 1

visitedList = [[]]
global max_len
max_len = -1
paths = depthFirst(new_graph, start, []) # here for part1 you need to plug in adjacency_list. Eventually for part 2 the DFS will end, however when printouts stop for a minute last one is your answer, you can halt the program
true_paths = []

for path in paths:
    if finish in path:
        true_paths.append(path)

length = []
for path in true_paths:
    travel_len = 0
    for i in range(len(path) - 1):
        travel_len += new_graph[path[i]][path[i+1]]
    length.append(travel_len)

print(max(length))


