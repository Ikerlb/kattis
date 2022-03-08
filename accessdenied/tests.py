import subprocess
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

def run(pw):
    s = f"diff <(python testing_tool.py -p {pw} go run sol.go) <(python testing_tool.py -p {pw} python /tmp/sol.py)"
    subprocess.call(['bash', '-c', s])

def create(length):
    poss = ascii_lowercase + ascii_uppercase + digits
    return "".join(choice(poss) for _ in range(length))

n = 100
for _ in range(n):
    pw = create(10)
    run(pw)

