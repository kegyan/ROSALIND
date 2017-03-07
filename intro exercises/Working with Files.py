# ROSALIND
# Introductory Exercises
# Working with Files
# Kofi E. Gyan
# Oct. 31st, 2016

"""
Problem

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

Sample Dataset:
Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat

Sample Output:
Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat
"""
import os

# Implement the function
def file_data(filename):
    with open(os.path.join('Datasets', filename), 'r') as file: # access the dataset in read mode and store the result in variable file
        data = file.read().splitlines() # store all lines of the file as indivdual lines
    data = list(data)
    # return data
    even_line = list() # create empty list
    counter = 0 # use counter to set-up 1-based numbering of lines
    for i in data:
        counter = counter + 1
        if counter % 2 == 0: # return only the even numbered lines
            even_line.append(i) # appened these lines to a list
    with open(os.path.join('Datasets', 'output.txt'), 'w') as file: # create a new file for output
        for i in even_line:
            data_2 = file.write(i + '\n') # store all elements of the list as indivdual lines in output file
            #data_2 = ('\n'.join(data_2))
        return data_2
    
    
# Test the function
#print file_data('test.txt')
print file_data('rosalind_ini5.txt')


