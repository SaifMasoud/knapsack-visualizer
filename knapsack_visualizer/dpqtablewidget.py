from PyQt5.QtWidgets import *
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QColor

class DPQTableWidget(QTableWidget):
    def __init__(self, layout):
        super().__init__(layout)
        self.highlighted = []
        self.setStyleSheet("gridline-color: #fffff8; font-size: 15pt;")
        self.cur_rowcol = None
        self.window = None
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
                self.reveal(selected.row(), selected.column())
            print("Now Highlighted: ", self.highlighted)
        return True

    def reveal(self, row, col):
        print(f"reveal: row, col {row, col}")
        # Clean up: if there was another item revealed, unmark its parents
        if (self.cur_rowcol and (row, col) != self.cur_rowcol):  
            self.unhighlight()

        # Reveal & highlight parents
        tmp_item = QTableWidgetItem()
        tmp_item.setBackground(QColor("Light Blue"))
        tmp_item.setText(self.window.alg.get_cell_value(row, col))
        self.setItem(row, col, tmp_item)
        self.cur_rowcol = row, col
        cur_pars = self.window.alg.get_cell_parents(row, col)
        pars_qtable_elems = [self.item(par[0], par[1]) for par in cur_pars] # gets the QTableWidgetItem from its row and col
        self.highlight(pars_qtable_elems)
        self.highlighted.extend(pars_qtable_elems + [tmp_item]) # keep track of whats highlighted to unmark it later.
    
    def reset_dp(self):
        self.set_all_0()
        self.cur_rowcol = None
    def unhighlight(self):
        for q_cell in self.highlighted:
            try:
                q_cell.setBackground(QColor("White"))
            except RuntimeError:  # Usually is the item being deleted due to new items
                pass
        self.highlighted = []

    def highlight(self, par_table_items):
        if len(par_table_items)==0: return
        # Reveal the table cell scores & color the parents Yellow(Higher score) & Red(Lower score) 
        for par in par_table_items:
            par.setText(self.window.alg.get_cell_value(par.row(), par.column()))
            par.setBackground(QColor("Red"))
        par_table_items[0].setBackground(QColor("Green")) # the first parent is the correct one. (Color it green not red).

    def set_all_0(self):
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                zero_item = QTableWidgetItem()
                zero_item.setText("0")
                self.setItem(row, col, zero_item)
                self.item(row, col).setBackground(QColor("White"))