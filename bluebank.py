# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 08:56:04 2022

@author: himanshu.mouli.jha
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

#transafrom to dataframe
loandata = pd.DataFrame(data)

#finding unique values for the purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()

#using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#FICO score
# fico >=300 and < 400: "very poor"
# fico >=400 and fico <= 600 : "poor"
# fico >= 601 and fico <=660 : "fair"
# fico >=660 and fico < 780 : "good"
# fico >= 780: "excellent"

# fico = 700

# if fico >= 300 and fico < 400:
#     ficocat = 'very poor'
# elif fico >= 400 and fico < 600:
#     ficocat = 'poor'
# elif fico >= 601 and fico <= 660:
#     ficocat = 'fair'
# elif fico >= 660 and fico < 700:
#     ficocat = 'good'
# elif fico >= 700:
#     ficocat = 'excellent'
# else:
#     ficocat = 'Unknown'
# print(ficocat)

#applying for loops for loan data

#using first 10

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'very poor'
        elif category >= 400 and category < 600:
            cat = 'poor'
        elif category >= 601 and category < 660:
            cat = 'fair'
        elif category >= 660 and category < 700:
            cat = 'good'
        elif category > 700:
            cat = 'excellent'
        else:
            cat = 'unknown'
    except:
        cat = 'unknown'
    
    ficocat.append(cat)

ficocat = pd.Series(ficocat)
loandata['ficocategory'] =ficocat


#df.loc as conditional statements
#df.loc[df[columnname] condition, newcolumnname] = 'value if condition is met'

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans/rows by fico.category

catplot = loandata.groupby(['ficocategory']).size()
catplot.plot.bar(color = 'green')
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar()
plt.show()

#scatter plot
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint,ypoint,color = 'red')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv',index = True)
















