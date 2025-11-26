
# here, this compiles a Lisp statement into Javascript. 

# A statement like this in python...add(2, sub(4, 3))
# (add 2 (sub 4 3))...will look like this in Lisp. The parentheses moved outside, and the commas were dropped.

from compiler import compiler

input_code = '(add 2 (sub 4 3))'
output = compiler(input_code)
print(output)