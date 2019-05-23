from nfa import NFA

class DFA(NFA):

    def minimize(self):
        self.remove_unreachable_states()
        # prevent to ignore trapa cuase they'll become one state
        classes = [{},{}]
        state_to_class = {}
        for state in range(0, self.numofStates):
            if state in self.finalState:
                classes[1][state] = self.transition_per_alphabet(state)
                state_to_class[state] = 1
            else:
                classes[0][state] = self.transition_per_alphabet(state)
                state_to_class[state] = 0
        while True:
            is_changed = False
            new_state_to_class = {}
            class_count = 0
            for class_ in classes:
                updated = set()
                for state,transitions in class_.items():
                    if state not in updated:
                        new_state_to_class[state] = class_count
                        for state1, transitions1 in class_.items():
                            if state1 not in updated:
                                if self.still_grouped(transitions, transitions1, state_to_class):
                                    new_state_to_class[state1] = class_count
                                    updated.add(state1)
                                else:
                                    is_changed = True
                        updated.add(state)
                        class_count += 1
            if not is_changed :
                break
            else : #update classes
                state_to_class = new_state_to_class.copy()
                classes = []
                for i in range(0, class_count):
                    class_ = {}
                    for state in range(0, self.numofStates):
                        if state_to_class[state] == i:
                            class_[state] = self.transition_per_alphabet(state)
                    classes.append(class_)
            self.construct_minimize(classes, state_to_class)

    def construct_minimize(self, classes, state_to_class):
        finals = self.finalState
        start = self.instance
        self.transitions = {}
        self.instance = None
        self.finalState = []
        self.numofStates = len(classes)
        for i in range(0, self.numofStates):
            self.transitions[i] = set()
        for class_ in classes:
            state = list(class_.keys())[0]
            nextStates = class_[state]
            for i in range(0, len(self.alphabet)):
                self.add(state_to_class[state], self.alphabet[i], state_to_class[nextStates[i]])

    def remove_unreachable_states(self):
        from queue import Queue
        reachables = set()
        q = Queue()
        q.put(self.instance)
        while q.qsize() > 0:
            state = q.get()
            reachables.add(state)
            for label, nextState in self.transitions[state]:
                if nextState not in reachables:
                    q.put(nextState)
        # now we reconstruct DFA with reachable states
        self.reconstruct(reachables)

    def still_grouped(self,state_transitions1, state_transitions2, state_to_class):
        for i in range(0, len(state_transitions1)):
            if state_to_class[state_transitions1[i]] != state_to_class[state_transitions2[i]]:
                return False
        return True

    def reconstruct(self, reachables):
        oldDFA = self
        dfaContent = str(oldDFA)
        # reset self and reconstruct
        self.transitions = {}
        self.instance = None
        self.finalState = []
        self.numofStates = None
        self.alphabet = []
        self.transitions = {}

        lines = dfaContent.split('\n')
        self.numofStates = len(reachables)
        self.alphabet = lines[1].split(',')
        lines = lines[2:]
        for i in range(0, self.numofStates):
            self.transitions[i] = set()
        for line in lines:
            parts = line.split(',')
            statesInt = []
            for state in [parts[0], parts[2]] :
                tmp = int(state.split('q')[1])
                statesInt.append(tmp)
                if '->' in state:
                    self.instance = tmp
                if '*' in state and tmp not in self.finalState:
                    self.finalState.append(tmp)
            if statesInt[0] in reachables and statesInt[1] in reachables:
                self.add(statesInt[0], parts[1], statesInt[1])

    def transition_per_alphabet(self, state):
        label_to_state = {}
        for label, destinition in self.transitions[state]:
            label_to_state[label] = destinition
        return [label_to_state[label] for label in self.alphabet]
