# roomGraph={0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}]}
# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}]}
# roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5, 'w': 11}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}], 9: [(1, 4), {'n': 8, 's': 10}], 10: [(1, 3), {'n': 9, 'e': 11}], 11: [(2, 3), {'w': 10, 'e': 6}]}
roomGraph={0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2, 'e': 12, 'w': 15}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5, 'w': 11}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7, 's': 9}], 9: [(1, 4), {'n': 8, 's': 10}], 10: [(1, 3), {'n': 9, 'e': 11}], 11: [(2, 3), {'w': 10, 'e': 6}], 12: [(4, 6), {'w': 1, 'e': 13}], 13: [(5, 6), {'w': 12, 'n': 14}], 14: [(5, 7), {'s': 13}], 15: [(2, 6), {'e': 1, 'w': 16}], 16: [(1, 6), {'n': 17, 'e': 15}], 17: [(1, 7), {'s': 16}]}


def find_dead_ends(graph):
    dead_ends = 0
    for i in graph.values():
        if len(i[1]) == 1:
            dead_ends += 1
    return dead_ends


def num_deg(graph):
    degrees = 0
    for i in graph.values():
        degrees += len(i[1])
    return degrees

def find_cycles(map,stack):
    current = stack[-1]
    neighboors = map[current][1]
    index = None
    if len(stack) < 4:
        return stack
    for a,b in neighboors.items():
        for i,j in enumerate(stack):
            if b == j and (index is None or i < index):
                index = i
    if index is not None and index+2 < len(stack):
        stack = stack[:index+2]
    return stack


def dft(graph):
    stack = []
    visited = set()
    path = []
    stack.append(0)
    while len(visited) != len(graph):

        current = stack[-1]

        if len(path)>0:
            print(stack,path[-1])
        
        visited.add(current)
        neighboors = graph[current][1]
        next_neighboor = []
        for i,j in neighboors.items():
            
            if j not in visited:
                next_neighboor.append(j)

        if len(next_neighboor) == 0:
            # stack = find_cycles(graph,stack)
            tile = stack[-2]
            stack.pop()
        else:
            tile = next_neighboor[0]
            stack.append(next_neighboor[0]) 

        for a,b in neighboors.items():
            if b == tile:
                path.append(a) 



    # print(visited,"visited")
    # print(stack,"stack")
    print(len(visited),"after while")
    print(path)
    return path


# print(num_deg(roomGraph))
# print(find_dead_ends(roomGraph))
# print(dft(roomGraph))

