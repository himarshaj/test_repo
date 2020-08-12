# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 03:51:15 2020

@author: Muntabir Choudhury 
"""
import os
import glob
import pandas as pd
import re
# os.chdir(r"advisor")

path = r"C:\Users\jhima\Desktop\Summer2020\LAMP-Sys\Data\Samples\JSON&XML\join_metadata\degree\*.csv"
# extension = 'csv'
# all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# #combine all files in the list
# combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
# print(combined_csv)
# #export to csv
# combined_csv.to_csv( "combined_advisor.csv", index=False, encoding='utf-8')

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

fileList = sorted(glob.glob(path),  key=numericalSort)
dfList=[]
colname=['degree']
#print()

for filename in fileList:
    print(filename)
    df=pd.read_csv(filename, header = None)
    dfList.append(df)
    print(dfList)

concatDf = pd.concat(dfList, axis =0, sort = True)
concatDf.columns=colname
concatDf.to_csv("metadata_degree.csv",index = None)