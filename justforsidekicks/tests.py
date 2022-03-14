import sys
from random import randint

def generate_test_case(n, q):
    s = [f"{n} {q}"]
    values = [randint(1, 10 ** 9) for _ in range(6)]
    s.append(" ".join(map(str, values)))
    initial = [randint(1, 6) for _ in range(n)]
    s.append("".join(map(str, initial)))
    for _ in range(q):
        op = randint(1, 3)
        if op == 1:
            k = randint(1, n)
            p = randint(1, 6)
            s.append(f"{op} {k} {p}")
        elif op == 2:
            p = randint(1, 6)
            v = randint(1, 10 ** 9)
            s.append(f"{op} {p} {v}")
        else:
            l = randint(1, n)
            r = randint(l, n) 
            s.append(f"{op} {l} {r}")
    return "\n".join(s)

res = generate_test_case(200000, 10)
#print(res, file = sys.stderr)
print(res)
