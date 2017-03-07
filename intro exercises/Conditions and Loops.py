# ROSALIND
# Introductory Exercises
# Conditions and Loops
# Kofi E. Gyan
# Oct. 20th, 2016
"""
Problem
Given: Two positive integers a and b (a < b < 10000).
Return: The sum of all odd integers from a through b, inclusively.

Sample Dataset
100 200

Sample Output
7500

Hint
You can use a % 2 == 1 to test if a is odd.
"""

# Implement the function
def sum_odd(a, b):
    b = b + 1 # add 1 to the upper limit so range includes all necessary values
    result = list() # create empty list
    for i in range(a, b): # for loop to itierate through elements between variables a and b
        if i % 2 == 1: # check if the element is an odd number
            result.append(i) # if the element is odd append to the list
    result = sum(result) # sum all of these elements
    return result

# Test the function
print sum_odd(100, 200)
print sum_odd(4495, 9145)

    
    
    
    
    