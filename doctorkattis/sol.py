import sys
from heapq import heappush, heappop

# https://codereview.stackexchange.com/questions/268416/prioritise-injured-cats-for-treatment-dictionary-map-search-optimization-python
# all credits go to Stefan Pochmann
# this is a fantastic solution!!
# couldn't get java to run in time
# and my rust solution needs rust 1.66

h = [(0, 0)]
entries = [h[0]]
indices = {}
names = ["The clinic is empty"]

_ = input()
for line in sys.stdin:
    s = line.split()
    #print("\n" + line[:-1])
    #print("entries", entries)
    #print("heap", h)
    #print(indices)
    if s[0] == '0':
        name, lvl = s[1], int(s[2])
        index = indices[name] = len(names)
        entry = (-lvl, index)
        heappush(h, entry)
        entries.append(entry)
        names.append(name)
    elif s[0] == '1':
        name, delta = s[1], int(s[2])
        index = indices[name]
        old_level = entries[index][0]
        entry = (old_level - delta, index)
        heappush(h, entry)
        entries[index] = entry
    elif s[0] == '2':
        name = s[1]
        index = indices[name]
        entries[index] = None
    else:
        while h[0] is not entries[h[0][1]]:
            heappop(h)
        sys.stdout.write(names[h[0][1]] + '\n')
