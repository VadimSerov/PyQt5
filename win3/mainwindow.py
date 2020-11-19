from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
#
class Ui_Form(QMainWindow):
   def __init__(self):
      super(Ui_Form, self).__init__()
      uic.loadUi('mainwindow.ui', self)