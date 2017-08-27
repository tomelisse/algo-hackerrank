def inRange(dist, s, t, x):
    return sum([1 for d in dist if x + d >= s and x + d <= t])

if __name__ == '__main__':
    s, t = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    m, n = list(map(int, input().split()))
    print(inRange(list(map(int, input().split())), s, t, a))
    print(inRange(list(map(int, input().split())), s, t, b))
