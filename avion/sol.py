from sys import stdin

def solve(codes):
    res = []
    for i, code in enumerate(codes):
        if "FBI" in code:
            res.append(str(i + 1))
    if not res:
        return "HE GOT AWAY!"
    return " ".join(res)

lines = [line[:-1] for line in stdin]
print(solve(lines))
