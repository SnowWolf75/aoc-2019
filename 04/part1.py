#!env python3

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

lo = 172851
hi = 675869
count = 0

for x in range(lo, hi):
  if is_ramp(x) and has_dupe(x):
    count += 1
    #print("{} ".format(x), end='')

print("\nCount: {}".format(count))


