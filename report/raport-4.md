# Topic: Chomsky Normal Form

### Course: Formal Languages & Finite Automata
### Author: Echim Mihail

----

## Overview
&ensp;&ensp;&ensp; 


## Objectives:
1. Learn about Chomsky Normal Form (CNF) [1].
2. Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
    1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    2. The implemented functionality needs executed and tested.
    3. A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.
    4. Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.

## Implementation:

* I made a function in the Grammar class to transform my grammar variant into Chomsky Normal Form. I made a lot of functions for every step of this process. Also, the last step was not needed with my variant, so I omitted it.
```python
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
```
* Changing the starter nonterminal variable. I only change it if it appears on the right hand side of any production. Otherwise, I leave it be
```python
def new_starter(self):
    for i in self.rules:
        for j in self.rules[i]:
            for k in j: 
                if self.starter_symbol == k:
                    self.rules['0'] = self.starter_symbol
                    self.starter_symbol = '0'
                    return
```
 
* Removing the unreachable nonterminal units from the Grammar. I make a sort of graph out of the grammar and using BFS to see which nonterminals are reachable from the starting variable. Those that are not accessible, are deleted.
```python
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
```

* Removing nullable (epsilon) productions. I add every nonterminal that leads to an epsilon to a list of nonterminals. Then, I add the versions of the nullable productions in which they are equal to an empty string.
```python
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
```
* Removing the unit productions (productions of type A -> B). SThese productions are solved by deleting constructing a separate dictionary with the unit productions and removing them from the main rules. Then, iterating through the new temporary dictionary, I add the productions of B to A (in the context of A - > B, so if B -> x1, x2... then A -> x1, x2... etc)
```python
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
```

* Removing the productions of type (A -> aB) which mix terminals and nonterminals in such a way. In order to remove these, I added separate nonterminals for every terminal symbol and replaced them in productions in the following way: A -> aB, X -> a, therefore A -> XB. Then I remove the original version of these productions.
```python
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
```
* Removing right hand sides which consist of more than two nonterminals (A -> ABC). In my grammar it does not occur, so I omitted this step.
* I did not implement unit test.
* My function only works on my Grammar (or maybe some other grammar too but the range is pretty slim)
## Output
```
S  ->  A
A  ->  aX
A  ->  bX
X  ->
X  ->  BX
X  ->  b
B  ->  AD
D  ->  aD
D  ->  a
C  ->  Ca
========================================================
If the starting string S is on the right hand side of any production, adds a new starting nonterminal
S  ->  A
A  ->  aX
A  ->  bX
X  ->
X  ->  BX
X  ->  b
B  ->  AD
D  ->  aD
D  ->  a
========================================================
Removed the epsilon producitons
S  ->  A
A  ->  aX
A  ->  bX
A  ->  a
A  ->  b
X  ->  BX
X  ->  b
X  ->  B
B  ->  AD
D  ->  aD
D  ->  a
========================================================
Removed the unit productions
S  ->  aX
S  ->  bX
S  ->  a
S  ->  b
A  ->  aX
A  ->  bX
A  ->  a
A  ->  b
X  ->  BX
X  ->  b
X  ->  AD
B  ->  AD
D  ->  aD
D  ->  a
========================================================
Removed productions of type A -> aB
S  ->  a
S  ->  b
S  ->  IX
S  ->  KX
A  ->  a
A  ->  b
A  ->  IX
A  ->  KX
X  ->  BX
X  ->  b
X  ->  AD
B  ->  AD
D  ->  a
D  ->  ID
I  ->  a
K  ->  b

C:\Users\micha\OneDrive\Desktop\University\Semestrul IV\LFAF\Labs\LFAF-LABS\src>python main.py
S  ->  A
A  ->  aX
A  ->  bX
X  ->
X  ->  BX
X  ->  b
B  ->  AD
D  ->  aD
D  ->  a
C  ->  Ca
========================================================
If the starting string S is on the right hand side of any production, adds a new starting nonterminal
S  ->  A
A  ->  aX
A  ->  bX
X  ->
X  ->  BX
X  ->  b
B  ->  AD
D  ->  aD
D  ->  a
C  ->  Ca
========================================================
Removed the unreachable nonterminals
S  ->  A
A  ->  aX
A  ->  bX
X  ->
X  ->  BX
X  ->  b
B  ->  AD
D  ->  aD
D  ->  a
========================================================
Removed the epsilon producitons
S  ->  A
A  ->  aX
A  ->  bX
A  ->  a
A  ->  b
X  ->  BX
X  ->  b
X  ->  B
B  ->  AD
D  ->  aD
D  ->  a
========================================================
Removed the unit productions
S  ->  aX
S  ->  bX
S  ->  a
S  ->  b
A  ->  aX
A  ->  bX
A  ->  a
A  ->  b
X  ->  BX
X  ->  b
X  ->  AD
B  ->  AD
D  ->  aD
D  ->  a
========================================================
Removed productions of type A -> aB
S  ->  a
S  ->  b
S  ->  YX
S  ->  GX
A  ->  a
A  ->  b
A  ->  YX
A  ->  GX
X  ->  BX
X  ->  b
X  ->  AD
B  ->  AD
D  ->  a
D  ->  YD
G  ->  b
Y  ->  a
```

## Conclusion
While working on this laboratory work, I learned about the Noam Chomsky's normal form. I learned how to make a Context Free Grammar a Chomsky Normal Form. I implemented the transition in python. 