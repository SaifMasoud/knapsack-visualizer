# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kslot_knapsack_input.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.size_label = QtWidgets.QLabel(self.centralwidget)
        self.size_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.size_label.setObjectName("size_label")
        self.horizontalLayout_2.addWidget(self.size_label)
        self.size_box = QtWidgets.QComboBox(self.centralwidget)
        self.size_box.setObjectName("size_box")
        self.horizontalLayout_2.addWidget(self.size_box)
        self.num_items_label = QtWidgets.QLabel(self.centralwidget)
        self.num_items_label.setObjectName("num_items_label")
        self.horizontalLayout_2.addWidget(self.num_items_label, 0, QtCore.Qt.AlignRight)
        self.num_items_box = QtWidgets.QComboBox(self.centralwidget)
        self.num_items_box.setObjectName("num_items_box")
        self.horizontalLayout_2.addWidget(self.num_items_box)
        self.slots_label = QtWidgets.QLabel(self.centralwidget)
        self.slots_label.setObjectName("slots_label")
        self.horizontalLayout_2.addWidget(self.slots_label, 0, QtCore.Qt.AlignRight)
        self.slot_box = QtWidgets.QComboBox(self.centralwidget)
        self.slot_box.setObjectName("slot_box")
        self.horizontalLayout_2.addWidget(self.slot_box)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.input_table = QtWidgets.QTableWidget(self.centralwidget)
        self.input_table.setObjectName("input_table")
        self.input_table.setColumnCount(0)
        self.input_table.setRowCount(0)
        self.verticalLayout.addWidget(self.input_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.done_btn = QtWidgets.QPushButton(self.centralwidget)
        self.done_btn.setObjectName("done_btn")
        self.horizontalLayout.addWidget(self.done_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 20))
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
        self.size_label.setText(_translate("MainWindow", "Size"))
        self.num_items_label.setText(_translate("MainWindow", "Num Items"))
        self.slots_label.setText(_translate("MainWindow", "Num. Slots"))
        self.label.setText(_translate("MainWindow", "NOTE: after filling the last cell, press tab or change your selection, otherwise the program thinks you\'re not done."))
        self.done_btn.setText(_translate("MainWindow", "Done (CTRL+D)"))
        self.done_btn.setShortcut(_translate("MainWindow", "Ctrl+D"))
