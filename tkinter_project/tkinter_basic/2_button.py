from tkinter import *

root = Tk()
root.title("Yeonii GUI")  # GUI 지정

# 버튼 추가
btn1 = Button(root, text="버튼1")
btn1.pack()

# pad -> 버튼 내용(text) 제외하고 여백을 5, 10으로 지정함
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

# width, height ->  pad와 다름. 크기를 직접 지정함
# --> text가 지정한 버튼 크기를 초과하였을때, 내용이 덜 보이더라도 크기는 그대로 유지함
btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

# 버튼 색깔 지정
btn5 = Button(root, fg="red", bg = "yellow", text="버튼5") # fg = foreground / bg = background
btn5.pack()

# 이미지 버튼
photo = PhotoImage(file = "btn6_img.png")
btn6 = Button(root, image=photo)
btn6.pack()

# 버튼에 동작 추가
def btncmd():
    print("버튼이 클릭되었어요!")

btn7 = Button(root, text = "동작하는 버튼", command = btncmd)
btn7.pack()


root.mainloop()
