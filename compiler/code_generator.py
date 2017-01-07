# code_generator.py
#
# Copyright(c) Exequiel Ceasar Navarrete <esnavarrete1@up.edu.ph>
# Licensed under MIT
# Version 1.0.0-alpha1

class CodeGenerator(object):
  """ Class that generates Python Code based on the transformer-generated AST """

  def __init__(self, ast):
    self.ast = ast

  def translate(self, node):
    if node['type'] == 'Program':
      result = map(self.translate, node['body'])
      result = r'\n'.join(result)

      return result

    if (node['type'] != 'ExpressionStatement' and
        node['type'] != 'CallExpression' and
        node['type'] != 'Identifier' and
        node['type'] != 'NumberLiteral' and
        node['type'] != 'StringLiteral'):

      raise ValueError("Unknown node type %s" % node['type'])

    if node['type'] == 'ExpressionStatement':
      return self.translate(node['expression'])

    if node['type'] == 'CallExpression':
      result = map(self.translate, node['arguments'])
      result = ', '.join(result)

      return "%s(%s)" % (self.translate(node['callee']), result)

    if node['type'] == 'Identifier':
      return node['name']

    if node['type'] == 'NumberLiteral':
      return node['value']

    if node['type'] == 'StringLiteral':
      return '"'+ node['value'] + '"'

  def run(self):
    return self.translate(self.ast)


