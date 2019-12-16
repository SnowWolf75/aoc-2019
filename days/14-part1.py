#!/usr/bin/env python3

import sys, os
sys.path.append( os.path.dirname("../lib/") )
from collections import Counter
from math import ceil
my_needs = Counter()

def load_equations(filename):
  equations = {}
  with open(filename) as fh:
    for fline in fh.readlines():
      line = fline.strip()
      (left,right) = line.split('=>')
      (amt, elem) = right.split(maxsplit=2)
      lefts = []
      #print("left: {}\n\tright: {}".format(left,right))
      #print("final: {}x{}".format(amt, elem))
      for op in left.split(","):
        (a,b) = op.strip().split(maxsplit=1)
        lefts.append({b:a})

      print("{}({}) from {}".format(elem, amt, lefts))
      equations[ elem ] = {int(amt):lefts}

  return equations

def find_needs(data):

  origin = data['FUEL']
  divisor = origin.keys()[0]

  component_list = origin[divisor]
  print("{} {} <= {}".format(1,'FUEL', component_list))
  for component in component_list:
    unit = component.keys()[0]
    elem = component[unit]
    my_needs[ elem ] += unit
    needs_recurse(divisor, unit, elem)

  
def needs_recurse(meen, units, elem):
  # load the units from the data-dict, figuring out the needs down the tree

  component_list = data[units]
  print("{} {} <= {}".format(units, elem, component_list))

  global my_needs

  pass

def min_mult(a,b):
  # a = amount needed
  # b = the multiple of units produced

  if a<=b:
    return b
  else:
    c = ceil(a/b)*b
    return c

if __name__ == '__main__':
  data = load_equations("../aoc_2019/inputs/2019_12_14_input.txt")
  print(data)
