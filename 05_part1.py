#!/usr/bin/env python3

import sys, os
sys.path.append( os.path.dirname("../lib/") )
print("path:",sys.path)
try:
  from aoc_2019.lib import IntcodeV2
  print("a")
except:
  try:
    from .lib.IntcodeV2 import IntcodeV2
    print("b")
  except:
    execfile(r"C:\Users\Wolf\Documents\git\aoc-2019\aoc_2019\lib\IntcodeV2.py")
    print("c")

filename = "aoc_2019/inputs/2019_12_05_input.txt"
print("hello")
with open(filename) as fh:
  ic = IntcodeV2( fh.read() )

print("goodbye")
