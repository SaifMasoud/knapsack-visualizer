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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.items_table = QtWidgets.QTableWidget(self.centralwidget)
        self.items_table.setObjectName("items_table")
        self.items_table.setColumnCount(0)
        self.items_table.setRowCount(0)
        self.verticalLayout.addWidget(self.items_table)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.done_label = QtWidgets.QLabel(self.centralwidget)
        self.done_label.setObjectName("done_label")
        self.horizontalLayout_3.addWidget(self.done_label)
        self.done_btn = QtWidgets.QPushButton(self.centralwidget)
        self.done_btn.setObjectName("done_btn")
        self.horizontalLayout_3.addWidget(self.done_btn)
        self.size_label = QtWidgets.QLabel(self.centralwidget)
        self.size_label.setObjectName("size_label")
        self.horizontalLayout_3.addWidget(self.size_label, 0, QtCore.Qt.AlignRight)
        self.size_box = QtWidgets.QComboBox(self.centralwidget)
        self.size_box.setObjectName("size_box")
        self.horizontalLayout_3.addWidget(self.size_box)
        self.items_label = QtWidgets.QLabel(self.centralwidget)
        self.items_label.setObjectName("items_label")
        self.horizontalLayout_3.addWidget(self.items_label, 0, QtCore.Qt.AlignRight)
        self.items_box = QtWidgets.QComboBox(self.centralwidget)
        self.items_box.setObjectName("items_box")
        self.horizontalLayout_3.addWidget(self.items_box)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.done_label.setText(_translate("MainWindow", "Press Done to display solution"))
        self.done_btn.setText(_translate("MainWindow", "Done"))
        self.size_label.setText(_translate("MainWindow", "Size"))
        self.items_label.setText(_translate("MainWindow", "Num. Items"))
        self.cleardp_btn.setText(_translate("MainWindow", "Clear Solution"))
from dpqtablewidget import DPQTableWidget
