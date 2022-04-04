s = input()

stack = []

d = []
for i, c in enumerate(s):
    if c == "(":
        stack.append(i)
    elif c == ")":
        d.append((stack.pop(), i))

res = set()
for ss in range(1, 1 << len(d)):
    ex = set()
    for i in range(len(d)):
        if ss & (1 << i):
            start, end = d[i]
            ex.add(start)
            ex.add(end)
    res.add("".join(c for i, c in enumerate(s) if i not in ex))

for s in sorted(res):
    print(s)
