from heapq import heappush, heappop

N, K = map(int, input().split(" "))

h = []
dropped = set()
for _ in range(N):
    s = input().split(" ")
    if s[0] == "1":
        t = int(s[1])
        name = s[2]
        s = int(s[3])
        priority = s - (K*t)
        heappush(h, (-priority, name, s, t)) 
    elif s[0] == "2":
        while h and h[0][1] in dropped:
            heappop(h)

        if not h:
            print("doctor takes a break")
            continue

        p, name, s, t = heappop(h)
        print(name)
    elif s[0] == "3":
        t = int(s[1])
        name = s[2]
        dropped.add(name)


# S1 + (K * (CT - T1)) = S1 - K*T1
# S2 + (K * (CT - T2)) = S2 - K*T2
# S3 + (K * (CT - T3)) = S3 - K*T3
