def partition(A):
    p = A[0]
    pre = []
    post = []
    for x in A:
        if x < p:
            pre.append(x)
        if x > p:
            post.append(x)
    return pre + [p] + post

if __name__ == '__main__':
    n = int(input())
    A = [int(x) for x in list(map(int, input().split()))]
    print(' '.join([str(x) for x in partition(A)]))
