from collections import defaultdict as dd

def find_flavours(m, costs):
    costs_to_id = {c : i+1 for (i, c) in enumerate(costs)}
    costs_to_id = dd(list)
    for i, c in enumerate(costs):
        costs_to_id[c].append(i+1)
        for c, i in costs_to_id.items():
            if m - c == c and len(costs_to_id[c]) == 2:
                ids = list(map(str, sorted(costs_to_id[c])))
                break
            elif m - c in costs_to_id:
                ids = list(map(str, sorted([i[0], costs_to_id[m-c][0]])))
                break
    print(' '.join(ids))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        m = int(input())
        n = int(input())
        costs = list(map(int, input().split()))
        find_flavours(m, costs)
