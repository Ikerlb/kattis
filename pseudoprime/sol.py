import fileinput

def is_prime(n):
    # Our list of deterministic bases
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    
    # Handle simple cases and check if n is one of our bases
    if n < 2:
        return False
    if n in bases:
        return True
    if any(n % b == 0 for b in bases): # Optimization for small factors
        return False

    # The single-base test function (our witness checker)
    def is_composite_witness(a, n):
        s = 0
        d = n - 1
        while d % 2 == 0:
            d >>= 1
            s += 1
        
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == 1:
                return True
            if x == n - 1:
                return False
        
        return True

    # Run the test for all our deterministic bases
    for a in bases:
        if is_composite_witness(a, n):
            return False
            
    return True

# The single-base test function (our witness checker)
def is_pseudoprime(p, a):
    res = pow(a, p, p)
    return res == a

for line in fileinput.input():
    p, a = map(int, line[:-1].split(" "))
    if p == a == 0:
        break
    if is_pseudoprime(p, a) and not is_prime(p):
        print("yes")
    else:
        print("no")
