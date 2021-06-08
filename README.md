# ⚽ Python TIL⚽

🏈 python의 라이브러리를 이용하여 다양한 프로젝트를 진행해본다.<br>
🏈 2021.05.01 ~ 진행 중<br>

## 🏐 목차 <br>
```shell
- beautifulsoup, requests <scrapping(crawling) project>
- pygame <게임 개발 project>
- pygame 기초 (character, enemy간 충돌 발생 시 게임 종료)
```


## 1. crawling

<details>
  <summary><b>새글 카톡알람 서비스</b></summary><br>

  > crawling/crawling.py 

  > <b>2021.05.21 (完)</b>
  
  beautifulsoup와 requests를 이용한 크롤링에 대하여 학습하였다.<br>한국외국어대학교 소프트웨어 중심대학 사이트 구조를 분석하여 공지사항이 올라올 때 카카오톡 api를 이용하여 내용을 전송 받을 수 있도록 설정하였다.
</details><br>

## 2. pygame<br>

> pygame 라이브러리를 이용한 학습은 유튜브 '나도코딩'님 강좌를 참고하였습니다.<br>

<details>
  <summary><b>pygame을 이용한 간단한 게임</b></summary><br>

  > pygame basic/7_text.py
  
  > <b>2021.05.23 (完)</b>
  
  pygame을 이용하여 character와 enemy가 서로 충돌할 경우 2초 delay -> 게임 종료 하도록 하는 프로젝트를 진행하였다.<br>
  추가로 timer도 세팅하여 화면 좌측 상단에 10초 타이머를 표시하였다.(time out일 때 게임 종료)<br>
  pygame을 이용한 게임 개발 시 기본 틀은 <code>pygame_basic/8_fram.py</code>와 같다.
  <br>
</details><br>
  
<details>
  <summary><b>똥피하기 게임</b></summary><br>

  > pygame_homework/ddong_avoid_game.py
  
  > <b>2021.05.24 (完)</b>
  
  위에서 배운 pygame 기초 개념 및 기본 틀을 이용하여, 실제 게임을 제작해보았다.<br>
  게임은 똥피하기 게임으로, 똥과 캐릭터가 충돌하는 경우 게임은 종료된다. 좌측 상단에 게임이 진행된 시간을 초 단위로 표시한다.<br>
  모든 이미지는 직접 그려 사용하였으며(저작권 본인_heeeon), 실습 내용은 아래와 같다.
  
  <p align="center"><img src="pygame_project/ddong_avoid/images/finished.png"></p>
  <br>
</details>

<details open>
  <summary><b>풍선 쪼개기 게임</b></summary><br>

  > pygame_project/split_balloon_game.py
  
  > <b>2021.05.24 - 2021.05.27 (完)</b>
  
  풍선 쪼개기 프로젝트를 진행하였다. 풍선은 각각 1~4레벨이 있으며 1레벨의 풍선을 터트리면 다음 레벨로 쪼개진다. 4레벨 풍선을 터트린 경우, 풍선은 사라진다.
  <br>life는 3회로 지정되어있고, game over 조건은 아래의 3가지가 있다.
  
  ```shell
  1. 풍선을 모두 터트린 경우(성공) - Mission Complete 문구가 뜬 후 2초 뒤 게임 종료
  2. 풍선에 3회 이상 맞은 경우(실패) - Game Over 문구가 뜬 후 2초 뒤 게임 종료
  3. 100초 안에 Clear하지 못한 경우(실패) - Time Over 문구가 뜬 후 2초 뒤 게임 종료
  ```
  
  모든 이미지는 직접 그려 사용하였으며(저작권 본인_heeeon), 실습 내용은 아래와 같다.
  <p align="center"><img src="pygame_project/split_balloon/images/split_ball_complete.png"></p>
<br>

</details><br>

## 3. tkinter<br>

<code>tkinter</code>은 python 설치시 기본으로 내장되어있는 표준 GUI 라이브러리이다(BUT 유일한 GUI Programming toolkit은 아님). 이는 TCI/TK 위 얇은 객체 지향 레이어 이다.

> tkinter 라이브러리를 이용한 실습은 유튜브 '나도코딩'님 강좌를 참고하였습니다.<br>

<details>
  <summary><b>tkinter</b></summary><br>
</details>

