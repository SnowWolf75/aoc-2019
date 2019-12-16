#!/usr/bin/env python3

import sys, os
import unittest
from lib.common import *


filename = "inputs/2019_12_16_input.txt"

class mylist(list):
  def list_str(self,digits = -1):
    s = ''
    if digits == -1:
      digits = self.__len__()
    for i in range(digits):
      s += str( self.__getitem__(i) )
    return s
  def list_sum(self,digits = -1):
    n = 0
    if digits == -1:
      digits = self.__len__()
    for c in range(digits):
      n += int(self.__getitem__(c))
    return n


class day16:
  def __init__(self):
    self.data = None
    self.base_pattern = [0,1,0,-1]
    self.len = 0
    self.verbose = False
    self.first_digits = 3
    self.phases = 1

  def load_data(self, data):
    self.data = mylit(data)
    self.len = len(self.data)

  def make_mults(self, offset=1):
    mults = []
    maxlen = self.len+1
    while len(mults) < maxlen:
      for item in self.base_pattern:
        mults.append( [item] * offset )
    
    mults.pop(0)
    return mults
  
  def zipper(self, ayy, bee):
    cee = []
    for x in range(ayy):
      try:
        dee = ayy[x]*bee[x]
      except:
        dee=0
      
      eee = int(str(dee)[-1])
      cee[x] = eee

  def make_str(self, num=8):
    return self.data.list_str(num)

  def run_phase(self):
    temp_array = mylist()
    for i in range(self.len):
      mults = self.make_mults(i+1)
      steps = mylist( map(lambda x,y:x*y,self.data,mults) )
      t = steps.list_sum(8)
      t2 = int(str(t)[-1])
      if self.verbose:
        print("{}: {} => {}".format(i, t, t2))
      temp_array[i] = t2

    return temp_array


  def run(phases=1, digits=5, verbose=False):
    self.verbose = verbose
    self.phases = phases
    self.first_digits = digits

    for p in range(self.phases):
      if self.verbose:
        print("Phase {} of {}\n------".format(p, self.phases))
      res = self.run_phase()
      if self.verbose:
        print("SS: {}".format( res.list_str(8) ))

    flat_str = self.make_str( self.first_digits )
    return flat_str

class day16part1(day16):
  def solve(self, args):
    pass

class day16part2(day16):
  def solve(self, args):
    pass


class examples(unittest.TestCase):
  def test_examples_part1(self):
    day16 = day16part1()
    day16.load_data( [int(s) for s in list('12345678') ] )
    res = day16.run(phases=1,digits=8,verbose=True)
    self.assetEqual('48226158', res)



  def test_examples_part2(self):
    day16 = day16part2()
    # self.assetTrue()

class solutions(unittest.TestCase):
  def test_part1(self):
    day16 = day16part1()

  def test_part2(self):
    day16 = day16part2()

def my_file(name):
  data = list(map(int, filemap(lambda x: x, name)[0]))
  return data

if __name__ == "__main__":

  

  #part1_data = my_file(filename)
  #d16 = day16part1()
  #d16.load_data( part1_data )
  #fft.run(phases=4,output=8,verbose=True)

   