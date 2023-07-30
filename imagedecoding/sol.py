import sys

stdin = sys.stdin

ch = ["#", "."]

def decode(scanline):
    sp = scanline.split(" ")
    cur = int(sp[0] != "#")
    res = []
    length = 0
    for n in sp[1:]:
        nenc = ch[cur] * int(n)
        res.extend(nenc)
        cur = 1 - cur
        length += len(nenc)
    return res, length

def solve(scanlines):
    res = []
    cln = None
    diff = False
    for sl in scanlines:
        enc, ln = decode(sl)
        if cln is not None and cln != ln:
            diff = True
        diff = diff or (cln is not None and cln != ln)
        res.append("".join(enc)) 
        cln = ln
    if diff:
        res.append("Error decoding image")
    return "\n".join(res)

res = []
while (n := int(next(stdin))) != 0:  
    scanlines = [next(stdin)[:-1] for _ in range(n)]
    res.append(solve(scanlines))
print("\n\n".join(res))
