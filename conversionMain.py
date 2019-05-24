from dfa_convertion import DFA
from nfa import NFA

with open("input2.txt") as f:
    sample = f.read()
    my_nfa = NFA()
    my_nfa.constructNFA(sample)
    my_dfa = DFA(my_nfa)
    my_dfa.convert_from_nfa()
    print(my_dfa)