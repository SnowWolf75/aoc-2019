#!/usr/bin/env python3
import operator

class Intcode():
  def __init__(self, *args):
    self.origin = []
    self.pos = 0
    self.data_array = []
    self.ops = { 1: operator.add, 2: operator.mul }

    # Handle the *args, populating origin with an array of INTs
    for a in args:
      #print("a is {}".format(type(a)))
      if type(a) == type(''):
        a = a.split(",")

      self.origin += self.sanitize(a)

    self.reinit()

  def get_zero(self):
    return self.data_array[0]

  def reinit(self):
    self.pos = 0
    self.data_array = self.origin[:]

  def sanitize(self, my_arg):
    clean = []
    for item in my_arg:
      try:
        clean.append( int(item) )
      except:
        pass

    #print("Clean: {}".format(clean))
    return clean

  def four(self):
    fore = self.data_array[ self.pos : self.pos+4 ]
    #print("{}: {}".format(self.pos, fore))
    self.pos += 4
    return fore

  def haystack(self, lo=0, hi=99, target=337049):
    my_lo = min( lo, hi )
    my_hi = max( lo, hi )

    for v in range( my_lo, my_hi ):
      for n in range( my_lo, my_hi ):
        self.reinit()
        val = self.run_program( {1: v, 2: n} )

        if val == target:
          return [v,n]

    return None


  def run_program(self, mods = {}):
    if mods:
      # Pull the modifiers, storing them into the array
      for k,v in mods.items():
        self.data_array[ k ] = v

    op = 0
    while op != 99:
      (op, a1, a2, st) = self.four()
      if op == 99:
        break
      elif op in self.ops.keys():
        my_op = self.ops[ op ]
        v1 = self.data_array[ a1 ]
        v2 = self.data_array[ a2 ]
        val = my_op(v1, v2)
        self.data_array[ st ] = val
      else:
        print("Unknown op or error occurred.")
        break

    # Made it to the end!
    return self.get_zero()

