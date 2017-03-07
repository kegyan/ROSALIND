# ROSALIND
# Bioinformatics Stronghold
# Rosalind
# Translating RNA into Protein
# Kofi E. Gyan
# Dec. 29th, 2016

"""
Problem

The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

Sample Dataset:
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output:
MAMAPRTEINSTRING
"""

from __future__ import division # conversion for python 2 to 3
import os # a portable way of using operating system dependent functionality in order to manipulate paths

# Implement the function
def mRNA_prtn(filename): # read in dataset
    with open(os.path.join('Datasets', filename), 'r') as f: # access the dataset in read mode and store the result in variable file
        dat = f.read() # read and store all lines of the file
    dat = str(dat) # convert file to string format
    dat = dat.replace('\n', '') # replace all occurences of \n with ''
    dat = dat.strip() # return a copy of the string with leading and trailing characters removed
    dat_length = int(len(dat) / 3) # calculate total length of the mRNA string
    index_1 = 0 # manually create a sliding window, start
    index_2 = 3 # manually create a sliding window, end
    result = list() # create empty list
    for i in range(dat_length): # loop through the string to convert RNA codons into amino acids
        substr = dat[index_1:index_2] # substring mRNA string into an RNA codon
        if substr == 'UUU' or substr == 'UUC': # convert RNA codon to amino acid
            substr = 'F'
        elif substr == 'UUA' or substr == 'UUG':
            substr = 'L'
        elif substr == 'UCU' or substr == 'UCC' or substr == 'UCA' or substr == 'UCG':
            substr = 'S'
        elif substr == 'UAU' or substr == 'UAC':
            substr = 'Y'
        elif substr == 'UGU' or substr == 'UGC':
            substr = 'C'
        elif substr == 'UGG':
            substr = 'W'
        elif substr == 'CUU' or substr == 'CUC' or substr == 'CUA' or substr == 'CUG':
            substr = 'L'
        elif substr == 'CCU' or substr == 'CCC' or substr == 'CCA' or substr == 'CCG':
            substr = 'P'
        elif substr == 'CAU' or substr == 'CAC':
            substr = 'H'
        elif substr == 'CAA' or substr == 'CAG':
            substr = 'Q'
        elif substr == 'CGU' or substr == 'CGC' or substr == 'CGA' or substr == 'CGG':
            substr = 'R'
        elif substr == 'AUU' or substr == 'AUC' or substr == 'AUA':
            substr = 'I'
        elif substr == 'AUG':
            substr = 'M'
        elif substr == 'ACU' or substr == 'ACC' or substr == 'ACA' or substr == 'ACG':
            substr = 'T'
        elif substr == 'AAU' or substr == 'AAC':
            substr = 'N'
        elif substr == 'AAA' or substr == 'AAG':
            substr = 'K'
        elif substr == 'AGU' or substr == 'AGC':
            substr = 'S'
        elif substr == 'AGA' or substr == 'AGG':
            substr = 'R'
        elif substr == 'GUU' or substr == 'GUC' or substr == 'GUA' or substr == 'GUG':
            substr = 'V'
        elif substr == 'GCU' or substr == 'GCC' or substr == 'GCA' or substr == 'GCG':
            substr = 'A'
        elif substr == 'GAU' or substr == 'GAC':
            substr = 'D'
        elif substr == 'GAA' or substr == 'GAG':
            substr = 'E'
        elif substr == 'GGU' or substr == 'GGC' or substr == 'GGA' or substr == 'GGG':
            substr = 'G'
        elif substr == 'UAA' or substr == 'UAG' or substr == 'UGA':
            substr = '*stop*' # enforce stop codons? stop codons are removed from result at the end
        result.append(substr) # append amino acid to output variable
        index_1 = index_1 + 3 # sliding window, start
        index_2 = index_2 + 3 # sliding window, end
    result = (''.join(result)) # joins each element of result into one element
    result = str(result) # convert to string data type
    stop_codon_pos = result.find('*stop*') # locate position of first stop codon
    # result = result.replace(result[stop_codon_pos:], '') # enforce stop codon by replacing everything after it with empty space
    with open(os.path.join('Datasets', 'output.txt'), 'w') as f: # create a new file for output
        for i in result:
            dat_2 = f.write(i) # store all elements of the string as a single line in output file
        return dat_2

# Test the function
mRNA_prtn('rosalind_prot.txt')


