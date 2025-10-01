#
# A Lisp Interpreter in Python
#
# This program interprets a subset of the Lisp language, including:
# - Nested function calls (e.g., `(add 1 2)`)
# - Local variable bindings with `let`
# - Conditional logic with `if`
# - Expanded data types: Numbers, Booleans
# - A basic standard library of functions (`+`, `-`, `*`, `/`, `>`, `<`, `=`)
#

import operator
import re


# 1. Environment: Manages Variables and Scope 
#    This is the heart of the interpreter, handling variable storage.

class Environment:
    """A dictionary-like object that holds variable bindings and scopes."""
    def __init__(self, parent=None):
        self.variables = {}
        self.parent = parent

    def define(self, name, value):
        """Define a variable in the current scope."""
        self.variables[name] = value

    def lookup(self, name):
        """Look up a variable's value, checking parent scopes if needed."""
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.lookup(name)
        else:
            raise NameError(f"'{name}' is not defined.")

# 2. Tokenizer: Breaks code into tokens 
def tokenize(code):
    """Splits the input string into a list of tokens."""
    code = code.replace("(", " ( ").replace(")", " ) ")
    return code.split()

# ==============================================================================
# 3. Parser: Creates the Abstract Syntax Tree (AST) 🌳
#    This version is smarter, creating a nested list structure that represents
#    the code's hierarchy. It also handles type conversion.
# ==============================================================================
def parse(tokens):
    """Parses a list of tokens into an AST (a nested list structure)."""
    if not tokens:
        raise SyntaxError("Unexpected end of input.")
    
    token = tokens.pop(0)
    
    if token == '(':
        ast = []
        while tokens[0] != ')':
            ast.append(parse(tokens))
        tokens.pop(0) # Pop off ')'
        return ast
    elif token == ')':
        raise SyntaxError("Unexpected ')'")
    else:
        return atom(token)

def atom(token):
    """Converts a token into its appropriate data type (int, float, bool, or symbol)."""
    if token == '#t':
        return True
    elif token == '#f':
        return False
    
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return str(token) # This is a symbol or string

# ==============================================================================
# 4. Global Environment: The Standard Library 📚
#    This sets up all the built-in functions and values.
# ==============================================================================
def create_global_env():
    """Creates the global environment with built-in functions."""
    env = Environment()
    env.define('+', operator.add)
    env.define('-', operator.sub)
    env.define('*', operator.mul)
    env.define('/', operator.truediv)
    env.define('>', operator.gt)
    env.define('<', operator.lt)
    env.define('=', operator.eq)
    env.define('abs', abs)
    env.define('#t', True)
    env.define('#f', False)
    return env

# 
# 5. Evaluator: Walks the AST to get the answer 
#    This is the main engine. It processes each part of the AST.
# 
def evaluate(ast, env):
    """Evaluates an AST node in a given environment."""
    
    # If the AST node is a symbol (string), look it up.
    if isinstance(ast, str):
        return env.lookup(ast)
    
    # If the AST node is a number, return it directly.
    if isinstance(ast, (int, float, bool)):
        return ast
        
    # If we have an empty list, it's an error.
    if not ast:
        raise SyntaxError("Empty expression '()' is not valid.")

    # This is an S-expression (a list). The first element determines what to do.
    keyword = ast[0]

    # --- Special Forms ---
    # These have unique evaluation rules and are not treated like normal functions.
    
    if keyword == 'if':
        # (if <test> <consequent> <alternative>)
        (_, test, consequent, alternative) = ast
        # Evaluate the test expression
        if evaluate(test, env):
            return evaluate(consequent, env)
        else:
            return evaluate(alternative, env)
            
    if keyword == 'let':
        # (let ((var1 val1) (var2 val2)...) <body>)
        (_, bindings, body) = ast
        # Create a new, local environment whose parent is the current one
        local_env = Environment(parent=env)
        for var, val_expr in bindings:
            # Evaluate the value in the *parent* environment
            value = evaluate(val_expr, env)
            # Define the variable in the *new local* environment
            local_env.define(var, value)
        # Evaluate the body of the `let` using the new local environment
        return evaluate(body, local_env)

    # --- Regular Function Call ---
    # If it's not a special form, it must be a function call.
    else:
        # Get the function object from the environment
        proc = evaluate(ast[0], env)
        # Evaluate all the arguments
        args = [evaluate(arg, env) for arg in ast[1:]]
        # Apply the function to the evaluated arguments
        return proc(*args)

# 6. Main Program Loop (REPL)
# 
if __name__ == "__main__":
    global_env = create_global_env()
    print("Welcome to the Lisp Interpreter! Type 'exit' to quit.")

    # --- EXAMPLES TO DEMONSTRATE FEATURES ---
    print("\n--- Running Examples ---")
    examples = [
        "(+ 2 (* 3 4))",
        "(let ((x 10) (y 20)) (+ x y))",
        "(if (> 10 5) 100 200)",
        "(let ((a 5)) (if (= a 5) (* a 10) 0))"
    ]
    for code in examples:
        try:
            result = evaluate(parse(tokenize(code)), global_env)
            print(f"> {code}\n  = {result}")
        except Exception as e:
            print(f"> {code}\n  Error: {e}")

    print("\n--- Interactive Mode ---")
    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == 'exit':
                break
            if user_input.strip() == "":
                continue
                
            tokens = tokenize(user_input)
            ast = parse(tokens)
            result = evaluate(ast, global_env)
            print(f"  = {result}")

        except (SyntaxError, NameError, TypeError, IndexError) as e:
            print(f"  Error: {e}")
        except Exception as e:
            print(f"  An unexpected error occurred: {e}")
