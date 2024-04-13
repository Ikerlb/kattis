from itertools import product

n, m = map(int, input().split(" "))
grid = [list(input()) for _ in range(n)]

def is_illegal(c):
    return c not in ",.?!" and not c.isalnum()
    
def empty(grid, sr, sc, er, ec):
    for r in range(sr, er):
        for c in range(sc, ec):
            grid[r][c] = " "
   

def get_border_corners(grid, r, c):
    sr, sc = r, c
    while r < len(grid) and grid[r][sc] == "#":
        r += 1
    r -= 1
    # r goes from sr to r

    while c < len(grid[0]) and grid[sr][c] == "#":
        c += 1
    c -= 1
    # c goes from sc to c

    return (sr, sc, r, c)

def remove_ads(grid):
    s = [(0, 0, len(grid) - 1, len(grid[0]) - 1, False)]
    while s:
        sr, sc, er, ec, image = s.pop()
        for r, c in product(range(sr, er + 1), range(sc, ec + 1)):
            if grid[r][c] == "+": # its a border start!
                # lots of things should happen here
                # first: get the border span
                # second: finding a border will subdivide current
                #         frame in the following manner (d means done):
                #     ddddddd
                #     d+++++2
                #     1+333+2
                #     1+++++2
                #     .......

                cr1, cc1, cr2, cc2 = get_border_corners(grid, r, c)

