# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 08:17:54 2022

@author: himanshu.mouli.jha
"""

import pandas as pd
# file_name = pd.read_csv('file.csv') <--- format of read.csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';')

#summary of the data
data.info()

#playing around with variables
var ='Hello World'
print(var)
var = 39
var = 2.5
var = 'w3f'
var = ['apple','banana','pear']
var1 = ('apple','banana','pear')
var2 = {'Name':'Himanshu','Location':'Ranchi'}

#working with calculations 
#Defining variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operation on Tableau
ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * SellingPricePerItem


# CostPerTransaction Column Calculation
# ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
# Variable = dataframe['columnname']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# Adding a new column to a Data Frame
data['CostPerTransaction'] = CostPerTransaction

# Sales Per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales - Cost)/Cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

roundmarkup = round(data['Markup'],2)

data['Markup'] = roundmarkup

#combining data fields
my_date = 'Day'+'-'+'Month'+'-'+'Year'
 
#Change column data type

day = data['Day'].astype(str)
year = data['Year'].astype(str)

#Checking columns data type
print(day.dtype)

my_date = day + '-'+data['Month'] + '-' + year

data['Date'] = my_date

#using iloc to view specific columns/rows
data.iloc[0] # views the row with index = 0

data.iloc[0:3] #first  3 rows
data.iloc[-5:]
data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all rows on 2nd column

data.iloc[4,3] #brings in 4th row in 3rd column

# using split to split the client keywords field
# new_var = column.str.split('sep',expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

# create new columns for the split columns in Client keywords
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#Using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

# Using the lower function to change item to lower case

data['ItemDescription'] = data['ItemDescription'].str.lower()

#How to merge files

#Bringing in a new data set

seasons = pd.read_csv('value_inc_seasons.csv',sep = ',')

#merging files: merge_df = pd.merge(df_old,df_new,on = 'key')

#df = dataframe
#key stands for common filed in two data

data = pd.merge(data,seasons,on = 'Month')

#Dropping columns
# df = df.drop('columnname',axis = 1)

data = data.drop('ClientKeywords',axis = 1)
data = data.drop('Day',axis = 1)
data = data.drop('Year',axis = 1)
data = data.drop('Month',axis = 1)

#Export into csv
data.to_csv('ValueInc_Cleaned.csv', index = False)





























