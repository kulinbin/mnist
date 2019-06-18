from PyQt5.QtWidgets import *

class MyTable(QTableWidget):

    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)

        self.resize(750, 240)
        self.setColumnCount(8)
        self.setRowCount(14)
        #设置表格有两行五列。
        self.table()

    def table(self):
        columnWidth=80
        all_number_eight = [[0.154, 0.192, 0.462, 0.192, 0.154, 0.192, 0.462, 0.192],
                            [0.0, 0.071, 0.786, 0.071, 0.0, 0.071, 0.786, 0.071],
                            [0.318, 0.364, 0.136, 0.136, 0.318, 0.364, 0.136, 0.136],
                            [0.25, 0.375, 0.042, 0.292, 0.25, 0.375, 0.042, 0.292],
                            [0.25, 0.25, 0.417, 0.125, 0.25, 0.25, 0.417, 0.125],
                            [0.458, 0.25, 0.125, 0.125, 0.458, 0.25, 0.125, 0.125],
                            [0.259, 0.296, 0.259, 0.185, 0.259, 0.296, 0.259, 0.185],
                            [0.278, 0.278, 0.333, 0.056, 0.278, 0.278, 0.333, 0.056],
                            [0.25, 0.286, 0.25, 0.25, 0.25, 0.286, 0.25, 0.25],
                            [0.36, 0.24, 0.24, 0.2, 0.36, 0.24, 0.24, 0.2]]
        for i in range(len(all_number_eight)):
            for j in range(len(all_number_eight[0])):
                self.setItem(i, j, QTableWidgetItem(str(all_number_eight[i][j])))

        # self.setColumnWidth(0,columnWidth)
        #添加表格的文字内容.
        self.setHorizontalHeaderLabels(["0度", "45度", "90度", "135度", "180度", "225度", "270度", "315度"])
        self.setVerticalHeaderLabels(["标准0激活频率","标准1激活频率","标准2激活频率","标准3激活频率","标准4激活频率","标准5激活频率","标准6激活频率","标准7激活频率","标准8激活频率","标准9激活频率",'  ','未知数激活率','损失','损失'])
        #设置表头
        lbp = QLabel()
        self.setCellWidget(1,1,lbp)


