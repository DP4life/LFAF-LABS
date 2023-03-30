# Topic: Lexer & Scanner

### Course: Formal Languages & Finite Automata
### Author: Echim Mihail

## Objectives:
1. Understand what lexical analysis [1] is.
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.

## Implementation:
* I made a lexer for a version of a DSL for sound processing
* I implemented the lexer by defining the TokenType class as an Enum to distinguish between different kinds of tokens that may be in the input
```pyhton 
class TokenType(Enum):
    INTEGER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    EOF = 7
```
* I also defined the Token class 
```python
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {self.value})"

    def __repr__(self):
        return self.__str__()
```

* Then, in the Lexer class, I defined the possible token patterns and how to parse them
```python
def __init__(self, code):
        self.code = code
        self.token_patterns = [
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('LBRACE', r'\{'),
            ('RBRACE', r'\}'),
            ('COMMA', r','),
            ('ASSIGN', r'='),
            ('ADD', r'add\b'),
            ('SEMICOLON', r';'),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MULTIPLY', r'\*'),
            ('DIVIDE', r'/'),
            ('GREATER', r'>'),
            ('GREATER_EQUAL', r'>='),
            ('EQUAL', r'=='),
            ('LESS', r'<'),
            ('LESS_EQUAL', r'<='),
            ('NOT_EQUAL', r'!='),
            ('IF', r'if\b'),
            ('ELSE', r'else\b'),
            ('FOR', r'for\b'),
            ('WHILE', r'while\b'),
            ('IN', r'in\b'),
            ('RETURN', r'return\b'),
            ('BREAK', r'break\b'),
            ('CONTINUE', r'continue\b'),
            ('VAR', r'var\b'),
            ('FUNC', r'func\b'),
            ('ID', r'[a-zA-Z_]\w*'),
            ('NUMBER', r'\d+(\.\d+)?'),
            ('STRING', r'"[^"]*"'),
            ('WHITESPACE', r'\s+'),
            ('COMMENT', r'//.*'),
            ('INVALID', r'.')
        ]
```
* In the lexer file, I added a tokenize function that combines all of the above in order to seperate the input into tokens
```python
def tokenize(self, program):
        tokens = []
        for match in self.token_regex.finditer(program):
            type = match.lastgroup
            value = match.group()
            token = Token(type, value)
            if type != 'WHITESPACE' and type != 'COMMENT':
                tokens.append(token)
        return tokens
```
## Input

```
func process() {
    var x = 123;
    var y = "hello, world!";
    set_gain(x + 456);
    if (x > 100) {
        return y;
    } else {
        for i = 0, 10 {
            delay(i);
        }
        break;
    }
}
```

## Output

```
Tokens:
[Token(FUNC, func), Token(ID, process), Token(LPAREN, (), Token(RPAREN, )), Token(LBRACE, {), Token(VAR, var), Token(ID, x), Token(ASSIGN, =), Token(NUMBER, 123), Token(SEMICOLON, ;), Token(VAR, var), Token(ID, y), Token(ASSIGN, =), Token(STRING, "hello, world!"), Token(SEMICOLON, ;), Token(ID, set_gain), Token(LPAREN, (), Token(ID, x), Token(PLUS, +), Token(NUMBER, 456), Token(RPAREN, )), Token(SEMICOLON, ;), Token(IF, if), Token(LPAREN, (), Token(ID, x), Token(GREATER, >), Token(NUMBER, 100), Token(RPAREN, )), Token(LBRACE, {), Token(RETURN, return), Token(ID, y), Token(SEMICOLON, ;), Token(RBRACE, }), Token(ELSE, else), Token(LBRACE, {), Token(FOR, for), Token(ID, i), Token(ASSIGN, =), Token(NUMBER, 0), Token(COMMA, ,), Token(NUMBER, 10), Token(LBRACE, {), Token(ID, delay), Token(LPAREN, (), Token(ID, i), Token(RPAREN, )), Token(SEMICOLON, ;), Token(RBRACE, }), Token(BREAK, break), Token(SEMICOLON, ;), Token(RBRACE, }), Token(RBRACE, }), Token(TokenType.EOF, )]
```

## Conclusion
While workin on this laboratory work, I learned what a Lexer, Scanner, and Tokenizer are. I implemented a Lexer an got a deeper understanding of the inner workings of formal languages, especially programming languages that I use on a daily basis.

## References
[1] [A sample of a lexer implementation](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl01.html)

[2] [Lexical analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
 