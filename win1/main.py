from PyQt5 import QtWidgets, QtGui, QtCore
from mainwindow import Ui_Form  # импорт нашего сгенерированного файла
import sys
#
def lineEditToFloat(edit) :
  try :
    edit.setStyleSheet("color: black")
    return float(edit.text())
  except :
    edit.setStyleSheet("color: red")
    return 0
#
class mainwindow(QtWidgets.QMainWindow) :
  #функция сигнал (отклик на событие слота pushButton.clicked) Сложить
    def pushButtonClicked(self) :
      x = lineEditToFloat(self.ui.lineEdit)
      y = lineEditToFloat(self.ui.lineEdit_2)
      self.ui.label_4.setText(str(x+y))
      # Если не использовать, то часть текста исчезнет.
      self.ui.label_4.adjustSize()
  #функция сигнал (отклик на событие слота pushButton_2.clicked) Умножить
    def pushButton_2Clicked(self) :
      x = lineEditToFloat(self.ui.lineEdit)
      y = lineEditToFloat(self.ui.lineEdit_2)
      self.ui.label_4.setText(str(x*y))
      # Если не использовать, то часть текста исчезнет.
      self.ui.label_4.adjustSize()
  #функция сигнал (отклик на событие слота pushButton_3.clicked) Вычесть
    def pushButton_3Clicked(self) :
      x = lineEditToFloat(self.ui.lineEdit)
      y = lineEditToFloat(self.ui.lineEdit_2)
      self.ui.label_4.setText(str(x-y))
      # Если не использовать, то часть текста исчезнет.
      self.ui.label_4.adjustSize()
  #функция сигнал (отклик на событие слота pushButton_4.clicked) Разделить
    def pushButton_4Clicked(self) :
      x = lineEditToFloat(self.ui.lineEdit)
      y = lineEditToFloat(self.ui.lineEdit_2)
      try :
        self.ui.label_4.setText(str(x/y))
      except :
        if x==0 : 
          self.ui.label_4.setText("indeterminacy")
        else :
          self.ui.label_4.setText("Infinity")
       # Если не использовать, то часть текста исчезнет.
      self.ui.label_4.adjustSize()
#
    def __init__(self) :
        super(mainwindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label.setFont(
            QtGui.QFont('SansSerif', 30)
        ) # Изменение шрифта и размера
        #self.ui.label.setGeometry(
        #    QtCore.QRect(10, 10, 200, 200)
        #) # изменить геометрию ярлыка
        self.ui.label.setText("Мы все психи!! Реально!!!")
        self.ui.label.setWordWrap(True)
        self.ui.label.adjustSize()
        # Меняем текст
        self.ui.lineEdit.setText("0")
        self.ui.lineEdit_2.setText("0")
        # указать максимальную длину
        self.ui.lineEdit_2.setMaxLength(10)
        # ввод пароля
        #self.ui.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        # только чтение без изменения содержимого.
        #self.ui.lineEdit_4.setReadOnly(True) 
        # меняем цвет вводимого текста
        #self.ui.lineEdit_5.setStyleSheet("color: rgb(28, 43, 255);") 
        # изменение цвета фона QLineEdit
        #self.ui.lineEdit_6.setStyleSheet("background-color: rgb(28, 43, 255);")
        # подключение клик-сигнал к слоту pushButtonClicked (Сложить)
        self.ui.pushButton.clicked.connect(self.pushButtonClicked)
        # подключение клик-сигнал к слоту pushButton_2Clicked (Умножить)
        self.ui.pushButton_2.clicked.connect(self.pushButton_2Clicked)
        # подключение клик-сигнал к слоту pushButton_3Clicked (Вычесть)
        self.ui.pushButton_3.clicked.connect(self.pushButton_3Clicked)
        # подключение клик-сигнал к слоту pushButton_4Clicked (Разделить)
        self.ui.pushButton_4.clicked.connect(self.pushButton_4Clicked)
#
app = QtWidgets.QApplication([])
application = mainwindow()
application.show()
#
sys.exit(app.exec())