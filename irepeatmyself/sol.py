
def repeat(s):
    i, n = 0, len(s)
    while True:
        yield s[i]
        i = (i + 1) % n 

tcs = int(input())

def explains(s, p):
    for ss, pp in zip(s, repeat(p)):
        if ss != pp:
            return False
    return True

for _ in range(tcs):
    s = input()
    i = 1

    while i < len(s) and not explains(s, s[:i]):    
        i += 1
    print(i)
