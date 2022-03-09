from random import randint

def generate_test_case(n, m, l):
    s = [f"{n} {m} {l}"]
    for i in range(l):
        a = randint(0, 10000)
        b = randint(0, 10000)
        s.append(f"{i}:{a},{b}")
    return "\n".join(s)

def gen_test(tcs):
    s = [str(tcs)]
    for i in range(tcs):
        n = 100000
        m = randint(1, n)
        l = 100
        s.append(generate_test_case(n, m, l))
    return "\n".join(s)

print(gen_test(250))
