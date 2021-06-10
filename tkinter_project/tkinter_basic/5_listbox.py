from tkinter import *

root = Tk()
root.title("Yeonii GUI")  # GUI 지정
root.geometry("640x480")  # 가로 * 세로 - 곱하기 표시할 때 소문자 x

# selectmode 속성 - single(한개)/extended(여러개)
# height - 0 이라고 하면 리스트 내용 모두 보임, others : 지정한 숫자 만큼만 보임
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # 삭제
    # listbox.delete(0) # 맨 앞 항목을 삭제
    # listbox.delete(END) # 맨 뒤 항목을 삭제

    # 갯수 확인
    print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인 (시작 idx, 끝 idx)
    print("1번째부터 3번째까지 항목 :", listbox.get(0, 2))

    # 선택한 항목 확인(위치로 반환 (ex) (1, 2, 3))
    print("선택된 항목:", listbox.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
