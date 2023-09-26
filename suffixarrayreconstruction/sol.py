def solve(l, suffixes):
    d = [None for _ in range(l)]
    for i, suffix in suffixes:
        asterisc = suffix.find("*")

        if asterisc == -1: # no asterisc
            for j, c in enumerate(suffix):
                if d[j + i] is None:
                    d[j + i] = c
                elif d[j + i] == c:
                    continue
                else:
                    return "IMPOSSIBLE"
        else:
            # otherwise the asterisc spans l - i - len(suffix) + 1
            span = l - i - len(suffix) + 1
            for j, c in enumerate(suffix[:asterisc]):
                if d[j + i] is None:
                    d[j + i] = c
                elif d[j + i] == c:
                    continue
                else:
                    return "IMPOSSIBLE"
            for j, c in enumerate(suffix[asterisc + 1:], asterisc):
                if d[span + j + i] is None:
                    d[span + j + i] = c
                elif d[span + j + i] == c:
                    continue
                else:
                    return "IMPOSSIBLE"

    if any(c is None for c in d):
        return "IMPOSSIBLE"

    return "".join(d)

def parse(s):
    si, s = s.split(" ")
    return int(si) - 1, s

tcs = int(input())
for _ in range(tcs):
    l, s = map(int, input().split(" "))

    d = [None for _ in range(l)]
    suffixes = [parse(input()) for _ in range(s)]

    print(solve(l, suffixes))
