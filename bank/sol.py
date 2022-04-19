def parse(l):
    return tuple(map(int, l.split(" ")))

# as long as this is called greedily
def stand(q, m, t):
    for i in range(t, -1, -1):    
        if q[i] == 0:
            q[i] = m        
            break

n, t = map(int, input().split(" "))

q = [0] * t

arr = [parse(input()) for _ in range(n)]
arr.sort(key = lambda x: x[0], reverse = True)

for ci, ti in arr:
    stand(q, ci, ti)
print(sum(q))
