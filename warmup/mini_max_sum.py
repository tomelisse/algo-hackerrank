if __name__ == '__main__':
    ar = list(map(int, input().split()))
    mi = min(ar)
    ma = max(ar)
    su = sum(ar)
    print(su-ma, su-mi)
