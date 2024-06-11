from collections import defaultdict

def last_idx(w):
    res = [-1 for _ in range(26)]
    for i, c in enumerate(w):
        res[ord(c) - ord('a')] = i
    return res

n, m = map(int, input().split(" "))
dictionary = [input() for _ in range(n)]
plates = [input().lower() for _ in range(m)]
lasts = [last_idx(w) for w in dictionary]

d = defaultdict(dict)
for p in plates:
    d[p[:2]][p[2]] = None

done = {}

for wi, w in enumerate(dictionary):
    for i in range(len(w)):
        for j in range(i + 1, len(w)):
            to_rem = []
            p = w[i] + w[j]
            for thd in d[p]:
                if lasts[wi][ord(thd) - ord('a')] > j:
                    to_rem.append(thd)
            for thd in to_rem:
                done[p + thd] = wi
                del d[p][thd]

for p in plates:
    if p in done:
        print(dictionary[done[p]])
    else:
        print("No valid word")
