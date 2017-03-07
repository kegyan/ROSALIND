# ROSALIND
# Introductory Exercises
# Dictionaries
# Kofi E. Gyan
# Nov. 4th, 2016


"""
Problem

Given: A string s of length at most 10000 letters.

Return: How many times any word occurred in string. Each letter case (upper or lower) in word matters. Lines in output can be in any order.

Sample Dataset:
We tried list and we tried dicts also we tried Zen

Sample Output:
and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1
"""

# Implement the function
def word_count(s):
    master_list = [] # create an empty master list to store each word from the input string
    count_dict = {} # create an empty dictionary to store each word with its specific number of occurences
    for i in s.split(' '): # iterate through the string
        master_list.append(i) # seperate and store each word from the string in a list
    # return master_list
    for j in master_list: # iterate through the list
        count = 0 # reset the count to 0 for each item in the list
        count = master_list.count(j) # count the number of occurences
        count_dict[j] = count # append this information into a dictionary
    # return count_dict
    for key, value in count_dict.items():
        print key, value # display each word and its number of occurences

# Test the function
s = 'We tried list and we tried dicts also we tried Zen'
print word_count(s)

p = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
print word_count(p)
