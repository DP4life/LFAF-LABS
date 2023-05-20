from analysis.ast import BinOp, Num, UnaryOp
from analysis.lexer import Lexer
from analysis.parser import Parser

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


