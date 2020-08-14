# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 13:46:29 2020

@author: Muntabir Hasan Choudhury
"""
#import libraries
import os, os.path
import glob
import re
import csv
import nltk.data
import nltk
from nltk.tokenize import sent_tokenize
import pandas as pd
from nameparser.config import CONSTANTS
from nameparser import HumanName

#create nltk_data directory in the root
mypath = os.path.expanduser("~/nltk_data")

#check to see if the folder exist or not
if not os.path.exists(mypath):
    os.mkdir(mypath)
    print('Folder Created!')

else:
    print("Folder exists")
    
#check to see the validity of the existance of the folder
varbool = mypath in nltk.data.path
#print(varbool)

#printing the textfile which exist in the custom nltk corpus
path = r'C:\Users\jhima\nltk_data\*.txt'

mypath = os.path.expanduser("~/nltk_data")
#print(mypath)


numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


files = sorted(glob.glob(path), key=numericalSort)

csvfile = open('degree_extracted.csv', 'w')
csv_writer = csv.writer(csvfile)


for name in files:
        with open(name) as f:
            directory = os.path.split(name)
            document = nltk.data.load(directory[1])
            
            #tokenize the sentence
            sent_tokens = sent_tokenize(document)
            #normalize the sentence
            sent_tokens = [sent.lower() for sent in sent_tokens]
            
            #converting tokens to a string
            def listToString(sent_tokens):
                _string = " "
                return(_string.join(sent_tokens))
                
            tokenized_string = listToString(sent_tokens)

            #extracting degree from each text document
            degree_data = re.compile(r'(degree(s)? of)(\n?|.+?|\n)(\w.+|\w?.+\n.+)')
            
            def matched(tokenized_string):
                degree = degree_data.match(tokenized_string) #giving the none values
                degree = degree_data.search(tokenized_string) #searching for the values which has a match
                if degree is None:
                    return " "
                return degree.group(4).strip() #the 4th capturing group which is a value (i.e degree) will be returned
            
            check = matched(tokenized_string)
            stopwords = ['\n', 'shipping', 'and', 'shipbuilding', 'management', 'at', 'the', 'at', 'the', 'massachusetts', 'institute', '.',
                         'technology.', 'technology', 'submitted', 'by________________', 'on', 'august', '30,', '1954', 'mechanical', 'engineering']
            key = check.split() #spliting the strings
            #print(key)
            resultwords = [word for word in key if word not in stopwords] #iterating through words in each row and checking the stopwords that needs to be removed
            result = ' '.join(resultwords).rstrip('of').strip() #joining the words with a space after removing the stopwords
  
            
            #print(result)
            
            degree_data = []
            degree_data.append(result)
            #print(degree_data)
                    
            
        csv_writer.writerow(degree_data)

csvfile.close()
#add a column name to the extracted author names
dfList=[]
colname=['extracted_degree']
df = pd.read_csv("degree_extracted.csv", header = None, encoding = "ISO-8859-1")
dfList.append(df)
concatDf = pd.concat(dfList, axis =0)
concatDf.columns=colname
concatDf.to_csv("extracted_degree.csv",index = None, encoding = "ISO-8859-1")

"""
(degree(s)? of)(\n(\w[^\n]*$))|(degree(s)? of)(.+\n\w+$)|(degree(s)? of)(.+)
(degree(s)? of)(\n?|.+\n)(\w.+)
(degree(s)? of)(\n?|.+?|\n)(\w.+|\w?.+\n.+) -- final one

https://regex101.com/r/kX5EcM/1
"""
#
f1 = open("degree_appendix.csv", 'r', encoding = "ISO-8859-1")
reader = csv.reader(f1)
print(reader)
##f2 = open("extracted_degree.csv", 'r', encoding = "ISO-8859-1")
##reader1 = csv.reader(f2)
#
#def dict_degree():
#    deg_appendix = {}
#    for row in reader:
#        deg_appendix.append(row[0]:row[1])
#    return deg_appendix
#
#dict_check = dict_degree()
#print(dict_check)
        
#reading the degree appendix file as a dictionary
def dict_degree():
    degree_appendix = {}
    for row in reader:
        degree_appendix[row[0]] = row[1]
    return degree_appendix

dict_check = dict_degree()
print(dict_check)

df = pd.read_csv("extracted_degree.csv", encoding = "ISO-8859-1")
frame = pd.DataFrame(df)
#print(frame)

#mapping a dictionary to a dataframe
frame['extracted_degree'] = frame['extracted_degree'].map(dict_check)
frame.to_csv("extracted_degree-mapped.csv", index = None)
#print(frame)

df1 = pd.read_csv("extracted_degree-mapped.csv")
frame1 = pd.read_csv("degree_metadata.csv")
df2 = pd.DataFrame(frame1)

df3 = pd.DataFrame(columns=['degree_match'])
df3['degree_match'] = df1['extracted_degree'].eq(df2['degree']).replace([True, False], ['1', '0'])

result = pd.concat([df1, df2, df3], axis = 1, sort = False)
result.to_csv("degree_output.csv")

df4 = pd.read_csv("degree_output.csv")
count = df4['degree_match'].value_counts()
print(count)

# #Remove intermediate files
# os.remove("extracted_degree.csv")
# os.remove("extracted_degree-mapped.csv")

#dfList=[]
#colname=['degree_major', 'abb']
#frame = pd.read_csv("degree_appendix.csv", header = None)
#dfList.append(frame)
#concatDf = pd.concat(dfList, axis =0)
#concatDf.columns=colname
#concatDf.to_csv("degree_appendix-v1.csv",index = None)
#
#frame1 = pd.read_csv("degree_appendix-v1.csv")
#frame2 = pd.read_csv("extracted_degree.csv")   


##unpacking the keys and values and save the key result
#def key_check(dict_data):
#    keys = [key for key, value in dict_check.items()]
#    if keys is not None:
#        return keys
#    
#key_result = key_check(dict_check)
#
##unpacking the keys and values and save the value result
#def value_check(dict_data):
#    values = [value['abb'] for key, value in dict_check.items()]
#    if values is not None:
#        return values
#
#value_result = value_check(dict_check)
##print(value_result)
#
#df1 = pd.read_csv("extracted_degree.csv")
#df2 = df1['extracted_degree'].all()

        
    

#df = pd.read_csv("extracted_degree.csv")
#frame = df
#
#def check(degree):
#    dict_degree = degree_appendix
#    if dict_degree:
#        return dict_degree[

    