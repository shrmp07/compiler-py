
# PyLisp: A Lisp Toolchain in Python

**A dual-engine implementation of a Lisp-like language, featuring both a Direct Interpreter and a Source-to-Source Transpiler.**

PyLisp was engineered to explore the architectural trade-offs between direct evaluation (preserving homoiconicity) and static compilation (structured transformation).

---

##  Repository Navigation Note



> Please navigate to the **`/LISP-PROJECT-ROOT`** directory to view the **current code**.

---

##  Project Architecture

Inside `/LISP-PROJECT-ROOT`, the system is divided into two distinct implementations to separate runtime logic from compilation logic.

| Directory | Description | AST Strategy |
| :--- | :--- | :--- |
| **/interpreter** | A runtime evaluator utilizing a **Direct Interpreter**. | Uses **Nested Python Lists** to maintain Lisp's "code-as-data" philosophy. |
| **/compiler** | A source-to-source **Transpiler** pipeline. | Uses **Dictionaries/Objects** to facilitate strict type checking and target code generation. |

---

## Engine 1: The Interpreter (Runtime Evaluation)

The interpreter is built on a custom **Environment Model** to support lexical scoping and closures. It prioritizes the dynamic nature of Lisp.

### Design Decisions

#### 1. AST Representation (Homoiconicity)
* **Decision:** Represent the AST as nested Python lists (e.g., `['add', 1, 2]`) rather than dedicated node classes.
* **Rationale:** This maintains a close structural correspondence to Lisp's own philosophy. While less rigid than class-based ASTs, it simplifies parsing and allows the interpreter to treat code sequences as manipulatable data structures.

#### 2. The Environment Model (Lexical Scoping)
* **Challenge:** Supporting nested `let` blocks and closures requires a mechanism to shadow variables correctly without polluting the global namespace.
* **Solution:** Each `Environment` object contains a dictionary for local bindings and a reference to its **parent environment**. Variable lookup recursively traverses this chain, elegantly modeling lexical scope.

### Features
* **Core Semantics:** Special forms for `let` (binding) and `if` (conditional flow).
* **First-Class Functions:** Supports `lambda` and `defun` for user-defined closures.
* **REPL:** An interactive Read-Eval-Print Loop for immediate feedback.

---

##  Engine 2: The Transpiler (Compilation Pipeline)

The transpiler decouples the source language from the execution model by treating Lisp as a frontend for Python. It transforms Lisp s-expressions into valid Python source code.

### Pipeline Architecture

1.  **Lexical Analysis:** A Regex-based tokenizer that handles parentheses and symbols robustly.
2.  **Syntactic Analysis:** A recursive descent parser generating a concrete, dictionary-based AST.
3.  **Semantic Analysis (Transformer):** Uses the **Visitor Pattern** to map functional Lisp nodes (e.g., `CallExpression`) to imperative Python nodes.
4.  **Code Generation:** Emits syntactically valid Python source code ready for execution by the host Python interpreter.

---

##  Getting Started

### Prerequisites
* Python 3.x

### Installation
Clone the repository and navigate to the **modern project root**:

```bash
git clone [https://github.com/shrmp07/compiler-py.git](https://github.com/shrmp07/compiler-py.git)
cd compiler-py/LISP-PROJECT-ROOT
````

### Usage

#### 1\. Running the Interpreter

The interpreter parses Lisp code into lists and evaluates them against the global environment.

```python
# Ensure you are inside the LISP-PROJECT-ROOT directory
from interpreter.core import evaluate, global_env, parse, tokenize

# Define a factorial function recursively
code = "(defun fact (n) (if (< n 2) 1 (* n (fact (- n 1)))))"

# Tokenize -> Parse -> Evaluate
ast = parse(tokenize(code))
evaluate(ast, global_env)

# Output: Function 'fact' defined.
```

#### 2\. Running the Transpiler

The transpiler takes Lisp syntax and outputs valid Python string code.

```python
# Ensure you are inside the LISP-PROJECT-ROOT directory
from compiler.compiler import compiler

lisp_code = "(add 2 (sub 4 3))"

# Compile to Python source
python_code = compiler(lisp_code)

print(python_code)
# Output: add(2, sub(4, 3))
```

-----

##  Testing

The project includes a comprehensive test suite validating all stages of both pipelines.

```bash
# Run tests from the LISP-PROJECT-ROOT directory
python -m unittest discover tests
```

