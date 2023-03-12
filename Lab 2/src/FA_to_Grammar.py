import random

class Converter:
    def alphabet_generator(self, typ):
        abc = []
        if typ == 1:
            start = ord('A')
            end = ord('Z')
        else:
            start = ord('a')
            end = ord('z')
        i = start
        while i != end:
            abc.append(chr(i)) 
            i+=1
        return abc
            
    
    def fa_to_grammar(self, fa):
        nonterminals = set()
        state_dict= {}
        
        upper_abc = self.alphabet_generator(1)
        for i in fa.states:
            if i == 0:
                state_dict[0] = "S"
                nonterminals.add("S")
                upper_abc.remove("S")
            else:
                addition = random.choice(upper_abc)
                state_dict[i] = addition
                upper_abc.remove(addition)
                nonterminals.add(addition)
        
        rules = {}
                
        for i in fa.transition_table:
            rules[state_dict[i]] = []

            for j in fa.alphabet:
                if len(fa.transition_table[i][j]) > 0:
                    for x in range(len(fa.transition_table[i][j])):
                        fa.transition_table[i][j] = list(fa.transition_table[i][j])
                        rules[state_dict[i]].append(j + state_dict[fa.transition_table[i][j][x]]) 
        return rules