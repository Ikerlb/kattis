def divisors(n):
    for i in range(1, n + 1):
        d, m = divmod(n, i)
        if m == 0:
            yield i, d

def smallest_support(s):
    for d1, d2 in divisors(len(s)):
        if s[:d1] * d2 == s:
            return d1
    return 

def direction(c):
    if c == "<":
        return (0, -1)
    elif c == ">":
        return (0, 1)
    elif c == "^":
        return (-1, 0)
    else:
        return (1, 0)

N = int(input())
#s = input()
ss = input()
s = ss[:smallest_support(ss)]
#print(f"{s=} <----> {ss=}")

instructions = [direction(c) for c in s]

grid = [list(input()) for _ in range(N)]

def move(grid, r, c, dr, dc):
    nr = r + dr
    nc = c + dc
    if grid[nr][nc] != "#": 
        return nr, nc
    return r, c 


sr = sc = None
for r in range(N):
    for c in range(N):
        if grid[r][c] == 'R':
            grid[r][c] = '.' 
            sr, sc = r, c

r, c = sr, sc
d = {}

# all operations
# which resulted
# in a different
# move than prev
operations = []

time = 0
while (tup := (r, c, time % len(instructions))) not in d:
    d[tup] = time
    dr, dc = instructions[time % len(instructions)]
    nr, nc = move(grid, r, c, dr, dc)
    if (nr, nc) != (r, c):
        operations.append(time)
    r, c = nr, nc
    time += 1

cyc_start = d[r, c, time % len(instructions)]
start = 0
while start < len(operations) and operations[start] < cyc_start: 
    start += 1

ns = "".join(s[i % len(instructions)] for i in operations[start:])

res = smallest_support(ns)

print("1" if not res else res)
