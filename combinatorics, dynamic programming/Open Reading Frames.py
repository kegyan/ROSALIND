# Main Directory
# ROSALIND
# Bioinformatics Stronghold
# Combinatorics, Dynamic Programming
# Open Reading Frames
# Kofi E. Gyan
# Jan. 8th, 2017

"""
Problem

Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset:
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
CTGAGATGCTACTCGGATCATTCAGGCTTATTCCAAAAGAGACTCTAATCCAAGTCGCGGGGTCATCCCCATGTAACCTGAGTTAGCTACATGGCT (Reverse Complement)

mRNA
AGCCAUGUAGCUAACUCAGGUUACAUGGGGAUGACCCCGCGACUUGGAUUAGAGUCUCUUUUGGAAUAAGCCUGAAUGAUCCGAGUAGCAUCUCAG
CUGAGAUGCUACUCGGAUCAUUCAGGCUUAUUCCAAAAGAGACUCUAAUCCAAGUCGCGGGGUCAUCCCCAUGUAACCUGAGUUAGCUACAUGGCU (Reverse Complement)

Sample Output:
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""

from __future__ import division # conversion for python 2 to 3
import operator # exports a set of efficient functions corresponding to the intrinsic operators of Python
import os # a portable way of using operating system dependent functionality in order to manipulate paths

# Helper function to create a complement strand of DNA
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

# Helper function to translate RNA into Protein, modify sliding window to only move by one instead of three, only append to result variable if substr begins with 'M'
def mRNA_prtn(dat):
    dat = str(dat) # convert file to string format
    dat = dat.replace('\n', '') # replace all occurences of \n with ''
    dat = dat.strip() # return a copy of the string with leading and trailing characters removed
    dat_length = int(len(dat)) # calculate total length of the mRNA string
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
        # result.append('\n') # begin a new line for following mRNA translation
        index_1 = index_1 + 3 # sliding window, start
        index_2 = index_2 + 3 # sliding window, end
    result = (''.join(result)) # joins each element of result into one element
    result = str(result) # convert to string data type
    return result

# Implement the function
def ORF_seq(filename): # read in the file
    with open(os.path.join('C:\Users\kegyan\Documents\Programming\Python\ROSALIND\Datasets', filename), 'r') as f: # access the dataset in read mode and store the result in variable file
        dat = f.read().splitlines() # store all lines of the file as indivdual lines
    dat = list(dat)
    FASTA_ID = dat[0] # assign the FASTA ID
    DNA_input = dat[1:] # assign the DNA sequence
    DNA_input = str(DNA_input) # convert file to string format
    DNA_input = DNA_input.replace('\n', '') # replace all occurences of \n with ''
    DNA_input = DNA_input.strip() # return a copy of the string with leading and trailing characters removed
    DNA_input = DNA_input.replace('[', '').replace(']', '').replace(',', '').replace("' '", '') # join each element of result into one element by removing brackets and commas
    DNA_input = DNA_input.strip() # return a copy of the string with leading and trailing characters removed
    DNA_input_cmplmnt = complement_strand(DNA_input) # create a reverse complement strand of the DNA input
    DNA_input = DNA_input.replace('T', 'U') # convert DNA_input from DNA into RNA
    DNA_input_cmplmnt = DNA_input_cmplmnt.replace('T', 'U') # convert DNA_input_cmplmnt from DNA into RNA
    result_DNA = mRNA_prtn(str(DNA_input)) # translating the first ORF
    result_DNA_cmplmnt = mRNA_prtn(str(DNA_input_cmplmnt)) # translating the first ORF
    result_DNA_2 = mRNA_prtn(str(DNA_input[1:])) # translating the second ORF
    result_DNA_cmplmnt_2 = mRNA_prtn(str(DNA_input_cmplmnt[1:])) # translating the second ORF
    result_DNA_3 = mRNA_prtn(str(DNA_input[2:])) # translating the third ORF
    result_DNA_cmplmnt_3 = mRNA_prtn(str(DNA_input_cmplmnt[2:])) # translating the third ORF
    # identify the position of all M's in each string in order to enforce lack of M and account for multiple M's
    total_M_result_DNA = result_DNA.count('M') # total number of Ms in the sequence
    result_DNA_pos_M = [pos for pos, char in enumerate(result_DNA) if char == 'M'] # find all positions of M in the string
    total_M_result_DNA_cmplmnt = result_DNA_cmplmnt.count('M') # total number of Ms in the sequence
    result_DNA_cmplmnt_pos_M = [pos for pos, char in enumerate(result_DNA_cmplmnt) if char == 'M'] # find all positions of M in the string
    total_M_result_DNA_2 = result_DNA_2.count('M') # total number of Ms in the sequence
    result_DNA_2_pos_M = [pos for pos, char in enumerate(result_DNA_2) if char == 'M'] # find all positions of M in the string
    total_M_result_DNA_cmplmnt_2 = result_DNA_cmplmnt_2.count('M') # total number of Ms in the sequence
    result_DNA_cmplmnt_2_pos_M = [pos for pos, char in enumerate(result_DNA_cmplmnt_2) if char == 'M'] # find all positions of M in the string
    total_M_result_DNA_3 = result_DNA_3.count('M') # total number of Ms in the sequence
    result_DNA_3_pos_M = [pos for pos, char in enumerate(result_DNA_3) if char == 'M'] # find all positions of M in the string
    total_M_result_DNA_cmplmnt_3 = result_DNA_cmplmnt_3.count('M') # total number of Ms in the sequence
    result_DNA_cmplmnt_3_pos_M = [pos for pos, char in enumerate(result_DNA_cmplmnt_3) if char == 'M'] # find all positions of M in the string
    result_master_list = list() # empty list
    result_output_list = list() # empty list for removing duplicates
    for i in range(total_M_result_DNA):
        result = result_DNA[result_DNA_pos_M[i]:] # store all elements of the string as a single line in output file
        stop_codon_pos = result.find('*stop*') # locate position of first stop codon
        if stop_codon_pos != -1: # identify and remove sequences which contain a start site but lack a transcription stop site
            result = result.replace(result[stop_codon_pos:], '') # enforce stop codon by replacing everything after it with empty space
            result_master_list.append(result) # store all elements of the string as a single element in the master list
    for i in range(total_M_result_DNA_cmplmnt):
        result = result_DNA_cmplmnt[result_DNA_cmplmnt_pos_M[i]:] # store all elements of the string as a single line in output file
        stop_codon_pos = result.find('*stop*') # locate position of first stop codon
        if stop_codon_pos != -1: # identify and remove sequences which contain a start site but lack a transcription stop site
            result = result.replace(result[stop_codon_pos:], '') # enforce stop codon by replacing everything after it with empty space
            result_master_list.append(result) # store all elements of the string as a single element in the master list
    for i in range(total_M_result_DNA_2):
        result = result_DNA_2[result_DNA_2_pos_M[i]:] # store all elements of the string as a single line in output file
        stop_codon_pos = result.find('*stop*') # locate position of first stop codon
        if stop_codon_pos != -1: # identify and remove sequences which contain a start site but lack a transcription stop site
            result = result.replace(result[stop_codon_pos:], '') # enforce stop codon by replacing everything after it with empty space
            result_master_list.append(result) # store all elements of the string as a single element in the master list
    for i in range(total_M_result_DNA_cmplmnt_2):
        result = result_DNA_cmplmnt_2[result_DNA_cmplmnt_2_pos_M[i]:] # store all elements of the string as a single line in output file
        stop_codon_pos = result.find('*stop*') # locate position of first stop codon
        if stop_codon_pos != -1: # identify and remove sequences which contain a start site but lack a transcription stop site
            result = result.replace(result[stop_codon_pos:], '') # enforce stop codon by replacing everything after it with empty space
            result_master_list.append(result) # store all elements of the string as a single element in the master list
    for i in range(total_M_result_DNA_3):
        result = result_DNA_3[result_DNA_3_pos_M[i]:] # store all elements of the string as a single line in output file
        stop_codon_pos = result.find('*stop*') # locate position of first stop codon
        if stop_codon_pos != -1: # identify and remove sequences which contain a start site but lack a transcription stop site
            result = result.replace(result[stop_codon_pos:], '') # enforce stop codon by replacing everything after it with empty space
            result_master_list.append(result) # store all elements of the string as a single element in the master list
    for i in range(total_M_result_DNA_cmplmnt_3):
        result = result_DNA_cmplmnt_3[result_DNA_cmplmnt_3_pos_M[i]:] # store all elements of the string as a single line in output file
        stop_codon_pos = result.find('*stop*') # locate position of first stop codon
        if stop_codon_pos != -1: # identify and remove sequences which contain a start site but lack a transcription stop site
            result = result.replace(result[stop_codon_pos:], '') # enforce stop codon by replacing everything after it with empty space
            result_master_list.append(result) # store all elements of the string as a single element in the master list
    for i in result_master_list:
        if i not in result_output_list: # create a new list which does not contain duplicates of any open reading frame sequences
            result_output_list.append(i)
    with open(os.path.join('C:\Users\kegyan\Documents\Programming\Python\ROSALIND\Datasets', 'output.txt'), 'w') as f: # create a new file for output
        f.write(FASTA_ID) # fasta ID information
        f.write('\n') # start writing on a new line
        for i in result_output_list:
            f.write(i) # all unique ORF sequences
            f.write('\n') # start writing on a new line


# Test the function
ORF_seq('Test_orf.txt')
ORF_seq('rosalind_orf.txt')