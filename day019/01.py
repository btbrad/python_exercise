from tkinter import *
from tkinter import messagebox

# 窗口大小
win_width = 900
win_height = 450

class Application(Frame):

    def __init__(self, master=None, bg_color="#000000"):
        super().__init__(master)
        self.master = master
        self.bg_color = bg_color
        self.x = 0
        self.y = 0
        self.fg_color = "#ff0000"
        self.last_draw = 0 # 最后绘制的图形id
        self.start_draw_flag = False
        self.pack()
        self.create_widget()

    def create_widget(self):
        # 创建绘图区
        self.draw_pad = Canvas(self.master, width=win_width, height=win_height*0.9, bg=self.bg_color)
        self.draw_pad.pack()

        # 创建按钮
        btn_start = Button(self.master, text="开始", name="start")
        btn_start.pack(side="left", padx="10")

        btn_pen = Button(self.master, text="画笔", name="pen")
        btn_pen.pack(side="left", padx="10")

        btn_rect = Button(self.master, text="矩形", name="rect")
        btn_rect.pack(side="left", padx="10")

        btn_clear = Button(self.master, text="清屏", name="clear")
        btn_clear.pack(side="left", padx="10")

        btn_eraser = Button(self.master, text="橡皮擦", name="eraser")
        btn_eraser.pack(side="left", padx="10")

        btn_line = Button(self.master, text="直线", name="line")
        btn_line.pack(side="left", padx="10")

        btn_line_arrow = Button(self.master, text="箭头直线", name="line_arrow")
        btn_line_arrow.pack(side="left", padx="10")

        btn_color = Button(self.master, text="颜色", name="color")
        btn_color.pack(side="left", padx="10")

        # 时间绑定
        btn_pen.bind_class("Button", "<1>", self.event_handler)
        self.draw_pad.bind("<ButtonRelease-1>", self.stop_draw)

    def event_handler(self, event):
        name = event.widget.winfo_name()
        if name == "line":
            self.draw_pad.bind("<B1-Motion>", self.draw_line)

    def draw_line(self, event):
        self.draw_pad.delete(self.last_draw)

        if not self.start_draw_flag:
            self.start_draw_flag = True
            self.x = event.x
            self.y = event.y

        self.last_draw = self.draw_pad.create_line(self.x, self.y, event.x, event.y, fill=self.fg_color)

    def stop_draw(self, event):
        self.start_draw_flag = False
        self.last_draw = 0



if __name__ == "__main__":
    root = Tk()
    root.geometry(f"{win_width}x{win_height}+200+100")
    root.title("画图软件")

    app = Application(master=root)

    root.mainloop()
