# compiler-py
the tiny compiler but in python


### Phase 1: Lexical Analysis (Tokenizer)
The first phase is called Lexical Analysis, which involves breaking the input code into smaller units called tokens. The `tokenizer.py` module handles this phase by defining a `tokenizer` function. It uses regular expressions to identify and extract different types of tokens, such as parentheses, letters, whitespace, and numbers.

### Phase 2: Syntactic Analysis (Parser)
The second phase is Syntactic Analysis, where the tokens produced in the previous phase are used to build an Abstract Syntax Tree (AST). The `parser_1.py` module implements this phase with the `parser` function. It recursively traverses the token stream and constructs an AST by recognizing different language constructs like numbers and function calls.

### Phase 3: Transformation (Transformer)
The third phase is Transformation, where the original AST is converted into a new AST that represents the desired target language. The `transformer.py` module handles this phase. It defines a `transformer` function that takes the original AST and generates a new AST suitable for Python code generation.

### Phase 4: Code Generation
The fourth and final phase is Code Generation, where the transformed AST is converted into actual code in the target language. The `generateCode.py` module implements this phase. It defines a `generateCode` function that recursively traverses the transformed AST and generates Python code based on the node types encountered.

### Putting It All Together (index.py)
The `index.py` file showcases how to use the different modules to compile input code. It imports the `compiler` function from the `compiler.py` module. This function orchestrates the entire compilation process by invoking the tokenizer, parser, transformer, and code generation steps. Finally, it prints the generated Python code to the console.


# Lisp Interpreter in Python - new ver 01

This project is a simple interpreter for a subset of the Lisp language, written in Python. It has evolved from a basic compiler to a full interpreter capable of evaluating expressions directly.

The program can handle nested function calls, local variable bindings, and conditional logic, made for understanding the core mechanics of a programming language.

---

## Features

* **Classic Interpreter Pipeline**: Implements a Tokenizer, Parser, and Evaluator.
* **Variable Scope**: Supports local variable bindings using the `let` special form.
* **Control Flow**: Includes conditional evaluation with the `if` special form.
* **Data Types**: Handles integers, floats, booleans (`#t`, `#f`), and symbols.
* **Standard Library**: Comes with a pre-configured global environment that includes basic arithmetic (`+`, `-`, `*`, `/`) and comparison (`>`, `<`, `=`) operators.
* **Interactive REPL**: Features a Read-Eval-Print Loop for running Lisp code interactively.

---

## Architecture

The interpreter is built around a few key components:

1.  **Tokenizer**: The `tokenize` function takes the raw Lisp code as a string and breaks it down into a list of tokens.

2.  **Parser**: The `parse` function converts the flat list of tokens into a hierarchical Abstract Syntax Tree (AST). The AST is represented as nested Python lists.

3.  **Environment**: The `Environment` class is crucial for managing state. It holds variable bindings and handles lexical scope by linking to a parent environment.

4.  **Evaluator**: The `evaluate` function is the core of the interpreter. It recursively walks the AST, looks up variables in the environment, evaluates special forms like `if` and `let`, and executes function calls.

---

## Getting Started

Follow these instructions to run the interpreter on your local machine.

### Prerequisites

* Python 3.x

### Usage

1.  **Clone the repository (if applicable) or save the code** to a file named `interpreter.py`.

2.  **Run the script:**
    Executing the file will automatically run a set of built-in examples and then start an interactive session.
    ```bash
    python interpreter.py
    ```

3.  **Use the Interactive REPL:**
    After the examples run, you'll see a `>` prompt. You can type Lisp expressions here and press Enter to see the result.
    ```lisp
    > (+ 10 20)
      = 30
    > (let ((x 5)) (* x x))
      = 25
    > (if (< 5 10) 1 0)
      = 1
    > exit
    ```

---



feel free to comment and raise any issues,
thank you
