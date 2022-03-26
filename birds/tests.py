from random import randint

# at most n birds in the tc
def generate_test_cases(l, d):
    total = l
    prev = 6
    birds = []
    l = l - 6
    while prev + d < l:
        birds.append(randint(prev + d, l))
        prev = birds[-1] 
    res = [f"{total} {d} {len(birds)}"]
    for b in birds:
        res.append(f"{b}")
    return "\n".join(res)

n = 1000000000
l = randint(1, n)
print(generate_test_cases(l, randint(1, l)))
