#!/usr/bin/env python

# Main Directory
# Sub-Directory
# Folder Name
# Program Name
# Kofi E. Gyan
# Date

"""
Program information and description.
"""

from __future__ import division # conversion for python 2 to 3
import operator # exports a set of efficient functions corresponding to the intrinsic operators of Python
import os # a portable way of using operating system dependent functionality in order to manipulate paths

# Implement the function
# read in the file
with open(os.path.join('C:\Users\kegyan\Documents\Programming\Python\ROSALIND\Datasets', filename), 'r') as f: # access the dataset in read mode and store the result in variable file
    dat = f.read().splitlines() # store all lines of the file as indivdual lines
dat = list(dat)
# return dat

with open(os.path.join('C:\Users\kegyan\Documents\Programming\Python\ROSALIND\Datasets', 'output.txt'), 'w') as f: # create a new file for output
    for i in result: # 0-based numbering result
        f.write(i) # store all elements of the string as a single line in output file
        f.write('\n') # start writing on a new line





# Test the function