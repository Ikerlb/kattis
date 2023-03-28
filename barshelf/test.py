from random import randint

N = randint(1, 20)
#M = 10 ** 9
M = 100

print(N)
print(" ".join(str(randint(1, M)) for _ in range(N)))
