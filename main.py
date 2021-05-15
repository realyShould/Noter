import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from gui import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # connects
        self.ui.actionNew.triggered.connect(self.btnNewClicked)
        self.ui.actionOpen.triggered.connect(self.btnOpenClicked)
        self.ui.actionSave.triggered.connect(self.btnSaveClicked)
        self.ui.actionSave_As.triggered.connect(self.btnSaveAsClicked)

    def btnNewClicked(self):
        # fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        pass
    def btnOpenClicked(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', '')[0]
        with open(self.fname, 'r+') as fil:
            text = fil.read()
            self.ui.textEdit.setText(text)
    def btnSaveClicked(self):
        text = self.textEdit.toPlainText()
        with open(self.fname, 'w+') as fil:
            fil.write(text)

    def btnSaveAsClicked(self):
        text = self.textEdit.toPlainText()
        saPath = QFileDialog.getSaveFileName(self, 'Save as file', '')[0]
        with open(saPath, 'w+') as fil:
            fil.write(text)

    def quitClicked(self):
        sys.exit(app.exec())

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())