# ROSALIND
# Bioinformatics Stronghold
# Alignment
# Counting Point Mutations
# Kofi E. Gyan
# Jan. 3rd, 2017

"""
Problem

Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).

Sample Dataset:
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output:
7
"""

from __future__ import division # conversion for python 2 to 3
import operator # exports a set of efficient functions corresponding to the intrinsic operators of Python
import os # a portable way of using operating system dependent functionality in order to manipulate paths

# Implement the function
def d_hmmng(filename): # read in the file
    with open(os.path.join('C:\Users\kegyan\Documents\Programming\Python\ROSALIND\Datasets', filename), 'r') as f: # access the dataset in read mode and store the result in variable file
        dat = f.read().splitlines() # store all lines of the file as indivdual lines
    dat = list(dat)
    # return dat
    DNA_1 = dat[0] # assign as the first DNA string
    DNA_2 = dat[1] # assign as the second DNA string
    counter = 0 # set-up counter to determine the Hamming distance between DNA_1 and DNA_2
    for i in range(len(DNA_1)):
        if DNA_1[i] != DNA_2[i]:
            counter = counter + 1 # at each position if DNA_1 and DNA_2 differ then add 1 to the counter
    with open(os.path.join('C:\Users\kegyan\Documents\Programming\Python\ROSALIND\Datasets', 'output.txt'), 'w') as f: # create a new file for output
        f.write('The Hamming distance between these DNA sequences is:')
        f.write('\n' + str(counter)) # return the counter on a new line


# Test the function
d_hmmng('Test_Hamming.txt')
d_hmmng('rosalind_hamm.txt')