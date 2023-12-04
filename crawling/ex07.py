import requests
from bs4 import BeautifulSoup

#url이동
url = 'https://www.google.com/search?q=%EA%B3%A0%EC%9C%A4%EC%A0%95&sca_esv=587611622&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjo0aPOqvWCAxUDB4gKHSYuDPgQ_AUoAXoECAIQAw&biw=1536&bih=747&dpr=1.25'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'}
res = requests.get(url, headers=header)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
images = soup.find_all('div', attrs={'class':'isv-r PNCib ViTmJb BUooTd'})
#print(len(images))

for idx, image in enumerate(images):
    title = image.find('div', attrs={'class':'zbRPDe M2qv4b P4HtKe'}).get_text()
    print(idx + 1, title)

#=> requests로 결과를 가져오는것