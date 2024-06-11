n = int(input())

for _ in range(n):
    w = input()
    if w.startswith("simon says"):
        print(w[len("simon says "):])
    else:
        print()
    
