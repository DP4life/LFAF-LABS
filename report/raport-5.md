# Topic: Parser & Building an Abstract Syntax Tree

### Course: Formal Languages & Finite Automata
### Author: Vasile Drumea

----

## Overview
&ensp;&ensp;&ensp; The process of gathering syntactical meaning or doing a syntactical analysis over some text can also be called parsing. It usually results in a parse tree which can also contain semantic information that could be used in subsequent stages of compilation, for example.

&ensp;&ensp;&ensp; Similarly to a parse tree, in order to represent the structure of an input text one could create an Abstract Syntax Tree (AST). This is a data structure that is organized hierarchically in abstraction layers that represent the constructs or entities that form up the initial text. These can come in handy also in the analysis of programs or some processes involved in compilation.


## Objectives:
1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens. 
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.

## Implementation:
* I rewrote the language into a simpler one to avoid confusion for myself.
* I wrote a ast data structure that is a series of classes for classifying tokens. Those classes are `BinOp` for binary operation, `UnaryOp` for unary operation, and `Num` for number.
```python
class AST:
    pass

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __str__(self):
        return f'BinOp({self.left}, {self.op}, {self.right})'

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return f'Num({self.value})'

class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr

    def __str__(self):
        return f'UnaryOp({self.op}, {self.expr})'
```
* I wrote a parser to traverse the lexer and use the ast file to create nodes, connect them to each other as a tree-like data structure and build up the tree. As an example the expression function that creates a node for binary operations and in a loop adds all the terms for the left and the right side of the binary operation

```python
def expr(self):
        node = self.term()

        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node
```
* I then wrote a visualizer file for the ast. I traverses the ast and prints the nodes with the right indent to help see what the ast looks like
``` python
def visualize_ast(node, indent=''):
    if isinstance(node, BinOp):
        print(f'{indent}BinOp({node.op.value})')
        print(f'{indent}├─ Left:')
        visualize_ast(node.left, indent + '│   ')
        print(f'{indent}└─ Right:')
        visualize_ast(node.right, indent + '    ')
    elif isinstance(node, Num):
        print(f'{indent}Num({node.value})')
    elif isinstance(node, UnaryOp):
        print(f'{indent}UnaryOp({node.op.value})')
        print(f'{indent}└─ Expression:')
        visualize_ast(node.expr, indent + '    ')
```
* In main, the lexer tokenizes the input of `(1 + 2) - 3 * 7 + 9 *(6 / 5)`. Those tokens are then passed on to the parser. Then we initialize the `ast` by assigning the `parse` function to it. Lastly we visualize the `ast`
```python
lexer = Lexer('(1 + 2) - 3 * 7 + 9 *(6 / 5) ')
parser = Parser(lexer)
ast = parser.parse()
visualize_ast(ast)
```
* Output
```
BinOp(+)
├─ Left:
│   BinOp(-)
│   ├─ Left:
│   │   BinOp(+)
│   │   ├─ Left:
│   │   │   Num(1)
│   │   └─ Right:
│   │       Num(2)
│   └─ Right:
│       BinOp(*)
│       ├─ Left:
│       │   Num(3)
│       └─ Right:
│           Num(7)
└─ Right:
    BinOp(*)
    ├─ Left:
    │   Num(9)
    └─ Right:
        BinOp(/)
        ├─ Left:
        │   Num(6)
        └─ Right:
            Num(5)
```
# Conclusion
While working on this laboratory work, I familiarized myself with the concept of AST. I learned how to implement a parser that can build an AST out of a collection of tokens. I implemented the AST data structure and the Parser. This has strengthened my understanding of Formal Languages and how to implement them.