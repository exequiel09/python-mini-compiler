# __init__.py
#
# Copyright(c) Exequiel Ceasar Navarrete <exequiel.navarrete09gmail.com>
# Licensed under MIT
# Version 1.0.0-alpha2

from compiler.tokenizer import Tokenizer
from compiler.parser import Parser
from compiler.transformer import Transformer
from compiler.code_generator import CodeGenerator

class Compiler(object):
  """ Class that compiles given code to another language """

  def __init__(self, input_code):
    self.input_code = input_code

  def compile(self):
    tknizer = Tokenizer(self.input_code)
    parser = Parser(tknizer.run())
    transformer = Transformer(parser.run())
    code_generator = CodeGenerator(transformer.run())

    return code_generator.run()


