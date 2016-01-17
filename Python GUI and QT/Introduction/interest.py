__author__ = 'Daniel'

from PySide.QtCore import *
from PySide.QtGui import *
from urllib.request import urlopen
import sys


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        principle_label = QLabel("Principle:")
        rate_label = QLabel("Rate:")
        years_label = QLabel("Years:")
        amount_label = QLabel("Amount:")
        self.principle_spin_box = QDoubleSpinBox()
        self.principle_spin_box.setPrefix("$")
        self.principle_spin_box.setMaximum(float("inf"))
        self.rate_spin_box = QDoubleSpinBox()
        self.rate_spin_box.setMaximum(float("inf"))
        self.rate_spin_box.setSuffix("%")
        self.year_combo_box = QComboBox()
        self.year_combo_box.addItems(["1 year", "2 years", "3 years"])
        self.amount_calculated = QLabel("$0.00")
        # Create the grid
        grid = QGridLayout()
        grid.addWidget(principle_label, 0, 0)
        grid.addWidget(rate_label, 1, 0)
        grid.addWidget(years_label, 2, 0)
        grid.addWidget(amount_label, 3, 0)
        grid.addWidget(self.principle_spin_box, 0, 1)
        grid.addWidget(self.rate_spin_box, 1, 1)
        grid.addWidget(self.year_combo_box, 2, 1)
        grid.addWidget(self.amount_calculated, 3, 1)

        self.setLayout(grid)
        self.connect(self.principle_spin_box, SIGNAL("valueChanged(double)"), self.update_ui)
        self.connect(self.rate_spin_box, SIGNAL("valueChanged(double)"), self.update_ui)
        self.connect(self.year_combo_box, SIGNAL("currentIndexChanged(int)"), self.update_ui)
        self.setWindowTitle("Interests")

    def update_ui(self):
        principle = float(self.principle_spin_box.value())
        rate = float(self.rate_spin_box.value())
        year = int(self.year_combo_box.currentIndex()) + 1
        amount = principle * (1 + rate/100) ** year
        self.amount_calculated.setText("%0.2f" % (amount,))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()