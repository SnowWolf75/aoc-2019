#!/usr/bin/env python3

import sys, os
sys.path.append( os.path.dirname("../lib/") )
try:
  from aoc_2019.lib.Intcode import Intcode
except:
  try:
    from Intcode import Intcode
  except:
    execfile(r"C:\Users\Wolf\Documents\git\aoc-2019\lib\Intcode.py")

class IntcodeV2(Intcode):
  def __init__(self, *args):
    print("Initializing super")
    super().__init__(args)
    #print(type(self.ops))
    #self.ops.update( {3:self.store, 4:self.harvest} )

  def get_op(self):
    t_op = self.data_array[ self.pos ]
    t_o = t_op % 100
    modes = []
    t_op //= 100
    while t_op > 0:
      modes.append(t_op % 10)
      t_op //= 10

    return t_o, modes

  def halt(self):
    return self.get_zero()

  def get_args(self, i=0, opcode=99):
    if i>0:
      q = self.pos+1
      r = self.pos+1+i
      return self.data_array[ q:r ]
    elif opcode!=99:
      op_args = {1:3,2:3,3:1,4:1}
      return self.get_args( i= op_args[opcode] )
    else:
      return []

  def store(self,loc):
    pass

  def harvest(self,loc):
    pass

  def run_op(self, opcode=99, modes=[0,0,0], args=[]):
    if opcode==99:
      return True

    

    return False


  def run_program(self, mods = {}):
    if mods:
      # Pull the modifiers, storing them into the array
      for k,v in mods.items():
        self.data_array[ k ] = v

    op = 0
    while op != 99:
      op_and_modes = self.get_op()
      op = op_and_modes[0]
      if op != 99:
        modes = op_and_modes[1]
        args = self.get_args(opcode=op)
        result = self.run_op(opcode=op, modes=modes, args=args)

    return self.get_zero if result else None