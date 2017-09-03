from collections import defaultdict as dd
from collections import deque

class graph(object):
    def __init__(self, n):
        self.n = n
        self.len = 6
        self.distance = {node : -1 for node in range(1, n+1)}
        self.adj = dd(list)
        self.queue = deque()

    def BFS(self, start):
        self.queue.append(start)
        while len(self.queue) > 0:
            node = self.queue.popleft()
            for neighbour in self.adj[node]:
                if self.distance[neighbour] == -1:
                    self.distance[neighbour] = self.distance[node] + self.len
                    self.queue.append(neighbour)       

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
    n, e = list(map(int, input().split()))
    g = graph(n)
    for _ in range(e):
        u, v = list(map(int, input().split()))
        g.adj[u].append(v)
        g.adj[v].append(u)
    s = int(input())        
    g.distance[s] = 0
    g.BFS(s)
    del g.distance[s]
    print(' '.join([str(dist) for dist in g.distance.values()]))
