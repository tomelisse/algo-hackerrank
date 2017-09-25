from collections import defaultdict as dd
from operator import itemgetter

class Graph(object):
    def __init__(self, n):
        ''' init '''
        self.adj  = dd(list)
        self.cost = {node : 100001 for node in range(1, n+1)}
        self.total_cost = 0
                    
    def update_costs(self, node):
        ''' update costs '''
        del self.cost[node]
        for neighbour, weight in self.adj[node]:
            if neighbour in self.cost and self.cost[neighbour] > weight:                
                 self.cost[neighbour] = weight

     def prim(self, node):
         ''' Prim's algorithm '''
         self.total_cost += self.cost[node]
         self.update_costs(node)
         if self.cost:
             node = min(self.cost.items(), key = itemgetter(1))[0]
             self.prim(node)

 if __name__ == '__main__':
     n, m = list(map(int, input().split()))
     g = Graph(n)
     for _ in range(m):
         u, v, r = list(map(int, input().split()))
         g.adj[u].append((v,r))
         g.adj[v].append((u,r))
     start = int(input())
     g.cost[start] = 0
     g.prim(start)
     print(g.total_cost)
