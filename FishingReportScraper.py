#Import the required library packages
#Getting the BeautifulSoup package for parsing HTML and XML documents
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Setting string type variable to grap the website we need and return it in HTML format
fish_url = 'https://littleriveroutfitters.com/pages/fishing/report.htm'

#Grabbing the fishing report table body
response = requests.get(fish_url)
soup = BeautifulSoup(response.text,'html.parser')

fish_report = soup.select('tbody:contains(Sunrise)')

fish_report

