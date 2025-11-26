# PyLisp: A Lisp Toolchain in Python

**A dual-engine implementation of a Lisp-like language, featuring both a Direct Interpreter and a Source-to-Source Transpiler.**

PyLisp was engineered to explore the architectural trade-offs between direct evaluation (preserving homoiconicity) and static compilation (structured transformation).

---

## 📂 Project Architecture

The repository contains two distinct implementations of the language, separating runtime logic from compilation logic.

| Directory | Description | AST Strategy |
| :--- | :--- | :--- |
| **/interpreter** | A runtime evaluator utilizing a **Direct Interpreter**. | Uses **Nested Python Lists** to maintain Lisp's "code-as-data" philosophy. |
| **/compiler** | A source-to-source **Transpiler** pipeline. | Uses **Dictionaries/Objects** to facilitate strict type checking and target code generation. |

---

## 🧠 Engine 1: The Interpreter (Runtime Evaluation)

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

## ⚙️ Engine 2: The Transpiler (Compilation Pipeline)

The transpiler decouples the source language from the execution model by treating Lisp as a frontend for Python. It transforms Lisp s-expressions into valid Python source code.

### Pipeline Architecture



1.  **Lexical Analysis:** A Regex-based tokenizer that handles parentheses and symbols robustly.
2.  **Syntactic Analysis:** A recursive descent parser generating a concrete, dictionary-based AST.
3.  **Semantic Analysis (Transformer):** Uses the **Visitor Pattern** to map functional Lisp nodes (e.g., `CallExpression`) to imperative Python nodes.
4.  **Code Generation:** Emits syntactically valid Python source code ready for execution by the host Python interpreter.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x

### Installation
Clone the repository:
```bash
git clone [https://github.com/yourusername/pylisp.git](https://github.com/yourusername/pylisp.git)
cd pylisp
