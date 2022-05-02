from random import randint

def generate_test_case(n, m):
    res = [f"{n} {m}"]    
    for _ in range(m):
        a = randint(1, n)
        b = randint(1, n)
        res.append(f"{a} {b}")
    return "\n".join(res)

print(generate_test_case(1000000, 100))
        
