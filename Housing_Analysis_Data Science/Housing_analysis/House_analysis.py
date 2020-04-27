# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:01:25 2020

@author: Cipher
"""
#Libraries Import
import pandas as pd
import requests
from bs4 import BeautifulSoup 
import seaborn as sns
import matplotlib.pyplot as plt

#load the scrap dataset
dataset = pd.read_csv('D:\Scripting\Professional Projects\Housing_Task\dataset.csv')

#Distribution plot of Price over the dataset
sns.distplot(dataset['Price in Pkr'],bins = 20)

#Distribution plot of Beds over the dataset
sns.distplot(dataset['Beds'],kde=False,bins = 9)

#Beds to Size analysis of houses

plt.figure(figsize=[10,8])

plt.bar(dataset['Size(Marla)'],dataset['Beds'], width = 1.5, color='#0504aa',alpha=0.8)
plt.xlim(min(dataset['Size(Marla)']), max(dataset['Size(Marla)']))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Size',fontsize=15)
plt.ylabel('Beds',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('Normal Distribution Histogram for Size to Beds',fontsize=15)
plt.show()

sns.boxplot(x='Beds',y='Size(Marla)',data = dataset)

Location = []
Price = []
res = {dataset['Location'][i]: dataset['Price in Pkr'][i] for i in range(len(dataset))}
for key in res.keys():
    Location.append(key)
    Price.append(res[key])

#Size to Price analysis via Histogram
plt.figure(figsize=[10,8])

plt.bar(dataset['Size(Marla)'],dataset['Price in Pkr'], width = 1.5, color='#0504aa',alpha=0.8)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Size',fontsize=15)
plt.ylabel('Price',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('Normal Distribution Histogram for Size to Price',fontsize=15)
plt.show()

#Pie chart representation of price to loaction
