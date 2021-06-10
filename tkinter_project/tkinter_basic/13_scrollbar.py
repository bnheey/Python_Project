from tkinter import *

root = Tk()
root.title("Yeonii GUI")  # GUI 지정
root.geometry("640x480")  # 가로 * 세로 - 곱하기 표시할 때 소문자 x

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):
    listbox.insert(END, str(i) + "일")

listbox.pack(side="left")
scrollbar.config(command=listbox.yview)

root.mainloop()
