import os
import shutil

import tkinter as tk
from tkinter import ttk

from bbsWash import *
from bbsNLP import *
from gettop import *
from gui import *
from main import web

def GUI():

    # 工作区创建文件夹
    os.mkdir('ima')
    os.mkdir('csv')

    # 创建主窗口和Frame
    root = tk.Tk()
    # 获取屏幕的宽度和高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # 窗口框架
    root.state('zoomed')
    root.title("未名BBS情绪分析")
    frame = tk.Frame(root)
    frame.pack()

    # 设置窗口主题
    root.style = ttk.Style(root)
    root.style.theme_use('classic')

    # 创建一个文本框
    text = tk.Text(frame, height = screen_height, width = screen_width)
    text.config(font = ("KaiTi", 15), background = "#c2dbf8", foreground = "#d52f9b")
    text.pack(fill = tk.BOTH, expand = True)

    # 统计10个页面
    top10 = gettop()
    # top10 = ['post-read.php?bid=690&threadid=18786764', 'post-read.php?bid=99&threadid=18786633', 'post-read.php?bid=36&threadid=18786273', 'post-read.php?bid=957&threadid=18785563', 'post-read.php?bid=90&threadid=18786711', 'post-read.php?bid=251&threadid=18786746', 'post-read.php?bid=94&threadid=18786342', 'post-read.php?bid=56&threadid=18786322', 'post-read.php?bid=1431&threadid=18786972', 'post-read.php?bid=167&threadid=18786526']
    num = 0
    lst = []
    title = []

    # 收集帖子题目
    title = get_title()

    for i in top10:
        url = 'https://bbs.pku.edu.cn/v2/' + i
        to = 'csv/' + cut(i) + '.csv'
        img = 'ima/' + cut(i) + '.png'

        get(url, to)
        tmp = nlp(to)

        now = web(url, to, num, img, title[num])
        now.values = tmp[:]
        lst.append(now)
        num += 1

    # 制作柱形图
    for i in range(10):
        text.insert(tk.END, "{:25}{:25.3}\t".format(title[i], sum(lst[i].values) / len(lst[i].values)))

        lst[i].button1 = tk.Button(frame, text = "查看统计", command = lst[i].show_image)
        lst[i].button1.config(font = ("KaiTi", 13), background = "pink", foreground = "white")

        lst[i].button2 = tk.Button(frame, text = "查看详情", command = lst[i].show_csv)
        lst[i].button2.config(font = ("KaiTi", 13), background = "purple", foreground = "white")

        lst[i].button3 = tk.Button(frame, text = "查看网站", command = lst[i].show_url)
        lst[i].button3.config(font = ("KaiTi", 13), background = "grey", foreground = "white")

        # 在Text组件中创建一个虚拟窗口，并在这个窗口中放置按钮，尽量不要使用pack()
        text.window_create(tk.END, window = lst[i].button1)
        text.window_create(tk.END, window = lst[i].button2)
        text.window_create(tk.END, window = lst[i].button3)
        text.insert(tk.END, '\n\n')

    # 绑定窗口关闭事件
    root.protocol("WM_DELETE_WINDOW", close_win)
    # 启动事件循环
    root.mainloop()

def close_win():

    # 删除文件夹及其所有内容
    shutil.rmtree('csv')
    shutil.rmtree('ima')

    exit()

if __name__ == '__main__':
    GUI()