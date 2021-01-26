"""
Python Tkinter 绘图项目

@author  : 周华健
@github  : https://github.com/zhouhuajian-course
@version : v1.0
"""
#
import os
from tkinter import *
#
#
class MainWindow(Tk):
    """主窗口"""

    def __init__(self):
        """初始化"""
        super().__init__()
        # 初始化主窗口
        self.init_main_window()

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
#
#
# 创建主窗口
win = MainWindow()
# 进入消息循环
win.mainloop()
