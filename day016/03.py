from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widget()

    def create_widget(self):
        self.btn01 = Button(self)
        self.btn01["text"] = "点击"
        self.btn01.pack()
        self.btn01["command"] = self.click_handler

        self.btn_quit = Button(self, text="退出", command=root.destroy)
        self.btn_quit.pack()

    def click_handler(self):
        messagebox.showinfo("message", "点击了！")


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x300+200+100")
    root.title("GUI类写法")

    app = Application(master=root)

    root.mainloop()
