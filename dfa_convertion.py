from nfa import NFA

class DFA():
    def __init__(self, nfa_sample):
        self.initialState = None
        self.finalStates = []
        self.numOfStates = None
        self.alphabet = nfa_sample.alphabet
        self.transitions = []
        self.nfa = nfa_sample
        self.q = []
        if '_' in self.alphabet:
            self.alphabet.remove('_')

    def convert_from_nfa(self):
        self.initialState = self.nfa.initialState

        nfa_transition_dict = {}
        dfa_transition_dict = {}

        #Combine NFA transitions            
        for (key, value) in self.nfa.transitions.items():
            for tupl in value:
                starting_state = key
                lable = tupl[0]
                ending_state = tupl[1]

                if lable != '_':
                    if (starting_state, lable) in nfa_transition_dict:
                        nfa_transition_dict[(starting_state, lable)].append(ending_state)
                    else:
                        nfa_transition_dict[(starting_state, lable)] = [ending_state]

                    lambda_transitions = []

                    #BFS for finding all lambda transitions
                    visited = []
                    queue = []

                    queue.insert(0, ending_state)

                    while(len(queue) != 0):
                        temp = queue.pop()
                        visited.append(temp)

                        for node in [item[1] for item in self.nfa.transitions[temp] if item[0] == '_']:
                            if node not in visited:
                                queue.insert(0, node)
                                lambda_transitions.append(node)


                    for node in lambda_transitions:
                        nfa_transition_dict[(starting_state, lable)].append(node)
        
        self.q.append((0,))
        
        #Convert NFA transitions to DFA transitions
        for dfa_state in self.q:
            for lable in self.alphabet:
                if len(dfa_state) == 1 and (dfa_state[0], lable) in nfa_transition_dict:
                    dfa_transition_dict[(dfa_state, lable)] = nfa_transition_dict[(dfa_state[0], lable)]

                    if tuple(dfa_transition_dict[(dfa_state, lable)]) not in self.q:
                        self.q.append(tuple(dfa_transition_dict[(dfa_state, lable)]))
                else:
                    destinations = []
                    final_destination = []

                    for nfa_state in dfa_state:
                        if (nfa_state, lable) in nfa_transition_dict and nfa_transition_dict[(nfa_state, lable)] not in destinations:
                            destinations.append(nfa_transition_dict[(nfa_state, lable)])
                    
                    if not destinations:
                        final_destination.append(None)
                    else:
                        for destination in destinations:
                            for value in destination:
                                if value not in final_destination:
                                    final_destination.append(value)
                    
                    dfa_transition_dict[(dfa_state, lable)] = final_destination

                    if tuple(final_destination) not in self.q:
                        self.q.append(tuple(final_destination))

        #Convert NFA states to DFA states
        for key in dfa_transition_dict:
            self.transitions.append((self.q.index(tuple(key[0])), key[1], self.q.index(tuple(dfa_transition_dict[key]))))
        
        for q_state in self.q:
            for nfa_final_state in self.nfa.finalState:
                if nfa_final_state in q_state:
                    self.finalStates.append(self.q.index(q_state))

        #Assigning number of states
        states = []
        for transition in self.transitions:
            if transition[0] not in states:
                states.append(transition[0])
            if transition[2] not in states:
                states.append(transition[2])
        
        self.numOfStates = len(states)
    
    def __str__(self):
        #demo = ''
        #demo += 'Initial state: {}\n'.format(self.initialState)
        #demo += 'Final states: {}\n'.format(self.finalStates)
        #demo += 'Transitions: {}\n'.format(self.transitions)

        demo = "{}\n{}\n".format(self.numOfStates, ','.join(self.alphabet))
        flag = False
        for transition in self.transitions:
            if transition[0] == self.initialState and not flag:    
                demo += "->"
                flag = True

            a = transition[0]
            l = transition[1]
            b = transition[2]

            if a in self.finalStates:
                demo += '*'

            demo += 'q{},{},'.format(a, l)

            if b in self.finalStates:
                demo += '*'

            demo += 'q{}\n'.format(b)
        
        return demo
