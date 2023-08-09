from collections import Counter
import re
from sys import stdin

def split_list(arr, f):
    res = []
    for e in arr:
        if f(e):
            yield res[:]
            res = []
        else:
            res.append(e)
    if res:
        yield res[:]

def solve(lines, freq):
    words = []
    counter = {}
    for line in lines:
        for w in re.findall("[a-zA-Z]+", line):
            w = w.lower()
            if w in counter:
                counter[w] += 1
            else:
                counter[w] = 1

    for w, f in counter.items():
        if f == freq:
            words.append(w)
    if not words:
        return "There is no such word."

    words.sort()
    return "\n".join(words)

l = [line[:-1] for line in stdin]

res = []
# DUH! I was skipping a line
# spent almost an hour trying
# to find why it wasn't passing
for text in split_list(l, lambda x: x == "EndOfText"):
    freq = int(text[0])
    res.append(solve(text[1:], freq))
print("\n\n".join(res))
