import os
import matplotlib.pyplot as plt

from PIL import Image, ImageTk
import webbrowser
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from gui import *

class web:

    def __init__(self, url, to, num, ima, title):

        self.url = url
        self.to = to
        self.num = num
        self.ima = ima
        self.title = title
        self.values = []
        self.button1 = None
        self.button2 = None
        self.button3 = None

    def make_image(self):

        # 设置全局字体
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.size'] = 15
        plt.rcParams['axes.titlesize'] = 15
        plt.rcParams['axes.labelsize'] = 15
        plt.rcParams['xtick.labelsize'] = 15
        plt.rcParams['ytick.labelsize'] = 15
        plt.rcParams['legend.fontsize'] = 15
        plt.rcParams['figure.titlesize'] = 15

        values = self.values

        # 绘制柱状图
        plt.figure(figsize=(10, 6))
        plt.bar([i for i in range(len(values))], values, color='purple')
        plt.style.use('Solarize_Light2')

        # 添加标题和标签
        plt.title(self.title)
        plt.xlabel('楼层', fontsize=20)
        plt.ylabel('情绪值', fontsize=20)
        for i in range(len(self.values)):
            plt.text(i, self.values[i] + 0.001, "{:.2f}".format(self.values[i]), ha='center')

        # 保存柱状图
        plt.savefig(self.ima)

    def show_image(self):

        self.make_image()
        name = self.ima

        x = tk.Toplevel()
        x.title(name)

        image = Image.open(name)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(x, image = photo)
        label.pack()

        x.mainloop()

    def show_csv(self):

        # 创建一个工作簿和工作表
        wb = Workbook()
        ws = wb.active

        # 读取CSV文件
        df = pd.read_csv(self.to)

        # 将CSV数据写入工作表
        for r in dataframe_to_rows(df, index=False, header=True):
            ws.append(r)

        # 保存工作簿
        file_path = re.sub('.csv', '.xlsx', self.to)
        wb.save(file_path)

        # 打开xlsx文件
        os.system('start "" "{}"'.format(file_path))

    def show_url(self):

        webbrowser.open(self.url)

if __name__ == '__main__':
    GUI()