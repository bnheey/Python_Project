from tkinter import *

root = Tk()
root.title("Yeonii GUI")  # GUI 지정
root.geometry("640x480")  # 가로 * 세로 - 곱하기 표시할 때 소문자 x
# 뒤에 +로 연결하여 창이 뜨는 x, y 좌표를 지정할 수 있음
# root.geometry("640x480+300+100")

root.resizable(False, False) # x(너비), y(높이) 값 변경 불가(창 크기 변경 불가)


root.mainloop()
