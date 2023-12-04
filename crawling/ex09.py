import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

summary = soup.find('p', attrs={'class':'summary'}).get_text()
print(summary)

#현재온도
temp_text = soup.find('div', attrs={'class':'temperature_text'})
print(temp_text)

summary_list = soup.find('dl', attrs={'class':'summary_list'}).find_all('dd', attrs={'class':'desc'})
print(summary_list)

print('-' * 100)

today_chart = soup.find('ul', attrs={'class':'today_chart_list'}).find('li', attrs={'class':'item_today level2'})
print(today_chart)