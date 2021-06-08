from tkinter import *

root = Tk()
root.title("Yeonii GUI")  # GUI 지정
root.geometry("640x480")

# text label
label1 = Label(root, text = "안녕하세요")
label1.pack()

# image label
photo = PhotoImage(file="img1.png")
label2 = Label(root, image=photo)
label2.pack()

# config -> 클릭 시 text & image label 내용 변경
def change():
    label1.config(text="또 만나요~")

    global photo2
    photo2 = PhotoImage(file = "img2.png")
    label2.config(image=photo2)

btn=Button(root, text="클릭", command=change)
btn.pack()



root.mainloop()
