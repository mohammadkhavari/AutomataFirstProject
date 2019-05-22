class NFA():
    def __init__(self):
        self.instance = None
        self.finalState = []
        self.numofStates = None
        self.alphabet = []
        self.transitions = {}

    def add(self, source, lable, destination):
        self.transitions[source].add((lable, destination))

    def constructNFA(self, nfaContent):
        lines = nfaContent.split('\n')
        self.numofStates = int(lines[0])
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
            
            self.add(statesInt[0], parts[1], statesInt[1])

    def __str__(self):
        demo = "{}\n{}\n".format(self.numofStates, ','.join(self.alphabet))
        flag = False
        for (key, value) in self.transitions.items():
            for tupl in value:
                if key == self.instance:
                    if not flag:
                        demo += "->"
                        flag = True
                a = key
                b = tupl[1]
                l = tupl[0]
                if a in self.finalState:
                    demo += '*'
                demo += 'q{},{},'.format(a, l)
                if b in self.finalState:
                    demo += '*'
                demo += 'q{}\n'.format(b)
        return demo

                

                
        