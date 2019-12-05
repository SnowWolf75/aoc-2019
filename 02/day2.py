#!/usr/bin/env python3

import sys, os
sys.path.append( os.path.dirname("../lib/") )

from Intcode import Intcode

with open("intcode.txt") as fh:
  ic = Intcode( fh.read() )

unit_test = ic.run_program()
print("Unit test results: {}".format( unit_test ))

ic.reinit()
twelve_two = ic.run_program({1:12, 2:2})
print("1202 Program alarm return: {}".format(twelve_two))

ic.reinit()
test_eleven = ic.run_program({1:1, 2:1})
print("Test 1:1 = {}".format(test_eleven))

needle = None
needle = ic.haystack(lo=0, hi=99, target=19690720)
if needle:
  word = (needle[0] * 100) + needle[1]
  print("Word: {}".format(word))
else:
  print("Unable to find target. :(")