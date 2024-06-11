def is_pink(s):
    return "pink" in s or "rose" in s

n = int(input())
s = sum(is_pink(input().lower()) for _ in range(n))
print(s if s else "I must watch Star Wars with my daughter")
