class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if self.val in "pqrst":
            return f"{self.val}"
        if self.val == "K":
            return f"AND({self.left},{self.right})"
        elif self.val == "A":
            return f"OR({self.left},{self.right})"
        elif self.val == "N":
            return f"NOT({self.left})"
        elif self.val == "C":
            return f"IMPL({self.left},{self.right})"
        else:
            return f"EQ({self.left},{self.right})"

    def idfk(self):
        if self.val in "pqrst":
            return f"{self.val}"
        elif self.val in "KACE":
            return f"{self.val}{self.left.idfk()}{self.right.idfk()}"
        else:
            return f"{self.val}{self.left.idfk()}"
        

def parse(s):
    if not s:
        return None
    c = s.pop()
    ret = Node(c)
    if c in "KACE":
        ret.left = parse(s)
        ret.right = parse(s)
    elif c == "N": 
        ret.left = parse(s)
    return ret

def _eval(node, table):
    if node.left is None and node.right is None:
        return table[node.val]
    elif node.val == "K":
        return _eval(node.left, table) and _eval(node.right, table)
    elif node.val == "A":
        return _eval(node.left, table) or _eval(node.right, table)
    elif node.val == "N":
        return not _eval(node.left, table)
    elif node.val == "C":
        return (not _eval(node.left, table)) or _eval(node.right, table)
    else:
        return _eval(node.left, table) == _eval(node.right, table)

