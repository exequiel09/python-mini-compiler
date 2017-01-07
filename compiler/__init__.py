# __init__.py
#
# Copyright(c) Exequiel Ceasar Navarrete <exequiel.navarrete09gmail.com>
# Licensed under MIT
# Version 0.0.0

from compiler.tokenizer import Tokenizer
from compiler.parser import Parser
from compiler.transformer import Transformer
from compiler.code_generator import CodeGenerator

class Compiler(object):
  """ Class that compiles given code to another language """

  def __init__(self, input_code):
    self.input_code = input_code

  def compile(self):
    tknizer = Tokenizer("(add 23 (subtract 4 2))")
    parser = Parser(tknizer.run())
    transformer = Transformer(parser.run())
    code_generator = CodeGenerator(transformer.run())

    return code_generator.run()


