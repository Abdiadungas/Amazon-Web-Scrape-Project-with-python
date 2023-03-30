from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import datetime

URL = 'https://www.amazon.nl/gp/bestsellers/?ref_=nav_cs_bestsellers'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","X-Amzn-Trace-Id": "Root=1-642589f4-2e9f95e100423c1d49e3ffa7"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

card1 = soup2.find_all(class_="a-carousel-card")

for card2 in card1:

    title = card2.find(class_="p13n-sc-truncate-desktop-type2").get_text().strip()
    link = card2.find('a').get('href')
    image = card2.find(class_="a-section a-spacing-mini _cDEzb_noop_3Xbw5").img.get('src')
    day = datetime.date.today()
    header = ['Title','Image','link','Date']
    data = [title,image,link,day]


    with open('Amazonlinks.csv','a+',newline='',encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(data)
   
    
    

