from dfa import DFA

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
