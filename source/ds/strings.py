#!/usr/bin/env python
# coding: utf-8

# # 'Strings' 

# # strings are written in single or double quotes eg 'hello ', ''hello''

# In[1]:


### assigning string to a variable 
a="hello"
print(a)


# In[7]:


### you can also use three double quotes or three single quotes 
a="""hello welcome you all to this 
CodeCell python workshop basic track."""
print(a)


# In[ ]:





# ## Looping through string

# In[9]:


for x in 'codecell':
    print(x)


# # String Length

# In[10]:


a="Kjsce CodeCell"
print(len(a))


# # Check string 

# In[11]:


b="hi hello welcome here"
print("hello "in b)


# # Check if not 

# In[12]:


txt = "Naruto is best "
print("Sakura" not in txt)


# # Slicing strings 
# 

# In[14]:


#Get the characterts printed from position 3 to position 6 not included
a="KJSCE CodeCell"
print(a[2:6])


# # Slice from the start 

# In[15]:


a="KJSCE CodeCell"
print(a[:6])


# # Slice To the End

# In[16]:


a="KJSCE CodeCell"
print(a[6:])


# # Negative Indexing
#  
# # AS the name prefers negative slicing will start from end  and last character  refers to -1

# In[19]:


#Get the characters:
#From: "o" in "World!" (position -5)

#To, but not included: "d" in "World!" (position -2):

b = "HELLO WORLD"
print(b[-5:-2])


# #  Modify strings

# # Upper case 

# In[20]:


a="kjsce codecell"
print(a.upper())


# # Lower case
# 

# In[21]:


a="KJSCE CODECELL"
print(a.lower())


# # Replace characters 
# 
# The replace() method replaces  character with another character 

# In[22]:


a = "Hello, World!"
print(a.replace("H", "J"))


# # Split string 
# 
# split() metjod splits the string iinto substrings if it finds instances of the seperator 

# In[23]:


a="Kjsce, CodeCell"
print(a.split(","))


# # String concatenation 

# In[25]:


a = "Kjsce"
b = "CODECELL"
c = a + b
print(c)


# In[26]:


# to add space between add a " "
a = "Kjsce"
b = "CODECELL"
c = a +" "+ b
print(c)


# # String format 
# 
# ## Note  you cannot combine strings and numbers with '+'

# In[29]:


age = 36
txt = "My name is Soumen, I am " + age
print(txt)
# you will get an error


# # format() method to insert numbers into strings

# In[31]:


age = 19
b=20
txt = "My name is Soumen  , and I am {}"
print(txt.format(age))


# In[ ]:




