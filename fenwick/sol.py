

def query(ft, i):
    s = 0
    while i > 0:
        s += ft[i] 
        i -= i & (-i)
    return s

def update(ft, i, delta):
    while i < len(ft):
        ft[i] += delta
        i += i & (-1)

n, tc = map(int, input().split(" "))

ft = [0 for _ in range(n + 1)]

for _ in range(tc):
    line = input().split(" ")
    if line[0] == "?":
        k = int(line[1])
        print(f"{query(ft, k)}")
    else:
        k, delta = map(int, line[1:])
        update(ft, k + 1, delta)
