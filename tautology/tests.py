from random import choice, randint
from node import Node

def terminal(pos):
    return Node(choice(pos))

def create(d, pos):
    if d == 0:    
        return terminal(pos)
    else:
        op = choice("KANCE")
        node = Node(op)
        if op in "KACE":
            node.left = terminal(pos) if randint(0, 10) <= 3 else create(d - 1, pos)
            node.right = terminal(pos) if randint(0, 10) <= 3 else create(d - 1, pos)
        else:
            node.left = terminal(pos) if randint(0, 10) <= 3 else create(d - 1, pos)
        return node

def create_test_case(depth, variables):
    pos = "pqrst"
    return create(depth, pos[:variables])

for _ in range(10):
    ast = create_test_case(3, 3)
    print(ast.idfk())
print("0")
