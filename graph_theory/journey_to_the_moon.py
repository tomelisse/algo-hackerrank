from collections import defaultdict as dd

def connected(graph, person, visited):
    ''' calculates the number of nodes in a connected subgraph'''
    visited[person] = True
    counts = 1
    for neighbour in graph[person]:
        if neighbour not in visited:
            counts += connected(graph, neighbour, visited)
    return counts            

def nationalities(graph, n):
    ''' calculates the number of people of each nationality'''
    #visited = {person : False for person in range(n)}
    visited = dict()
    counts = []
    for person in graph:
        if person not in visited:
            counts.append(connected(graph, person, visited))
    singles = n - len(visited)
    for single in range(singles):
        counts.append(1)
    return counts
        

if __name__ == '__main__':
    n, p = list(map(int, input().split()))
    graph = dd(list)
    for _ in range(p):
        person1, person2 = list(map(int, input().split()))
        graph[person1].append(person2)
        graph[person2].append(person1)
        counts = nationalities(graph, n)
        sum = 0
        for i in counts:
            sum += i*(n-i)
            sum = int(sum/2)
            print(sum)
