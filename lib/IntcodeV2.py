#!/usr/bin/env python3
from Intcode import Intcode

class IntcodeV2(Intcode):
  def __init__(self, *args):
    print("Initializing super")
    super().__init__(args)

