from tkinter import *

root = Tk()
root.title("Yeonii GUI")  # GUI 지정
root.geometry("640x480")  # 가로 * 세로 - 곱하기 표시할 때 소문자 x

btn1= Button(root, text="버튼1")
btn2= Button(root, text="버튼2")

btn1.grid(row=0, column=0)
btn2.grid(row=1, column=1)
root.mainloop()
