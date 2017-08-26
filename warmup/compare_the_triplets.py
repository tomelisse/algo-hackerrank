def solve(Alice, Bob):
    a = sum([1 for x, y in zip(Alice, Bob) if x > y])
    b = sum([1 for x, y in zip(Alice, Bob) if x < y])    
    return a, b

Alice = list(map(int, input().split()))
Bob   = list(map(int, input().split()))
result = solve(Alice, Bob)
print (" ".join(map(str, result)))
