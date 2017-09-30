def count(A):
    counts = [0 for _ in range(100)]
    for x in A:
        counts[x] += 1
    return counts
    
def order(A):
    counts = count(A)
    ordered = []
    for i, x in enumerate(counts):
        ordered.extend([i]*x)
    return ordered
       
    
if __name__ == '__main__':
    n = int(input())
    A = [int(x) for x in list(map(int, input().split()))]
    print(' '.join([str(x) for x in order(A)]))
