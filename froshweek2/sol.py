n, m = map(int, input().split(" "))

tasks = [int(n) for n in input().split(" ")]
quiet = [int(n) for n in input().split(" ")]

tasks.sort(reverse = True)
quiet.sort(reverse = True)

i = j = res = 0
while i < len(tasks) and j < len(quiet):
    if quiet[j] >= tasks[i]:
        i += 1
        j += 1
        res += 1
    else:
        i += 1
print(res)
