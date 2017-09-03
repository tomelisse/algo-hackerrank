from collections import defaultdict as dd

def DFS(graph, city, visited):
    access = 0
    visited[city] = True
    for neighbour in graph[city]:
        if not visited[neighbour]:
            access += 1 + DFS(graph, neighbour, visited)
    return access

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n, m, cl, cr = list(map(int, input().split()))
        graph = dd(list)
        for _ in range(m):
            city1, city2 = list(map(int, input().split()))
            graph[city1].append(city2)
            graph[city2].append(city1)
        visited = {city : False for city in range(1, n+1)}
        roads     = 0
        libraries = 0
        for city in graph.keys():
            if not visited[city]:
                libraries += 1
                roads     += DFS(graph, city, visited)
        singles = sum([1 for value in visited.values() if not value])
        libraries += singles
        print(min(cl*n, libraries*cl + roads*cr))
