from itertools import product
from node import _eval, Node, parse

while True:
    line = input()
    if line == "0":
        break
    variables = set(c for c in line if c in "pqrst")
    ast = parse(list(reversed(line)))
    #print("line", line)
    #print("ast", ast)
    for p in product([True, False], repeat = len(variables)):
        table = dict(zip(variables, p))
        if not _eval(ast, table):
            print("not")
            break
    else:
        print("tautology")
