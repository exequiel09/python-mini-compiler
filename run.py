#!/usr/bin/env python

# run.py
#
# Copyright(c) Exequiel Ceasar Navarrete <esnavarrete1@up.edu.ph>
# Licensed under MIT
# Version 0.0.0

import pprint
from compiler.tokenizer import Tokenizer
from compiler.parser import Parser

if __name__ == "__main__":
  tknizer = Tokenizer("(add 23 (subtract 4 2))")
  parser = Parser(tknizer.run())

  # setup the pretty printer
  pp = pprint.PrettyPrinter(indent=2)

  # print the ast
  pp.pprint(parser.run())


