import copy
import random

class Grammar:

    
    def __init__(self, rules):
        self.rules = rules
        self.is_cnf = False
        self.starter_symbol = 'S'

    def check_string(self, string):
        for i in range (len(string)):
            if string[i] in self.rules.keys():
                return "false"
        return "true"
    
    def generate_string(self):
        new_str = self.starter_symbol

        j = len(new_str) - 1
        while (self.check_string(new_str) == "false"):
            if new_str[j] in self.rules.keys():
                new_str = new_str[0:j] + random.choice(self.rules[new_str[j]])
                j = len(new_str) - 1
        return new_str
    
    def new_starter(self):
        for i in self.rules:
            for j in self.rules[i]:
                for k in j: 
                    if self.starter_symbol == k:
                        self.rules['0'] = self.starter_symbol
                        self.starter_symbol = '0'
                        return
        

    def bfs(self, nonterminal):
        visited = []  
        queue = []

        queue.append('S')
        visited.append('S')
        
        while queue:
            m = queue.pop(0)
            for neighbour in self.rules[m]:
                for letter in neighbour:
                    if letter in nonterminal:
                        if letter not in visited:
                            visited.append(letter)
                            queue.append(letter)

        for i in list(self.rules):
            if i not in visited:
                del self.rules[i]   

    def remove_nullable(self):
        nullable = []
        for i in self.rules:
            for j in self.rules[i]:
                if j == '':
                    nullable.append(i)
                    self.rules[i].remove(j)
        
        for i in self.rules:
            for j in self.rules[i]:
                for k in j:
                    if k in nullable:
                        self.rules[i].append(j[:j.rfind(k)])
                        

    def remove_units(self, nonterminal):
        g = {}
        for i in self.rules:
            for j in self.rules[i]:
                g_keys = []
                guf_keys = []

                if len(j) == 1 and j in nonterminal:
                    g_keys.append(j)
                    self.rules[i].remove(j)
                else:
                    guf_keys.append(j)

            if g_keys:
                g[i] = g_keys

        for i in g:
            for j in g[i]:
                temp = self.rules[i] + self.rules[j]
                self.rules[i] = temp

    def remove_mixing(self, terminal, upper_alphabet):
        new_rules = {}
        for i in terminal:
            new_key = random.choice(upper_alphabet)
            upper_alphabet.remove(new_key)
            self.rules[new_key] = [i]
            new_rules[i] = new_key
        remove_dict = {}

        for i in self.rules:
            remove_list = []
            for j in self.rules[i]:
                if len(j)>1:
                    for k in j:
                        if k in terminal:
                            new_str = j[:j.find(k)] + new_rules[k] +j[j.find(k)+1]
                            self.rules[i].append(new_str)
                            remove_dict[i] = []
                            remove_list.append(j)
            remove_dict[i] = remove_list

        for i in remove_dict:
            for j in remove_dict[i]:
                if j in self.rules[i]:
                    self.rules[i].remove(j)


    def visualize(self):
        for i in self.rules:
            for j in self.rules[i]:
                print(i, " -> ", j)
                
    def to_cnf(self):
        # step 1: make a new starter symbol
        self.new_starter()

        print("========================================================")
        print("If the starting string S is on the right hand side of any production, adds a new starting nonterminal")
        self.visualize()
        # step 2: remove epsilon and redundant producitons
        # remove the inacsessible nodes
        nonterminal = []
        for i in self.rules:
            nonterminal.append(i)

        self.bfs(nonterminal)
        print("========================================================")
        print("Removed the unreachable nonterminals")
        self.visualize()
        # remove epsilon productions
        self.remove_nullable()
        print("========================================================")
        print("Removed the epsilon producitons")
        self.visualize()
        # remove unit productions
        self.remove_units(nonterminal)
        print("========================================================")
        print("Removed the unit productions")
        self.visualize()
        # step3
        terminal = set()
        for i in self.rules:
            for j in self.rules[i]:
                for k in j:
                    if ord(k) <= ord('z') and ord(k) >= ord('a'):
                        terminal.add(k)

        upper_alphabet = []
        for i in range(ord('A'), ord('Z')):
            upper_alphabet.append(chr(i))

        for i in nonterminal[:]:
            if i in upper_alphabet:
                upper_alphabet.remove(i)

        self.remove_mixing(terminal, upper_alphabet)
        print("========================================================")
        print("Removed productions of type A -> aB")
        self.visualize()



