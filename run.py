#!/usr/bin/env python

# run.py
#
# Copyright(c) Exequiel Ceasar Navarrete <esnavarrete1@up.edu.ph>
# Licensed under MIT
# Version 0.0.0

from compiler import Compiler

if __name__ == "__main__":
  code = "(list 1 2 (quote foo))"

  compiler = Compiler(code)

  print("LISP input code: %s" % code)
  print("Generated Python Code: %s" % compiler.compile())


