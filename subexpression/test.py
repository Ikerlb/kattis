from random import randint, shuffle, choice
from string import ascii_lowercase

class Node:
    def __init__(self, f, left = None, right = None):
        self.f = f
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left is None and self.right is None:
            return self.f
        return f"{self.f}({self.left},{self.right})"

def random_label():
    size = randint(1, 4)
    return "".join(choice(ascii_lowercase) for _ in range(size))

# takes k leaves
def create_random_tree(k):
    leaves = [Node(random_label()) for _ in range(k)]

    # take last two
    while len(leaves) > 1:
        shuffle(leaves)
        s1 = leaves.pop()
        s2 = leaves.pop()
        leaves.append(Node(random_label(), s1, s2))

    return leaves.pop()

tcs = 100000
print(tcs)
for _ in range(tcs):
    k = randint(5, 10)
    node = create_random_tree(k)
    print(node)
