from bisect import bisect_left
from math import inf

def query(arr, target):
    i = bisect_left(arr, target)
    return arr[i] - target

n, m = map(int, input().split(" "))
arr = [int(input()) for _ in range(n)]
arr.sort()

res = sum(query(arr, int(input())) for _ in range(m))
print(res)
