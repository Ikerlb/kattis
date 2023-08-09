from sys import stdin

lines = [line[:-1] for line in stdin]

n = max(len(line) for line in lines)

print(sum((n - len(line)) ** 2 for line in lines[:-1]))
