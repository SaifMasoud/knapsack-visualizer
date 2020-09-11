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
        try:
            par1_r, par1_c = self.knapsack.dp_parents(row, col)[0]
            par2_r, par2_c = self.knapsack.dp_parents(row, col)[1]
            par1 = self.item(par1_r, par1_c)
            par2 = self.item(par2_r, par2_c)
            pars = par1, par2
            return [par for par in pars if par is not None]
        except TypeError:  # means there is only 1 par
            row, col = self.knapsack.dp_parents(row, col)
            return [self.item(row, col)]

    def highlight(self, pars):
        for par in pars:
            par.setText(str(self.knapsack.dp[par.row()][par.column()]))
        if not pars:
            return
        if len(pars) == 1:
            pars[0].setBackground(QColor("Yellow"))
            return

        par1, par2 = pars[0], pars[1]
        # par 2 is *taken* in self.knapsack.dp
        par2_score = (
            self.knapsack.dp[par2.row()][par2.column()] + self.knapsack.items[self.cur.column()].value
        )
        par1_score = self.knapsack.dp[par1.row()][par1.column()]

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