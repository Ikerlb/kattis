import re

class Node:
    def __init__(self, val = None):
        self.children = []
        self.val = val 
        self.op = "?"

    def __repr__(self):
        if self.val is not None:
            return f"{self.val}"
        inside = self.op.join(f"{ch}" for ch in self.children)
        return f"({inside})"

def parse(tokens):
    s = [Node()]
    for tok in tokens:
        if tok == "(":
            n = Node()
            s[-1].children.append(n)
            s.append(n)
        elif tok == ")":
            s.pop()
        elif tok[0] == "R":
            s[-1].children.append(Node(tok))
        elif tok in "|-":
            s[-1].op = tok
    return s[0].children[0]        

def tokenize(s):
    res = []
    for tok in re.split(r'(R[0-9]+|[()|])', s):
        if tok.strip() == "":
            continue
        res.append(tok)
    return res

def _eval(node, d):
    if node.val is not None:
        return d[int(node.val[1:])]
    vals = [_eval(nn, d) for nn in node.children] 
    if node.op == "-":
        return sum(vals)
    return 1/(sum(1/v for v in vals))

n = int(input())
vals = {i:v for i, v in enumerate(map(float, input().split(" ")), 1)}
expr = input()

tokens = tokenize(expr)
n = parse(tokens)
print(_eval(n, vals))
