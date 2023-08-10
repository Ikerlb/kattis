from itertools import product

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

def dfs(b, r, c, path, depth, res, words):
    if depth < 0:
        return
    if path + b[r][c] in words:
        res.add(path + b[r][c])
    prev, b[r][c] = b[r][c], None
    for nr, nc in neighbors(b, r, c):
        dfs(b, nr, nc, path + prev, depth - 1, res, words)
    b[r][c] = prev


def solve(words, boggle):
    res = set()
    for row in range(len(boggle)):
        for col in range(len(boggle[0])):
            dfs(boggle, row, col, "", 8, res, words)
    return parse_solution(list(res))

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
def parse_solution(l):
    score = sum(scores[len(w)] for w in l)
    max_length = max(len(w) for w in l)
    same = [w for w in l if len(w) == max_length]
    same.sort()
    biggest = same[0]
    num = len(l)
    return f"{score} {biggest} {num}"

num_words = int(input())
words = {input() for _ in range(num_words)}

input()

boggles = int(input())
for _ in range(boggles - 1):
    boggle = [list(input()) for _ in range(4)]
    print(solve(words, boggle))
    input()

boggle = [list(input()) for _ in range(4)]
print(solve(words, boggle))
