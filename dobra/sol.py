from string import ascii_uppercase

vowels = "AEIOU"
consonants = "BCDFGHJKLMNPQRSTVWXYZ"

def dfs(s, i, cons_c, cons_v, has_l):
    if cons_c >= 3 or cons_v >= 3:
        return 0
    if i == len(s):
        return int(has_l)
    res = 0
    if s[i] == "_": 
        res += 5 * dfs(s, i + 1, 0, cons_v + 1, has_l) # vowels
        res += 20 * dfs(s, i + 1, cons_c + 1, 0, has_l) # consonants - "L"
        res += dfs(s, i + 1, cons_c + 1, 0, True)  # "L"
    elif s[i] in vowels:
        res += dfs(s, i + 1, 0, cons_v + 1, has_l)
    else:
        res += dfs(s, i + 1, cons_c + 1, 0, has_l or s[i] == "L")
    return res
    
            

s = input()
res = []
print(dfs(s, 0, 0, 0, False))
#print(len(res), res)
