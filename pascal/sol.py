from math import ceil

"""
readln(N);
counter := 0;
for i := N - 1 downto 1 do begin
  counter := counter + 1;
  if N mod i = 0 then break;
end;
writeln(counter);
"""

def simulate(n):
    counter = 0
    for i in range(n - 1, 0, -1):
        counter += 1
        if n % i == 0:
            break
    return counter

def largest_factor(n):
    lim = ceil(n ** 0.5) + 1
    for i in range(2, lim):    
        if n % i == 0:        
            return n // i
    return n

#def side_by_side(n):
#    print("have", n - largest_factor(n))
#    print("should be", simulate(n))

n = int(input())
f = largest_factor(n)
if f == n: # is prime
    print(n - 1)
else:
    print(n - f) 
