from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widget()

    def create_widget(self):
        self.photo01 = PhotoImage(file="slogan.gif")
        self.label01 = (Label(self.master, image=self.photo01))
        self.label01.place(x=10, y=50)
        self.label01.bind_class("Label", "<Button-1>", self.click_handler)
    def click_handler(self, event):
        if event.widget.winfo_y() == 50:
            self.label01.place(x=10, y=20)
        else:
            self.label01.place(x=10, y=50)


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x400+200+100")
    root.title("Label测试")

    app = Application(master=root)

    root.mainloop()
