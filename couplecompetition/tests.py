from random import randint

N_limit = 1_000_00
N = randint(1, N_limit)
#N = N_limit

print(N)
for _ in range(N):
    print(randint(1, 10 ** 9))
