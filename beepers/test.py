from random import randint

tcs = randint(1, 20)
print(tcs)

for _ in range(tcs):
    rows = 20
    cols = 20
    print(rows, cols)

    sr = randint(1, rows)
    sc = randint(1, cols)
    print(sr, sc)

    beepers = 10
    print(beepers)

    s = set()
    for _ in range(beepers):
        r, c = randint(1, rows), randint(1, cols)
        while (r, c) in s:
            r, c = randint(1, rows), randint(1, cols)
        print(r, c)

