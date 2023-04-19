from lexer.lexer import Lexer
from grammar.grammar import Grammar
from fa import *
from utils import *


# productions:
# S -> A 

# A -> aX 
# A -> bX 

# X -> e 
# X -> BX 
# X -> b 

# B -> AD 

# D -> aD 
# D -> a 

# C -> Ca 

productions = {
    'S' : ['A'],
    'A' : ['aX', 'bX'],
    'X' : ['', 'BX', 'b'],
    'B' : ['AD'],
    'D' : ['aD', 'a'],
    'C' : ['Ca']
}

grm = Grammar(productions)
grm.visualize()
grm.to_cnf() 
 
# print(gr qm.rules)
# print(grm.generate_string())
