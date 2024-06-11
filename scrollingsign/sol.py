# longest common suffix/prefix
def solve(words, k):
    res = words[0][:]
    for w in words[1:]:
        for i in reversed(range(k)):
            if res[-i-1:] == w[:i + 1]:
                res.extend(w[i + 1:])
                break
        else:
            res.extend(w)
    return len(res)

tcs = int(input())
for _ in range(tcs):
    k, w = map(int, input().split(" "))
    words = [list(input()) for _ in range(w)]
    print(solve(words, k))
