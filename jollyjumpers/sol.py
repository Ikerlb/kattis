from sys import stdin

def is_jolly(nums):
    if len(nums) == 1:    
        return True    
    s = {i for i in range(1, len(nums))}
    for i in range(1, len(nums)):
        s.discard(abs(nums[i] - nums[i - 1]))
    return not bool(s) 

for line in stdin:
    arr = [int(n) for n in line.split(" ")[1:]]
    print("Jolly" if is_jolly(arr) else "Not jolly")
