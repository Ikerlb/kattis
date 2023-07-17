from collections import deque
from sys import stdin
import re

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

lines = [line[:-1] for line in stdin]

# god forgive me for using eval
# i had originally implemented
# shunting-yard but forgot to handle
# unary -, at which point I decided to just use eval
print("\n".join(f"{eval(line):.2f}" for line in lines))
