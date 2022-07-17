

def solve(n):
    # is n is a consecutive num
    # sum, then it is of the form

    # (a * (a + 1) // 2) - (b * (b + 1) // 2) = n
    # if we know b then we can calculate a as follows

    # (a^2 + a) // 2 - (b^2 + b) // 2 = n 
    # 1/2 * (a^2 + a - b^2 - b) = n
    # a^2 + a - b^2 - b = n/2

    
