from math import sqrt

n, m, k = map(int, input().split(" "))


plots = [int(r) ** 2 for r in input().split(" ")]
circs = [int(r) ** 2 for r in input().split(" ")]
squares = [2 * ((int(s) / 2) ** 2) for s in input().split(" ")]


# kinda worried about floating point precision
# might aswell map to its squares to avoid squared roots
circs.extend(squares)

circs.sort(reverse = True)
plots.sort(reverse = True)

i = j = res = 0
while i < len(plots) and j < len(circs):
    if plots[i] > circs[j]:    
        res += 1     
        j += 1
        i += 1
    else:
        j += 1
print(res)
