# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:11:04 2020

@author: Kshitiz Regmi
"""

from clean_data import clean_data
import pandas as pd

# read dataframe isear
df = pd.read_csv('D:\Fuse taining\ISEAR.csv',names=  ['index','emotions','message'])
df1 = df.copy() # copy values to work on temp dataset
df1.drop(columns =['index'],inplace=True)# drop column index
ob = clean_data() # call clean data class to clean data in dataframe
df1['message'] = df1['message'].apply(lambda msg: ob.get_value(msg)) # call get_value to clean data fraom special strings




print(df1.message.values[0])

