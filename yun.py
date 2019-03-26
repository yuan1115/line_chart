# -*- coding: utf-8 -*-
# @Author: jmx
# @Date:   2019-03-25 11:13:44
# @Last Modified by:   jmx
# @Last Modified time: 2019-03-26 14:42:35
from wx import App, OK, ICON_INFORMATION, MessageBox
from gui import MyFrame1, dataList
import matplotlib.pyplot as plt
from pylab import *  # 支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']


class yun(MyFrame1):
    # Virtual event handlers, overide them in your derived class
    def sublime(self, event):
        event.Skip()
        hisData = open("data", 'r', encoding='utf-8').read()
        newData = self.m_textCtrl1.GetValue()
        if hisData:
            if newData:
                hisData += "\n"+newData
        else:
            if newData:
                hisData = newData

        open("data", 'w', encoding='utf-8').write(hisData)
        dataList = hisData.replace("；", ';').replace(
            "\r", '').replace(' ', '').strip().split("\n")

        for i in dataList:
            if i.strip() == '':
                dataList.remove(i)

        x = range(len(dataList))
        if len(dataList) <= 3:
            MessageBox(u"数据太少,至少3对数据", "Message",
                       OK | ICON_INFORMATION)
            return False
        names = []
        y = []
        y1 = []
        for i in x:
            if dataList[i].strip() != '':
                dataList[i] = dataList[i].split(";")
                names.append(dataList[i][0])
                y.append(float(dataList[i][1]))
                y1.append(float(dataList[i][2]))
        self.fig = plt.figure(figsize=(13, 7))
        # 数据一
        x = range(len(y))
        if len(y) >= 30:
            startPoint = len(y)-30.0
        else:
            startPoint = 0
        ax1 = plt.subplot(2, 1, 1)
        plt.plot(x, y, marker='', mec='r', mfc='w', label=u'数据1')
        plt.xticks(x, names, rotation=45)
        plt.xlim(startPoint, len(y))
        plt.ylabel("RMSE")  # Y轴标签
        for i in x:
            plt.annotate(y[i], xy=(i, y[i]), xytext=(10, 5), textcoords='offset points', color='red', fontsize=10,
                         arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.10", color='red'))
        # 数据二
        x1 = range(len(y1))
        if len(y1) >= 30:
            startPoint1 = len(y)-30.0
        else:
            startPoint1 = 0
        plt.subplot(2, 1, 2)
        plt.plot(x1, y1, marker='', label=u'数据2')
        plt.xticks(x, names, rotation=45)
        plt.xlim(startPoint1, len(y1))
        plt.ylabel("RMSE")  # Y轴标签
        for i in x1:
            plt.annotate(y1[i], xy=(i, y1[i]), xytext=(10, 5), textcoords='offset points', color='red', fontsize=10,
                         arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.10", color='red'))

        # 鼠标滚动控制缩放
        self.fig.canvas.mpl_connect('scroll_event', self.call_back)
        # 键盘控制移动
        self.fig.canvas.mpl_connect('key_press_event', self.move)
        plt.show()

    def call_back(self, event):
        axtemp = event.inaxes
        x_min, x_max = axtemp.get_xlim()
        fanwei = (x_max - x_min) / 10
        if event.button == 'up':
            axtemp.set(xlim=(x_min + fanwei, x_max - fanwei))
        elif event.button == 'down':
            axtemp.set(xlim=(x_min - fanwei, x_max + fanwei))
        self.fig.canvas.draw_idle()  # 绘图动作实时反映在图像上

    def move(self, event):
        axtemp = event.inaxes
        if event.key == 'left':
            pass
        elif event.key == 'right':
            pass
        self.fig.canvas.draw_idle()

    def listact(self, event):
        event.Skip()
        link = dataList(None)
        link.Show()


if __name__ == '__main__':
    app = App()
    main_win = yun(None)
    main_win.Show()
    app.MainLoop()
