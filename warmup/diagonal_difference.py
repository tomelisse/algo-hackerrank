if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) 
           for _ in range(n)]  
    d1 = sum([arr[i][i] for i in range(n)])
    d2 = sum([arr[i][n-i-1] for i in range(n)]) 
    print(abs(d1-d2))
