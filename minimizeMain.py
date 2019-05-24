from dfa import DFA

with open("input1.txt") as f:
    tmp = DFA()
    sample = f.read()
    tmp.constructNFA(sample)
    tmp.minimize()
    print(tmp)

