from analysis.lexer import Lexer
from analysis.parser import Parser
from analysis.ast_visualize import visualize_ast

from utils import *

lexer = Lexer('(1 + 2) - 3 * 7 + 9 *(6 / 5) ')
parser = Parser(lexer)
ast = parser.parse()
visualize_ast(ast)
