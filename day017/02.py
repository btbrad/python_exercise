from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widget()

    def create_widget(self):
        self.label01 = Label(self, text="用户名")
        self.label01.grid(row=0, column=0, sticky="w")

        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.grid(row=0, column=1)

        self.label02 = Label(self, text="密码")
        self.label02.grid(row=1, column=0, sticky="w")

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show="*")
        self.entry02.grid(row=1, column=1)

        self.btn01 = Button(self, text="登录", command=self.click_handler)
        self.btn01.grid(row=2, column=1)
        self.btn01.grid(row=2, column=1)

    def click_handler(self):
        username = self.entry01.get()
        password = self.entry02.get()
        print("用户名："+username+"\n密码："+password)
        if username == "admin" and password == "123456":
            messagebox.showinfo("message", "登录成功！")
        else:
            messagebox.showinfo("message", "登录失败！用户名或密码错误！")

if __name__ == "__main__":
    root = Tk()
    root.geometry("400x400+200+100")
    root.title("登录页布局")

    app = Application(master=root)

    root.mainloop()
