import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvas

#
class ApplicationWindow(QtWidgets.QMainWindow) :
	def __init__(self):
		super().__init__()
		self._main = QtWidgets.QWidget()
		self.setCentralWidget(self._main)
		#
		self.btnOpenFile = QtWidgets.QPushButton('Выбор файла')
		self.kksView = QtWidgets.QListWidget()
		self.kksView.addItems(['item1', 'item2', 'item3', 'item4', 'item5', ])
		#
		self.fig = Figure() 
		self.canvas = FigureCanvas(self.fig)
		#
		layout = QtWidgets.QGridLayout(self._main)
		layout.addWidget(self.btnOpenFile, 0, 0, 1, 1)
		layout.addWidget(self.canvas, 0, 1, 6, 1)
		layout.addWidget(self.kksView, 1, 0, 5, 1)
		#
		self._ax = self.fig.subplots()
		#
		self._timer = self.canvas.new_timer(
			100, [(self._update_canvas, (), {})])
		self._timer.start()
	#
	def _update_canvas(self):
		self._ax.clear()
		t = np.linspace(0, 10, 101)
		self._ax.plot(t, np.sin(t + time.time()))
		self.canvas.draw()

#
if __name__ == "__main__":
	qapp = QtWidgets.QApplication(sys.argv)
	app = ApplicationWindow()
	app.show()
	qapp.exec_()