n = int(input())

START = "Simon says"

for _ in range(n):
    sentence = input()
    if sentence.startswith(START):
        print(sentence[len(START):])
