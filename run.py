#!/usr/bin/env python

# run.py
#
# Copyright(c) Exequiel Ceasar Navarrete <esnavarrete1@up.edu.ph>
# Licensed under MIT
# Version 0.0.0

from compiler.tokenizer import Tokenizer

if __name__ == "__main__":
  tknizer = Tokenizer("(add 23 (subtract 4 2))")
  print(tknizer.run())


