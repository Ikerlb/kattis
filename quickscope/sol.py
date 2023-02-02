from sys import stdin

OPEN_SCOPE = 1
CLOSE_SCOPE = 2
TYPE_DECLARATION = 3
TYPE_QUERY = 4

class Token:
    def __init__(self, token, ident = None, ttype = None):
        self.token = token
        self.ident = ident
        self.ttype = ttype

    def __repr__(self):
        if self.token == "OPEN_SCOPE":
            return "{"
        elif self.token == "CLOSE_SCOPE":
            return "}"
        elif self.token == "TYPE_DECLARATION":
            return f"{self.ident}: {self.ttype}"
        else:
            return f"{self.ident}?"

def tokenize(line):
    stripped = line.strip()
    if stripped == "{":
        return Token(OPEN_SCOPE)
    elif stripped == "}":
        return Token(CLOSE_SCOPE)
    elif stripped.startswith("DECLARE"):
        _, ident, ttype = stripped.split(" ")
        return Token(TYPE_DECLARATION, ident = ident, ttype = ttype)
    else:
        _, ident = stripped.split(" ")
        return Token(TYPE_QUERY, ident = ident)

def find_first(contexts, k):
    for d in reversed(contexts):
        if k in d:
            return d[k]
    return None

n = int(input())

tokens = [tokenize(input()) for _ in range(n)]

contexts = [{}]
lookup = {}

# prune
prev = None
ignore = set()
for i, t in enumerate(tokens):
    if prev and t.token == CLOSE_SCOPE and prev.token == OPEN_SCOPE:
        ignore.add(i)
        ignore.add(i - 1)
    prev = t

for i, t in enumerate(tokens):
    if i in ignore:
        continue
    if t.token == OPEN_SCOPE:
        contexts.append({})
    elif t.token == CLOSE_SCOPE:
        d = contexts.pop()
        for k in d:
            del lookup[k]
    elif t.token == TYPE_DECLARATION and t.ident not in contexts[-1]:
        contexts[-1][t.ident] = t.ttype
        lookup[t.ident] = len(contexts) - 1
    elif t.token == TYPE_DECLARATION:
        print("MULTIPLE DECLARATION")
        break
    else:
        #v = find_first(contexts, t.ident)
        if t.ident in lookup:
            level = lookup[t.ident]
            print(contexts[level][t.ident])
        else:
            print("UNDECLARED")
