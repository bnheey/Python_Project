import json

import requests
from bs4 import BeautifulSoup
import time
import secret

KAKAO_TOKEN = secret.kakao_rest_api
send_list=[]

def send_to_kakao(text):
    header = {"Authorization": "Bearer " + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    # url = "https://kapi.kakao.com/v2/api/talk/memo/send?template_id=53949"



    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
    }
    data = {"template_object": json.dumps(post)}

    return requests.post(url, headers=header, data=data)


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

    for data in datas:
        # data 안에 a 가 있으면,
        a_tag = data.select_one('td.title > a')
        title = a_tag.text.strip()
        link = a_tag['href']

        date = data.select_one('td:nth-child(2)').text.strip()

        no = data.select_one("td.no > span.mini_eng")
        if no is not None:
            number = int(no.text.strip())
            if(number > 68):
                send = True
                for s in send_list:
                    if(s['title'] == title):
                        print("보낸적 있음")
                        send = False
                if send :
                    text = f"제목 : {title}\n날짜 : {date}\n\n링크 : {link}"
                    r = send_to_kakao(text)
                    print(r.text)
                    send_list.append({
                        "title" : title,
                        "link" : link,
                        "number" : number,
                        "date" : date
                    })

if __name__ == "__main__":
    # while True:
    #     get_data()
    #     time.sleep(60)
    get_data()