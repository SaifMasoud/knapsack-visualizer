from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
import knapsack

class win(QWidget):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        # widgets
        self.string1_input = QLineEdit()
        self.string2_input = QLineEdit()
        self.string1_input.setMaxLength(15)
        self.string2_input.setMaxLength(15)
        self.done_btn = QPushButton("Done (CTRL+D)")
        self.done_btn.setShortcut("CTRL+D")
        self.done_btn.clicked.connect(self.on_done_btn)
        # layout
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(QLabel("First sequence: "))
        self.vlayout.addWidget(self.string1_input)
        self.vlayout.addWidget(QLabel("Second sequence: "))
        self.vlayout.addWidget(self.string2_input)
        self.vlayout.addWidget(self.done_btn)
        self.setLayout(self.vlayout)
        self.show()
    
    def on_done_btn(self):
        self.main_window.alg = knapsack.LCS(self.string1_input.text(), self.string2_input.text())
        self.main_window.update_dp_table()
        self.close()
    