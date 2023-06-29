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

feel free to comment and raise any issues,
thank you
