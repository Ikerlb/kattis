tcs = int(input())

def lcp(w1, w2):
    pi = 0
    while pi < len(w1) and pi < len(w2) and w1[pi] == w2[pi]: 
        pi += 1
    return pi

def keypresses(w, sug):
    pi = lcp(w, sug)
    # then we go from sug to sug[:pi]
    # then we go from sug[:pi] to w
    return len(sug) + len(w) - (2 * pi) 

def solve(word, current, suggestions):
    l = [1 + keypresses(word, sug) for sug in suggestions]
    l.append(keypresses(word, current))

    return min(l)

for _ in range(tcs):
    word = input()

    current = input()

    suggestions = [None for _ in range(3)]
    suggestions[0] = input()
    suggestions[1] = input()
    suggestions[2] = input()

    print(solve(word, current, suggestions))
