import time
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Yeonii GUI")  # GUI 지정
root.geometry("640x480")  # 가로 * 세로 - 곱하기 표시할 때 소문자 x

# 언제끝날지 모르는 작업 - mode="indeterminate"
progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar.start(10)
progressbar.pack()

# 0 부터 maximun 까지 진행상태 표현
progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar2.start(10)
progressbar2.pack()


def btncmd():
    # 작동 중지
    progressbar.stop()
    progressbar2.stop()

############################################################################
# 시작 버튼을 클릭하였을 때 progress bar - 0% ~ 100% 까지 동작하도록 설정해보기

p_var3 = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var3)
progressbar3.pack()

btn = Button(root, text="중지", command=btncmd)
btn.pack()


def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)

        p_var3.set(i)  # progress bar 의 값 설정
        progressbar3.update()  # ui 업데이트
        print(p_var3.get())

btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()

root.mainloop()
