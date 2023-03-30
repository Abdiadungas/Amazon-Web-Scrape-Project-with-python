from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

import time
import datetime


def Amanzon():
    URL = 'https://www.amazon.nl/TAB-EX-tabletten-stoppen-roken-tagen/dp/B07GMPM93L?ref_=Oct_d_obs_d_16366030031_0&pd_rd_w=QjtLk&content-id=amzn1.sym.9587a357-42c7-43b2-a311-95af6ca6b9c7&pf_rd_p=9587a357-42c7-43b2-a311-95af6ca6b9c7&pf_rd_r=K21EANBC4P2ZCWPHWENN&pd_rd_wg=98mNo&pd_rd_r=f8297185-dbcd-4e52-895f-25d606afcb0c&pd_rd_i=B07GMPM93L'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","X-Amzn-Trace-Id": "Root=1-642589f4-2e9f95e100423c1d49e3ffa7"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text().strip()

    image = soup2.find(id='imgTagWrapperId').img.get('src')

    price = soup2.find(class_="a-offscreen").get_text().strip()

    day = datetime.date.today()


    print(price)

    header = ['Title','Image','Price','Date']
    data = [title,image,price,day]


    with open('AmazonSinglePage.csv','a+',newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
        
while(True):
  Amanzon()
  time.sleep(5)


#df =pd.read_csv(r'E:\new\amazon\AmazonSinglePage.csv')

#print(df)