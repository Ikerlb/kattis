statues = int(input())

# bottom line is
# if you have to spend
# a day to print statues
# anyway, you can just as well
# spend that day to doulb the printers
# and print double the statues for next
# day. so if you can double, you SHOULD double

i = 0
while (1 << i) < statues:
    i += 1
print(i + 1)
