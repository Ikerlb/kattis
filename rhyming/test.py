from random import choice, randint
from string import ascii_lowercase


n = randint(1, 20)
common_word = "".join(choice(ascii_lowercase) for _ in range(n))
print(common_word)

num_equivs = randint(1, 10)
for _ in range(num_equivs):
    equivs_words = " ".join()
    print()
