from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
#
Form, Window = uic.loadUiType("1.ui")
#
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
#
def pushButtonClicked(self) :
	form.label.setText(form.lineEdit.text())
#
form.pushButton.clicked.connect(pushButtonClicked)
#
window.show()
app.exec_()
