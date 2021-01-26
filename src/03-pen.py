"""
Python Tkinter 绘图项目

@author  : 周华健
@github  : https://github.com/zhouhuajian-course
@version : v1.0
"""

import os
from tkinter import *


class MainWindow(Tk):
    """主窗口"""

    def __init__(self):
        """初始化"""
        super().__init__()
        # 初始化主窗口
        self.init_main_window()
        # 初始化左侧容器
        self.left_container = None
        self.init_left_container()
        # 初始化颜色容器
        self.pen_color = 'black'
        self.init_pen_color_container()

    def init_main_window(self):
        """主窗口"""
        # 隐藏窗口
        self.withdraw()
        # 标题
        self.title("绘图")
        # 图标
        ico_path = 'image/app.ico'
        if os.path.exists(ico_path):
            self.iconbitmap(ico_path)
        # 窗口大小
        self.geometry("800x520")
        # 固定窗口大小
        self.resizable(width=False, height=False)
        # 显示窗口
        self.deiconify()

    def init_left_container(self):
        """左侧容器"""
        # self.left_container = Frame(self, padx=10, pady=10, bg="red")
        self.left_container = Frame(self, padx=10, pady=10)
        # self.left_container.pack(side=LEFT, fill=Y)
        self.left_container.pack(side=LEFT, fill=Y)
        # Label(self.left_container, text="测试左侧容器").pack()

    def init_pen_color_container(self):
        """颜色容器"""
        pen_color_container = LabelFrame(
            self.left_container, text="画笔", font="宋体 10", padx=9, pady=5
        )
        pen_color_container.pack(side=TOP, fill=X)
        # Label(pen_color_container, text="测试一下").pack()
        colors = [
            # 黑、白
            'black', 'white',
            # 红、橙、黄、绿、蓝、靛、紫
            'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple',
            # 灰、淡黄色、淡蓝色、粉色、青色
            'gray', 'lightyellow', 'lightblue', 'pink', 'cyan'
        ]
        # 生成画笔颜色按钮
        i = 0
        # row_num = int(len(colors) / 2)
        # row_num = 7
        for row in range(7):
            for column in range(2):
                btn = Button(
                    pen_color_container,
                    width=3,  # 不是3像素，3个字符的长度
                    bd=2,
                    relief=RIDGE,  # 按钮的3D样式 山岭
                    bg=colors[i],
                    activebackground=colors[i],
                    command=lambda color=colors[i]: self.set_pen_color(color)
                )
                # 网格布局
                btn.grid(row=row, column=column)
                i += 1

    def set_pen_color(self, color):
        """画笔颜色"""
        self.pen_color = color
        print(f'{ self.pen_color = }')


# 创建主窗口
win = MainWindow()
# 进入消息循环
win.mainloop()
