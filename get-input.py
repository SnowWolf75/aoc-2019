#!/usr/bin/env python3
import argparse
import subprocess
import requests
from datetime import datetime

cur_day = datetime.now().day
cur_year = datetime.now().year

parser = argparse.ArgumentParser(description='Read Input for Advent of Code')
parser.add_argument('--day', type=int, default=cur_day)
parser.add_argument('--year', type=int, default=cur_year)
args = parser.parse_args()

cook = {"session":"53616c7465645f5f929b0f8abf13f82ed097688a169ddc8ffacbc8e9aef59bba3f8d4186d54568eb41b354fef3143ebc"}
url = "https://adventofcode.com/{}/day/{}/input".format(args.year, args.day)

res = requests.get(url, cookies=cook)

if res.status_code == 200:
  outfile = "aoc_2019/inputs/{0:04d}_12_{1:02d}_input.txt".format( args.year, args.day )
  with open(outfile, "w") as fh:
    fh.write( str( res.text.strip() ) )
  print("Input text fetched and saved:",outfile)

# https://adventofcode.com/2019/day/8/input
