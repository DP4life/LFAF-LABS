# Topic: Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.

### Course: Formal Languages & Finite Automata
### Author: Echim Mihail

## Objectives:
1. Understand what an automaton is and what it can be used for.

2. Continuing the work in the same repository and the same project, the following need to be added:
    a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

    b. For this you can use the variant from the previous lab.

3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.

    b. Determine whether your FA is deterministic or non-deterministic.

    c. Implement some functionality that would convert an NDFA to a DFA.
    
    d. Represent the finite automaton graphically (Optional, and can be considered as a __*bonus point*__):
      
    - You can use external libraries, tools or APIs to generate the figures/diagrams.
        
    - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.
## Implementation

* I remade the first lab in python
    * Grammar
        ```python
        class Grammar:
        
            def __init__(self, rules):
                self.rules = rules
            
            def check_string(self, string):
                for i in range (len(string)):
                    if string[i] in self.rules.keys():
                        return "false"
                return "true"
            
            def generate_string(self):
                new_str = "S"
                j = len(new_str) - 1
                while (self.check_string(new_str) == "false"):
                    if new_str[j] in self.rules.keys():
                        new_str = new_str[0:j] + random.choice(self.rules[new_str[j]])
                        j = len(new_str) - 1
                return new_str
        ```
    * Finite Automata
        ```python
            class FA:
                def __init__(self, states, alphabet, transition_table, start_state, accept_states):
                    self.states = states
                    self.alphabet = alphabet
                    self.transition_table = transition_table
                    self.start_state = start_state
                    self.accept_states = accept_states

                def accepts(self, s):
                    current_state = self.start_state
                    for c in s:
                        if c not in self.alphabet:
                            return False
                        next_states = self.transition_table[current_state][c]
                        if isinstance(next_states, list):
                            current_state = next_states[0]
                        else:
                            current_state = next_states
                    return current_state in self.accept_states
        ```
    * Grammar Classifier Class
        ```python
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
        ```
* I made a parser to parse the Finite Automata from a text file
    ```python
        class Parser:
            def strip(self, line):
                lhs, rhs = line.split("{",1)
                lhs, rhs = rhs.split("}", 1)
                return lhs
            
            def unload(self, line):
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
    ```
* I made a class to Convert Finite Automata to a Grammar
    ```python
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
    ```
* I added functions to FA to check for DFA, to convert to NFA, and to visualize the FA
    ```python
   def is_dfa(self):
        isnfa = 0
        for i in self.transition_table:
            for j in self.alphabet:
                if len(self.transition_table[i][j]) > 1:
                    isnfa += 1
                    break
        if isnfa > 0:
            return False
        else: 
            return True
    def epsilon_closure(self, states):
        # Compute the epsilon closure of a set of NFA states
        closure = set(states)
        stack = list(states)
        while stack:
            state = stack.pop()
            for next_state in self.transition_table[state].get(None, []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure
    def nfa_to_dfa(self):
        # Start with the epsilon closure of the start state
        start_set = self.epsilon_closure( [self.start_state])
        dfa_states = {frozenset(start_set): 0}
        dfa_alphabet = self.alphabet
        dfa_transition_table = {}
        dfa_accept_states = set()

        # Queue of DFA states to process
        unprocessed_states = [start_set]

        while unprocessed_states:
            current_set = unprocessed_states.pop(0)
            current_state = dfa_states[frozenset(current_set)]

            # Check if the current set contains an accept state
            if any(state in self.accept_states for state in current_set):
                dfa_accept_states.add(current_state)

            # Build the transition table for the current state on each input symbol
            for symbol in dfa_alphabet:
                next_set = set()
                for state in current_set:
                    next_states = self.transition_table[state].get(symbol, [])
                    next_set.update(self.epsilon_closure(next_states))

                # Create a new DFA state for the next set if it doesn't already exist
                if next_set and frozenset(next_set) not in dfa_states:
                    dfa_states[frozenset(next_set)] = len(dfa_states)
                    unprocessed_states.append(next_set)

                # Add the transition from the current DFA state to the next DFA state
                if next_set:
                    next_state = dfa_states[frozenset(next_set)]
                    dfa_transition_table.setdefault(current_state, {})[symbol] = next_state

        # Build the DFA object
        dfa_states = list(range(len(dfa_states)))
        dfa_start_state = 0
        dfa_accept_states = list(dfa_accept_states)
        print(dfa_transition_table)
        return FA(dfa_states, dfa_alphabet, dfa_transition_table, dfa_start_state, dfa_accept_states)

    def visualize(self):
        for i in self.transition_table:
            for j in self.alphabet:
                if j in self.transition_table[i]:
                    if type(self.transition_table[i][j]) != int:
                        for x in self.transition_table[i][j]:
                            print('q',i, ' ---',j,'---> ',x)
                    elif type(self.transition_table[i][j]) == int:
                        print('q',i, ' ---',j,'---> ',self.transition_table[i][j])
    ```
    ## Output
    ```
    >>> Remaking the first lab in python

    Generating a string with grammar: accaccaa
    Does the FA accept the generated string: True

    >>> Classifying the Grammar

    Type 3: The grammar is a regular grammar.

    ============================ LAB2 ============================

    >>> Parsing the FA from the text file

    {0: {'a': {1}, 'b': {0}, 'c': set()}, 1: {'a': {2}, 'b': set(), 'c': {1}}, 2: {'a': {3}, 'b': set(), 'c': set()}, 3: {'a': {1, 3}, 'b': set(), 'c': set()}}

    >>> Converting FA to Grammar

    {'S': ['aT', 'bS'], 'T': ['aE', 'cT'], 'E': ['aU'], 'U': ['aT', 'aU']}

    >>> Checking if FA a DFA

    False

    >>> Converting NFA to DFA

    {0: {'a': 1, 'b': 0}, 1: {'a': 2, 'c': 1}, 2: {'a': 3}, 3: {'a': 4}, 4: {'a': 5, 'c': 1}, 5: {'a': 5, 'c': 1}}
    >>> Visualizing

    FA before conversion [NFA]
    q 0  --- a --->  1
    q 0  --- b --->  0
    q 1  --- a --->  2
    q 1  --- c --->  1
    q 2  --- a --->  3
    q 3  --- a --->  1
    q 3  --- a --->  3

    FA after conversion [DFA]
    q 0  --- a --->  1
    q 0  --- b --->  0
    q 1  --- a --->  2
    q 1  --- c --->  1
    q 2  --- a --->  3
    q 3  --- a --->  4
    q 4  --- a --->  5
    q 4  --- c --->  1
    q 5  --- a --->  5
    q 5  --- c --->  1
    ```
    * I'm sorry for being so late with the Laboratory Work. I'm not very smart but I'm trying my best
## Conclusion
In this laboratory work I learned and implemented converter from NFA to DFA or from FA to Regular Grammar. 
I learned how to determine if an FA is deterministic or non-deterministic. I found out the steps to convert an NDFA to a DFA
## References
* Regular Expressions, Regular Grammar and Regular Languages: https://www.geeksforgeeks.org/regular-expressions-regular-grammar-and-regular-languages/?ref=lbp
* Deterministic finite automaton: https://en.wikipedia.org/wiki/Deterministic_finite_automaton
* Nondeterministic finite automaton: https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
                 
