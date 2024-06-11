from collections import defaultdict

def search(word, plate):
    last = -1 
    for p in plate:
        try:
            last = word.index(p, last + 1)
        except:
            return False
    return True

n, m = map(int, input().split(" "))
dictionary = [input() for _ in range(n)]
plates = [input().lower() for _ in range(m)]

for p in plates:
    for d in dictionary:
        if search(d, p):
            print(d)
            break
    else:
        print("No valid word")
