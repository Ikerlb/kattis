def tokenize(s):
    l = []
    cur = []
    for c in s:
        if c in "{,}" and not cur:
            l.append(c)
        elif c in "{,}":
            l.append("".join(cur))
            cur = []
            l.append(c)
        else:
            cur.append(c)
    return l

def parse(tokens):
    s = [[]]
    for t in tokens:
        if t == ",": 
            continue
        elif t == "{":
            s.append([])
        elif t == "}":
            last = s.pop()
            s[-1].append(last)
        else:
            s[-1].append(t)
    return s[0].pop()


def dfs(node, indent, last, res):
    bstart, bend = "{", "}"
    spaces = " " * (indent * 2)
    comma = "," if not last else ""
    if type(node) == list:
        res.append(f"{spaces}{bstart}")
        for nn in node[:-1]:
            dfs(nn, indent + 1, False, res)
        for nn in node[-1:]:
            dfs(nn, indent + 1, True, res)
        res.append(f"{spaces}{bend}{comma}")
    else:
        res.append(f"{spaces}{node}{comma}")

s = input()
tokens = tokenize(s)
node = parse(tokens)
res = []
dfs(node, 0, True, res)
print("\n".join(res))
