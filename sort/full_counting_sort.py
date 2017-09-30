def counts(A):
    count = [0 for _ in range(100)]
    for x in A:
        count[x] += 1
    return count

def positions(A):
    count = counts(A)
    position = [0]
    prev = 0
    for x in count[:-1]:
        position.append(prev + x)
        prev += x
    return position
        
def order(A, B):
    position = positions(A)    
    ordered = ['' for _ in range(len(A))]
    for x, s in zip(A, B):
        ordered[position[x]] = s
        position[x] += 1
    return ordered
       
    
if __name__ == '__main__':
    n = int(input())
    A = []
    B = []
    for i in range(n):
        x, s = input().split()
        x = int(x)
        if i < n/2:
            s = '-'
        A.append(x)
        B.append(s)
    print(' '.join([str(x) for x in order(A, B)]))
