#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Python Program to merge two files into a third file


# In[6]:


firstfile = Path(r'C:\Users\Mayureshwar\Desktop\python\GFG.txt') 
secondfile = Path(r'C:\Users\Mayureshwar\Desktop\python\CSE.txt') 
  
newfile = input("Enter the name of the new file: ") 
print() 
print("The merged content of the 2 files will be in", newfile) 
  
with open(newfile, "wb") as wfd: 
  
    for f in [firstfile, secondfile]: 
        with open(f, "rb") as fd: 
            shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10) 
  
print("\nThe content is merged successfully.!") 
print("Do you want to view it ? (y / n): ") 
  
check = input() 
if check == 'n': 
    exit() 
else: 
    print() 
    c = open(newfile, "r") 
    print(c.read()) 
    c.close() 


# In[7]:


def unique_values_in_list_of_lists(lst):
    result = set(x for l in lst for x in l)
    return list(result)
nums = [[1,2,3,5], [2,3,5,4], [0,5,4,1], [3,7,2,1], [1,2,1,2]]
print("Original list:")
print(nums)
print("Unique values of the said list of lists:")
print(unique_values_in_list_of_lists(nums))
chars = [['h','g','l','k'], ['a','b','d','e','c'], ['j','i','y'], ['n','b','v','c'], ['x','z']]
print("\nOriginal list:")
print(chars)
print("Unique values of the said list of lists:")
print(unique_values_in_list_of_lists(chars))


# In[ ]:




