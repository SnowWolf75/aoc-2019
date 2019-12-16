#!/usr/bin/env python3

import sys, os
from lib.IntcodeV2 import IntcodeV2
from lib.common import *

filename = "inputs/2019_12_05_input.txt"
file_data = filemap(int, filename, ',')

print("hello")
ic = IntcodeV2( file_data )

print("goodbye")
