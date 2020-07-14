import os, os.path
import sys
import glob
import re
import csv
import pandas as pd

predicted = sys.argv[1]
metadata = sys.argv[2]
output_file = sys.argv[3]

# predicted = "pr_author_updated.csv"
# metadata = "mg_author_updated.csv"
# output_file = "author.csv"

df1 = pd.read_csv(predicted)
df2 = pd.read_csv(metadata)

df3 = pd.DataFrame(columns=['first_name_status'])
df3['first_name_status'] = df1['first_name1'].eq(df2['first_name2']).replace([True, False], ['1', '0'])
df4 = pd.DataFrame(columns=['middle_name_status'])
df4['middle_name_status'] = df1['middle_name1'].eq(df2['middle_name2']).replace([True, False], ['1', '0'])
df5 = pd.DataFrame(columns=['last_name_status'])
df5['last_name_status'] = df1['last_name1'].eq(df2['last_name2']).replace([True, False], ['1', '0'])

result = pd.concat([df1, df2, df3, df4, df5], axis = 1, sort = False)
result.to_csv("temp.csv")
#print(result)
df6 = pd.read_csv("temp.csv", usecols = ['first_name1','middle_name1','last_name1','first_name2','middle_name2','last_name2','first_name_status','middle_name_status','last_name_status'])
#print(df6)
matched = df6['first_name_status'].eq(df6['last_name_status']).replace([True, False], ['1', '0'])
df6['matched'] = matched
df6.to_csv(output_file)

