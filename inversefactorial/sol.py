from math import log10, floor
from bisect import bisect_left, bisect_right

def fact(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

lengths = [1, 1]
i = 2
res = 1
while res <= 10 ** 6: 
    res += log10(i)
    lengths.append(floor(res))
    i += 1

s = input()

left = bisect_left(lengths, len(s))
right = bisect_right(lengths, len(s)) - 1

if left == right:
    print(left)
else:
    for i in reversed(range(left, right + 1)):    
        if fact(i) == int(s):
            print(i)
            break
