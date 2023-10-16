#Import the required library packages
#Getting the BeautifulSoup package for parsing HTML and XML documents
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Setting string type variable to grap the website we need and return it in HTML format
url = 'https://hikinginthesmokys.com/alphabetical-trail-list/'

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

#Now we have to find the exact table we want in the HTML script
my_list = soup.find_all('table')

#Creating a dataframe and using the panda package to read the HTML
df = pd.read_html(str(my_list))[0]
df

#Saving the new df as a csv file
df.to_csv('C:\Users\Bay\Desktop\saved_table.csv', index=False)
