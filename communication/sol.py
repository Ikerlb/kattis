from functools import lru_cache

@lru_cache(None)
def decode(b):
    # it barely makes a difference
    # but it is interesting to note
    # that the last bit of the unknown
    # byte is the same as the last bit
    # in the encoded byte
    start = int((b & 1) != 0)
    for x in range(start, 256, 2):
        if ((x ^ (x << 1)) & 255) == b:
            return x    

for i in range(256):
    decode(i)

_ = int(input())
bs = print(" ".join(str(decode(int(s))) for s in input().split(" ")))
