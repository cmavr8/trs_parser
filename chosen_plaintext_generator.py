#!/usr/bin/python

cube = [1, 2, 4];                   # Holds the cubes

plaintexts = [];                    # List to hold all plaintexts
plaintexts.append(0);               # Initial element

for x in cube:
  tmplist = [];                     # Temporary list
  for y in plaintexts: 
    tmp = y;                        # Obtain a copy
    mask = 1 << x                   # Shift a "1" left x places and use it as a mask for the XOR operation
    tmplist.append(tmp ^ mask);     # Save the plaintext
  plaintexts.extend(tmplist);        # Append temporary list to the main

# Now print the list
for z in plaintexts:
  print bin(z);
