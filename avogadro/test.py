from random import shuffle, randint

# mutates muts
def change(a, muts):
    for _ in range(muts):
        i = randint(0, len(a) - 1)    
        a[i] = randint(1, len(a))

N = 5
a1 = list(i + 1 for i in range(N))
a2 = a1[:]
a3 = a1[:]

change(a2, randint(0, N - 1))
change(a3, randint(0, N - 1))

shuffle(a1)
shuffle(a2)
shuffle(a3)

print(N)
print(" ".join(map(str, a1)))
print(" ".join(map(str, a2)))
print(" ".join(map(str, a3)))

