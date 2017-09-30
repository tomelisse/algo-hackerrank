def partition(A):
    if len(A) == 0:
        return A
    p    = A[0]
    pre  = []
    piv  = []
    post = []
    for x in A:
        if x < p:
            pre.append(x)
        if x > p:
            post.append(x)
        if x == p:
            piv.append(x)
    pre  = partition(pre)
    post = partition(post)
    return pre + piv + post

if __name__ == '__main__':
    A = [int(x) for x in list(map(int, input().split()))]
    print(' '.join([str(x) for x in partition(A)]))
