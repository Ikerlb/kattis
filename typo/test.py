from random import randint, choice
from string import ascii_lowercase

n = randint(100, 1000)
print(n)
for i in range(n):
    length = randint(1, 20)
    print("".join(choice(ascii_lowercase) for _ in range(length)))
