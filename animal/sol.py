
def tokenize(s):
    res, cur = [], 0
    for i in range(len(s)):
        #print(res)
        if s[i] in ")(," and cur != 0:
            res.append(cur)
            res.append(s[i])
            cur = 0
        elif s[i] in ")(," and cur == 0:
            res.append(s[i])
        else:
            cur = (cur * 10) + int(s[i])
    return res

#def parse(tokens):
#    s = [[]]
#    for c in tokens:
#        if c == "(":
#            s.append([])
#        elif c == ",":
#            continue
#        elif c == ")":
#            ret = s.pop()
#            s[-1].append(ret)
#        else:
#            s[-1].append(c)
#    return s.pop()

def dfs(tokens, bases, mod):
    s = [0]
    st = set()
    for c in tokens:
        if c == "(":
            s.append(0)
        elif c == ",":
            continue
        elif c == ")":
            ret = s.pop()
            st.add(ret)
            s[-1] = (s[-1] + ret) % mod
        else:
            st.add(bases[c])
            s[-1] = (s[-1] + bases[c]) % mod
    return st


n = int(input())

alice_string = input()
bob_string = input()

alice_tokens = tokenize(alice_string)
bob_tokens = tokenize(bob_string)

b = 131
mod = 614889782588491410

bases = [1]
for i in range(n + 1):
    bases.append((bases[-1] * b) % mod)

s1 = dfs(alice_tokens, bases, mod)
s2 = dfs(bob_tokens, bases, mod)

print(len(s1 & s2))
