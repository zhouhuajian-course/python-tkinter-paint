"""
Python Tkinter 绘图项目

@author  : 周华健
@github  : https://github.com/zhouhuajian-course
@version : v1.0
"""

import os
import time
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser, filedialog, messagebox
# 第三方图片处理库pillow
from PIL import ImageGrab


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
        # 初始化画布
        self.canvas = None
        self.canvas_old_x = None
        self.canvas_old_y = None
        self.init_canvas()
        # 初始化画笔大小容器
        # 画笔大小范围控件
        self.pen_size_scale = None
        self.init_pen_size_container()
        # 初始化工具按钮
        self.init_tool_buttons()

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
        self.left_container = Frame(self, padx=10, pady=10)
        self.left_container.pack(side=LEFT, fill=Y)

    def init_pen_color_container(self):
        """颜色容器"""
        pen_color_container = LabelFrame(
            self.left_container, text="画笔", font="宋体 10", padx=9, pady=5
        )
        pen_color_container.pack(side=TOP, fill=X)
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
        row_num = int(len(colors) / 2)
        for row in range(row_num):
            for column in range(2):
                btn = Button(
                    pen_color_container, width=3, bd=2, relief=RIDGE,
                    bg=colors[i],
                    activebackground=colors[i],
                    command=lambda color=colors[i]: self.set_pen_color(color)
                )
                # 网格布局
                btn.grid(row=row, column=column)
                i += 1

    def set_pen_color(self, color):
        """画笔颜色"""
        self.canvas.config(cursor="plus")
        self.pen_color = color

    def init_canvas(self):
        """画布"""
        self.canvas = Canvas(self, bg='white', cursor="plus")
        canvas = self.canvas
        canvas.pack(side=LEFT, fill=BOTH, expand=YES, padx=10, pady=10)
        # 绑定事件
        # 鼠标按下左键
        canvas.bind('<ButtonPress-1>', self.canvas_mouse_press)
        # 按住鼠标左键，并移动（拖动鼠标左键）
        canvas.bind('<Button1-Motion>', self.canvas_mouse_drag)
        # 鼠标左键释放
        canvas.bind('<ButtonRelease-1>', self.canvas_mouse_release)

    def canvas_mouse_press(self, event):
        """鼠标左键按下"""
        self.canvas_old_x = event.x
        self.canvas_old_y = event.y

    def canvas_mouse_release(self, event):
        """鼠标左键释放"""
        self.canvas_old_x = None
        self.canvas_old_y = None

    def canvas_mouse_drag(self, event):
        """鼠标左键拖拽"""
        x = event.x
        y = event.y
        # 画直线
        if self.canvas_old_x and self.canvas_old_y:
            self.canvas.create_line(
                (self.canvas_old_x, self.canvas_old_y),
                (x, y),
                width=self.pen_size_scale.get(),
                fill=self.pen_color,
                capstyle=ROUND  # , smooth=True
            )
        self.canvas_old_x = event.x
        self.canvas_old_y = event.y

    def init_pen_size_container(self):
        """画笔大小"""
        pen_size_container = LabelFrame(self.left_container, text="尺寸", font="宋体 10", pady=3)
        pen_size_container.pack(side=TOP, pady=10, fill=X)
        # 画笔大小 范围控件
        self.pen_size_scale = ttk.Scale(
            pen_size_container, orient='vertical', from_=50, to=1, length=50
        )
        # 默认为5
        self.pen_size_scale.set(5)
        self.pen_size_scale.pack(side=TOP)

    def init_tool_buttons(self):
        """工具按钮"""
        ttk.Button(
            self.left_container, text="背景颜色", command=self.set_canvas_bg_color
        ).pack(side=TOP, pady=3)
        ttk.Button(
            self.left_container, text="橡皮檫", command=self.erase_canvas
        ).pack(side=TOP, pady=3)
        ttk.Button(
            self.left_container, text="清除", command=self.clear_canvas
        ).pack(side=TOP, pady=3)
        ttk.Button(
            self.left_container, text="保存", command=self.save_canvas
        ).pack(side=TOP, pady=3)

    def set_canvas_bg_color(self):
        """设置画布背景颜色"""
        # 询问清除绘图内容
        if messagebox.askokcancel(title="提示", message="修改背景颜色会清除所有已绘制的内容，是否继续？"):
            # 选择颜色对话框。
            # 点击确定，返回RGB数值和十六进制颜色的元组
            # 点击取消或关闭对话返回(None, None)元组
            chosen_colors = colorchooser.askcolor()
            if chosen_colors[1] is not None:
                self.clear_canvas()
                self.canvas.config(bg=chosen_colors[1])

    def erase_canvas(self):
        """擦除画布"""
        self.pen_color = self.canvas['bg']
        self.canvas.config(cursor="dot")

    def clear_canvas(self):
        """清除画布"""
        self.canvas.delete(ALL)

    def save_canvas(self):
        """保存画布"""
        canvas = self.canvas
        # 画布在屏幕中的左上角坐标x1 y1，右下角坐标x2 y2
        x1 = canvas.winfo_rootx()
        y1 = canvas.winfo_rooty()
        canvas.update()
        x2 = x1 + canvas.winfo_width()
        y2 = y1 + canvas.winfo_height()
        # 屏幕截图
        full_screen_image = ImageGrab.grab()
        image = full_screen_image.resize(
            (self.winfo_screenwidth(), self.winfo_screenheight())
        )
        # 图像裁剪
        image = image.crop((x1 + 2, y1 + 3, x2 - 2, y2 - 2))
        # 保存图片
        try:
            datetime = time.strftime("%Y%m%d_%H%M%S")
            # 询问保存文件对话框。如果点击取消或关闭对话框，返回空字符串
            filepath = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                initialfile=f'图片_{datetime}.png'
            )
            if filepath:
                image.save(filepath)
                messagebox.showinfo('保存成功', f'已保存在{filepath}')
        except (ValueError, OSError):
            pass


# 创建主窗口
win = MainWindow()
# 进入消息循环
win.mainloop()
