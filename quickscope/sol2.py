from sys import stdin
from collections import defaultdict

context = [{}]

h = defaultdict(list)
n = int(input())

for line in stdin:
    line = line[:-1].strip()
    if line == "{":
        context.append({})
        continue
    elif line == "}":
        for k in context[-1]:
            h[k].pop()
            if not h[k]:
                del h[k]
        context.pop()
        continue
    #print(line)
    op, rest = line.split(" ", 1)
    if op == "DECLARE":
        i, t = rest.split(" ")
        if i in context[-1]:
            print("MULTIPLE DECLARATION")
            break
        else:
            context[-1][i] = t
            h[i].append(len(context) - 1)
    else:
        i = rest
        if i not in h:
            print("UNDECLARED")
        else:
            print(context[h[i][-1]][i])
