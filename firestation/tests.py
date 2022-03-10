from random import randint

def generate_test_case(i, fs):
    # we need a connected graph    
    # we'll just do the easiest thing
    # possible
    s = [f"{fs} {i}"]
    fss = set(range(1, i + 1))
    for _ in range(fs):
        while (n := randint(1, i)) not in fss:
            n = randint(1, i)
        fss.remove(n)
        s.append(f"{n}")
    for n in range(i): 
        s.append(f"{(n % i) + 1} {((n+1) % i) + 1} 10")
    return "\n".join(s)

tc = 100
print(tc, end = "\n\n")
print("\n\n".join(generate_test_case(500, 100) for _ in range(tc)))
