from dfa import DFA

with open("input.txt") as f:
    tmp = DFA()
    sample = f.read()
    tmp.constructNFA(sample)
    tmp.minimize()
    print(tmp)


