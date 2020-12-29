#!/usr/bin/env python
# coding: utf-8

# In[1]:


def main():
    file = open ("rosalind_dna.txt", "r")
    dna = file.read()
    print (dna.replace('T', 'U'))
main()


# In[ ]:




