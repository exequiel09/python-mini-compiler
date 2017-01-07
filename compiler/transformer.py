# transformer.py
#
# Copyright(c) Exequiel Ceasar Navarrete <esnavarrete1@up.edu.ph>
# Licensed under MIT
# Version 0.0.0

class Transformer(object):
  """ Transforms AST into a more verbose AST """

  def __init__(self, ast):
    self.new_ast = {
      'type': 'Program',
      'body': []
    }

    self.ast = ast

  def run(self):
    self.ast['_context'] = self.new_ast['body']

    traverser = Traverser(self.ast)
    traverser.run()

    return self.new_ast

class Traverser(object):
  """ Class that iterates all elements inside the Parser-generated AST """

  def __init__(self, ast):
    self.ast = ast

  def traverse_array(self, array: list, parent):
    counter = 0

    while counter < len(array):
      self.traverse_node(array[counter], parent)
      counter += 1

  def traverse_node(self, node, parent):
    # call any of ths static method of the Visitor class if present. If not, just pass through
    try:
      getattr(Visitor, node['type'].lower())(node, parent)
    except AttributeError:
      pass

    # freak out here
    if node['type'] != 'Program' and node['type'] != 'CallExpression' and node['type'] != 'NumberLiteral':
      raise ValueError("Unknown node type %s" % node['type'])

    if node['type'] == 'Program':
      self.traverse_array(node['body'], node)

    if node['type'] == 'CallExpression':
      self.traverse_array(node['params'], node)

  def run(self):
    self.traverse_node(self.ast, None)

class Visitor(object):
  """ Class that defines how each AST node is transformed """

  @staticmethod
  def callexpression(node, parent):
    expression = {
      'type': 'CallExpression',
      'callee': {
        'type': 'Identifier',
        'name': node['name']
      },
      'arguments': []
    }

    node['_context'] = expression['arguments']

    if parent['type'] != 'CallExpression':
      expression = {
        'type': 'ExpressionStatement',
        'expression': expression
      }

    parent['_context'].append(expression)

  @staticmethod
  def numberliteral(node, parent):
    parent['_context'].append({
      'type': 'NumberLiteral',
      'value': node['value']
    })


