n, _ = map(int, input().split(" "))
div = [0] + [int(s) for s in input().split(" ")] + [n]
widths = set()

for i in range(len(div)):
    for j in range(i + 1, len(div)):
        widths.add(div[j] - div[i])

print(" ".join(str(i) for i in sorted(widths)))
