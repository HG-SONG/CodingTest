from collections import deque

numberOfNode, numberOfEdge = map(int, input().split())

graph = {}

def makeGraph(key, value):
    if key not in graph:
        graph[key] = []
    graph[key].append(value)

def bfs():
    visited = {}
    count = 0 

    for key in graph.keys():
        if key in visited:
            continue  

        queue = deque()
        queue.append(key)
        visited[key] = set()

        while queue:
            node = queue.popleft()
            if node not in graph:
                continue

            if node not in visited:
                visited[node] = set()

            for neighbor in graph[node]:
                if neighbor not in visited[node]:
                    queue.append(neighbor)
                    visited[node].add(neighbor)

        count += 1

    print(count)

for _ in range(numberOfEdge):
    node, neighbor = map(int, input().split())
    makeGraph(node, neighbor)

bfs()
