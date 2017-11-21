#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf8


from PyQt4 import QtGui, uic, QtCore
import sys 
import numpy as np 

 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("Agra_lecto.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
	
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.button_imprimir.clicked.connect(self.imprimir)
		self.button_desagregar.clicked.connect(self.desagregar)
		self.button_agregar.clicked.connect(self.agregar)
		self.button_reducir.clicked.connect(self.reducir)
		self.actionAbrir.triggered.connect(self.Abrir)
		self.actionGuardar_Como.triggered.connect(self.Guardar)


	def Guardar(self):

		cantidad_columnas = self.tableWidget.columnCount()  
		cantidad_filas = self.tableWidget.rowCount()
		#print cantidad_columnas,cantidad_filas

		#print str(self.tableWidget.item(0, 1).text()) 
		
		
		for i in range(0,cantidad_columnas):
			for y in range(0,cantidad_filas):
				#print i 
				print str(self.tableWidget.item(y, i).text()) 
			
		"""
		
		self.fila_actual = self.tableWidget.currentRow()
		self.columna_actual = self.tableWidget.currentColumn()
		self.celda_actual = self.tableWidget.item(self.fila_actual, self.columna_actual).text()
		self.imprimir1 = str(self.celda_actual)
		
		print label1
		
		for i in range(1,len(imprimir1)):
			lugar = self.tableWidget.columnCount()
			
			self.tableWidget.setItem(self.fila_actual, self.columna_actual, QtGui.QTableWidgetItem(i))
		
		#print self.imprimir1
		#print len(label1)
		#print str(label1)
		
		"""

	def Abrir(self):
		print ""
	
	def agregar(self):

		self.tableWidget.insertColumn(self.tableWidget.currentColumn()+1)

	def reducir(self):
		cant_columna = self.tableWidget.columnCount() - 1
		self.tableWidget.removeColumn(cant_columna)
		

	def desagregar(self):
		# +0+/+k+w+s/+0+/+0
		
		self.fila_actual = self.tableWidget.currentRow()
		self.columna_actual = self.tableWidget.currentColumn()
		self.celda_actual = self.tableWidget.item(self.fila_actual, 0).text()
		self.imprimir1 = str(self.celda_actual)
		
		self.label = str(self.imprimir1.replace('+',''))
		label1 = self.label.split(',')
		for i,y in zip(label1,range(0,len(label1))):
			ubicacion_col =  self.tableWidget.currentColumn() + y + 1
			self.tableWidget.setItem(self.fila_actual, ubicacion_col , QtGui.QTableWidgetItem(i))
			ubicacion_col = ubicacion_col +1
		self.tableWidget.insertRow(self.tableWidget.currentRow()+1)
		item = self.tableWidget.model().index((self.tableWidget.currentRow()+1),0)
		self.tableWidget.setCurrentIndex(item)
		self.tableWidget.selectRow(1)
		self.tableWidget.selectColumn(0 )
	
	def imprimir(self):
		
		self.fila_actual = self.tableWidget.currentRow()
		self.columna_actual = self.tableWidget.currentColumn()
		self.celda_actual = self.tableWidget.item(self.fila_actual, self.columna_actual).text()
		self.imprimir1 = str(self.celda_actual.encode('utf-8'))
		self.imprimir1 = self.imprimir1.encode('utf-8')
		self.label = str(self.imprimir1.replace('¡',''))
		label1 = self.label.split('-')
		print label1
		
		#for i in range(1,len(label1)):
		#	lugar = self.tableWidget.columnCount())
		#	#self.tableWidget.insertColumn(self.tableWidget.columnCount()+1)
		#	self.tableWidget.setItem(self.fila_actual, self.columna_actual, QtGui.QTableWidgetItem(i))
		#for i in lab+0+/+k+w+s+/+0+/+0
		#	print i 
		#print self.imprimir1
		#print len(label1)
		#print str(label1)
		
app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()