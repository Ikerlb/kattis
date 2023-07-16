from sys import stdin

def is_integer(string):
  if string[0] == '-':
    return string[1:].isdigit()
  else:
    return string.isdigit()

class Node:
    def __init__(self, val, left = None, right = None, terminal = True):
        self.val = val
        self.left = left
        self.right = right
        self.terminal = terminal

    def __repr__(self):
        if self.terminal:
            return f"{self.val}"
        return f"{self.val} {self.left} {self.right}"

f = {
    "+": lambda x,y: x + y, 
    "*": lambda x,y: x * y,
    "-": lambda x,y: x - y,
}

def parse(tokens):
    if not tokens:
        return None
    val = tokens.pop()
    if is_integer(val):
        return Node(int(val))
    elif val.isalpha():
        return Node(val)
    else:
        return Node(val, left = parse(tokens), right = parse(tokens), terminal = False)

def simpl(node):
    if node.terminal:
        return node.val
    l = simpl(node.left)
    r = simpl(node.right)
    if type(l) is int and type(r) is int:
        return f[node.val](l,r)
    node.left = l
    node.right = r
    return node

for i, line in enumerate(stdin, 1):
    tokens = line[:-1].split(" ")
    tokens.reverse()
    root = parse(tokens) 
    nroot = simpl(root)
    print(f"Case {i}: {nroot}")
