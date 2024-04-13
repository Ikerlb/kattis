def find(i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(i, j):
    i = find(i)
    j = find(j)
    if size[i] < size[j]:
        (i, j) = (j, i)
    size[i] += size[j]
    parent[j] = i

(n, m) = list(map(int, input().split()))
size = [1] * n
parent = list(range(n))
answer = n
res = 0
for _ in range(m):
    (u, v) = list(map(int, input().split()))
    u -= 1
    v -= 1
    if (f1 := find(u)) != (f2 := find(v)):
        answer -= 1
    res += f1 + f2
    union(u, v)

print(f"cost was {res}")
print(answer)
