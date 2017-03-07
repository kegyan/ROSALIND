# ROSALIND
# Bioinformatics Stronghold
# String Algorithms
# Complementing a Strand of DNA  
# Kofi E. Gyan
# Nov. 6th, 2016

"""
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string s^c formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement s^c of s.

Sample Dataset:
AAAACCCGGT

Sample Output:
ACCGGGTTTT
"""

# Implement the function
def complement_strand(t):
    master_list = [] # create an empty master list to store each nucleotide from the input string
    for i in t: # iterate through the string
        master_list.append(i) # seperate and store each nucleotide from the string in a list
    count = 0
    for j in master_list:
        if j == 'A':
            master_list[count] = 'T'
        elif j == 'C':
            master_list[count] = 'G'
        elif j == 'G':
            master_list[count] = 'C'
        elif j == 'T':
            master_list[count] = 'A'
        count = count + 1
    five_prime = range(len(master_list)) # create an empty list to place complement strand in 5' to 3' orientation
    pos = len(five_prime) - 1 # pos to specify list indices
    for k in master_list:
        five_prime[pos] = k
        pos = pos - 1
    five_prime = ''.join(map(str, five_prime))
    return five_prime
    


# Test the function
t = 'AAAACCCGGT'
print complement_strand(t)

t = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
print complement_strand(t)

p = 'CGCAATCCGGCCGGCTCTAGTTGTTAACTACATAAGGTACACCCTTAACTGTGGACAAAAACGTAAGCTGCCGGGGATCACACTCTGTTCTGTCCTCATATGCGCCAGAGGGCAACAGCAGACATTGGACACTATTTCTAGCGGGACATCAACATCCAACCGGGGAGGGACGCTATTGAATTGAGAAACACGGAGCGAAACGTAACTTTCTGAAGAACTATACGGGCCTTGGGTTACATCTCTGATCGGCGCATATGTGCCTCTCAGTTTTCTGGCGCCCTAATCGTTTCGAAAGGCGGTGAACCCTCAAGGCCATGGGGTACCCTGCTCGCGTTCCATTCCGCACCGGGTGACAGGGTACGTCTAGTATATCTTCGTTAACCCACACTGCTGAACTATCAACCGGTTCCGAGACGCGCCGTTGTTAAGGAGCAAAGTGCGAGGATCCGGGACAGTAGACTGCCAAGACATTAATTAAAAATGCAATGTTGTGAGCGCTCGCCCCCTTGCTAGGTGCACAATTAGTCCAAACCAGTGAACCGCTTTTACTCGCCGCGTGATCTCCATGTCTCACTGCGCTCATGCCCAGACGCAATGTCGCAGATGCCATGTCCCTGGCCATCCTGCCATTTCCTGTTTACGGTACCATTTCTCGGGCTATCTCAGTGACAGCCGTCCGTCCCTGGGATTGCTAGGGTGCTGACGTTTGCCGTCCACGCAGAACAAGCTCATACAGTATGAGTGCGATAGAGCCTGTTTGATACTGTTAAGATCGGAGTAGCTGAAGCGCGCAGAGATTAGAGATACTCAGGGATCGAAAGCCGAATTTGGAGGAGCGATTGAGGCGCTACCAGCGGTCAGAGCCCTGGTAGGTT'
print complement_strand(p)

