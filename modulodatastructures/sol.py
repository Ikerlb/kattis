from math import floor, sqrt

N, Q = map(int, input().split(" "))

arr = [0 for _ in range(N)]

sqr = floor(sqrt(len(arr)))

for _ in range(Q):
    op, rest = input().split(" ", 1)
    if op == "1":
        A, B, C = map(int, rest.split(" "))
        # for example if B = 7, N = 30
        if B <= sqr:
            
        else:
            
    else:
        print(arr[int(rest) - 1])

print(sqr)
