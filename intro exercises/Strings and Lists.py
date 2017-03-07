# ROSALIND
# Introductory Exercises
# Strings and Lists
# Kofi E. Gyan
# Oct. 20th, 2016

"""
Problem
Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.

Sample Dataset
HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102

Sample Output
Humpty Dumpty
"""

# Implement the function
def pos(a, b, c, d): # first function for recording the given slice site positions
    global pos1 # record position and move information from function frame to global frame
    pos1 = a
    global pos2 # record position and move information from function frame to global frame
    pos2 = b + 1
    global pos3 # record position and move information from function frame to global frame
    pos3 = c
    global pos4 # record position and move information from function frame to global frame
    pos4 = d + 1
    
def phrase(s): # second function for slicing the string
    s = str(s) # ensure data-type is a string
    first = s[pos1:pos2] # slice the string using available global frame variables
    second = s[pos3:pos4] # slice the string using available global frame variables
    return first + ' ' + second # string with space in between
    

# Test the function
pos(12, 18, 43, 48)
print phrase('Bdb3byb7Bk7bNerodia3v7Q5L689tDah8dQXDspOOpxcoroneG9oFRKSnZilVtfiuI7zvf3Esoyzom7vi6rQdGSsSBzDdmkccM0K3TmYZZOqFziYlseZ5vUit7fe74TUW8G7kVDhFkCuK56cqpFgPSZtfsFktUBaPToMiSD38.')





