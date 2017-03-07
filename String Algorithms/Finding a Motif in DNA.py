# ROSALIND
# Bioinformatics Stronghold
# String Algorithms
# Finding a Motif in DNA 
# Kofi E. Gyan
# Jan. 2nd, 2017

"""
Problem

Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset:
GATATATGCATATACTT
ATAT

Sample Output:
2 4 10
"""

from __future__ import division # conversion for python 2 to 3
import operator # exports a set of efficient functions corresponding to the intrinsic operators of Python
import os # a portable way of using operating system dependent functionality in order to manipulate paths

# Implement the function
def motif_seq(filename): # read in the dataset
    with open(os.path.join('C:\Users\kegyan\Documents\Programming\Python\ROSALIND\Datasets', filename), 'r') as f: # access the dataset in read mode and store the result in variable file
        dat = f.read().splitlines() # store all lines of the file as indivdual lines
    dat = list(dat)
    # return dat
    q = str(dat[0]) # assign q as the string
    p = str(dat[1]) # assign p as the substring
    motif_pos = [] # empty list
    motif_pos1 = [] # empty list
    motif_pos = [i for i in xrange(len(q)) if q.find(p, i) == i] # find all positions of substring p in string q
    result = motif_pos
    result = str(result) # convert to string data type
    result = result.replace('[', '').replace(']', '').replace(',', '') # join each element of result into one element by removing brackets and commas
    result = str(result) # convert to string data type
    # 0-based numbering result
    for k in motif_pos: # convert output
        motif_pos1.append(k + 1)
    result1 = motif_pos1
    result1 = str(result1) # convert to string data type
    result1 = result1.replace('[', '').replace(']', '').replace(',', '') # join each element of result into one element by removing brackets and commas
    result1 = str(result1) # convert to string data type
    # 1-based numbering result
    with open(os.path.join('C:\Users\kegyan\Documents\Programming\Python\ROSALIND\Datasets', 'output.txt'), 'w') as f: # create a new file for output
        for i in result: # 0-based numbering result
            dat_2 = f.write(i) # store all elements of the string as a single line in output file
        f.write('\n') # start writing on a new line
        for i in result1: # 1-based numbering result
            dat_3 = f.write(i) # store all elements of the string as a single line in output file



# Test the function
motif_seq('rosalind_subs.txt')
# C:\Users\kegyan\Documents\Programming\Python\ROSALIND\Datasets\rosalind_subs.txt
# C:\Users\kegyan\Documents\Programming\Python\ROSALIND\Datasets\output.txt