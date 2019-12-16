#!/usr/bin/env python3
import re

def is_ramp(i):
  s = str(i)
  ts = s[0]
  for v in s[1:6]:
    if int(v) < int(ts):
      return False
    else:
      ts = v
  return True

def has_dupe(i):
  s = str(i)
  ts = s[0]
  for v in s[1:6]:
    if v == ts:
      return True
    else:
      ts = v
  return False

def one_double(i):
  s = str(i)
  groups = None
  groups = re.findall(r"((.)\2{1,})", s)
  if groups:
    #print("{} GG ".format(s), end='')
    for g in groups:
      gz = g[0]
      #print("{} ".format(gz), end='')
      if len(gz) == 2:
        print("+",end='')
        return True

  print("-",end='')
  return False

lo = 153517
hi = 630395
part1 = 0
part2 = 0

for x in range(lo, hi):
  if is_ramp(x) and has_dupe(x):
    part1 += 1
    if one_double(x):
      part2 += 1
  #if count > 35:
  #  break

print("\nPart1 count: {}\nPart2 count: {}".format(part1, part2))


