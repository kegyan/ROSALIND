# ROSALIND
# Introductory Exercises
# Variables and Some Arithmetic
# Kofi E. Gyan
# Oct. 20th, 2016

"""
Problem
Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
"""

# Implement the function
def hypotenuse(a, b):
    c = ((a ** 2) + (b ** 2)) # each variable is 'squared' and then added together
    return c

# Test the function
print hypotenuse(3, 5)
print hypotenuse(964, 937)
