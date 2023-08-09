tcs = int(input())

for _ in range(tcs):
    fst = input()
    snd = input()

    print(fst)
    print(snd)
    print("".join("*" if c1 != c2 else "." for c1, c2 in zip(fst, snd)))
    print()
