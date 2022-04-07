def idfk(i, path):
    if path > limit:
        return
    if i == 9 or i == 11:
        res.add(path)
        return
    if i == 10:
        res.add(path)
        if path == 0: 
            return
        idfk(i, path * 10)
        return
    idfk(i, path * 10 + (i + 1))
    if i % 3 != 2:
        idfk(i + 1, (path * 10) + (i + 1))
        idfk(i + 1, path)
    idfk(i + 3, (path * 10) + (i + 1))
    idfk(i + 3, path)

limit = 200
res = set()
idfk(0, 0)
#print(sorted(res))

tcs = int(input())
for _ in range(tcs):
    k = int(input())    
    print(min(res, key = lambda x: abs(k - x)))
