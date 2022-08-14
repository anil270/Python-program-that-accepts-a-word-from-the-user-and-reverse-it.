#!/usr/bin/env python
# coding: utf-8

# # Write a Python program that accepts a word from the user and reverse it.

# In[22]:


word = input("Enter the word")
print(word)
for x in range(len(word) -1,-1,-1):
    print(word[x],end="")

