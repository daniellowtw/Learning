__author__ = 'Daniel'

from test import *
from findandreplacedialog import *

from PySide.QtCore import *
from PySide.QtGui import *
import sys

class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class FindAndReplaceDialog (QDialog, Ui_FindAndReplaceDlg):
    def __init__(self, parent=None):
        super(FindAndReplaceDialog, self).__init__(parent)
        self.__index = 0
        # self.ui = Ui_FindAndReplaceDlg()
        self.setupUi(self)
        self.updateUi()

    @Slot(str)
    def on_findLineEdit_textEdited(self, text):
        self.__index = 0
        self.updateUi()


    def updateUi(self):
        # print(type(self.findLineEdit.text()))
        enable = not (len(self.findLineEdit.text()) == 0)
        self.pushButton.setEnabled(enable)
        # self.replaceButton.setEnabled(enable)
        # self.replaceAllButton.setEnabled(enable)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = FindAndReplaceDialog()
    mySW.show()
    sys.exit(app.exec_())

