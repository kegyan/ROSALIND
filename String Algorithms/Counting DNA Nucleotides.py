# ROSALIND
# Bioinformatics Stronghold
# String Algorithms
# Counting DNA Nucleotides
# Kofi E. Gyan
# Nov. 4th, 2016

"""
Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output
20 12 17 21
"""

# Implement the function
def nucleotide_count(s):
    master_list = [] # create an empty master list to store each letter from the input string
    for i in s: # iterate through the string
        master_list.append(i) # seperate and store each nucleotide from the string in a list
    count_A = 0 # set up counters
    count_C = 0
    count_G = 0
    count_T = 0
    for j in master_list: # iterate through the list
        if j == 'A':
            count_A = count_A + 1
        elif j == 'C':
            count_C = count_C + 1
        elif j == 'G':
            count_G = count_G + 1
        elif j == 'T':
            count_T = count_T + 1
    print count_A, count_C, count_G, count_T

# Test the function
s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
print nucleotide_count(s)

p = 'CAAACTATCGTGAGACTTACGATCACGCGATGGCAGTTATCGACTTGGGAAATCCTATCTCCTGGGCGGCCATCAGTGCTTTAAACACTCGTTTATTCGGCTTTTGCTAGTTTCAAAGGTCTAGTCGAGAGTAAGAGAACAGCCTGCGCGGTCGCATCGACGTACTCAATGTCCCCGCACCAATCTAAGGCGGTAGTTTTATATCGCGGTCACGCCTGGTGCTGGAGGTAATATACTGCTTTCCTTAGAGCGAAACTAAATCCAAAGTTTTCTTGAGTCACACAAGAAGTTTCAGGCTTCAGTGGTAATCGGGAGCAAGTTGAGACGCCAGGGCGGGACCGCAGGCAGACAATCCGTTTATCCCCTCGCACTTATTCCATTGAGCTCGCGCTTAGCGGCTACCTACGCGACTTACGGTTTCAAGAGTGAGCGTAATCTATCGCGATGCGTAGACTACTTCGGGGAATAAGACCAGGTTGGAGCATAGATCGCAGGGTTCTTCGGCAGCTTGCGAAGCACACATGAGTGTGTTCTTGCTTTGAGTATAGTAAGTGTATTGACGCCCCGATCGAAATATAGGCGTGCCCGCGCATTATAAATTCACAAACCGGGTTATTATATCCAGTGCAGTCGCGATGATACTTTAATCTCATCTCATCAAGAACCACTCATATCCCGTTGCTGATAGCGCCAGTGTTAACTCATGTTCGCGGCCTGAATCCTCCTGATTAAGTCTTTCCTCGTTCAACGGGGTGCGGTCTCACTTGCATACCAGTACACTTCTTTTTCACCCTGAAAAACCGTTAGGCTCAACACAGTTATTTGCAGTATACTAGGGGGATCGAAGACAGGAGAGCTTAGAGTCAGGCCTTAGGATCTTCGGCAGCGGATAACGATGCGGGTGACCGTCTGATCGACCACGTACATTCTGCGCTAAGCCCTACGGCTGGCGTTGTTAGCCCC'
print nucleotide_count(p)