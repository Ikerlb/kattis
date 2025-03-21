def decimal(number, language):
    d = {c:i for i, c in enumerate(language)}
    res = 0
    for c in number:
        res *= len(language)
        res += d[c]
    return res
    
def alienal(number, language):
    #d = {c:i for i, c in enumerate(language)}
    res = []
    while number:
        number, rem = divmod(number, len(language))
        res.append(language[rem])
    return "".join(reversed(res))
    
n = int(input())
for i in range(1, n + 1):
    number, source, target = input().split(" ")
    d = decimal(number, source)
    a = alienal(d, target)
    print(f"Case #{i}: {a}")

