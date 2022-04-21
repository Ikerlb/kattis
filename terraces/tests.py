from random import randint

def create_test_case(rows, cols, height):
    res = [f"{cols} {rows}"]
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(str(randint(0, height)))
        res.append(" ".join(row))
    return "\n".join(res)


with open("/tmp/terraces.in", "w") as f:
    rows = 500
    cols = 500
    height = randint(1, 999)
    tc = create_test_case(rows, cols, height)
    f.write(tc)
    print(tc)
