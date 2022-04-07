tcs = int(input())

# s, e is guaranteed
# to be in range [1, 10]
def is_island(arr, s, e):
    m = max(arr[s - 1], arr[e + 1])
    for i in range(s, e + 1):
        if arr[i] <= m:
            return False
    return True

def islands(arr):
    for s in range(1, len(arr)):
        for e in range(s, len(arr) - 1):
            yield s, e    

for tc in range(tcs):
    arr = [int(s) for s in input().split(" ")[1:]]
    print(tc + 1, sum(1 for s, e in islands(arr) if is_island(arr, s, e)))
