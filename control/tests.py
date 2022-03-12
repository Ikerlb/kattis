from random import randint

def generate_test(n, m):
    s = [f"{n}"]
    for _ in range(n):
        row = []
        ni = randint(1, m)
        used = set()
        for _ in range(ni):
            while (r := randint(0, m)) in used:
                pass    
            used.add(r)
            row.append(f"{r}")
        s.append(f"{ni} {' '.join(row)}")
    return "\n".join(s)

n, m = randint(2, 200000), randint(1, 1000)
#print(n, m)
print(generate_test(n, m))
