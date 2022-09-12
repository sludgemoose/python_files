#Import the required library packages
#Getting the BeautifulSoup package for parsing HTML and XML documents
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Setting string type variable to grap the website we need and return it in HTML format
wiki_url = 'https://en.wikipedia.org/wiki/List_of_mass_shootings_in_the_United_States#List_of_mass_shootings_(20th_century)'

response = requests.get(wiki_url)
soup = BeautifulSoup(response.text,'html.parser')

#Now we have to find the exact table we want in the HTML script

my_list = soup.find_all('table')

#Creating a dataframe and using the panda package to read the HTML
df = pd.read_html(str(my_list))[0]
df

#Saving the new df as a csv file
df.to_csv(r'C:\Users\Bay\Desktop\list_of_shootings22.csv', index=False)