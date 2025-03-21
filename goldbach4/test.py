from random import randint

N = randint(10**17, 10 ** 18)
N = N if N % 2 == 1 else N - 1

print(N)
