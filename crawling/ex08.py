from selenium import webdriver
from bs4 import BeautifulSoup

import time

#=> selenium으로 결과(데이터)를 가져오는 것-> beautifulsoup으로 파싱함

def fn_soup(res):
    soup = BeautifulSoup(res, 'lxml')
    images = soup.find_all('div', attrs={'class':'isv-r PNCib ViTmJb BUooTd'})

    for idx, image in enumerate(images):
        title = image.find('div', attrs={'class':'zbRPDe M2qv4b P4HtKe'}).get_text()
        print(idx + 1, title)

options = webdriver.ChromeOptions()
options.add_argument('headless') #chrome 안나오고 하고 싶을때
options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = 'https://www.google.com/search?q=%EA%B3%A0%EC%9C%A4%EC%A0%95&sca_esv=587611622&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjo0aPOqvWCAxUDB4gKHSYuDPgQ_AUoAXoECAIQAw&biw=1536&bih=747&dpr=1.25'
browser.get(url)


#이전 스크롤 높이
prev_height = browser.execute_script("return document.body.scrollHeight") #처음높이
print('이전높이', prev_height)

while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 밑으로 내려간 높이
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height

res = browser.page_source
fn_soup(res)
time.sleep(2)

