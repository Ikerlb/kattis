def solve(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

tcs = int(input())
for i in range(tcs):
    _ = input()
    v1 = [int(n) for n in input().split(" ")]
    v2 = [int(n) for n in input().split(" ")]
    v1.sort()
    v2.sort(reverse = True)
    print(f"Case #{i + 1}: {solve(v1, v2)}")    
