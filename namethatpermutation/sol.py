from functools import lru_cache
from sys import stdin

@lru_cache(None)
def fact(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

# arr is sorted
# arr is of size n
# then perms 0 - (n - 1) if
# arr[0] is placed at the beggining 
def kth_perm(arr, k):
    if not arr:
        return []
    step = fact(len(arr) - 1)
    prev = 0
    for i in range(len(arr)):
        if prev <= k < prev + step:
            return [arr[i]] + kth_perm(arr[:i] + arr[i + 1:], k - prev)
        prev += step

for line in stdin:
    n, k = map(int, line[:-1].split(" "))
    arr = list(range(1, n + 1))
    print(" ".join(str(nn) for nn in kth_perm(arr, k)))
