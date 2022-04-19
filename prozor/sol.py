from math import inf

r, s, k = map(int, input().split(" "))

m = [[int(c == "*") for c in input()] for _ in range(r)]
ps = [[m[row][col] for col in range(s)] for row in range(r)]

for col in range(1, s):
    ps[0][col] += ps[0][col - 1]

for row in range(1, r):
    ps[row][0] += ps[row - 1][0]

for col in range(1, s):
    for row in range(1, r):
        ps[row][col] += ps[row - 1][col] + ps[row][col - 1] - ps[row - 1][col - 1]

def query(ps, r1, c1, r2, c2):
    if r1 == c1 == 0:    
        return ps[r2][c2]
    elif r1 == 0:
        return ps[r2][c2] - ps[r2][c1 - 1]
    elif c1 == 0:
        return ps[r2][c2] - ps[r1 - 1][c2]
    return ps[r2][c2] - ps[r2][c1 - 1] - ps[r1 - 1][c2] + ps[r1 - 1][c1 - 1]

k = k - 2
resr = resc = None
res = -inf
for row in range(1, r - k):
    for col in range(1, s - k):
        rr = query(ps, row, col, row + k - 1, col + k - 1)
        if rr > res:
            resr, resc, res = row, col, rr
            


#print(ps)
#print(resr, resc, res)


corners = [
        (resr - 1, resc - 1),
        (resr - 1, resc + k),
        (resr + k, resc - 1),
        (resr + k, resc + k)
]

print(res)
for row in range(r):
    rr = []
    for col in range(s):
        if (row, col) in corners:
            rr.append("+")    
        elif (col == resc - 1 or col == resc + k) and resr <= row <= resr + k:
            rr.append("|")
        elif (row == resr - 1 or row == resr + k) and resc <= col <= resc + k:
            rr.append("-")
        else:
            rr.append("*" if m[row][col] == 1 else ".")
    print("".join(rr))
