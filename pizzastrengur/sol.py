from random import randint, shuffle, choice

def _try(res, a):
    print("".join(res) + a, flush = True)
    return int(input())


n = int(input())

res = []
poss = ["P", "I", "Z", "A"]
for _ in range(n):
    shuffle(poss)
    for c in poss[:3]:
        t = _try(res, c)
        if t == 0:
            continue
        elif t == 1:
            res.append(c)
            break
        else:
            exit(0)
    else: # important to skip last try! if there is no other way!
        res.append(poss[-1])
print("".join(res))
