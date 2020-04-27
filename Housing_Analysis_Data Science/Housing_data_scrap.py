from bs4 import BeautifulSoup as soup
import  requests
import re
from word2number import w2n
import pandas as pd

response = requests.get('https://www.zameen.com/Houses_Property/Lahore-1-1.html')
Price=[]
Location=[]
Beds=[]
Size = []

#file1 = open("myfile.txt","w") 
#file1.writelines(response.text)
#file1.close
#print(response.text)
data = soup(response.text)
dataa = data.find_all('li',role = 'article')
for info in dataa:
    Pirces = info.find_all('span',class_ = 'f343d9ce')
    Locations = info.find_all('div',class_ = '_162e6469')
    Bedss = info.find_all('span',class_ = 'b6a29bc0')
    Sizes = info.find_all('h2',class_='c0df3811')
    #print(Locations[0].text)
    #print(Pirces[0].text)
    #print(Bedss[0].text)
    Sizes = Sizes[0].text
    sizer = Sizes.split(' ')
    Sizes = str(sizer[0])
    Price.append(Pirces[0].text)
    Location.append(Locations[0].text)
    Beds.append(Bedss[0].text)
    Size.append(Sizes)
'''
print(Price)
print()
print(Location)
print()
print(Beds)
print()
print(Size)
print()
'''
i = 0
for items in Price:
    if(str(items).endswith('Crore')):
        num = items.split(' ')
        number = float(num[0])*pow(10,7)
        Price[i] = number
        i+=1
    else:
        num = items.split(' ')
        number = float(num[0])*pow(10,5)
        Price[i]=number
        i+=1
df = pd.DataFrame(list(zip(Location,Size,Beds,Price)),columns =['Location', 'Size(Marla)','Beds','Price in Pkr']) 
print(df)
df.to_csv('dataset.csv', index=False)
#info = dataa[0]
'''
file1 = open("myfile.txt","w") 
file1.writelines(str(info))
file1.close
#print(response.text)
'''

#print(Size)
#span aria-label = Listing price
#span aria-label = Beds
#span aria-label = Listing price
