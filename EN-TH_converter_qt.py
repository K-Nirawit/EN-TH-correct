import GUI_01
from PyQt6 import QtWidgets, QtCore, QtGui
import sys
import pyperclip


def my_excepthook(type, value,tback):
    sys.__excepthook__(type,value,tback)

sys.excepthook = my_excepthook

class my_MainWindow(QtWidgets.QMainWindow,GUI_01.Ui_MainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
    
        self.setupUi(self)
        self._connect_signal()

    def _connect_signal(self):
        self.pb_process.clicked.connect(self.convert)
        self.pb_copy.clicked.connect(self.GUI_copy)
        self.pb_exit.clicked.connect(self.exit_GUI)

    def convert(self):
        input_text = self.pte_input.toPlainText()
        print("Your input text is : ",input_text)
        if self.rb_TH2EN.isChecked():
            print("convert TH to EN")
        elif self.rb_EN2TH.isChecked():
            print("convert EN to TH")
        else:
            print("please select mode")
            self.tb_output.setText("please select mode")
   
    def GUI_copy(self):
        input_text = self.tb_output.text()
        pyperclip.copy(input_text)
        print("Coppied your input text to clipboard", input_text)

    def exit_GUI(self):
        self.close()
        print("===nothing error=====")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = my_MainWindow()
    win.show()
    sys.exit(app.exec())

