# ROSALIND
# Bioinformatics Stronghold
# Heredity and Probability
# Mendel's First Law
# Kofi E. Gyan
# Dec. 19th, 2016

"""
Problem

Probability is the mathematical study of randomly occurring phenomena. We will model such a phenomenon with a random variable, which is simply a variable that can take a number of different distinct outcomes depending on the result of an underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X represent the random variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X = red) = 3 / 5 and Pr(X = blue) = 2 / 5.

Random variables can be combined to yield new random variables. Returning to the ball example, let Y model the color of a second ball drawn from the bag (without replacing the first ball). The probability of Y being red depends on whether the first ball was red or blue. To represent all outcomes of X and Y, we therefore use a probability tree diagram. This branching diagram represents all possible individual probabilities for X and Y, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree; see Figure 2. (rosalind.info) for an illustrative example.

An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A be the event "Y is blue." Pr(A) is equal to the sum of the probabilities of two different outcomes: Pr(X = blue and Y = blue) + Pr(X = red and Y = blue), or 3 / 10 + 1 / 10 = 2 / 5 (see Figure 2 above).

Given: Three positive integers k, m, and n, representing a population containing k + m + n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Sample Dataset:
2 2 2

Sample Output:
0.78333
"""


# Implement the function
def mendel_prob(k, m, n):
    k = float(k) # convert to floats in order to work with decimals
    m = float(m)
    n = float(n)
    N = k + m + n # total population size
    
    ## calculate the proabilty for all non-guarrunteed mating pairs
    n_1 = n / N # prob. of choosing n the 1st time
    n_2 = (n - 1) / (N - 1) # prob. of choosing n the 2nd time
    hmzgs_rcssv = (n_1 * n_2) # prob. of choosing two homozygous recessive pairs to mate
    
    m_1 = m / N # prob. of choosing m the 1st time
    m_2 = (m - 1) / (N - 1) # prob. of choosing m the 2nd time
    htrzgs = (m_1 * m_2) # prob. of choosing two heterozygous pairs to mate
    
    m_1 = m / N # prob. of choosing m the 1st time
    n_2 = (n) / (N - 1) # prob. of choosing n the 2nd time
    htrzgs_rcssv = m_1 * n_2 # prob. of choosing a heterozygous and a homozygous recessive pair to mate
    
    n_1 = n / N # prob. of choosing n the 1st time
    m_2 = (m) / (N - 1) # prob. of choosing m the 2nd time
    rcssv_htrzgs = n_1 * m_2 # prob. of choosing a homozygous recessive and a heterozygous pair to mate
    
    result  = (1 - (hmzgs_rcssv + (htrzgs / 4) + (htrzgs_rcssv / 2) + (rcssv_htrzgs / 2)))
    return result

    
    
# Test the function
print mendel_prob(2, 2, 2)
print mendel_prob(16, 29, 23)

