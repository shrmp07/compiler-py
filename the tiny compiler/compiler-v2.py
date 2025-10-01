#
# A Lisp Interpreter in Python with User-Defined Functions
#
# This program interprets a subset of the Lisp language, including:
# - User-defined functions with `lambda` and `defun`
# - Closures (lexical scoping for functions)
# - Recursion
# - Local variable bindings with `let`
# - Conditional logic with `if`
#

import operator
import re

# 1. Environment: Manages Variables and Scope

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


# 2. Function Class: Represents user-defined functions (Closures)
class Function:
    """A class to represent a user-defined function (a closure)."""
    def __init__(self, params, body, env):
        self.params = params
        self.body = body
        self.env = env  # The environment where the function was created

    def __call__(self, *args):
        # When called, create a new environment for the function's scope
        local_env = Environment(parent=self.env)
        # Bind the arguments to the function's parameters
        for i, param in enumerate(self.params):
            local_env.define(param, args[i])
        # Evaluate the function's body in this new environment
        return evaluate(self.body, local_env)

# 3. Tokenizer and Parser
def tokenize(code):
    """Splits the input string into a list of tokens."""
    code = code.replace("(", " ( ").replace(")", " ) ")
    return code.split()

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
    """Converts a token into its appropriate data type."""
    if token == '#t': return True
    if token == '#f': return False
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError: return str(token)

# 4. Global Environment: The Standard Library
def create_global_env():
    """Creates the global environment with built-in functions."""
    env = Environment()
    built_ins = {
        '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv,
        '>': operator.gt, '<': operator.lt, '=': operator.eq, 'abs': abs,
        '#t': True, '#f': False,
    }
    for name, func in built_ins.items():
        env.define(name, func)
    return env

# 5. Evaluator: Walks the AST to get the answer
def evaluate(ast, env):
    """Evaluates an AST node in a given environment."""
    
    if isinstance(ast, str):      # Symbol lookup
        return env.lookup(ast)
    if isinstance(ast, (int, float, bool)): # Literal value
        return ast
        
    if not ast:
        raise SyntaxError("Empty expression '()' is not valid.")

    keyword = ast[0]

    # --- Special Forms ---
    if keyword == 'if':
        (_, test, consequent, alternative) = ast
        if evaluate(test, env):
            return evaluate(consequent, env)
        else:
            return evaluate(alternative, env)
            
    if keyword == 'let':
        (_, bindings, body) = ast
        local_env = Environment(parent=env)
        for var, val_expr in bindings:
            value = evaluate(val_expr, env)
            local_env.define(var, value)
        return evaluate(body, local_env)

    if keyword == 'lambda':
        # (lambda (params...) <body>)
        (_, params, body) = ast
        # Create a closure: a function + the environment it was created in
        return Function(params, body, env)

    if keyword == 'defun':
        # (defun name (params...) <body>)
        (_, name, params, body) = ast
        # Create a function and define it in the current environment
        function = Function(params, body, env)
        env.define(name, function)
        return f"Function '{name}' defined."

    # --- Regular Function Call ---
    else:
        proc = evaluate(ast[0], env)
        args = [evaluate(arg, env) for arg in ast[1:]]
        if not callable(proc):
            raise TypeError(f"'{proc}' is not a function.")
        return proc(*args)

# 6. Main Program Loop (REPL)
if __name__ == "__main__":
    global_env = create_global_env()
    print("Welcome to the Enhanced Lisp Interpreter! Type 'exit' to quit.")

    # --- EXAMPLES TO DEMONSTRATE FEATURES ---
    print("\n--- Running Examples ---")
    examples = [
        "(defun factorial (n) (if (< n 2) 1 (* n (factorial (- n 1)))))",
        "(factorial 5)",
        "(defun fib (n) (if (< n 2) n (+ (fib (- n 1)) (fib (- n 2)))))",
        "(fib 7)",
        "((lambda (x) (* x x)) 10)"
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
            
            result = evaluate(parse(tokenize(user_input)), global_env)
            print(f"  = {result}")
        except Exception as e:
            print(f"  Error: {e}")
