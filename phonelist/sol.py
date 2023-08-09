class Node:
    def __init__(self):
        self.d = {}
        self.w = False

    def add(self, w):
        node = self
        for c in w:
            if c not in node.d: 
                node.d[c] = Node()
            node = node.d[c]
        node.word = True

    def is_prefix(self, w):
        node = self
        for c in w:
            node = node.d[c]
        return len(node.d) > 0

def solve(telephones):
    node = Node()
    for telephone in telephones:
        node.add(telephone)

    if any(node.is_prefix(telephone) for telephone in telephones):
        return "NO"
    return "YES"

tcs = int(input())
for _ in range(tcs):
    n = int(input())
    telephones = [input() for _ in range(n)]    
    print(solve(telephones))
