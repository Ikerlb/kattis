words = input().split(" ")

def is_ostgotska(w):
    return "ae" in w

n = sum(is_ostgotska(w) for w in words)
if n / len(words) >= 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
