import requests
from bs4 import BeautifulSoup
import json
import streamlit as st

url='http://www.cgv.co.kr/movies/?lt=1&ft=0'
res=requests.get(url)
res.raise_for_status() #오류나면 자동으로 멈추게하는
#print(res.text)

soup = BeautifulSoup(res.text, 'lxml')  #res의 text를 lxml로 파싱해서 문서전체의 결과가  soup에 들어감
#title = soup.title.get_text()
#print(title)
#print(soup.a) # soup에 나오는 첫번째 a태그를 가져오는
#print(soup.a.attrs) #a태그의 속성보기
#print(soup.a['href'])

chart = soup.find('div', attrs={'class':'sect-movie-chart'})
movies = chart.find_all('li')
print(len(movies))

print('-' * 100)

json_movies = []
for movie in movies:
    #예매사이트
    link = 'http://www.cgv.co.kr'
    link = link + movie.find('a', attrs={'class', 'link-reservation'})['href']
    
    #예매율
    percent = movie.find('strong', attrs={'class':'percent'})
    percent = percent.span.get_text()
    
    #포스터
    image = movie.find('img')['src']
    
    #랭킹
    rank = movie.find('strong', attrs={'class':'rank'}).get_text()
    
    #제목
    title=movie.find('strong', attrs={'class':'title'}).get_text()
    #print(rank  + title)
    #print(f'{rank} : {title} : {image} : {percent}')
    
    #결과출력
    # print(f'순위: {rank}')
    # print(f'제목: {title}')
    # print(f'포스터: {image}')
    # print(f'예매율: {percent}')
    # print(f'예매: {link}')
    
    # print('-' * 100)
    
    #json으로 데이터 출력
    json_movie = {'rank': rank, 'title': title, 'image': image, 'percent': percent, 'link': link}
    json_movies.append(json_movie)
    
#print(json_movies)

#movie.json을 파일로 
# with open('movie.json', 'w', encoding='utf-8') as file:
#     json.dump(json_movies, file, indent='\t', ensure_ascii=False) #실행시 왼쪽에 movie.json 파일이 생성됨(한글깨짐은 ensure_ascii=False로 설정)

#print(len(json_movies))

st.set_page_config(layout='wide')
st.header('CGV  무비차트') #실행 -> 터미널에서  streamlit run ex01.py

idx = 0
for row in range(0, 5):
    cols = st.columns(4)
    for col in cols:
        if idx >= 19:
            break
        else:
            movie = json_movies[idx]
            col.image(movie['image'])
            col.write(movie['title'])
            idx += 1
        