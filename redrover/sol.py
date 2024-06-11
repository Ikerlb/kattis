from collections import Counter

instructions = input()

def substrings(w, size):
    res = set()
    for i in range(len(w) - size + 1):
        res.add(w[i:i + size])
    return res

# get the macro that will minimize
# the size of the encoded instructions
def macro(w, size):
    res = len(w)
    for ss in substrings(w, size):
        nw = w.replace(ss, "M")
        res = min(res, len(nw) + len(ss)) 
    return res
    

res = len(instructions)
for ml in range(2, len(instructions)):
    res = min(res, macro(instructions, ml))
print(res)
