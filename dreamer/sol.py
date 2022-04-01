from itertools import permutations

def is_leap(yyyy):
    if yyyy % 4 != 0:
        return False
    if yyyy % 100 == 0:
        return yyyy % 400 == 0
    return True

def parse_date(s):
    dd = int(s[0:2])
    mm = int(s[2:4])
    yyyy = int(s[4:])
    return dd, mm, yyyy

def is_valid(s):
    dd, mm, yyyy = parse_date(s)
    if yyyy < 2000 or not 1 <= mm <= 12 or not 1 <= dd <= 31:
        return False
    if mm == 2 and is_leap(yyyy):
        return dd <= 29
    if mm == 2:
        return dd <= 28
    if mm == 1: 
        return dd <= 31
    if mm == 3:
        return dd <= 31
    if mm == 4:
        return dd <= 30
    if mm == 5:
        return dd <= 31
    if mm == 6:
        return dd <= 30
    if mm == 7:
        return dd <= 31
    if mm == 8:
        return dd <= 31
    if mm == 9:
        return dd <= 30
    if mm == 10:
        return dd <= 31
    if mm == 11:
        return dd <= 30
    if mm == 12:
        return dd <= 31
    return True

def less(d1, d2):
    dd1, mm1, yyyy1 = parse_date(d1)
    dd2, mm2, yyyy2 = parse_date(d2)
    if yyyy1 < yyyy2: 
        return True
    elif yyyy1 > yyyy2:
        return False
    elif mm1 < mm2:
        return True
    elif mm1 > mm2:    
        return False
    elif dd1 < dd2:
        return True
    else:
        return False

tcs = int(input())
for _ in range(tcs):
    date = input().replace(" ", "")
    m, valids = None, set()
    for p in permutations(date): 
        p = "".join(p)
        if is_valid(p) and p not in valids:
            valids.add(p)
            if m is None or less(p, m):
                m = p
    if m is None: 
        print(0)
    else:
        dd, mm, yyyy = parse_date(m)
        dd = str(dd).zfill(2) 
        mm = str(mm).zfill(2) 
        print(f"{len(valids)} {dd} {mm} {yyyy}")
