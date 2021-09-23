#!/usr/bin/env python
# coding: utf-8

# In[16]:


#importing the module
from isbntools.app import *
import isbnlib
#getting the information about a book from its isbn


isbn= input('Enter isbn number ')

book=isbnlib.meta(isbn)

title = book['Title']
authors = book['Authors']
print (title)
print(authors)


# In[ ]:





# In[ ]:




