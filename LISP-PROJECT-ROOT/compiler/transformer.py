from traverse import traverse

def transformer(originalAST):
    pyAST = {
        'type': 'Program',
        'body': []
    }
    position = pyAST['body']

    def NumberLiteral(node, parent):
        nonlocal position
        position.append({
            'type': 'NumericLiteral',
            'value': node['value']
        })

    def CallExpression(node, parent):
        nonlocal position
        expression = {
            'type': 'CallExpression',
            'callee': {
                'type': 'Identifier',
                'name': node['name']
            },
            'arguments': []
        }

        prevPosition = position
        position = expression['arguments']

        if parent['type'] != 'CallExpression':
            expression = {
                'type': 'ExpressionStatement',
                'expression': expression
            }

        prevPosition.append(expression)

    traverse(originalAST, {
        'NumberLiteral': NumberLiteral,
        'CallExpression': CallExpression
    })

    return pyAST
