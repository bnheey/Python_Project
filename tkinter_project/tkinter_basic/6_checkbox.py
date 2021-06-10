from tkinter import *

root = Tk()
root.title("Yeonii GUI")  # GUI 지정
root.geometry("640x480")  # 가로 * 세로 - 곱하기 표시할 때 소문자 x

chkvar = IntVar()  # chkvar에 int형으로 값을 저장한다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.select()  # default 값 지정(선택됨)
chkbox.deselect()  # default 값 지정(선택 해제 처리)
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable = chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())  # 0 : 선택되지 않음, 1 : 선택됨
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
