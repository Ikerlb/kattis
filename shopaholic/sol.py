n = int(input())
l = [int(x) for x in input().split(" ")]
l.sort()

res = 0
while len(l) >= 3:
    l.pop()
    l.pop()
    res += l.pop()
print(res)
    
