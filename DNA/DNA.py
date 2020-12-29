#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Description: Code basically reads through a text file containing a DNA sequence and output 
#              the number of A, T, C, G nucleotides within it
# Created: Dec 23, 2020
def main():
    file = open ("rosalind_dna.txt", "r")
    dna = file.read()
    numA = dna.count('A') # counts number of A occurences
    numT = dna.count('T') # counts number of T occurences
    numC = dna.count('C') # counts number of C occurences
    numG = dna.count('G') # counts number of G occurences
    print ("{0} {1} {2} {3}\n".format(numA, numC, numG, numT))
main()


# In[ ]:




