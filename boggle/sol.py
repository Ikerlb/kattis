from itertools import product

def f(c):
    return ord(c) - ord('A')

class Node:
    def __init__(self):
        #self.d = {}
        self.d = [None for _ in range(26)]
        self.word = None

    def add(self, w, i):
        node = self
        for c in w:
            #if c not in node.d:
            if node.d[c] is None:
                node.d[c] = Node()
            node = node.d[c]
        node.word = i

word_count = int(input())
words = [input() for _ in range(word_count)]

root = Node()
for i, w in enumerate(words):
    root.add([f(c) for c in w], i)

input() # empty line

def neighbors(b, r, c):
    for dr, dc in product(range(-1, 2), repeat = 2):
        if dr == dc == 0:
            continue
        if not 0 <= r + dr < len(b):
            continue
        if not 0 <= c + dc < len(b[0]):
            continue
        if b[r + dr][c + dc] is None:
            continue
        yield (r + dr, c + dc)

def fmt(b):
    s = []
    for row in b:
        s.append(",".join(map(lambda x: "__" if x is None else str(x).zfill(2), row)))
    return "\n".join(s) + "\n"

# worst case scenario it is depth 16
def dfs(b, r, c, node, depth, res):
    if depth < 0:
        return
    nxt = node.d[b[r][c]]
    prev, b[r][c] = b[r][c], None
    for nr, nc in neighbors(b, r, c):
        if nxt.d[b[nr][nc]] is not None and nxt.d[b[nr][nc]].word is not None:
            res.add(nxt.d[b[nr][nc]].word)
            dfs(b, nr, nc, nxt, depth - 1, res)
        elif nxt.d[b[nr][nc]] is not None:
            dfs(b, nr, nc, nxt, depth - 1, res)
    b[r][c] = prev

def solve_boggle(b, root):
    res = set()
    for row in range(len(b)):
        for col in range(len(b[0])):
            #if b[row][col] in root.d:
            if root.d[b[row][col]] is not None:
                dfs(b, row, col, root, 8, res) # we know words are at most 8
    return list(res)

scores = {
    1: 0,
    2: 0,
    3: 1,
    4: 1,
    5: 2,
    6: 3,
    7: 5,
    8: 11,
}
def parse_solution(words, l):
    l.sort(key = lambda i: len(words[i]))
    score = sum(scores[len(words[wi])] for wi in l)
    #same = sorted((i for i in l if len(words[i]) == len(words[l[-1]])), key = lambda x: words[x])

    same = [i for i in l if len(words[i]) == len(words[l[-1]])]
    same.sort(key = lambda x: words[x])

    biggest = words[same[0]]
    num = len(l)
    return f"{score} {biggest} {num}"

board_count = int(input())
for i in range(board_count):
    b = [[f(c) for c in input()] for _ in range(4)]

    l = solve_boggle(b, root)
    #print(l)
    print(parse_solution(words, l))

    if i != board_count - 1: 
        input() # empty line
