import os, os.path
import sys
import glob
import re
import csv
import pandas as pd

predicted = sys.argv[1]
metadata = sys.argv[2]
output_file = sys.argv[3]

dfList=[]
colname=['predicted']
df = pd.read_csv(predicted, encoding = 'latin1', header = None)
dfList.append(df)
concatDf = pd.concat(dfList, axis =0)
concatDf.columns=colname
concatDf.to_csv(predicted,index = None, encoding = 'utf-8') #appended column and saved as dataframe


dfList2=[]
colname2=['metadata']
df0 = pd.read_csv(metadata , encoding = 'latin1', header = None)
dfList2.append(df0)
concatDf2 = pd.concat(dfList2, axis =0)
concatDf2.columns=colname2
concatDf2.to_csv(metadata ,index = None, encoding = 'utf-8') #appended column and saved as dataframe

df1 = pd.read_csv(predicted)
df2 = pd.read_csv(metadata)

df3 = pd.DataFrame(columns=['match'])
df3['match'] = df1['predicted'].eq(df2['metadata']).replace([True, False], [1,0])
result = pd.concat([df1, df2, df3], axis = 1, sort = False)
result.to_csv(output_file)

#df4 = pd.read_csv("title_output.csv")
#count = df4['title_match'].value_counts()
#print(count)
