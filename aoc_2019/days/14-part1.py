#!/usr/bin/env python3

import sys, os
sys.path.append( os.path.dirname("../lib/") )

data = {}
with open(("../inputs/2019_12_14_input.txt")) as fh:
  for fline in fh.readlines():
    line = fline.strip()
    print("Line: {}".format(line))
    splits = line.split('=>')
    left = splits[0]
    right = splits[1]

    (amt, elem) = right.split(maxsplit=2)
    lefts = []
    print("left: {}\n\tright: {}".format(left,right))
    print("final: {}x{}".format(amt, elem))
    for op in left.split(","):
      (a,b) = op.strip().split(maxsplit=1)
      lefts.append({b:a})

    print("{}({}) from {}".format(elem, amt, lefts))
    data[ elem ] = {int(amt):lefts}
    #print("P:",parts)
    #loc = line.find('=>')
    #left = line[0:loc]
    #right = line[ loc+2 : ]

print(data)
