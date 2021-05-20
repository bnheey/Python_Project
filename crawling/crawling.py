import pprint

import requests
from bs4 import BeautifulSoup


def get_data():
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

        date = data.select_one('td:nth-child(2)').text.strip()

        send_data = f"제목 : {title}\n날짜 : {date}\n\n링크 : {link}"
        print(send_data)


if __name__ == "__main__":
    get_data()