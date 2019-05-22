class NFA():

    def __init__(self):
        self.InitialState = None
        self.FinalStates = []
        self.NumofStates = None
        self.Alphabet = []
        self.Transitions = {}

    def Add(self, source, lable, destination):
        self.Transitions[source].Add((lable, destination))

    def ConstructNFA(self, nfaContent):
        lines = nfaContent.split('\n')
        self.NumofStates = int(lines[0])
        self.Alphabet = lines[1].split(',')
        lines = lines[2:]
        for i in range(0, self.NumofStates - 1):
            self.Transitions[i] = set()
        for line in lines:
            parts = line.split(',')

            statesInt = []
            for state in [parts[0], parts[2]] :
                tmp = int(state.split('q')[1])
                statesInt.append(tmp)
                if '->' in state:
                    self.InitialState = tmp
                if '*' in state and tmp not in self.FinalStates:
                    self.FinalStates.append(tmp)
            
            self.Add(statesInt[0], parts[1], statesInt[1])

    def __str__(self):
        demo = "{}\n{}".format(self.NumofStates, ','.join(self.Alphabet))
        flag = False
        for (key, value) in self.Transitions:
            for tupl in value:
                if key == self.InitialState:
                    if not flag:
                        demo += "->"
                        flag = True
                a = key
                b = tupl[1]
                l = tupl[0]
                if a in self.FinalStates:
                    demo += '*'
                demo += 'q{},{},'.format(a, l)
                if b in self.FinalStates:
                    demo += '*'
                demo += 'q{}\n'.format(b)

                

                
        