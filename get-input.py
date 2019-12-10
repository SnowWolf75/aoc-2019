#!/usr/bin/env python3
import argparse
import subprocess
from datetime import datetime
from pytz import timezone
import pytz

utc_dt = datetime.utcnow().replace(tzinfo=pytz.utc)
eastern = timezone('US/Eastern')
east_coast = utc_dt.astimezone(eastern)
cur_day = east_coast.day
cur_year = east_coast.year
print("Current UTC:",utc_dt)
print("Current datetime:",east_coast)

parser = argparse.ArgumentParser(description='Read Input for Advent of Code')
parser.add_argument('--day', type=int, default=cur_day)
parser.add_argument('--year', type=int, default=cur_year)
args = parser.parse_args()

cmd = 'curl https://adventofcode.com/{}/day/{}/input --cookie "session=53616c7465645f5f929b0f8abf13f82ed097688a169ddc8ffacbc8e9aef59bba3f8d4186d54568eb41b354fef3143ebc"'.format(
    args.year, args.day)
output = subprocess.check_output(cmd, shell=True)
print(output,)

outfile = "aoc_2019/inputs/{0:04d}_12_{1:02d}_input.txt".format( args.year, args.day )
with open(outfile, "w") as fh:
    fh.write(str(output))

# https://adventofcode.com/2019/day/8/input
