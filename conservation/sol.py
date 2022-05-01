from collections import defaultdict, deque

def topo(g, indegree, arr, curr):
    qarr = [deque(), deque()]
    for i in range(len(arr)):
        if indegree[i] == 0:
            qarr[arr[i]].append(i)

    res = 0
    while qarr[0] or qarr[1]:
        while qarr[curr]:
            n = qarr[curr].popleft()
            for nn in g[n]:
                indegree[nn] -= 1
                if indegree[nn] == 0:
                    qarr[arr[nn]].append(nn)
        curr = 1 - curr
        res += 1
    return res - 1

def solve():
    n, m = map(int, input().split(" "))
    arr = [int(d) - 1 for d in input().split(" ")]
    g = defaultdict(list)
    ind1 = defaultdict(int)
    ind2 = defaultdict(int)
    for _ in range(m):
        s, t = map(lambda c: int(c) - 1, input().split(" "))
        g[s].append(t)
        ind1[t] += 1
        ind2[t] += 1 
    return min(topo(g, ind1, arr, 0), topo(g, ind2, arr, 1))

#def kahn(g, visited, indegree, arr, color):
#    while q: 
#        n = q.popleft()
#        visited.add(n)
#        for nn in g[n]:
#            indegree[nn] -= 1
#            if indegree[nn] == 0 and arr[nn] == color:
#                q.append(nn)

tcs = int(input())
for _ in range(tcs):
    print(solve())
