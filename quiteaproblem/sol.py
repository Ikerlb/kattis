from sys import stdin

for line in stdin:
    l = line[:-1].lower()
    print("yes" if "problem" in l else "no")
