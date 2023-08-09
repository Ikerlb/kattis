class Node:
    def __init__(self):
        self.d = {}
        self.word = False

    def add(self, w):
        node = self
        for c in w:
            if c not in node.d:
                node.d[c] = Node()
            node = node.d[c]
        node.word = True

    def __repr__(self):
        return f"(d={self.d},w={self.word})"


def solve(q, root):
    node = root
    for c in reversed(q):
        if node.word:
            return True
        elif c not in node.d:
            return False
        node = node.d[c]
    return node.word

def suffixes(w):
    for i in range(len(w) - 1):
        yield w[i:]

equivs = Node()
common_word = input()

num_equiv = int(input())
equivs_string = [input() for _ in range(num_equiv)]

for es in equivs_string:
    words = es.split()
    if any(common_word.endswith(w) for w in words):
        for word in words:
            equivs.add(reversed(word))

num_queries = int(input())

for _ in range(num_queries):
    q = input().split().pop()
    if solve(q, equivs):
        print("YES")
    else:
        print("NO")

