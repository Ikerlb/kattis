from random import randint, choice, shuffle
from string import ascii_lowercase, ascii_uppercase

poss = ascii_lowercase + ascii_uppercase

max_tcs = 10
tcs = randint(1, max_tcs)
for _ in range(tcs):
    mn_str = 1
    mx_str = 100000
    l = randint(mn_str, mx_str)
    s = "".join(choice(poss) for _ in range(l))
    mn_qs = 1
    mx_qs = l
    poss_qs = list(range(l))
    shuffle(poss_qs)
    qsl = randint(mn_qs, mx_qs)
    qs = [poss_qs.pop() for _ in range(qsl)]
    print(s)
    print(f"{qsl} {' '.join(map(str, qs))}")
