import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QEvent
import knapsack
from pprint import pprint

KS = knapsack.KnapSack()
SIZE = 5
NUM_ITEMS = 3
 
class DPQTableWidget(QTableWidget):

    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.highlighted = []
        self.cur = None
    
    def event(self, e):
        if e.type() != QEvent.MouseButtonPress and e.type() != QEvent.KeyPress:
            return True
        super().event(e)
        # Reveal
        if self.hasFocus() and self.selectedItems():
            print("revealing", self.selectedItems()[0].row(), self.selectedItems()[0].column())
            print("Currently Highlighted: ", self.highlighted)
            selected = self.selectedItems()[0]
            if selected: self.reveal(selected)
            print("Now Highlighted: ", self.highlighted)
        return True
    
    def reveal(self, selected):
        if self.cur:
            if selected is self.cur: print("Same item"); return
        row, col = selected.row(), selected.column()

        # Clean up 
        if self.cur and selected != self.cur: # if there was another item revealed, unmark its parents
            self.unhighlight()

        # Reveal & highlight parents
        selected.setBackground(QColor("Green"))
        selected.setText(str(KS.dp[row][col]))
        self.cur = selected
        pars = self.table_pars(selected)
        for par in pars:
            if len(pars) > 2: print("AAAA")
            self.highlight(par)
        self.highlighted.extend(pars)
    
    def unhighlight(self):
        if self.highlighted:
            self.highlighted[0].setBackground(QColor("Green")); self.highlighted[1].setBackground(QColor("Green"))
            self.highlighted = []

    def table_pars(self, selected):
        row, col = selected.row(), selected.column()
        par1_r, par1_c,  = KS.dp_parents(row, col)[0]
        par2_r, par2_c = KS.dp_parents(row, col)[1]
        par1 = self.item(par1_r, par1_c)
        par2 = self.item(par2_r, par2_c)
        pars = par1, par2
        return [par for par in pars if par]

    
    def highlight(self, par):
        row, col = par.row(), par.column()
        par.setText(str(KS.dp[row][col]))
        par.setBackground(QColor("Yellow"))


    def set_all_0(self):
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                self.item(row, col).setText('0')
                self.item(row, col).setBackground(QColor("White"))

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "anki_ocr_gui"
        self.initUI()
        self.setGeometry(100, 100, 800 ,600)

    def initUI(self):
        # Creating our widgets
        self.items_table = QTableWidget(NUM_ITEMS, 4); self.items_table.setHorizontalHeaderLabels(['Name', 'Weight', 'Value', 'Icon'])
        self.done_btn = QPushButton('Done')
        self.cwd_label = QLabel("Press Done To Show Solution")

        self.dp_table = DPQTableWidget(SIZE+1, NUM_ITEMS+1)
        self.dp_table.setVerticalHeaderLabels([str(i) for i in range(0, SIZE+1)]) # make the rows start at 0->SIZE
        self.dp_table.setHorizontalHeaderLabels([str(i) for i in range(0, NUM_ITEMS+1)])
        self.cleardp_btn = QPushButton("Clear Solution")

        # Gathering the widgets in a layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.items_table)
        self.layout.addWidget(self.done_btn)
        self.layout.addWidget(self.cwd_label)
        self.layout.addWidget(self.dp_table)
        self.layout.addWidget(self.cleardp_btn)

        # Connecting the buttons to their functions
        self.done_btn.clicked.connect(self.on_done_btn)
        self.cleardp_btn.clicked.connect(self.on_cleardp_btn)

        # Adding our widgets to the window then showing the window
        self.setLayout(self.layout)
        self.show()



    def on_cleardp_btn(self):
        self.dp_table.set_all_0()
        QMessageBox.about(self, "Usage", "Focus a table slot to show its solution")
        


    def on_done_btn(self):
        # Read/Verify data
        print("pressed done")
        names_obj = [self.items_table.item(r, 0) for r in range(self.items_table.rowCount())]
        weights_obj = [self.items_table.item(r, 1) for r in range(self.items_table.rowCount())]
        values_obj = [self.items_table.item(r, 2) for r in range(self.items_table.rowCount())]
        filenames_obj = [self.items_table.item(r, 3) for r in range(self.items_table.rowCount())]
        print("got data")
        if None in weights_obj or None in values_obj:
            QMessageBox.about(self, "Error", "Please Fill Weights & Values with numbers")
            return
        weights, values = [int(w.data(0)) for w in weights_obj], [int(v.data(0)) for v in values_obj]
        fnames = [f.data(0) if f else None for f in filenames_obj] # Default to None if list not specified

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
        self.dp_table.setHorizontalHeaderLabels([(f"W: {str(item.weight)} V: {str(item.value)}") for item in KS.items])

        
        # Clean
        # KS.items = []; KS.size = SIZE
        self.items_table.clearContents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = Window()
    app.exec_()
