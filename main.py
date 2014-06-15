#!/usr/bin/python

# Input file that holds all the data
infile = "/home/chris/tmp/DO_NOT_BACKUP/PRESENT_10x1000_Select_resampled_StaticAlign.trs";

i = 0; 
toprint = ['','','','',''];
with open(infile, "rb") as f:
  byte = f.read(1)
  while byte != "":
    toprint[i] = byte.encode('hex');
    if i % 4 == 0:  
      for x in toprint: print x,
      print "";
      i = 0;
    byte = f.read(1)
    i += 1;
