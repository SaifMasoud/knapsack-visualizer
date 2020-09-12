from PyQt5.QtWidgets import *
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QColor

class DPQTableWidget(QTableWidget):
    def __init__(self, layout):
        super().__init__(layout)
        self.highlighted = []
        self.cur = None
        # self.setVerticalHeaderLabels([str(i) for i in range(SIZE + 1)])  # make the rows start at 0->SIZE
        # self.setHorizontalHeaderLabels([" " + str(i) for i in range(NUM_ITEMS + 1)])

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
        selected.setText(str(self.knapsack.dp[row][col]))
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
        pars = self.knapsack.dp_parents_sorted(row, col)
        print("PARS: ", pars)
        par_table_items = [self.item(par[0], par[1]) for par in pars]
        return par_table_items

    def highlight(self, par_table_items):
        if len(par_table_items)==0: return
        # Reveal the table cell scores & color the parents Yellow(Higher score) & Red(Lower score) 
        for par in par_table_items:
            par.setText(str(self.knapsack.dp[par.row()][par.column()]))
        par_table_items[0].setBackground(QColor("Yellow"))
        if len(par_table_items) == 2:
            par_table_items[1].setBackground(QColor("Red"))

    def set_all_0(self):
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                zero_item = QTableWidgetItem()
                zero_item.setText("0")
                self.setItem(row, col, zero_item)
                self.item(row, col).setBackground(QColor("White"))