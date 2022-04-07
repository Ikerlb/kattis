n, k = map(int, input().split(" "))

prev = 0
for i in range(2, n + 1):
    prev = (prev + k) % i
print(prev)
