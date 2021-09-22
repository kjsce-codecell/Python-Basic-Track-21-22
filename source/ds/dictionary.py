#!/usr/bin/env python
# coding: utf-8

# # Dictionaries 
# 

# In[2]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 
}
print(my_dict)


# # printing particular items in dictionaries 
# 

# In[5]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 
}
print(my_dict["college"])


# # duplicates not allowed 
# 

# In[7]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021,
    "year": 2022
}
print(my_dict)


# In[8]:


print(len(my_dict))


# ## Dictionary can hold any data type 

# In[16]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 ,
    "events": ['a','b','c'] #eg of lists in dict
}
print(my_dict)


# In[17]:


print(type(my_dict))


# # Accessing Items 

# In[19]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 ,
  #  "events": ['a','b','c'] #eg of lists in dict
}
print(my_dict)
s=my_dict["college"]
print(s)


# # Accessing through get() method
# 

# In[21]:


s=my_dict.get("college")
print(s)


# # Get keys 
# 
# The keys() method returns all the keys from my_dict

# In[23]:


x=my_dict.keys()
print(x)


# # Get values
#  
# The value() method will return all the values of my_dict

# In[24]:


d=my_dict.values()
print(d)


# # Get items
# 
# The items() method will return the bunch as in the key as well as values 

# In[25]:


x=my_dict.items()
print(x)


# # Using if for verifying particular key is present or not 
# 

# In[27]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 ,
  #  "events": ['a','b','c'] #eg of lists in dict
}
print(my_dict)
if "Council"in my_dict:
    print("yes")


# # Change values

# In[28]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 ,
  #  "events": ['a','b','c'] #eg of lists in dict
}
print(my_dict)
my_dict["year"]=2022
print(my_dict)


# # Update Dictionary 
# 
# The update() is used to update the dictionary "but pass the key  value pair at the same time"

# In[31]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 ,
  #  "events": ['a','b','c'] #eg of lists in dict
}
print(my_dict)
my_dict.update({"year": 2022})
print(my_dict)


# # Adding Items 
# 

# In[33]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 ,
  #  "events": ['a','b','c'] #eg of lists in dict
}
print(my_dict)
my_dict["speaker"]="Soumen"
print(my_dict)


# # Let's introduce the concepts of push and pop
# 
# # The pop() method is used to remove the item with key name 
# 
# # The push() method 

# In[34]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 ,
  #  "events": ['a','b','c'] #eg of lists in dict
}
print(my_dict)
my_dict.pop("college")
print(my_dict)


# # popitem() is used to removes the last element 

# In[36]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 ,
  #  "events": ['a','b','c'] #eg of lists in dict
}
print(my_dict)
my_dict.popitem()
print(my_dict)


# # the del keyword removes the item with the specified key name 

# In[38]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 ,
  #  "events": ['a','b','c'] #eg of lists in dict
}
print(my_dict)
del my_dict["college"]
print(my_dict)


# # Note del keyword can be used to delete the dictionary completely 

# In[39]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 ,
  #  "events": ['a','b','c'] #eg of lists in dict
}
print(my_dict)
del my_dict
print(my_dict)


# # IN the above code you may be thinking that the code went  wrong can anybody tell what happened in the above code????

# # clear() method 

# In[40]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 ,
  #  "events": ['a','b','c'] #eg of lists in dict
}
print(my_dict)
my_dict.clear()
print(my_dict)


# # loop in dictionaries 

# In[41]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 ,
  #  "events": ['a','b','c'] #eg of lists in dict
}
print(my_dict)
for x in my_dict: #printing all the key names in dictioary 
    print(x)


# In[43]:


my_dict = {
  "college": "Kjsce",
  "Council": "CodeCell",
  "year": 2021 ,
  #  "events": ['a','b','c'] #eg of lists in dict
}
print(my_dict)
for x in my_dict:
    print(my_dict[x])


# # Using keys() and values()  to loop

# In[47]:


for x in my_dict.keys():
  print(x)


# In[ ]:


for x in thisdict.values():
  print(x)


# In[ ]: