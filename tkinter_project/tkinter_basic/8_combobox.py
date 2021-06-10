from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Yeonii GUI")  # GUI 지정
root.geometry("640x480")  # 가로 * 세로 - 곱하기 표시할 때 소문자 x

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")  # 최초 목록 제목 설정

# state 를 readonly 라고 지정하여 별도의 값 입력을 방지한다.
readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0)  # 0번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get())  # 선택된 값 출력
    print(readonly_combobox.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()
