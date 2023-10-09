from sys import stdin

r = c = 0
mxr = mnr = 0
mxc = mnc = 0

s = {(0, 0)}

for line in stdin:
    if line.startswith("down"):
        r += 1
    elif line.startswith("left"):
        c -= 1
    elif line.startswith("right"):
        c += 1
    elif line.startswith("up"):
        r -= 1

    s.add((r, c))

    mxr = max(mxr, r)
    mnr = min(mnr, r)

    mxc = max(mxc, c)
    mnc = min(mnc, c)

er, ec = r, c

# format
res = []
res.append("".join("#" for _ in range(mnc, mxc + 3)))
for r in range(mnr, mxr + 1):
    row = []
    row.append("#")
    for c in range(mnc, mxc + 1):
        if r == c == 0:
            row.append("S")
        elif r == er and c == ec: 
            row.append("E")
        elif (r, c) in s:
            row.append("*")
        else:
            row.append(" ")
    row.append("#")
    res.append("".join(row))
res.append("".join("#" for _ in range(mnc, mxc + 3)))

print("\n".join(res))
