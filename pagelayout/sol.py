class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"


class Rect:
    def __init__(self, x, y, w, h):
        self.p = Point(x, y)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def intersects(self, other):
        axmn, aymn, axmx, aymx = self.ul_lr()
        bxmn, bymn, bxmx, bymx = other.ul_lr()

        first = not ((aymn <= bymn and aymx <= bymn) or (aymn >= bymx and aymx >= bymx))
        second = not ((axmn <= bxmn and axmx <= bxmn) or (axmn >= bxmx and axmx >= bxmx))
        return first and second

    def ul_lr(self):
        return self.p.x, self.p.y, self.p.x + self.w, self.p.y + self.h

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.w
        yield self.h

    def __repr__(self):
        return f"({self.p.x},{self.p.y}) width is {self.w} {self.h}"

def dfs(rects, i, area, taken):
    #print(i, area, taken)
    if i == len(rects):
        return area
    res = dfs(rects, i + 1, area, taken) # without
    if all(not rects[i].intersects(rects[t]) for t in taken):
        na = rects[i].area()
        taken.append(i)
        res = max(res, dfs(rects, i + 1, area + na, taken))
        taken.pop()
    return res

while True:
    n = int(input())
    if n == 0:
        break
    rects = []
    for _ in range(n):
        w, h, x, y = map(int, input().split(" "))
        rects.append(Rect(x, y, w, h))
    taken = []
    print(dfs(rects, 0, 0, taken))
