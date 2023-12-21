with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

adjacency_list = {}

#if you want part 1 remove this input expansion
lines2 = []
for i in range(5):
    for line in lines:
        lines2.append(line+line+line+line+line)

print(len(lines2), len(lines2[0]))
for y in range(len(lines2)):
    for x in range(len(lines2[0])):
        if lines2[y][x] != '#':
            coordinates = (x, y)
            adjacent = {}
            if x < len(lines2[0]) - 1:
                if lines2[y][x + 1] != '#':
                    adjacent[(x + 1, y)] = 1
            if x > 0:
                if lines2[y][x - 1] != '#':
                    adjacent[(x - 1, y)] = 1
            if y < len(lines2) - 1:
                if lines2[y+1][x] != '#':
                    adjacent[(x, y+1)] = 1
            if y > 0:
                if lines2[y-1][x] != '#':
                    adjacent[(x, y-1)] = 1
            adjacency_list[coordinates] = adjacent



def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
# part 1 data trimming
# steps = 64
# check1 = set(adjacency_list.keys())
# for key in check1:
#     if manhattan(start, key) > steps:
#         del adjacency_list[key]
#     else:
#         check2 = set(adjacency_list[key].keys())
#         for neighbor in check2:
#             if manhattan(start, neighbor) > steps:
#                 del adjacency_list[key][neighbor]

# stolen dijkstra strikes back
import sys

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.keys())
    shortest_path = {}
    previous_nodes = {}

    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors = graph[current_min_node].keys()
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph[current_min_node][neighbor]
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)
        print(len(unvisited_nodes))

    return shortest_path

# uncomment for part 1
# path = dijkstra_algorithm(adjacency_list, start)
#
# reachable = []
# for key in path.keys():
#     if path[key] <= steps and manhattan(start, key) % 2 == steps % 2:
#         reachable.append(key)
#
# print(len(reachable))

# some prep for part 2 - it didn't work in the end

# path_up = dijkstra_algorithm(adjacency_list, (start[0], len(lines) - 1))
#
# total_up = 0
# max_up = 0
# for key in path_up.keys():
#     if path_up[key] < sys.maxsize/2:
#         total_up += 1
#         if path_up[key] > max_up:
#             max_up = path_up[key]
#
# print(total_up, max_up)
#
# path_down = dijkstra_algorithm(adjacency_list, (start[0], 0))
#
# total_down = 0
# max_down = 0
# for key in path_down.keys():
#     if path_down[key] < sys.maxsize/2:
#         total_down += 1
#         if path_down[key] > max_down:
#             max_down = path_down[key]
#
# print(total_down, max_down)
#
# path_left = dijkstra_algorithm(adjacency_list, (len(lines[0]) - 1, start[1]))
#
# total_left = 0
# max_left = 0
# for key in path_left.keys():
#     if path_left[key] < sys.maxsize/2:
#         total_left += 1
#         if path_left[key] > max_left:
#             max_left = path_left[key]
#
# print(total_left, max_left)
#
# path_right = dijkstra_algorithm(adjacency_list, (0, start[1]))
#
# total_right = 0
# max_right = 0
# for key in path_right.keys():
#     if path_right[key] < sys.maxsize/2:
#         total_right += 1
#         if path_right[key] > max_right:
#             max_right = path_right[key]
#
# print(total_right, max_right)
#
# left_up = 0
# left_down = 0
# right_up = 0
# right_down = 0
# left = 0
# up = 0
# right = 0
# down = 0
# for key in path_left.keys():
#     if path_up[key] < 131 or path_left[key] < 131:
#         left_up += 1
#     if path_up[key] < 131 or path_right[key] < 131:
#         right_up += 1
#     if path_down[key] < 131 or path_left[key] < 131:
#         left_down += 1
#     if path_down[key] < 131 or path_right[key] < 131:
#         right_down += 1
#     if path_up[key] < 131:
#         up += 1
#     if path_down[key] < 131:
#         down += 1
#     if path_left[key] < 131:
#         left += 1
#     if path_right[key] < 131:
#         right += 1
#
# print(right_up + right_down + left_up + left_down)
# print(up+left+right+down)
#
#
# path_nw = dijkstra_algorithm(adjacency_list, (130, 130))
# path_se = dijkstra_algorithm(adjacency_list, (0, 0))
# path_ne = dijkstra_algorithm(adjacency_list, (0, 130))
# path_sw = dijkstra_algorithm(adjacency_list, (130, 0))
#
# sw = 0
# nw = 0
# ne = 0
# se = 0
# for key in path_nw.keys():
#     if path_nw[key] < 65:
#         nw += 1
#     if path_ne[key] < 65:
#         ne += 1
#     if path_sw[key] < 65:
#         sw += 1
#     if path_se[key] < 65:
#         se += 1
#
# print(nw + ne + sw + se)

# 607331303128606 too low (assumes N = 202298)
# 607337307407444 too high (assumes N = 202299)

# reddit stealing time

start = (327, 327)
steps = 327
check1 = set(adjacency_list.keys())
for key in check1:
    if manhattan(start, key) > steps:
        del adjacency_list[key]
    else:
        check2 = set(adjacency_list[key].keys())
        for neighbor in check2:
            if manhattan(start, neighbor) > steps:
                del adjacency_list[key][neighbor]

# hope you aren't doing anything in next 30-50 minutes
path = dijkstra_algorithm(adjacency_list, start)

ans_65 = ans_196 = ans_327 = 0
for key in path.keys():
    if path[key] <= 65 and manhattan(start, key) % 2 == 65 % 2:
        ans_65 += 1
    if path[key] <= 196 and manhattan(start, key) % 2 == 196 % 2:
        ans_196 += 1
    if path[key] <= 327 and manhattan(start, key) % 2 == 327 % 2:
        ans_327 += 1

print(ans_65, ans_196, ans_327)

# 65 - 3751
# 196 - 33531
# 327 - 92991

# find a parabola with f(0) = ans_65, f(1) = ans_196, f(2) = ans_327. Answer to part 2 is f(202300)