def first_bigger(a):
    if a[0] > a[1]:
        return "Bigger"
    elif a[0] == a[1]:
        return "Equal"
    return "Smaller"

def first_median(a):
    a1, a2, a3 = sorted(a[:3])
    return a2

def charify(a):
    return "".join(chr((n % 26) + ord('a')) for n in a)

def jump_game(a):
    i = 0
    used = set()
    while i not in used: 
        used.add(i)
        ni = a[i]
        if ni >= len(a):
            return "Out"
        elif ni == (len(a) - 1): 
            return "Done"
        i = ni
    return "Cyclic"

funcs = [
    lambda a: print(7),
    lambda a: print(first_bigger(a)),
    lambda a: print(first_median(a)), 
    lambda a: print(sum(a)),
    lambda a: print(sum(n for n in a if n % 2 == 0)),
    lambda a: print(charify(a)),
    lambda a: print(jump_game(a))
]

_, t = map(int, input().split(" "))
arr = [int(n) for n in input().split(" ")]
funcs[t - 1](arr)
