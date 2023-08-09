from sys import stdin

inv = {"|": "-", "-": "|", " ": " ", "+": "+"}

def rotate(figure):
    res = []
    m = max(len(row) for row in figure)
    for i in range(m):
        nr = [inv[row[i]] if i < len(row) else " " for row in figure]
        res.append("".join(reversed(nr)))
    return "\n".join(row.rstrip() for row in res)
    

res = []
while (n := int(next(stdin))) != 0:
    figure = [next(stdin)[:-1] for _ in range(n)]
    res.append(rotate(figure)) 
print("\n\n".join(res))
