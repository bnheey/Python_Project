'''
tkinter를 이용한 메모장 프로그램 만들기

[GUI 조건]
1. title : 제목없음 - windows 메모장
2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
    3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
    3-2. 저장 : mynote.txt 파일에서 현재 내용 저장하기
    3-3. 끝내기 : 프로그램 종료
4. 프로그램 시작 시 본문은 비어있는 상태
5. 하단 status 바는 필요 없음
6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정이 가능해야함
7. 본문 우측에 상하 스크롤바 넣기
'''

from tkinter import *

root = Tk()
root.title("제목없음 - windows 메모장")
root.geometry("640x480")  # 크기 지정

root.resizable(True, True)  # 조건 6 - OK 크기조정이 가능하도록 설정

# 화면 전체에 텍스트 엔트리 배치
txt_box = Text(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
txt_box.pack()

root.mainloop()
