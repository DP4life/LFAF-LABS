class Parser:
    def strip(self, line):
        lhs, rhs = line.split("{",1)
        lhs, rhs = rhs.split("}", 1)
        return lhs
    
    def unload(self, line):
#         state, inpt, dest
        lhs, rhs = line.split("(q", 1)
        lhs, rhs = rhs.split(",",1)
        state = int(lhs)
        lhs, rhs = line.split(",",1)
        lhs, rhs = rhs.split(")",1)
        inpt = lhs
        lhs, rhs = line.split("= q", 1)
        dest = int(rhs[0])
        
        return [state, inpt, dest]
    
    def parse(self):
        f = open('./var.txt')
        states = set([])
        alphabet = []
        accept_states = []
        start_state = int(0)
        line = self.strip(f.readline())
        
        for i in line:
            if i.isnumeric():
                states.add(int(i))        
        
        line = self.strip(f.readline())
        for i in line:
            if i.isalpha():
                alphabet.append(i)
               
        line = self.strip(f.readline())
        for i in line: 
            if i.isnumeric():
                accept_states.append(int(i))
   
        transition_table = {}
        transition = {}
       
        for j in alphabet:
            transition[j] = set([])
         
        states = list(states)
        for i in states:
            for j in alphabet:
                transition[j] = set([])
            transition_table[states[i]]= dict(transition)
        
        for x in f:
            line = self.unload(x)
            state = line[0]
            inpt = line[1]
            dest = line[2]
            transition_table[state][inpt].add(dest)
           
        return states, alphabet, transition_table, start_state, accept_states
        
        f.close()