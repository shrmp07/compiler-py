def parser(tokens):
    current = 0

    def walk():
        nonlocal current
        token = tokens[current]

        if token['type'] == 'number':
            current += 1
            return {
                'type': 'NumberLiteral',
                'value': token['value']
            }

        if token['type'] == 'paren' and token['value'] == '(':
            current += 1
            token = tokens[current]

            expression = {
                'type': 'CallExpression',
                'name': token['value'],
                'params': []
            }

            current += 1
            token = tokens[current]

            while token['value'] != ')':
                expression['params'].append(walk())
                token = tokens[current]

            current += 1
            return expression

        raise TypeError(f"Unknown token: '{token}'")

    ast = {
        'type': 'Program',
        'body': [walk()]
    }

    return ast

