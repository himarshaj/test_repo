# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:47:53 2020

@author: Muntabir Hasan Choudhury
"""

import csv
import pandas as pd
from nameparser.config import CONSTANTS
from nameparser import HumanName

csvfile = open('pr_author_temp.csv', 'w')        
fieldnames = ('first_name1', 'middle_name1', 'last_name1')
csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
csv_writer.writeheader()
#read the extracted author-names from the clean data and convert data from list to string
with open("pr_author.csv", 'r') as f:
    for lines in f:
        list_string = lines
         #converting author list in string
        def listExtractedString(list_string):
            str1 = ""
            return(str1.join(list_string))
         
         #saved the result of the author list to string convertion
        authorListtoString = listExtractedString(list_string)
        #print(authorListtoString)
        CONSTANTS.string_format = "{first} {middle} {last}"
        name = HumanName(authorListtoString)           
        data = [
                {'first_name1': name.first,
                  'middle_name1': name.middle, 
                  'last_name1': name.last
                  } 
         ]
        for row in data:            
            #csv_writer.writerow(row)
            #print(row)
csvfile.close()

dfList=[]
df=pd.read_csv('pr_author_temp.csv')
dfList.append(df)
concatDf=pd.concat(dfList, axis=0)
concatDf.to_csv('pr_author_updated.csv', index=True)


csvfile = open('mg_author_temp.csv', 'w')
fieldnames = ('first_name2', 'middle_name2', 'last_name2')
csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
csv_writer.writeheader()

with open("mg_author.csv", 'r') as f:
    for lines in f:
        lines = ' '.join(filter(None,lines.split()))
        lines = lines.rstrip('"')
        list_string = lines.lstrip('"')
        #converting author list in string
        def listExtractedString(list_string):
            str1 = ""
            return(str1.join(list_string))         
        #saved the result of the author list to string convertion
        authorListtoString = listExtractedString(list_string)
        #print(authorListtoString)
        lname = authorListtoString.split(" ")[0]
        fmname = authorListtoString.split(" ")[1:]
        fmname = " ".join(fmname)
        last_name2 =  authorListtoString.split(",")[0].strip('"["').strip("'").strip()
        author_fname_mname = authorListtoString.split(",")[-1]
        #CONSTANTS.string_format = "{last} {middle} {first}"
        name = HumanName(fmname)
        fname = name.first
        mname1 = name.middle 
        mname2 = name.last
        mname = mname1 + " " + mname2  
        data1 = [
                 {'first_name2': fname,
                   'middle_name2': mname.lstrip(), 
                   'last_name2': lname
                   } 
          ]
        #print(data1)
        for row in data1:            
            csv_writer.writerow(row)
            #print(row)
        
csvfile.close()

dfList=[]
df=pd.read_csv('mg_author_temp.csv')
dfList.append(df)
concatDf=pd.concat(dfList, axis=0)
concatDf.to_csv('mg_author_updated.csv', index=True)