import requests
from bs4 import BeautifulSoup
import csv

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

file = open('시가총액.csv', 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(file)

title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split('\t')
writer.writerow(title)

tbody = soup.find('table', attrs={'class':'type_2'}).find('tbody')
rows = tbody.find_all('tr')
#print(len(rows))

for row in rows:
    cols = row.find_all('td')
    if len(cols) <= 1:
        continue
    data = [col.get_text().strip() for col in cols]
    #print(data)
    writer.writerow(data)
