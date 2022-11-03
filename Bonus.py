reps = (1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
        10, 11, 12, 13, 14, 14, 16, 18, 18, 27, 27, 36)

counter = {}
global counts = 0


class State:
    def __init__(self, biden, trump, flags, mark_new_index=-1):
        self.biden = biden
        self.trump = trump
        if mark_new_index == -1:
            self.flags = flags
        else:
            self.flags = flags[:mark_new_index] + (True,) + flags[mark_new_index + 1:]

    def __eq__(self, other):
        return self.biden == other.biden and self.trump == other.trump and self.flags == other.flags

    def __hash__(self):
        return hash((self.biden, self.trump, self.flags))


I = {State(0, 0, (False,) * 49)}


def post(s: State):
    p = set()
    for idx, flag in enumerate(s.flags):
        if not flag:
            if (State(s.biden + reps[idx], s.trump, s.flags, idx)) in counter.keys():
                counter[(State(s.biden + reps[idx], s.trump, s.flags, idx))] += 1
            else:
                counter[(State(s.biden + reps[idx], s.trump, s.flags, idx))] = 0
                counts = counts + 1
                p.add(State(s.biden + reps[idx], s.trump, s.flags, idx))

            if (State(s.biden, s.trump + reps[idx], s.flags, idx)) in counter.keys():
                counter[(State(s.biden, s.trump + reps[idx], s.flags, idx))] += 1
            else:
                counter[(State(s.biden, s.trump + reps[idx], s.flags, idx))] = 0
                counts = counts + 1
                p.add(State(s.biden, s.trump + reps[idx], s.flags, idx))
    return p


def POST(S):
    print(counts)
    return set.union(*(post(s) for s in S))


S = I
print(f'1 --> {len(S)}')

for i in range(2, 100):
    counts = 0
    S = POST(S)
    print(f'{i} --> {len(S)}')