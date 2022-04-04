def subset(arr, m):
    if not arr:
        #print(f"{arr=} prev={[[]]}")
        return [[]]
    prev = subset(arr[1:], m)
    ignore = set()
    for a, b in m:
        for i, p in enumerate(prev):
            if (a == arr[0] and b in p) or (b == arr[0] and a in p):
                ignore.add(i)
            
    for i in range(len(prev)):
        if i not in ignore:
            prev.append(prev[i] + [arr[0]])
    #print(f"{arr=} {prev=}")
    return prev

n, m = map(int, input().split(" "))
restr = [sorted(map(int, input().split(" "))) for _ in range(m)]
#print(restr)
arr = list(range(1, n + 1))
print(len(subset(arr, restr)))
