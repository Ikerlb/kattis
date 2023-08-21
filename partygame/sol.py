tcs = int(input())

def cond(arr, s):
    done = True
    used = False
    for i, n in enumerate(arr):
        if i == n:
            continue
        done = False
        if (i, n) in s:
            used = True
    return done, used

def solve(arr):
    aux = arr[:]
    s = set()
    while True:
        done, used = cond(arr, s)
        if done or used:
            break
        for i, n in enumerate(arr):
            aux[i] = arr[n]
        arr, aux = aux, arr
        s.update(enumerate(aux))
    return done

for _ in range(tcs):
    input()
    arr = [int(n) - 1 for n in input().split(" ")]
    if solve(arr):
        print("All can eat.")
    else:
        print("Some starve.")
