#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Description: Code reads through a text file containing a DNA sequence and outputs 
#              the corresponding complimentary strand of DNA 
# Created: Dec 26, 2020
def main():
    file = open ("rosalind_revc.txt", "r")
    dna = file.read()
    output = ""
    for x in dna:
        if x == "A":
            output += "T"
        elif x == "T":
            output += "A"
        elif x == "C":
            output += "G"
        elif x == "G":
            output += "C"
    final = output[::-1]
    print (final)
main()


# In[ ]:




