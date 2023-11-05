#!/usr/bin/env python
# coding: utf-8

# # To Do:
# ## Clean up code in general
# ## Make sure to figure out what format to write in
# ## Check errors and comment throughout code 
# ## Remove redundant stuff
# 
# #### Note: I think javascript can check if a file submitted is a legit file, so I won't have to verify the files in this code I think for now, just check if it's excel file (prob javascript can also do that but just in case I did it here as well)

# In[1]:


import pandas as pd
import os
import sys
from pathlib import Path


# In[2]:


#Note to self, put double quotes around file to work in juypter, otherwise take it out to work in cmd prompt
# os.chdir(os.path.dirname(os.path.abspath(__file__)))


# In[3]:


# print(os.getcwd())


# In[4]:


if (args_count:=len(sys.argv))!=4: #Checks if there is 3 arguments, num says 4 cause the file itself counts as an arg
    print("Needs 3 arguments(files) in order to run, got",args_count-1)
    for x in sys.argv: #Just for clarity I suppose, prints out the arg files if less/more than 3 args are submitted
        print(x)
    sys.exit(3)


# In[5]:


#Assigns the files paths in this order, riboswitch sequences, linker, and primers
ribo_file = Path(sys.argv[1])
print("Riboswitch File path is:",ribo_file)
linker_file = Path(sys.argv[2])
print("Linker File path is:",linker_file)
primer_file = Path(sys.argv[3])
print("Target/Trigger File path is:",primer_file)


# In[ ]:


ribo_ext = os.path.splitext(ribo_file) #Gets the path ender like .txt and .pdf but we are looking for .xlsx (excel files)
linker_ext = os.path.splitext(linker_file)
primer_ext = os.path.splitext(primer_file)
ext_list = [ribo_ext[1], linker_ext[1], primer_ext[1]]


# In[ ]:


search = ".xlsx" #Verify that it's an excel file in the path at least
for x in ext_list:
    if(search not in x):
        print("These files need to be excel (xlsx) files")
        sys.exit(2)


# In[ ]:


riboswitches = pd.read_excel(ribo_file) #reads the excel files, makes them into database type
linker_database = pd.read_excel(linker_file,usecols="B") #Don't exactly know the excel format of linker files so I'll just use col B of the file for now
primer_database = pd.read_excel(primer_file)


# In[ ]:


# For testing purposes
# print(riboswitches)
# print(linker_database)
# print(primer_database)


# In[9]:


ribo_dict = riboswitches.to_dict() #Converts database into a dictionary, but pandas makes a dictionary of dictionary so we have to get the dictionary inside of it with the key/name of the column


# In[11]:


name_ribo_keys = ribo_dict.keys() #makes a list of keys


# In[12]:


ind = 0; #If follows the original format of the excel file, the first col of the file is the description, 2nd is the letters in sequences
for key in name_ribo_keys:
    if(ind==0): #Now we get an actual dictionary of what we want, in this case the descriptions and letters and volia dictionary for each
        desc = ribo_dict.get(key)
    else:
        letters = ribo_dict.get(key)
    ind+=1
    


# In[13]:


# print(desc)


# In[14]:


# print(letters)


# In[17]:


link_dict = linker_database.to_dict() #Basically just do the same now for both linker and primer sequences


# In[19]:


link_key = list(link_dict.keys())[0]


# In[21]:


linker_sequences = link_dict.get(link_key)


# In[22]:


# print(linker_sequences)


# In[25]:


check = "primer" #We just drop anything that does not "primer" in the header row. Def potential for errors but this will do for now as the offical format for these files are not given/decided yet
for col in primer_database.columns:
    if check not in col.lower():
        remove = col
        primer_database.drop(columns=remove, inplace=True)


# In[27]:


primer_dict = primer_database.to_dict()


# In[28]:


left_key = list(primer_dict.keys())[0]


# In[29]:


right_key = list(primer_dict.keys())[1]


# In[30]:


left_primer_sequences = primer_dict.get(left_key)


# In[31]:


right_primer_sequences = primer_dict.get(right_key)


# In[32]:


# print(left_primer_sequences)


# In[33]:


# print(right_primer_sequences)


# In[34]:


for x in range(len(left_primer_sequences)): #Just prints out all the combinations of sequences with row+1 to account for 0th row
    for y in range(len(linker_sequences)):
        for z in range(len(letters)):
            print("Primer row:",x+1,"Linker Row:",y+1,"Riboswitch Row:",z+1)
            print("Target Sequence:",left_primer_sequences.get(x))
            print("Trigger Sequence:",right_primer_sequences.get(x))
            print("Linker:",linker_sequences.get(y))
            print("Description of Riboswitch:",desc.get(z))
            print("Letters of Riboswitch:",letters.get(z))
        

    




