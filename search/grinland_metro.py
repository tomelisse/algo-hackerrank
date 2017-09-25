from collections import defaultdict as dd

def lampposts():
    n, m, k = list(map(int, input().split()))
    rowroads = dd(list)
    for _ in range(k):
        r, c1, c2 = list(map(int, input().split())) 
        rowroads[r].append((c1, c2))
        taken = 0
        for r in rowroads:
            roads = sorted(rowroads[r])
            previous_end = -1
            for road in roads:
                start = road[0]
                end   = road[1]
                if start <= previous_end:
                    start = previous_end + 1
                    if end > previous_end:
                        taken += end - start + 1
                        previous_end = end
    print(n*m - taken)
                

if __name__ == '__main__':
        lampposts()
