word = set(input())
guesses = list(input())

MAX_FAILS = 10

#HANGMAN
#ABCDEFGHIJKLMNOPQRSTUVWXYZ

#_A_G_A_

fails = i = 0
while fails < MAX_FAILS:
    if guesses[i] in word:
        word.discard(guesses[i])
    else:
        fails += 1
    i += 1

if word:
    print("LOSE")
else:
    print("WIN")
