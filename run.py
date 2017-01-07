#!/usr/bin/env python

# run.py
#
# Copyright(c) Exequiel Ceasar Navarrete <esnavarrete1@up.edu.ph>
# Licensed under MIT
# Version 0.0.0

import pprint
from compiler.tokenizer import Tokenizer
from compiler.parser import Parser
from compiler.transformer import Transformer
from compiler.code_generator import CodeGenerator

if __name__ == "__main__":
  # setup the pretty printer
  pp = pprint.PrettyPrinter(indent=2)

  tknizer = Tokenizer("(add 23 (subtract 4 2))")

  parser = Parser(tknizer.run())
  ast = parser.run()

  # print('Original AST:')
  # pp.pprint(ast)

  transformer = Transformer(ast)
  new_ast = transformer.run()

  # print('Transformed AST:')
  # pp.pprint(new_ast)

  code_generator = CodeGenerator(new_ast)
  print(code_generator.run())


