import sys
from knapsack_layout_GEN import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt5 import QtWidgets
from alg_input_windows import *
import alg_input_windows

# Constants
ALG_TO_WIN = {"knapsack": knapsack_input_window.win, "lcs": lcs_input_window.win, "k_knapsack": kslot_knapsack_input_window.win}

class Window(QMainWindow):
    def __init__(self):
        self.alg = None
        super().__init__()
        self.title = "KnapSack Visualizer"
        self.initUI()
        self.setGeometry(100, 100, 800, 600)

    def initUI(self):
        # Adding UI widgets to the window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dp_table.window = self
        self.ui.alg_box.addItems(ALG_TO_WIN)

        # Connecting the buttons to their functions
        self.ui.alg_btn.clicked.connect(self.on_alg_btn)
        self.ui.cleardp_btn.clicked.connect(self.on_cleardp_btn)

    def on_alg_btn(self):
        chosen_alg_name = self.ui.alg_box.currentText()
        self.inputwin = ALG_TO_WIN[chosen_alg_name](self)

    def on_cleardp_btn(self):
        self.ui.dp_table.set_all_0()
        QMessageBox.about(
            self,
            "Usage",
            "Row number represents capacity for that row. Columns represent the items (A column can include its own item and any items to its left.). Use Arrow Keys to reveal the solutions.\n\nLight Gray: Solved\nYellow: Better option\nRed: Worse option.\n\nFollow the yellow from a cell to trace back the solution, straight left means to skip an item and left+up means to take the current item.",
        )

    def update_dp_table(self):
        self.ui.dp_table.setColumnCount(len(self.alg.gui_horizontal_headers))
        self.ui.dp_table.setRowCount(len(self.alg.gui_vert_headers))
        self.ui.dp_table.setHorizontalHeaderLabels(self.alg.gui_horizontal_headers)
        self.ui.dp_table.setVerticalHeaderLabels(self.alg.gui_vert_headers)
        self.ui.dp_table.set_all_0()

        # Display solution in dp_table
        for col in range(self.ui.dp_table.columnCount()):
            for row in range(self.ui.dp_table.rowCount()):
                cur_item = QTableWidgetItem()
                cur_item.setText(self.alg.get_cell_value(row, col))
                self.ui.dp_table.setItem(row, col, cur_item)

def main():
    # connect
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()