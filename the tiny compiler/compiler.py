from tokenizer import tokenizer
from parser_1 import parser
from transformer import transformer
from generateCode import generateCode
def compiler(input):
    # 1. Lexical Analysis -
    #    Breaks the input code (string) into the basic syntax
    #    of the language (array of objects)
    tokens = tokenizer(input)
    
    # 2. Syntactic Analysis -
    #    Transforms the tokens (array of objects) into an
    #    AST (tree of objects) which represents our program
    lispAST = parser(tokens)
    
    # 3. Transformation - Transforms our original Lisp AST into
    #                     our target Python AST
    pyAST = transformer(lispAST)
    # 4. Code Generation - Transforms our target AST (object of objects)
    #                     into actual code (string)
    #
    pyCode = generateCode(pyAST)
    
    
    return pyCode


