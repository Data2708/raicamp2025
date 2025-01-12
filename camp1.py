# print(1)

# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

###############
#     A
#    / \
#   B   C
#  / \    \
# D   E    F
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

start = 'A'
goal = 'E'
frontier = [start]
explored = set()

print(frontier, explored)

while len(frontier) > 0:
    current = frontier.pop() 
    print(current)

    if current == goal:
        print("Goal reach")
        break
    
    for neighbor in graph [current]:
        frontier.append(neighbor)