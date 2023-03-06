from PyQt5.QtWidgets import *
from knapsack_input_GEN import Ui_MainWindow
import knapsack

MAX_SIZE = 10
MAX_ITEMS = 10
DEFAULT_SIZE = 5
DEFAULT_ITEMS = 3
ITEM_HEADERS = ["Name", "Weight", "Value"]

class win(QMainWindow):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUI()
    
    def setupUI(self):
        # Add UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Set defaults
        self.ui.input_table.setRowCount(DEFAULT_ITEMS)
        self.ui.input_table.setColumnCount(len(ITEM_HEADERS))
        self.ui.input_table.setHorizontalHeaderLabels(ITEM_HEADERS)
        self.ui.num_items_box.addItems([str(i) for i in range(1, MAX_ITEMS+1)])
        self.ui.size_box.addItems([str(i) for i in range(1, MAX_SIZE+1)])
        self.ui.size_box.setCurrentIndex(DEFAULT_SIZE-1)
        self.ui.num_items_box.setCurrentIndex(DEFAULT_ITEMS-1)
        # Connect to functions
        self.ui.size_box.currentIndexChanged.connect(self.on_size_change)
        self.ui.num_items_box.currentIndexChanged.connect(self.on_num_items_change)
        self.ui.done_btn.clicked.connect(self.on_done_btn)
        self.show()
    
    def on_done_btn(self):
        names, weights, vals = [], [], []
        for item_row in range(self.ui.input_table.rowCount()):
            names.append(self.ui.input_table.item(item_row, 0).text())
            weights.append(int(self.ui.input_table.item(item_row, 1).text()))
            vals.append(int(self.ui.input_table.item(item_row, 2).text()))
            print("Weights, vals: ", weights, vals)
        self.main_window.alg = knapsack.KnapSack(weights, vals, size=self.ui.size_box.currentIndex()+1, names=names)
        self.close()
        self.main_window.update_dp_table()

    def on_num_items_change(self):
        self.ui.input_table.setRowCount(self.ui.num_items_box.currentIndex() + 1)

    def on_size_change(self):
        self.ui.input_table.setRowCount(self.ui.num_items_box.currentIndex() + 1)
    