import requests
from bs4 import BeautifulSoup

def fn_soup(text):
    soup = BeautifulSoup(text, 'lxml')
    items = soup.find_all('div', attrs={'class':'box__item-container'})
    #print(len(items))
    seq = 0
    for i, item in enumerate(items): #enumerate 함수 (인덱스도 같이 사용하고 싶을때) i(index)
        name = item.find('span', attrs={'class':'text__item'})['title']
        price = item.find('strong', attrs={'class':'text text__value'}).get_text()
        rate = item.find('span', attrs={'class':'image__awards-points'})
        if rate:
            rate=rate['style']
            index=rate.find(':') + 1 #index는 :다음부터니까 +1
            #rate=rate[index:] #평점은 index끝까지
            rate=rate[index:-1] # %빼고 숫자만 가져오고 싶을때
        else:
            continue
        
        #피드백 수
        count = item.find('li', attrs={'class':'list-item list-item__feedback-count'})
        if count:
            count= count.find('span', attrs={'class':'text'}).get_text()
            count= count.replace('(', '').replace(')', '').replace(',' , '')
        else:
            continue
        
        if int(rate) >= 90 and int(count) >= 300:
            seq = seq + 1
            print(f'{seq} : {name} : {price} : 평점:{rate} : 피드백수:{count}')

for i in range(1, 6):
    print(i, '-' * 100)
    url='https://browse.gmarket.co.kr/search?keyword={}&k=41&p={}'.format('키보드', i)
    res=requests.get(url)
    res.raise_for_status()
    fn_soup(res.text)