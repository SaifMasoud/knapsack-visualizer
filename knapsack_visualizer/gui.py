import sys
from knapsack_layout_GEN import Ui_MainWindow
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QTableWidgetItem,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from alg_input_windows import *
import alg_input_windows

# Constants
ALG_TO_WIN = {
    "Longest Common Subsequence": lcs_input_window.win,
    "knapsack": knapsack_input_window.win,
    "k_knapsack": kslot_knapsack_input_window.win,
}
SPEED = 250


class Window(QMainWindow):
    def __init__(self):
        self.alg = None
        super().__init__()
        self.title = "KnapSack Visualizer"
        self.initUI()
        self.setGeometry(100, 100, 800, 600)
        self.paused = False

    def event(self, e):
        super().event(e)
        if self.alg:
            self.ui.status_lbl.setText("Status: Ready (click show solution below).")
            self.ui.status_lbl.setStyleSheet("color: green;")
            return True
        return True

    def initUI(self):
        # Adding UI widgets to the window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dp_table.window = self
        self.ui.alg_box.addItems(ALG_TO_WIN)

        # Connecting the buttons to their functions
        self.ui.alg_btn.clicked.connect(self.on_alg_btn)
        self.ui.cleardp_btn.clicked.connect(self.on_cleardp_btn)
        self.ui.show_sol_btn.clicked.connect(self.on_show_sol_btn)
        self.ui.pause_btn.clicked.connect(self.on_pause_btn)
        self.ui.step_back_btn.clicked.connect(self.on_step_back_btn)

    def on_step_back_btn(self):
        self.paused = True
        row, col = self.prev_dp_cell()
        print(f"on_back: trying to reveal {row, col}")
        self.ui.dp_table.reveal(row, col)

    def on_pause_btn(self):
        self.paused = not self.paused
        self.on_show_sol_btn()

    def on_alg_btn(self):
        chosen_alg_name = self.ui.alg_box.currentText()
        self.inputwin = ALG_TO_WIN[chosen_alg_name](self)
        self.ui.dp_table.reset_dp()

    def on_cleardp_btn(self):
        self.ui.dp_table.set_all_0()
        self.ui.dp_table.cur_rowcol = (0, 0)
        QMessageBox.about(
            self,
            "Usage",
            "Row number represents capacity for that row. Columns represent the items (A column can include its own item and any items to its left.). Use Arrow Keys to reveal the solutions.\n\nLight Gray: Solved\nYellow: Better option\nRed: Worse option.\n\nFollow the yellow from a cell to trace back the solution, straight left means to skip an item and left+up means to take the current item.",
        )

    def on_show_sol_btn(self):
        """ Shows solution step-by-step. """
        if self.paused:
            return
        self.ui.dp_table.setColumnCount(len(self.alg.gui_horizontal_headers))
        self.ui.dp_table.setRowCount(len(self.alg.gui_vert_headers))
        self.ui.dp_table.setHorizontalHeaderLabels(self.alg.gui_horizontal_headers)
        self.ui.dp_table.setVerticalHeaderLabels(self.alg.gui_vert_headers)

        # Display solution in dp_table
        while self.next_dp_cell():
            if self.paused:
                return
            print(f"on_show: Trying to reveal at {self.next_dp_cell()}")
            row, col = self.next_dp_cell()
            speed = 2000 // self.ui.speed_slider.value()
            self.ui.dp_table.reveal(row, col)
            loop = QEventLoop()
            QTimer.singleShot(speed, loop.quit)
            loop.exec_()

    def prev_dp_cell(self):
        if not self.ui.dp_table.cur_rowcol:
            return
        row, col = self.ui.dp_table.cur_rowcol
        self.ui.dp_table.setItem(row, col, QTableWidgetItem("0"))
        if 0 <= row - 1:
            return (row - 1, col)
        elif 0 <= col - 1:
            return (self.ui.dp_table.rowCount() - 1, col - 1)
        return (0, 0)

    def next_dp_cell(self, reverse=False):
        if not self.ui.dp_table.cur_rowcol:
            self.ui.dp_table.set_all_0()
            return (0, 0)
        row, col = self.ui.dp_table.cur_rowcol
        if 0 <= row + 1 < self.ui.dp_table.rowCount():
            print(f"NEXT CELL: {row+1, col}")
            return (row + 1, col)
        elif 0 <= col + 1 < self.ui.dp_table.columnCount():
            print(f"NEXT CELL: {0, col+1}")
            return (0, col + 1)
        return None

    def update_dp_table(self):
        pass  # Deprecated function


def main():
    # connect
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
