from sys import stdin

for e in stdin:
    if "no solution" in e:
        continue
    e = e.replace("/", "//")
    e, res = e.split(" = ")
    correct = eval(e)
    if int(correct) != int(res): 
        print(f"Error! {e} is {res}, should be {int(correct)}")
