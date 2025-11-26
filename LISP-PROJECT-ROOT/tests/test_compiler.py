import unittest
from compiler.compiler import compiler
from interpreter.core import evaluate, global_env
from interpreter.core import parse as parse_interp
from interpreter.core import tokenize as tokenize_interp

class TestLispToolchain(unittest.TestCase):

    def test_transpiler_simple(self):
        """Test if the compiler translates Lisp to Python correctly"""
        input_code = '(add 2 (sub 4 3))'
        # Note: Ensure your compiler returns string, not prints it
        output = compiler(input_code) 
        self.assertIn('add(2, sub(4, 3))', output)

    def test_interpreter_math(self):
        """Test if the interpreter calculates math correctly"""
        code = "(+ 1 (* 2 3))"
        ast = parse_interp(tokenize_interp(code))
        result = evaluate(ast, global_env)
        self.assertEqual(result, 7)

    def test_interpreter_lambda(self):
        """Test if the interpreter handles lambda functions"""
        code = "((lambda (x) (* x x)) 5)"
        ast = parse_interp(tokenize_interp(code))
        result = evaluate(ast, global_env)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()