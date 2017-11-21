#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtGui, uic
import sys 
import numpy as np 

 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("lectora.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
	
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.button_imprimir.clicked.connect(self.imprimir)
		#self.button_desagregar.clicked.connect(self.desagregar)
		#self.Button_agregar_fila.clicked.connect(self.agregar_fila)		

	def agregar_columna(self):
		self.tableWidget.insertColumn(0) # El valor que requiere es el lugar donde agrega la columna, en que puesto

	def reducir_columna(self):
		self.tableWidget.removeColumn(0)

	def desagregar(self):
		actual = self.tableWidget.currentItem().text()
		actual.split()
		print actual 


	def imprimir(self):
		
		#self.imprimir1 = str(self.tableWidget.item(0,0).text())
		#self.imprimir.split()
		#print self.imprimir1,type(self.imprimir1)
		#print self.imprimir1.replace('+','')
		actual = self.tableWidget.currentItem().text()
		print actual 

	
			
app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()