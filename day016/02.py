from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("第一个GUI程序")
root.geometry("500x300+100+200")

btn01 = Button(root)
btn01["text"] = "点击"

btn01.pack()


def click_handler(e):
    messagebox.showinfo("Message", "点击了！")
    print("点击了")


btn01.bind("<Button-1>", click_handler)

root.mainloop()
