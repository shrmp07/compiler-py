# PyLisp: A Lisp Interpreter in Python

This project is an interpreter for a subset of the Lisp language, built from the ground up in Python. It began as a foundational four-stage compiler and was intentionally refactored into an AST-walking interpreter to explore the architectural trade-offs between transpilation and direct evaluation.

The primary goal of this project was not just to build a working interpreter, but to analyze the design decisions required to support core language features like lexical scoping and first-class functions, which are challenging to implement in a simple transpiler model.

---

## Features

* **Lexical Scoping**: Implements a robust environment model with parent pointers to correctly handle nested local scopes, a cornerstone of functional programming languages.
* **Core Lisp Semantics**: Supports special forms `(let)` for variable binding and `(if)` for conditional logic, which require non-standard evaluation rules.
* **Rich Data Types**: Handles integers, floats, booleans (`#t`, `#f`), and symbols.
* **Standard Library**: Provides a global environment pre-populated with essential arithmetic and comparison functions.
* **Interactive REPL**: Includes a Read-Eval-Print Loop for live experimentation and testing of Lisp code.

---

## Architecture and Design Decisions

The interpreter's architecture evolved significantly from its initial compiler design. The final version consists of three main components that directly evaluate code.

### 1. Parsing: From Tokens to AST

The parser transforms a token stream into an Abstract Syntax Tree (AST). A key design choice was to represent the AST as nested Python lists rather than dedicated node classes.

* **Rationale**: This approach maintains a close structural correspondence to Lisp's own "code-as-data" philosophy (homoiconicity). While less rigid than class-based ASTs, it provides a flexible foundation and simplifies the initial parsing logic for this project's scope.
* **Process**: A recursive descent parser reads the token stream. Special forms like `if` and `let` are parsed as standard lists, with their unique behavior handled later by the evaluator.

### 2. The Environment Model

The `Environment` class is the backbone of the interpreter, enabling lexical scoping.

* **Challenge**: Supporting nested `let` blocks requires a mechanism to shadow variables correctly. A simple dictionary is insufficient.
* **Solution**: Each `Environment` object contains a dictionary for local bindings and a reference to its parent (or "enclosing") environment. When looking up a variable, the interpreter checks the current scope and traverses up the chain of parent environments until it finds the variable or reaches the global scope. This elegantly models lexical scope.

### 3. The AST-Walking Evaluator

The `evaluate` function is the core of the interpreter. It traverses the AST and computes the final value.

* **Architectural Shift**: The project was deliberately pivoted from a transpiler (which generates Python code) to a direct evaluator. The transpiler approach proved cumbersome for implementing special forms like `if`, which requires selective evaluation of its branches—a behavior that doesn't map cleanly to standard Python function calls.
* **Implementation**: The evaluator recursively processes each node of the AST. It differentiates between:
    * **Literals** (numbers, booleans), which evaluate to themselves.
    * **Symbols**, which are looked up in the current environment.
    * **Special Forms** (`if`, `let`), which have custom evaluation rules that manipulate the environment or control the flow of evaluation.
    * **Function Calls**, where the arguments are evaluated first, and then the corresponding procedure is applied.

---

## Getting Started

### Prerequisites

* Python 3.x

### Usage

1.  **Save the code** to a file (e.g., `pylisp.py`).

2.  **Run the script** from your terminal. It will execute a series of example tests and then launch the interactive REPL.
    ```bash
    python pylisp.py
    ```

3.  **Interact with the REPL:**
    ```lisp
    > (let ((x 10)) (* x (+ x 5)))
      = 150
    > (if (> 5 10) "yes" "no")
      = no
    ```

---

## Future Work and Limitations



* **Testing Framework**: Implement a formal testing suite using a framework like `pytest` to create unit tests for the parser and integration tests for the evaluator.
* **Expanded Standard Library**: Add more built-in functions, such as list manipulation utilities (`car`, `cdr`, `cons`).
* **User-Defined Functions**: Implement the `lambda` and `defun` special forms to allow users to create their own first-class functions and closures.
* **Error Handling**: Improve error reporting with more descriptive messages and line number tracking.
