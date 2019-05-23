from nfa import NFA

class DFA(NFA):

    def minimize(self):
        self.remove_unreachable_states()

    def remove_unreachable_states(self):
        from queue import Queue
        reachables = set()
        q = Queue()
        q.put(dfa,instance)
        while not q.empty:
            state = q.get()
            reachables.add(state)
            for label, nextState in dfa.transitions[state]:
                if nextState not in reachables:
                    q.put(nextState)
        # now we reconstruct DFA with reachable states
        self.reconstruct(reachable)

    def reconstruct(self, rechables):
        dfaContent = str(self)
        lines = dfaContent.split('\n')
        newDFA = DFA()
        newDFA.numofStates = int(lines[0])
        newDFA.alphabet = lines[1].split(',')
        lines = lines[2:]
        for i in range(0, newDFA.numofStates):
            newDFA.transitions[i] = set()
        for line in lines:
            parts = line.split(',')
            statesInt = []
            for state in [parts[0], parts[2]] :
                tmp = int(state.split('q')[1])
                statesInt.append(tmp)
                if '->' in state:
                    newDFA.instance = tmp
                if '*' in state and tmp not in newDFA.finalState:
                    newDFA.finalState.append(tmp)
            if statesInt[0] not in reachables and statesInt[1] not in reachables:
                newDFA.add(statesInt[0], parts[1], statesInt[1])
        self = newDFA
