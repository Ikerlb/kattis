def parse_votes(s):
    return [int(w) - 1 for w in s.split(" ")][::-1]


n, m = map(int, input().split(" "))

candidates = [input() for _ in range(m)]

votes = [[] for _ in range(m)]

for _ in range(n):
    order = parse_votes(input().strip())
    v = order.pop()
    votes[v].append(order)
