def lcm(*nums):
    m = nums[0]
    for i in range(1, len(nums)):
        m = _lcm(m, nums[i])
    return m

def _lcm(a, b):
    return (a * b) // _gcd(a, b)

def gcd(*nums):
    d = nums[0]
    for i in range(1, len(nums)):
        d = _gcd(d, nums[i])
    return d

def _gcd(a, b):
    if b == 0:
        return a
    return _gcd(b, a % b)

machines = int(input())
for _ in range(machines):
    _ = int(input())
    jackpots = list(map(int, input().split(" ")))
    res = lcm(*jackpots)
    if res <= 10 ** 9:
        print(res)
    else:
        print("More than a billion.")
