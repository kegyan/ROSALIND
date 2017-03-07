#!/usr/bin/env python

# ROSALIND
# Bioinformatics Stronghold
# Combinatorics, Dynamic Programming
# Mortal Fibonacci Rabbits
# Kofi E. Gyan
# Jan. 12th, 2017


"""
Problem

Recall the definition of the Fibonacci numbers from: Rabbits and Recurrence Relations, which followed the recurrence relation Fn = F_(n - 1) + F_(n - 2) and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n \leq 100 and m \leq 20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Sample Dataset:
6 3

Sample Output:
4
"""

from __future__ import division # conversion for python 2 to 3
import operator # exports a set of efficient functions corresponding to the intrinsic operators of Python
import os # a portable way of using operating system dependent functionality in order to manipulate paths

# Implement the function
def mortal_fbncc_seq(n, m):
    n = int(n) # n represents the number of months to simulate
    m = int(m) # m represents the lifespan of each rabbit
    rab_pair_total = 1 # total number of rabbit pairs to begin with
    rab_reproduce = 0 # total number of rabbit pairs of reproduction age
    lifespan_counter = 0 # counter to keep track of rabbit lifespan
    maturity = 1 # lenth of time for rabbit pairs to become mature
    for i in range(n):
        if i != 0:
            # track time to maturity
            # track births
            # track time to death
            # track deaths
     
            if lifespan_counter >= maturity:
                rab_reproduce = rab_reproduce + 
            rab_pair_total = rab_reproduce * 2 # population doubles for each pair of mature rabbit pairs
            lifespan_counter = lifespan_counter + 1
            # track how old the rabbits are dynamically
            
            
            
                # lose 1 after 3, lose one after 5, lose one after 6, lose one after 7, lose two after 8, lose two after 9, lose two after 10, lose 4 after 11
    return rab_reproduce

# output = starting population + births - deaths        
        
# Test the function
print mortal_fbncc_seq(6, 3)
print mortal_fbncc_seq(8, 3)
print mortal_fbncc_seq(10, 3)
print mortal_fbncc_seq(99, 20)
# 135287380010682069829
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            