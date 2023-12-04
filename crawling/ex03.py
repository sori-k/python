import requests
from bs4 import BeautifulSoup

url='https://search.daum.net/search?w=tot&q=2022%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text, 'lxml')
images = soup.find_all('img', attrs={'class':'thumb_img'})

for index, image in enumerate(images):
    image_url = image['src']
    print(f'{index} : {image_url}')
    
    image_res = requests.get(image_url)
    res.raise_for_status()
    with open('./movie/movie{}.jpg'.format(index), 'wb') as file:
        file.write(image_res.content)
        