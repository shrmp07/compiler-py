def traverse(ast, visitors):
    def walkNode(node, parent):
        method = visitors.get(node['type'])
        if method:
            method(node, parent)
        if node['type'] == 'Program':
            walkNodes(node['body'], node)
        elif node['type'] == 'CallExpression':
            walkNodes(node['params'], node)

    def walkNodes(nodes, parent):
        for node in nodes:
            walkNode(node, parent)

    walkNode(ast, None)