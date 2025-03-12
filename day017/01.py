from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widget()

    def create_widget(self):
        self.btn01 = Button(self, text="登录", width=10, anchor="e", command=self.click_handler)
        self.btn01.pack()

        self.label04 = Label(self, text="I\nam\nlearning\n GUI", borderwidth=1, relief="solid", justify="right")
        self.label04.pack()

    def click_handler(self):
        messagebox.showinfo("message", "点击了！")


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x400+200+100")
    root.title("Label测试")

    app = Application(master=root)

    root.mainloop()
