from window_auto import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem
import knapsack
import sys

# Constants
MAX_SIZE = 10
MAX_ITEMS = 10
DEFAULT_SIZE = 5
DEFAULT_ITEMS = 3
ITEM_HEADERS = ["Name", "Weight", "Value"]


class Window(QMainWindow):
    def __init__(self):
        self.num_items = DEFAULT_ITEMS
        self.ks_size = DEFAULT_SIZE
        self.knapsack = knapsack.KnapSack()
        super().__init__()
        self.title = "KnapSack Visualizer"
        self.initUI()
        self.setGeometry(100, 100, 800, 600)

    def initUI(self):
        # Adding UI widgets to the window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.dp_table.knapsack = self.knapsack

        # Setting up Rows/Cols & values
        self.ui.items_table.setRowCount(DEFAULT_ITEMS)
        self.ui.items_table.setColumnCount(len(ITEM_HEADERS))
        self.ui.items_table.setHorizontalHeaderLabels(ITEM_HEADERS)
        self.ui.dp_table.setRowCount(DEFAULT_SIZE+1)
        self.ui.dp_table.setColumnCount(DEFAULT_ITEMS)
        self.ui.dp_table.setVerticalHeaderLabels([str(i) for i in range(DEFAULT_SIZE + 1)])  # make the rows start at 0->SIZE
        self.ui.dp_table.setHorizontalHeaderLabels([" " + str(i) for i in range(DEFAULT_ITEMS)])
        self.ui.size_box.addItems([str(i) for i in range(1, MAX_SIZE + 1)])
        self.ui.items_box.addItems([str(i) for i in range(1, MAX_ITEMS + 1)])

        # Connecting the buttons to their functions
        self.ui.done_btn.clicked.connect(self.on_done_btn)
        self.ui.cleardp_btn.clicked.connect(self.on_cleardp_btn)
        self.ui.size_box.currentIndexChanged.connect(self.on_size_change)
        self.ui.items_box.currentIndexChanged.connect(self.on_items_change)

    def on_items_change(self):
        self.num_items = self.items_box.currentIndex() + 1
        self.items_table.setRowCount(self.num_items)
        self.dp_table.setColumnCount(self.num_items)

    def on_size_change(self):
        self.ks_size = self.ui.size_box.currentIndex() + 1
        self.ui.dp_table.setRowCount(self.ks_size + 1)
        self.ui.dp_table.setVerticalHeaderLabels([str(i) for i in range(self.ks_size + 1)])
        if self.knapsack.dp:
            # Update solution
            self.ui.dp_table.set_all_0()
            self.knapsack.size = self.ks_size
            self.knapsack.solve()

    def on_cleardp_btn(self):
        self.ui.dp_table.set_all_0()
        QMessageBox.about(
            self,
            "Usage",
            "Row number represents capacity for that row. Columns represent the items (A column can include its own item and any items to its left.). Use Arrow Keys to reveal the solutions.\n\nGreen: Solved\nYellow: Better option\nRed: Worse option.\n\nFollow the yellow from a cell to trace back the solution, straight left means to skip an item and left+up means to take the current item.",
        )

    def on_done_btn(self):
        # Read/Verify data
        print("pressed done")
        names_tableitems = [
            self.ui.items_table.item(r, 0) for r in range(self.ui.items_table.rowCount())
        ]
        weights_tableitems = [
            self.ui.items_table.item(r, 1) for r in range(self.ui.items_table.rowCount())
        ]
        values_tableitems = [
            self.ui.items_table.item(r, 2) for r in range(self.ui.items_table.rowCount())
        ]
        filenames_tableitems = [
            self.ui.items_table.item(r, 3) for r in range(self.ui.items_table.rowCount())
        ]
        print("got data")
        if None in weights_tableitems or None in values_tableitems:
            QMessageBox.about(
                self, "Error", "Please Fill Weights & Values with numbers"
            )
            return
        weights, values = (
            [int(w.data(0)) for w in weights_tableitems],
            [int(v.data(0)) for v in values_tableitems],
        )
        fnames = [
            f.data(0) if f else None for f in filenames_tableitems
        ]  # Default to None if list not specified

        # Solve

        self.knapsack._build_from_lists(weights, values, self.ks_size, fnames)
        self.knapsack.solve()

        # Display in dp_table
        for col in range(self.ui.dp_table.columnCount()):
            for row in range(self.ui.dp_table.rowCount()):
                cur_item = QTableWidgetItem()
                cur_item.setText(str(self.knapsack.dp[row][col]))
                self.ui.dp_table.setItem(row, col, cur_item)

        # Update dp header (Weights Values for each item)
        self.ui.dp_table.setHorizontalHeaderLabels(
            [(f"W: {str(item.weight)} V: {str(item.value)}") for item in self.knapsack.items]
        )

        # Clean
        self.ui.items_table.clearContents()



def main():
    # connect
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()