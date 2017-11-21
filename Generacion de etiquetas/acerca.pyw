#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, uic
import os
from pylab import *
 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("acerca.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.button_salir.clicked.connect(self.salir)
	
	def salir(self):
		exit()

app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
