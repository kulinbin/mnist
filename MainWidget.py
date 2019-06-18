from PyQt5.Qt import QWidget,QFont
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QLabel,QTableWidgetItem
from PaintBoard import PaintBoard
from MyTable import MyTable

import 分辨数字 as fenb
from 八邻域 import *

from PIL import Image

class MainWidget(QWidget):

    def __init__(self, Parent=None):
        super().__init__(Parent)
        self.__InitData()  # 先初始化数据，再初始化界面
        self.__InitView()

    def __InitData(self):
        self.__paintBoard = PaintBoard(self)
        self.__mytable=MyTable()

    def __InitView(self):
        self.lastResult = '0'
        self.setFixedSize(1250, 700)
        self.setWindowTitle("手写数字识别")

        main_layout = QHBoxLayout(self)  # 新建一个水平布局作为本窗体的主布局
        main_layout.setSpacing(10)  # 设置主布局内边距以及控件间距为10px

        sub_left_layout = QVBoxLayout()  # 新建垂直子布局用于放置按键
        sub_right_layout = QVBoxLayout()

        sub_left_layout.addWidget(self.__mytable)


        self.__l1 = QLabel('在画板上画一个数字')
        sub_right_layout.addWidget(self.__l1)

        sub_right_layout.addWidget(self.__paintBoard)

        self.__btn_Clear = QPushButton("清空画板")
        self.__btn_Clear.setParent(self)  # 设置父对象为本界面

        self.__btn_Clear.clicked.connect(self.__paintBoard.Clear)  # 将按键按下信号与画板清空函数相关联
        sub_right_layout.addWidget(self.__btn_Clear)

        self.__btn_Save = QPushButton("识别")
        self.__btn_Save.setParent(self)
        self.__btn_Save.clicked.connect(self.on_btn_Save_Clicked)
        sub_right_layout.addWidget(self.__btn_Save)

        self.__l2 = QLabel('卷积神经网络识别结果')
        sub_right_layout.addWidget(self.__l2)
        self.__lab_Result1 = QLabel(self.lastResult)
        self.__lab_Result1.setGeometry(100, 100, 100, 100)
        sub_right_layout.addWidget(self.__lab_Result1)

        self.__l3 = QLabel('八邻域神经元识别结果')
        sub_right_layout.addWidget(self.__l3)
        self.__lab_Result2 = QLabel(self.lastResult)
        self.__lab_Result2.setGeometry(100, 100, 100, 100)
        sub_right_layout.addWidget(self.__lab_Result2)

        main_layout.addLayout(sub_left_layout)  # 将子布局加入主布局
        main_layout.addLayout(sub_right_layout)

    def on_btn_Save_Clicked(self):
        image = self.__paintBoard.GetContentAsQImage()

        img=Image.fromqimage(image)

        img=img.resize((28,28),Image.ANTIALIAS)

        c=find_all_loss(img)
        for i in range(len(c[2])):
            self.__mytable.setItem(11,i,QTableWidgetItem(str(c[2][i])))
        for i in range(10):
            self.__mytable.setItem(12,i, QTableWidgetItem(str(i)+'loss '+str(c[0][i])))

        d=str(c[1])

        myimage = img.convert('L')
        tv = list(myimage.getdata())  # 获取图片像素值
        tva = [(255 - x) * 1.0 / 255.0 for x in tv]  # 转换像素范围到[0 1], 0是纯白 1是纯黑
        tva = [tva]
        a = fenb.distinguish(tva)
        b = str(a)
        self.__lab_Result1.setText(b)
        self.__lab_Result2.setText(d)

        return a