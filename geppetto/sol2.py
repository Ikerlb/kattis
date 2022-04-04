def subset(arr):
    if not arr:    
        return [()]
    prev = subset(arr[1:])
    for i in range(len(prev)):
        prev.append(prev[i] + (arr[0],))
    return prev

n, m = map(int, input().split(" "))
restr = [tuple(map(int, input().split(" "))) for _ in range(m)]
arr = list(range(1, n + 1))
illegal = set()
for ss in subset(arr):
    for a, b in restr:
        if a in ss and b in ss:
            illegal.add(ss)
            continue    
print(2 ** n - len(illegal))
