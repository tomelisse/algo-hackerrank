from collections import defaultdict as dd
from collections import deque

class graph(object):
    def __init__(self):
        ''' init '''
        self.children = dd(list)
        self.subtree_size = dict()
        self.removed_branches = 0
                
    def find_subtree_size(self, node):
        ''' find sizes of each subtree rooted in the node - DFS'''
        subtree_size = 1
        for child in self.children[node]:
        subtree_size += self.find_subtree_size(child)
        self.subtree_size[node] = subtree_size
        return subtree_size
        
    def cut_branches(self):
        ''' cut max number of branches to create a forest of even trees - BFS'''
        queue = deque()
        queue.append(1)
        while len(queue) > 0:
            node = queue.popleft()
            for child in self.children[node]:
                queue.append(child)
                if self.subtree_size[child]%2 == 0:
                    self.removed_branches += 1

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    g = graph()
    for _ in range(m):
        u, v = list(map(int, input().split()))
        g.children[v].append(u)
        g.find_subtree_size(1)
        g.cut_branches()
        print(g.removed_branches)
