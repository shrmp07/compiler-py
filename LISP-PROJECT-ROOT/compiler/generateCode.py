def generateCode(node):
    if node['type'] == 'NumericLiteral':
        return node['value']
    if node['type'] == 'Identifier':
        return node['name']
    if node['type'] == 'CallExpression':
        arguments = ', '.join([generateCode(arg) for arg in node['arguments']])
        return f"{generateCode(node['callee'])}({arguments})"
    if node['type'] == 'ExpressionStatement':
        return generateCode(node['expression'])
    if node['type'] == 'Program':
        return '\n'.join([generateCode(body) for body in node['body']])
