
# we could naively
# do all intervals
# and get its sum
# O(N^2)
# but since n = 100,000 this is unfeasible

# variation of kadane's algorithm!

def kadane(l):
    ms = cs = 0
    for n in l:    
        cs = max(n, n + cs, 0)
        ms = max(ms, cs)
    return ms

n, p = map(int, input().split(" "))
arr = [int(s) - p for s in input().split(" ")]
print(kadane(arr))
