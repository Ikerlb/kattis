# we don't want memory overhead
# so we might as well do a two
# pointer solution
def solve(jack, jill):
    j = res = 0
    for i in range(len(jack)): 
        while j < len(jill) and jill[j] < jack[i]:    
            j += 1
        if jack[i] == jill[j]:
            res += 1
    return res

#while (l := input()) != "0 0": # python 3.9
while True:
    l = input()
    if l == "0 0":
        break
    n, m = map(int, l.split(" "))
    jack = [int(input()) for _ in range(n)]
    jill = [int(input()) for _ in range(m)]
    print(solve(jack, jill))

