### Features

- DataStructure for saving deterministic and non-deterministic finite automata
- Transform NFA to DFA
- Minimize DFA states

## NFA and DFA Classes
### construction
It's possible to construct DFA and NFA by input string content.
```python
from dfa import DFA
with open("input.txt") as f:
    tmp = DFA()
    sample = f.read()
    tmp.constructNFA(sample)
```
or add transitions with `add(source, label, destination)`

### String Representation
NFA and DFA objects could represent in string format : (like the input format)
```python
sample = '''5
0,1
->q0,0,q1
q0,1,q3
q1,0,q2
q1,1,*q4
q2,0,q1
q2,1,*q4 
q3,0,q2
q3,1,*q4
*q4,0,*q4
*q4,1,*q4'''

tmp = DFA()
tmp.constructNFA(sample)
tmp.minimize()
print(tmp)
'''3
0,1
->q0,1,q1
q0,0,q1
q1,1,*q2
q1,0,q1
*q2,0,*q2
*q2,1,*q2'''
```
### Properties
NFA Properties: 
```python
#attributes
nfa.initilState = None
nfa.finalState = []
nfa.numofStates = None
nfa.alphabet = []
nfa.transitions = {}
#methods
nfa.add(source, lable, destination)
nfa.constructNFA(nfaContent)
str(nfa)
```
    
DFA class is inherited from NFA. It has extra methods for minization.
```python
dfa.minimize()
dfa.minimization(classes, state_to_class)
dfa.get_reachable_states()
# other logic methods ...
```


## Transform NFA to DFA

## Minimization
Insert DFA content in input.txt and run minimizeMain.py


