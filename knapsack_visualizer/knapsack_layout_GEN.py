# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knapsack_layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        self.alg_box = QtWidgets.QComboBox(self.centralwidget)
        self.alg_box.setObjectName("alg_box")
        self.horizontalLayout_6.addWidget(self.alg_box)
        self.alg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.alg_btn.setObjectName("alg_btn")
        self.horizontalLayout_6.addWidget(self.alg_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.dp_table = DPQTableWidget(self.centralwidget)
        self.dp_table.setObjectName("dp_table")
        self.dp_table.setColumnCount(0)
        self.dp_table.setRowCount(0)
        self.verticalLayout.addWidget(self.dp_table)
        self.cleardp_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cleardp_btn.setObjectName("cleardp_btn")
        self.verticalLayout.addWidget(self.cleardp_btn)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KnapSack Visualizer"))
        self.label.setText(_translate("MainWindow", "Choose your algorithm: "))
        self.alg_btn.setText(_translate("MainWindow", "Click To Solve."))
        self.label_2.setText(_translate("MainWindow", "NOTE: Use Arrow Keys to move around table. Mouse clicks are ignored when visualizing the solutions."))
        self.cleardp_btn.setText(_translate("MainWindow", "Clear Solution"))
from dpqtablewidget import DPQTableWidget
