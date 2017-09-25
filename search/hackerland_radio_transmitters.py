if __name__ == '__main__':
    n, k      = list(map(int, input().split()))
    locations = list(map(int, input().split()))
    locations.sort()
    # first-left house without access to a transitter
    start = locations[0]
    # initial number of needed transmitters
    m     = 1
    for x in locations:
        if x - start <= k:
            trans = x
        elif x - trans > k:
            m += 1
            start = x
            print(m)
