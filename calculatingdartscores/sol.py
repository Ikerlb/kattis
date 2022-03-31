def k_sum(arr, k, target):
    return _k_sum(arr, 0, k, target)

def _k_sum(arr, i, k, target):
    if k == 2:
        return two_sum(arr, i, target)
    for j in range(i, len(arr)):
        t = _k_sum(arr, j, k - 1, target - arr[j])
        if t:
            return (arr[j],) + t
    return None

def two_sum(arr, i, target):
    start, end = i, len(arr) - 1 
    while start <= end:
        s = arr[start] + arr[end]
        if s == target:
            return (arr[start], arr[end])
        elif s < target:
            start += 1
        else:
            end -= 1
    return None

desc = {} 
for i in range(1, 21):
    desc[i] = f"single {i}"
    desc[i * 2] = f"double {i}"
    desc[i * 3] = f"triple {i}"

#print(desc)


n = int(input())
arr = list(desc.keys())
if n in desc:
    print(desc[n])
    quit()
else:
    for k in [2, 3]:
        t = k_sum(arr, k, n)
        if t:
            for nn in t:
                print(desc[nn])
            quit()
print("impossible")
