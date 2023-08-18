from random import randint, choice
import sys

class Node:
    def __init__(self, val, nxt = None):
        self.val = val
        self.next = nxt

def fmt(node, d):
    if d["GABBY"] == node == d["SPIKE"]:
        return f"S"
    elif d["GABBY"] == node:
        return f"t"
    elif d["SPIKE"] == node:
        return f"h"
    return str(node.val)

def walk(node, pos, st = set()):
    if node is None:
        return
    if node.val in st:
        yield f"{fmt(node, d)}|"
        return 
    yield fmt(node, d)
    st.add(node.val)
    yield from walk(node.next, pos, st)

LOCATIONS = randint(100, 200)

N = randint(LOCATIONS, 10 ** 5) # just to be able to traverse linearly and check the answer

nodes = [Node(i) for i in range(LOCATIONS)]

pointers = [i + 1 for i in range(LOCATIONS)]
if choice([True, False]):
    pointers[-1] = randint(0, len(pointers) - 2)

for n, pn in zip(nodes, pointers):
    n.next = nodes[pn] if pn < len(nodes) else None

commands = 0

dummy = Node("post_office", nodes[0])

d = {}

d["GABBY"] = dummy
d["SPIKE"] = dummy

finish = dummy
i = 0
while i < N and finish.next:
    finish = finish.next
    i += 1


sys.stdout.write(f"{N}\n")
sys.stdout.flush()

def return_state(d, sub):
    s = int(d[sub].next is not None)
    e = int(d["GABBY"] == d["SPIKE"])
    return f"{s} {e}\n"

while commands < 30000:
    #sys.stdout.write("->".join(walk(nodes[0], d, set())) + "\n")
    #sys.stdout.flush()

    cmd, sub = input().split(" ")
    if cmd == "ASK":
        print(f"{d[sub] == finish} node.val is {d[sub].val}")
        break
    if cmd == "NEXT":
        d[sub] = d[sub].next
        sys.stdout.write(return_state(d, sub))
        sys.stdout.flush()
    if cmd == "RETURN":
        d[sub] = dummy
        sys.stdout.write(return_state(d, sub))
        sys.stdout.flush()
    commands += 1
