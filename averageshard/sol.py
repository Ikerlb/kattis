tcs = int(input())

def solve(comp, econ):
    sc = sum(comp)
    ac = sc / len(comp)
    se = sum(econ)
    ae = se / len(econ)

    
    res = 0
    for c in comp:
        #print("new csci average", (sc - c) / (len(comp) - 1))
        #print("new econ average", (se + c) / (len(econ) + 1))
        if (sc - c) / (len(comp) - 1) <= ac:
            continue
        if (se + c) / (len(econ) + 1) <= ae:
            continue
        res += 1
    return res

for _ in range(tcs):
    _ = input()
    _ = input()
    comp = list(map(int, input().split(" ")))
    econ = list(map(int, input().split(" ")))
    print(solve(comp, econ))



