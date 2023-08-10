from string import ascii_uppercase
from random import choice, randint

def generate_word(k):
    return "".join(choice(ascii_uppercase) for _ in range(k))

def generate_boggle():
    s = []
    for row in range(4):
        s.append("".join(choice(ascii_uppercase) for _ in range(4)))
    return "\n".join(s)

num_words = randint(300000, 300000)
print(num_words)
for _ in range(num_words):
    print(generate_word(randint(2, 8)))
print()
num_boggles = randint(30, 30)
print(num_boggles)
for _ in range(num_boggles - 1):
    print(generate_boggle())
    print()
print(generate_boggle())
