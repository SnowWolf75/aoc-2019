#!/usr/bin/env python3

import sys, os
sys.path.append( os.path.dirname("../lib/") )
try:
  from IntcodeV2 import IntcodeV2
except:
  from aoc_2019.lib.IntcodeV2 import IntcodeV2

filename = "../inputs/2019_12_0_input.txt"
print("hello")
with open(filename) as fh:
  ic = IntcodeV2( fh.read() )
  print("goodbye")
