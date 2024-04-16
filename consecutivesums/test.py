from random import randint

TEST_CASES = 2000
MAX_GAUSSIAN_TERM = 100000

arr = [0]
for i in range(MAX_GAUSSIAN_TERM):
    arr.append(arr[-1] + i)

print(TEST_CASES)
for _ in range(TEST_CASES):
    i = randint(1, MAX_GAUSSIAN_TERM)
    j = randint(0, i)
    print(arr[i] - arr[j])
