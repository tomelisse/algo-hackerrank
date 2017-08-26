if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    p = float(sum([1 for x in arr if x > 0]))
    m = float(sum([1 for x in arr if x < 0]))
    z = float(sum([1 for x in arr if x == 0]))
    print(p/n, m/n, z/n, sep = '\n')
