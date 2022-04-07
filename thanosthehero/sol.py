_ = int(input())
arr = [int(n) for n in input().split(" ")]

res = 0
for i in range(len(arr) - 1, 0, -1):
    #print(i, arr)
    need = arr[i - 1] - arr[i] + 1
    if arr[i] <= arr[i - 1] and arr[i - 1] >= need:
        arr[i - 1] -= need
        res += need
    elif arr[i] <= arr[i - 1]:
        print(1)
        break
else:
    print(res)
