def f(s):
    return {"p"} if s == "s1" else {"p", "q"} if s == "s2" else {}
def pre(TS, C, a=None):
    preSet = set()
    if isinstance(C, str):
        C = {C}
    for transition in TS["to"]:
        if transition[2] in C:
            if a is None or transition[1] == a:
                preSet.add(transition[0])
    return preSet


def post(TS, C, a=None):
    postSet = set()
    if isinstance(C, str):
        C = {C}
    for transition in TS["to"]:
        if transition[0] in C:
            if a is None or transition[1] == a:
                postSet.add(transition[2])
    return postSet


def is_action_deterministic(TS):
    if len(TS["I"])>1:
        return False
    for state in TS["S"]:
        for act in TS["Act"]:
            if len(post(TS, {state}, act))>1:
                return False
    return True

def is_label_deterministic(TS):
    if len(TS["I"])>1:
        return False
    for state in TS["S"]:
        postset=post(TS, {state})
        labelSet=set()
        for poststate in postset:
            labelSet.add(frozenset(TS["L"](poststate)))
        if len(labelSet)!=len(postset):
            return False
    return True



TS = {
    "S": {"s1", "s2", "s3"},
    "I": {"s1"},
    "Act": {"a", "b", "c"},
    "to": {("s1", "a", "s2"), ("s1", "a", "s1"), ("s1", "b", "s2"),
           ("s2", "c", "s3"), ("s3", "c", "s1")},
    "AP": {"p", "q"},
    "L": lambda s: {"p"} if s == "s1" else {"p", "q"} if s == "s2" else {}
}
print(pre(TS, {"s1", "s2"}))
assert pre(TS, {"s1", "s2"}) == {"s1", "s3"}
assert post(TS, "s1", "a") == {"s1", "s2"}
assert post(TS, {"s1", "s2"}, "a") == {"s1", "s2"}
assert pre(TS, {"s1", "s2"}) == {"s1", "s3"}
assert pre(TS, "s1") == {"s1", "s3"}
assert not is_action_deterministic(TS)
assert is_label_deterministic(TS)

