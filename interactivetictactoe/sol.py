from itertools import product
from heapq import heappush, heappop

def neighbors(state):
    for r, c in product(range(3), range(3)):
        if state[r][c] == '.':
            yield r, c

def diagonal(s):
    for c in ['X', 'O']:
        if all(s[i][i] == c for i in range(3)) or \
        all(s[i][2 - i] == c for i in range(3)):
            return c
    return None

def vertical(state):
    for ch in ['X', 'O']:
        for c in range(3):
            if all(state[r][c] == ch for r in range(3)):
                return ch
    return None

def horizontal(state):
    for ch in ['X', 'O']:
        for r in range(3):
            if all(state[r][c] == ch for c in range(3)):
                return ch
    return None

def is_finished(state):
    if all(all(x != '.' for x in row) for row in state):
        return 'tie'
    if (d := diagonal(state)):
        return d
    if (v := vertical(state)):
        return v
    if (h := horizontal(state)):
        return h
    return None

def next_turn(turn):
    return 'X' if turn == 'O' else 'O'

def fmt(state):
    return "\n".join("".join(row) for row in state)

def parse_state():
    state = []
    for i in range(3):
        state.append(list(input()))
    return state



first_move = input()
print(first_move)

l = parse_state()
print(l)

solve(l, 'X')
