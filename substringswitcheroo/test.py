from random import randint, choice, shuffle
from string import ascii_lowercase

mn_tcs = 10
mx_tcs = 10

mn_size = 1000
mx_size = 1000

tcs = randint(mn_tcs, mx_tcs)
print(tcs)
for _ in range(tcs):
    og = [choice(ascii_lowercase) for _ in range(randint(mn_size, mx_size))]
    messed = og[:] 
    for i in range(len(og)):
        if randint(1, 10) > 1:
            messed[i] = choice(ascii_lowercase)
    shuffle(messed)
    print("".join(og))
    print("".join(messed))
