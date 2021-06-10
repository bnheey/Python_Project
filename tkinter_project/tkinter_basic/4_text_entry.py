from tkinter import *

root = Tk()
root.title("Yeonii GUI")  # GUI 지정
root.geometry("640x480")  # 가로 * 세로 - 곱하기 표시할 때 소문자 x

txt = Text(root, width=30, height=5)
txt.pack()
# 안내 멘트 insert 가능
txt.insert(END, "글자를 입력하세요")

# 한줄로 값을 입력받을 때 entry 사용
e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력해요!")


def btncmd():
    print(txt.get("1.0", END))  # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()
