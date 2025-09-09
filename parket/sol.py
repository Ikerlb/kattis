from math import sqrt

# we want a numbers
# such that
# 2*L + 2*W = RED + 4
# L * W = RED + BROWN
# then
# L = (((RED + 4) - 2*W) / 2)
# ((RED + 4) - 2*W) * W / 2 = RED + BROWN
# ((RED + 4) - 2*W) * W = 2 * (RED + BROWN)
# W*(RED + 4) - 2*W*W = 2 * (RED + BROWN)

# 2*L + 2*W = a + 4
# L * W = a + b
# L = ((a + 4 - 2*W) / 2)
# ((a + 4 - 2*W) / 2) * W = a + b

a, b = map(int, input().split(" "))
sq = sqrt((-8*a) + (a*a) - (16*b) + 16)
n1 = abs(int((-a-4-sq) / 4))
n2 = abs(int((-a-4+sq) / 4))
l = [n1, n2]
print(" ".join(map(str, sorted(l, reverse = True))))
