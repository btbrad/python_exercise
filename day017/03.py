from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widget()

    def create_widget(self):
        btn_text = (("MC", "M+", "M-", "MR"),
                    ("C", "±", "÷", "×"),
                    (7, 8, 9, "－"),
                    (4, 5, 6, "＋"),
                    (1, 2, 3, "="),
                    (0, ".")
                    )
        Entry(self).grid(row=0,column=0,columnspan=4,pady=10)
        for index, text in enumerate(btn_text):
            for idx, s in enumerate(text):
                if s == "=":
                    Button(self, text=s).grid(row=index+1, column=idx, sticky="nsew", rowspan=2)
                elif s == 0:
                    Button(self, text=s).grid(row=index+1, column=idx, sticky="nsew", columnspan=2)
                elif s == ".":
                    Button(self, text=s).grid(row=index+1, column=idx+1, sticky="nsew")
                else:
                    Button(self, text=s).grid(row=index + 1, column=idx, sticky="nsew")

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
    root.title("计算器布局")

    app = Application(master=root)

    root.mainloop()
