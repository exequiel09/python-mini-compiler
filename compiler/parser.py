# parser.py
#
# Copyright(c) Exequiel Ceasar Navarrete <esnavarrete1@up.edu.ph>
# Licensed under MIT
# Version 1.0.0-alpha1

class Parser(object):
  """ Class that generates ASTs for the given set of tokens """

  def __init__(self, tokens):
    self.ast = {
      'type': 'Program',
      'body': []
    }

    self.current = 0
    self.tokens = tokens

  def get_current_token(self):
    return self.tokens[self.current]

  def get_next_token(self):
    self.current += 1

    return self.get_current_token()

  def walk(self):
    token = self.tokens[self.current]

    # if the token type is a number, mark it as a NumberLiteral
    if token['type'] == 'number':
      self.current += 1

      return {
        'type': 'NumberLiteral',
        'value': token['value']
      }

    # if the token type is a string, mark it as a StringLiteral
    if token['type'] == 'name':
      self.current += 1

      return {
        'type': 'StringLiteral',
        'value': token['value']
      }

    # mark the text after the open parenthesis as a 'CallExpression'
    if token['type'] == 'paren' and token['value'] == '(':
      token = self.get_next_token()

      # assemble the 'CallExpression' node
      node = {
        'type': 'CallExpression',
        'name': token['value'],
        'params': []
      }

      token = self.get_next_token()

      # recurse until all parameters are resolved and identified
      while token['type'] != 'paren' or token['value'] != ')':
        node['params'].append(self.walk())

        token = self.get_current_token()

      self.current += 1

      return node

    raise ValueError('Unknown token')

  def run(self):
    while self.current < len(self.tokens):
      self.ast['body'].append(self.walk())

    return self.ast


