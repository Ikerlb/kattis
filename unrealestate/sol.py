# I think we can get away with 
# having an O(n^2) solution
# because of the constraints

from sys import stdin
from itertools import chain

START, END = 0, 1

def parse(line):
    swx, swy, nex, ney = line.split()
    yield (float(swx), START, float(swy), float(ney))
    yield (float(nex), END, float(swy), float(ney))

# mutates intervals
def remove(intervals, s, e):
    i = intervals.index((s, e))
    intervals.pop(i)

# intervals can have overlapping intervals
def span(intervals):
    res = 0
    if not intervals:
        return res    
    s, e = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] > e:
            res += e - s
            s, e = intervals[i]
        else:
            e = max(e, intervals[i][1])
    return res + (e - s)

lines = [line[:-1] for line in stdin]
events = list(chain(*map(parse, lines[1:])))

events.sort()

cur = []
prev = events[0][0]
res = 0

for x, t, y1, y2 in events:
    res += (x - prev) * span(cur)
    if t == START:
        cur.append((y1, y2))
        cur.sort()
    else:
        remove(cur, y1, y2)
    prev = x

print(f"{res:0.2f}")
