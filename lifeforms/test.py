from random import randint, choice

MIN_TEST_CASES = 10
MAX_TEST_CASES = 10

MIN_STRING_SIZE = 1006
MAX_STRING_SIZE = 1006

MIN_NUMBER_OF_STRINGS = 100
MAX_NUMBER_OF_STRINGS = 100

tcs = randint(MIN_TEST_CASES, MAX_TEST_CASES)
for _ in range(tcs):
    n = randint(MIN_NUMBER_OF_STRINGS, MAX_NUMBER_OF_STRINGS)
    print(n)
    for _ in range(n):
        sl = randint(MIN_STRING_SIZE, MAX_STRING_SIZE)
        print("".join(choice("abcdefghijklmnopqrstuvwxyz") for _ in range(sl)))
print(0)
