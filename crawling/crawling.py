import pprint

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

response = requests.get(
    'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=129898191&siteId=soft&menuType=T&uId=9&sortChar=A&linkUrl=06-3.html&mainFrame=right',
    headers=headers
)

# print(response.text)
# HTML 데이터 가공
soup = BeautifulSoup(response.text, 'html.parser')
# pprint.pprint(soup)

# select를 이용해서, tr들을 불러오기
datas = soup.select('#board-container > div.list > form:nth-child(2) > table > tbody > tr')
# print(datas)


for data in datas:
    # data 안에 a 가 있으면,
    a_tag = data.select_one('td.title > a')
    title = a_tag.text.strip()
    link = a_tag['href']
    print(link)
    # if a_tag:
    #     rank = movie.select_one('td:nth-child(1) > img')['alt']  # img 태그의 alt 속성값을 가져오기
    #     title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
    #     star = movie.select_one('td.point').text  # td 태그 사이의 텍스트를 가져오기
