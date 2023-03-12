import random, re, string

import FA
import Grammar
import GrammarClassifier
import Parser 
import FA_to_Grammar

#lab 1 remade
print()
print(" >>> Remaking the first lab in python")
print()
rules={
        "S" : ["aF", "bS"],
        "F" : ["bF", "cD", "a"],
        "D" : ["cS", "a"]
}
gram = Grammar.Grammar(rules)
sas = gram.generate_string()
print(" Generating a string with grammar:",sas)

states = {-1, 0, 1, 2, 3}
alphabet = {'a', 'b', 'c'}
transition_table = {
    -1: {'a' : [-1], 'b' : [-1], 'c' : [-1]},
    0: {'a': [1], 'b': [0], 'c' :[-1]},
    1: {'a': [3], 'b': [1], 'c' : [2]},
    2: {'a': [3], 'b': [-1], 'c': [0]},
    3: {'a': [-1], 'b' : [-1], 'c' : [-1]}
}
start_state = int(0)
accept_states = {3}

fa = FA.FA(states, alphabet, transition_table, start_state, accept_states)
print(" Does the FA accept the generated string:",fa.accepts(sas))


print()
print(" >>> Classifying the Grammar")
print() 
rules={
        "S" : ["aF", "bS"],
        "F" : ["bF", "cD", "a"],
        "D" : ["cS", "a"]
}

gram = Grammar.Grammar(rules)
gram_class = GrammarClassifier.GrammarClassifier()
print('',gram_class.check_grammar(gram.rules))

print()
print('============================ LAB2 ============================')
print()
print(" >>> Parsing the FA from the text file")
print()
parser = Parser.Parser()
states, alphabet, transition_table, start_state, accept_states = parser.parse()
fa = FA.FA(states, alphabet, transition_table, start_state, accept_states)
print(transition_table)
print()
print(" >>> Converting FA to Grammar")
print()
converter = FA_to_Grammar.Converter()
rr = converter.fa_to_grammar(fa)
# print(rr)
grammar = Grammar.Grammar(rr)
print(grammar.rules)

print()
print(" >>> Checking if FA a DFA")
print()

print("",fa.is_dfa())

print()
print(" >>> Converting NFA to DFA")
print()

dfa = fa.nfa_to_dfa()
print(" >>> Visualizing")

print()
print(" FA before conversion [NFA]")
fa.visualize()
print()
print(" FA after conversion [DFA]")
dfa.visualize()