from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widget()

    def create_widget(self):
        self.label01 = Label(self, text="学习Python", width=10, height=2, fg="white", bg="black")
        self.label01.pack()

        self.label02 = Label(self, text="学习TypeScript", width=10, height=2, fg="yellow", bg="green", font=("黑体", 30))
        self.label02.pack()

        global photo
        photo = PhotoImage(file="slogan.gif")
        self.label03 = Label(self, image=photo)
        self.label03.pack()

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
