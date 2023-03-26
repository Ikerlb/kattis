N = int(input())
A = list(map(int, input().split()))

res = 0
for i in range(len(A)):
    #print(A[:i], A[i], A[i + 1:])
    l = sum(1 for e in A[:i] if e >= A[i] * 2)
    r = sum(1 for e in A[i + 1:] if e <= A[i] // 2)
    #print(f"{l=}, {r=}")

    res += r * l
    #print()

print(res)
