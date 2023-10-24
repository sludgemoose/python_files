#Import the required library packages
#Getting the BeautifulSoup package for parsing HTML and XML documents
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os.path
from typing import List

#Setting string type variable to grap the website we need and return it in HTML format
URL = 'https://littleriveroutfitters.com/pages/fishing/report.htm'

#Grabbing the fishing report table body
response = requests.get(URL)

soup = BeautifulSoup(response.text,'html.parser')

save_path = "C:/Users/Bay/Documents/Python_Files/FishWebScrape/"

#Finding the specific p class that contains daily information
dailydata = (soup.find('p', attrs={"class": "style22"}).get_text())
dailydata
#Getting rid of the \n's and \t's in the string
to_replace =['\n\t\t\t\t\t\t','\n\t\t\t\t\t\t ','\xa0','  ',' ']
for rep1 in to_replace:
    dailydata = dailydata.replace(rep1, '_')


rep2 = ['__','_']
for r in rep2:
    dailydata = dailydata.replace(r, '_')

#Splitting the string into lists
splitdd = dailydata.split('_')


#Finding the specific division class that contains the report information
reportinfo = (soup.find('div', attrs={"class": "style18"}).get_text())
#Getting rid of \n
reportinfo.replace('\n',' ')
reportinfo = reportinfo.split(' ')
reportinfo



#Finding the specific p class that contains title information for daily data
titles = list(soup.find('p', attrs={"class": "style21"}).get_text())
titles = titles.replace('\n\t\t\t\t\t\t', ' ')

#Putting the daily info into a dataframe
d = {'Date': [reportinfo[3]],
     'Water Temp (Little River)':[splitdd[0] +' degrees Fahrenheit'],
     'Stream Flow Rate':[splitdd[2] + ' Feet ' + splitdd[4] + ' CF/s'],
     'Sunrise':[splitdd[6]],
     'Sunset':[splitdd[7]],
     'Rainfall 2023 YTD Knoxville Apt':[splitdd[8]],
     'Rainfall Normal YTD Knoxville Apt':[splitdd[9]]
}

#Calling data to put into dataframe
df = pd.DataFrame(data=d)
    
print(df)
df.to_csv(save_path + 'output.csv')
