from collections import defaultdict

def djikstra(g, s):
    

def parse_edge(line):
    return tuple(map(int, line.split(" ")))

N, M, Q, S = map(int, input().split(" "))

g = defaultdict(list)

for _ in range(M):
    print(parse_edge(input()))
