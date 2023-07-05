from itertools import product

def diagonal(l, turn):
    if all(l[i][i] == turn for i in range(3)) or \
        all(l[i][2 - i] == turn for i in range(3)):
            return True
    return False

def vertical(l, turn):
    for c in range(3):
        if all(l[r][c] == turn for r in range(3)):
            return True
    return False

def horizontal(l, turn):
    for r in range(3):
        if all(l[r][c] == turn for c in range(3)):
            return True
    return False 

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
    if turn == 'X':
        return 'O'
    else:
        return 'X'

def solve(state):
    

class State:
    def __init__(self, turn, l = None):
        self.turn = turn
        if l is None:
            self.board = [[None] * 3 for _ in range(3)]
        else:
            self.board = [row[:] for row in l]

    def __repr__(self):
        res = []
        for r in self.board:
            res.append("".join("." if e is None else e for e in r))
        return "\n".join(res)

    def neighbors(self):
        nt = next_turn(self.turn)
        for r, c in product(range(3), range(3)):
            if self.board[r][r] is None:
                nb = [row[:] for row in self.board]
                nb[r][c] = nt
                yield State(nt, l = nb)
