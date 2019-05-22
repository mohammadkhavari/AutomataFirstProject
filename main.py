from nfa import NFA

sample = '''4
a,b
->q0,a,q1
q0,b,q1
q0,a,q2 
q0,b,*q3 
q1,a,q1 
q1,a,*q3 
q2,_,q0 
*q3,a,q1 
*q3,b,q2'''

tmp = NFA()
tmp.constructNFA(sample)

print(tmp)