import sys

# from PyQt5.QtWidgets import *, QHBoxLayout, Q
from PyQt5.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QPushButton,
    QComboBox,
    QWidget,
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QMessageBox,
)
from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QEvent
import knapsack

KS = knapsack.KnapSack()
MAX_SIZE = 10
MAX_ITEMS = 10
SIZE = 5
NUM_ITEMS = 3
ITEM_HEADERS = ["Name", "Weight", "Value"]


def widgets_to_QHBoxLayout(widgets):
    hbox = QHBoxLayout()
    for widget in widgets:
        hbox.addWidget(widget)
    return hbox


class DPQTableWidget(QTableWidget):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.highlighted = []
        self.cur = None
        self.setVerticalHeaderLabels([str(i) for i in range(SIZE + 1)])  # make the rows start at 0->SIZE
        self.setHorizontalHeaderLabels([" " + str(i) for i in range(NUM_ITEMS + 1)])

    def event(self, e):
        super().event(e)
        if e.type() != QEvent.MouseButtonRelease and e.type() != QEvent.KeyPress:
            return True
        # Reveal
        if self.hasFocus() and self.selectedItems():
            print(
                "\nrevealing",
                self.selectedItems()[0].row(),
                self.selectedItems()[0].column(),
            )
            print("Was Highlighted: ", self.highlighted)
            selected = self.selectedItems()[0]
            if selected:
                self.reveal(selected)
            print("Now Highlighted: ", self.highlighted)
        return True

    def reveal(self, selected):
        if self.cur:
            if selected is self.cur:
                print("Same item")
                return
        row, col = selected.row(), selected.column()

        # Clean up: if there was another item revealed, unmark its parents
        if (self.cur and selected != self.cur):  
            self.unhighlight()

        # Reveal & highlight parents
        selected.setBackground(QColor("Green"))
        selected.setText(str(KS.dp[row][col]))
        self.cur = selected
        pars = self.table_pars(selected)
        self.highlight(pars)
        self.highlighted.extend(pars)

    def unhighlight(self):
        try:
            if self.highlighted:
                for par in self.highlighted:
                    par.setBackground(QColor("Green"))
                    # par.setBackground(QColor("White"))
                self.highlighted = []
        except RuntimeError:  # Usually is the item being deleted due to new items
            self.highlighted = []

    def table_pars(self, selected):
        row, col = selected.row(), selected.column()
        try:
            par1_r, par1_c = KS.dp_parents(row, col)[0]
            par2_r, par2_c = KS.dp_parents(row, col)[1]
            par1 = self.item(par1_r, par1_c)
            par2 = self.item(par2_r, par2_c)
            pars = par1, par2
            return [par for par in pars if par is not None]
        except TypeError:  # means there is only 1 par
            row, col = KS.dp_parents(row, col)
            return [self.item(row, col)]

    def highlight(self, pars):
        for par in pars:
            par.setText(str(KS.dp[par.row()][par.column()]))
        if not pars:
            return
        if len(pars) == 1:
            pars[0].setBackground(QColor("Yellow"))
            return

        par1, par2 = pars[0], pars[1]
        # par 2 is *taken* in KS.dp
        par2_score = (
            KS.dp[par2.row()][par2.column()] + KS.items[self.cur.column()].value
        )
        par1_score = KS.dp[par1.row()][par1.column()]

        if par2_score > par1_score:
            par2.setBackground(QColor("Yellow"))
            par1.setBackground(QColor("Red"))
        else:
            par2.setBackground(QColor("Red"))
            par1.setBackground(QColor("Yellow"))

    def set_all_0(self):
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                zero_item = QTableWidgetItem()
                zero_item.setText("0")
                self.setItem(row, col, zero_item)
                self.item(row, col).setBackground(QColor("White"))


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "KnapSack Visualizer"
        self.initUI()
        self.setGeometry(100, 100, 800, 600)

    def initUI(self):
        # Creating our widgets
        self.items_table = QTableWidget(NUM_ITEMS, len(ITEM_HEADERS))
        self.items_table.setHorizontalHeaderLabels(ITEM_HEADERS)
        self.done_label = QLabel("Press Done To Show Solution")
        self.done_btn = QPushButton("Done")
        self.size_label = QLabel("Size")
        self.size_box = QComboBox()
        self.size_box.addItems([str(i) for i in range(1, MAX_SIZE + 1)])
        self.items_label = QLabel("Num. Items")
        self.items_box = QComboBox()
        self.items_box.addItems([str(i) for i in range(1, MAX_ITEMS + 1)])
        self.middle_row = widgets_to_QHBoxLayout(
            [
                self.done_label,
                self.done_btn,
                self.size_label,
                self.size_box,
                self.items_label,
                self.items_box,
            ]
        )

        self.dp_table = DPQTableWidget(SIZE + 1, NUM_ITEMS + 1)
        self.cleardp_btn = QPushButton("Clear Solution")

        # Gathering the widgets in layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.items_table)
        self.layout.addLayout(self.middle_row)
        self.layout.addWidget(self.dp_table)
        self.layout.addWidget(self.cleardp_btn)

        # Connecting the buttons to their functions
        self.done_btn.clicked.connect(self.on_done_btn)
        self.cleardp_btn.clicked.connect(self.on_cleardp_btn)
        self.size_box.currentIndexChanged.connect(self.on_size_change)
        self.items_box.currentIndexChanged.connect(self.on_items_change)

        # Adding our widgets to the window then showing the window
        self.setLayout(self.layout)
        self.show()

    def on_items_change(self):
        global NUM_ITEMS
        NUM_ITEMS = self.items_box.currentIndex() + 1
        self.items_table.setRowCount(NUM_ITEMS)
        self.dp_table.setColumnCount(NUM_ITEMS + 1)

    def on_size_change(self):
        global SIZE
        SIZE = self.size_box.currentIndex() + 1
        self.dp_table.setRowCount(SIZE + 1)
        self.dp_table.setVerticalHeaderLabels([str(i) for i in range(SIZE + 1)])
        if KS.dp:
            # Update solution
            self.dp_table.set_all_0()
            KS.size = SIZE
            KS.solve()

    def on_cleardp_btn(self):
        self.dp_table.set_all_0()
        QMessageBox.about(
            self,
            "Usage",
            "Row number represents capacity for that row. Columns represent the items (A column can include its own item and any items to its left.). Use Arrow Keys to reveal the solutions.\n\nGreen: Solved\nYellow: Better option\nRed: Worse option.\n\nFollow the yellow from a cell to trace back the solution, straight left means to skip an item and left+up means to take the current item.",
        )

    def on_done_btn(self):
        # Read/Verify data
        print("pressed done")
        names_tableitems = [
            self.items_table.item(r, 0) for r in range(self.items_table.rowCount())
        ]
        weights_tableitems = [
            self.items_table.item(r, 1) for r in range(self.items_table.rowCount())
        ]
        values_tableitems = [
            self.items_table.item(r, 2) for r in range(self.items_table.rowCount())
        ]
        filenames_tableitems = [
            self.items_table.item(r, 3) for r in range(self.items_table.rowCount())
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
        global KS
        KS._build_from_lists(weights, values, SIZE, fnames)
        KS.solve()

        # Display in dp_table
        for col in range(self.dp_table.columnCount()):
            for row in range(self.dp_table.rowCount()):
                cur_item = QTableWidgetItem()
                cur_item.setText(str(KS.dp[row][col]))
                self.dp_table.setItem(row, col, cur_item)

        # Update dp header (Icon or Values?)
        self.dp_table.setHorizontalHeaderLabels(
            [(f"W: {str(item.weight)} V: {str(item.value)}") for item in KS.items]
        )

        # Clean
        self.items_table.clearContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Window()
    app.exec_()
