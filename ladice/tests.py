from random import randint

def generate_test_case(n, l):
    s = [f"{n} {l}"]
    for _ in range(n):    
        fst = randint(1, l)
        while (snd := randint(1, l)) == fst:
            pass    
        s.append(f"{fst} {snd}")
    return "\n".join(s)

print(generate_test_case(100000, 300000))
