import sys
from collections import deque
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 3):
    n = int(lines[ii])
    n*=2
    trump = lines[ii+1]
    def beats(a, b):
        if a[1] == trump and b[1] == trump:
            return a[0] > b[0]
        if a[1] == trump:
            return True
        if a[1] != b[1]:
            return False
        return a[0] > b[0]
    cards = lines[ii+2].split()
    def find_soln(preds):
        curr = (1 << n) - 1
        printed = 0
        to_print = []
        while curr != 0:
            for bit in range(n):
                if (1 << bit & curr) and not (1 << bit & preds[curr]):
                    to_print.append(cards[bit])
                    curr = preds[curr]
                    if len(to_print) == 2:
                        print(" ".join(to_print[::-1]))
                        to_print = []
                    
    def find_played(state_a, state_b):
        for bit in range(n):
            if (1 << bit & state_a) and not (1 << bit & state_b):
                return cards[bit]
        raise ValueError("No played card found")
    seen = set()
    preds = {}
    dq = deque([0])
    while dq:
        state = dq.popleft()
        if state in seen:
            continue
        if state == (1<<n)-1:
            find_soln(preds)
            break
        seen.add(state)
        to_beat = state.bit_count() % 2 == 1
        for i in range(n):
            if (state & (1<<i)) == 0:
                other_state = state | (1<<i)
                if other_state not in preds:
                    if to_beat:
                        prev_card = find_played(state, preds[state])
                        if not beats(cards[i], prev_card):
                            continue
                    preds[other_state] = state
                    dq.append(other_state)
    else:
        print("IMPOSSIBLE")
    # print(seen)
    

