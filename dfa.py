from nfa import NFA

class DFA(NFA):

    def minimize(self):
        # find all reachable states and do the minimization peocess just for reachables
        reachables = self.get_reachable_states()
        # prevent to ignore trapa cuase they'll become one state
        classes = [{},{}]
        state_to_class = {}
        for state in reachables:
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
                    for state in reachables:
                        if state_to_class[state] == i:
                            class_[state] = self.transition_per_alphabet(state)
                    classes.append(class_)
            self.minimization(classes, state_to_class)


    def minimization(self, classes, state_to_class):
        finals = self.finalState
        self.transitions = {}
        self.finalState = []
        self.numofStates = len(classes)
        for i in range(0, self.numofStates):
            self.transitions[i] = set()
        for class_ in classes:
            state = list(class_.keys())[0]
            nextStates = class_[state]
            if state in finals:
                self.finalState.append(state_to_class[state])
            for i in range(0, len(self.alphabet)):
                self.add(state_to_class[state], self.alphabet[i], state_to_class[nextStates[i]])

    def get_reachable_states(self):
        from queue import Queue
        reachables = set()
        q = Queue()
        q.put(self.initialState)
        while q.qsize() > 0:
            state = q.get()
            reachables.add(state)
            for _, nextState in self.transitions[state]:
                if nextState not in reachables:
                    q.put(nextState)
        return reachables

    def still_grouped(self,state_transitions1, state_transitions2, state_to_class):
        for i in range(0, len(state_transitions1)):
            if state_to_class[state_transitions1[i]] != state_to_class[state_transitions2[i]]:
                return False
        return True

    def transition_per_alphabet(self, state):
        label_to_state = {}
        for label, destinition in self.transitions[state]:
            label_to_state[label] = destinition
        return [label_to_state[label] for label in self.alphabet]
