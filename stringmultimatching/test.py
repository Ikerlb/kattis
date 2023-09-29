from random import randint, choice
from string import ascii_letters

poss = ascii_letters + " "

tcs = randint(1, 1)

for _ in range(tcs):
    patterns = randint(100_000, 100_000)
    print(patterns)
    for _ in range(patterns): 
        print("".join(choice(poss) for _ in range(randint(2, 10))))
    s_len = randint(100_000, 200_000)
    s = "".join(choice(poss) for _ in range(s_len))
    print(s)
