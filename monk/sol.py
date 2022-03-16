# there we found the monotonic property!
def position(arr, t, pos = 0):
    for sd, st in arr:
        if t <= st:
            # sd -> st
            # ?  -> t
            return abs(pos + (t * sd / st))
        t -= st
        pos += sd
    return pos

# should probably do it ascent
def calc_height_time(arr):
    rd = rt = 0
    for sd, st in arr:
        rd += sd
        rt += st
    return rd, rt
        

def _try(ascent, descent, time, maxh):
    apos = position(ascent, time)
    dpos = position(descent, time, pos = -maxh)
    return apos > dpos or abs(apos - dpos) <= 10 ** -5
    

def find_earliest(ascent, descent, mh, mt):
    l, r = 0, mt
    res = None
    for _ in range(50):
        m = (l + r) / 2
        if _try(ascent, descent, m, mh):
            res = m    
            r = m
        else:
            l = m
    return res

a, d = map(int, input().split(" "))
ascent = [tuple(map(int, input().split(" "))) for _ in range(a)]
descent = [tuple(map(int, input().split(" "))) for _ in range(d)]

maxh, maxt = calc_height_time(ascent)
print(find_earliest(ascent, descent, maxh, maxt))
