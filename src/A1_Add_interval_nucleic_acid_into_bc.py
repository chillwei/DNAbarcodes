#!/usr/bin/env python
# coding: utf-8

# This py file is basically to add interval A/T nucleic acid into the barcode library generated by LZamparo bc design tool

# #  Import barcode library file

# In[1]:


import os
import numpy as np
import pandas as pd
import re
import sys
import common as common


dir = common.THIS_MODULE_PATH

BC_dir = os.path.join(dir,'Barcode_length12.csv')


data = pd.read_csv(BC_dir,index_col = False)

df = pd.DataFrame(data)


BC_df = df.iloc[: , 1:]



# break the barcode string and add intervel nucleic acid
def Add_BC_intervel(inputdf, outputdf):
    BC_list = []
    count = 0 
    outputdf = pd.DataFrame()
    for _, row in inputdf.iterrows():
        Barcode = row['Barcode']
        BC = 'T'+ Barcode + 'A'
        sp1 = BC[0:3]
        sp2 = BC[3:6]
        sp3 = BC[6:8]
        sp4 = BC[8:11]
        sp5 = BC[11:14]
        NewBC = sp1+'T'+ sp2 + 'A' +sp3 + 'T'+sp4+'A'+sp5
        BC_list.append(NewBC)
        count += 1
        print(count)
    outputdf['Barcode'] = BC_list
    outputdf.to_csv(r'NIST_Barcode_raw.txt', header=None, index=None, sep='\n', mode='a')
    return count

# Run the function
outputdf = pd.DataFrame()
Add_BC_intervel(BC_df, outputdf)

