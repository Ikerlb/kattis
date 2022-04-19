def dfs(arr, i, s):
    if s >= 200:
        return 0
    if i == len(arr):
        return s
    return dfs(arr, i + 1, s + arr[i]) + dfs(arr, i + 1, s)

n = int(input())
arr = [int(s) for s in input().split(" ")]
arr.sort(reverse = True)
total = 2 ** (n - 1)

# each element appears in exactly 2 ** (n - 1) sets
below_200 = dfs(arr, 0, 0)
print(sum(w * total for w in arr) - below_200)
