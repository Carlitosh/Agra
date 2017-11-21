#!/usr/bin/python
# -*- coding: utf-8 -*-

from itertools import permutations
from PyQt4 import QtGui, uic
import sys 
import numpy as np 
import csv 
import xlsxwriter as xls 
import funciones 
import os  
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("Agra_generadora.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
	
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.Button_agregar_fila.clicked.connect(self.agregar_fila)
		self.button_reducir_fila.clicked.connect(self.reducir_fila)
		self.button_agregar_column.clicked.connect(self.agregar_columna)	
		self.button_reducir_column.clicked.connect(self.reducir_columna)
		self.button_imprimir.clicked.connect(self.imprimir)
		self.Button_print_combinatoria.clicked.connect(self.imprimir_combinatoria)
		#self.button_guardar.clicked.connect(self.guardar)
		self.button_limpiar.clicked.connect(self.limpiar)
		
		#=========================== botones menu
		self.actionAcerca.triggered.connect(self.acerca)
		
		

########################################################	
	

	def acerca(self):
		os.system('pythonw acerca.pyw')
	"""
	def abrir(self):


	"""


	def limpiar(self):
		self.textEdit.clear()
		self.textEdit_2.clear()	
	
	"""
	def guardar(self):
		
		
		direc = QtGui.QFileDialog.getSaveFileName(self, 'Guardar CSV',
		 'Archivos/', selectedFilter='*.csv')
		self.lineEdit_path.setText(str(direc))
		self.lineEdit_path.Text(str(direc))

		
		csvsalida = open('salidat.csv', 'w', newline='')
		salida = csv.writer(csvsalida)
		salida.writerow(['campo1', 'campo2'])
		salida.writerows(datos)
		self.textEdit.toPlainText()
		del salida
		csvsalida.close()
		
		
	"""
	def borrar_todo(self):
		pass
	def agregar_columna(self):
		self.tableWidget.insertColumn(0) # El valor que requiere es el lugar donde agrega la columna, en que puesto
		
		#self.tableWidget.insertColumn(0) 
	def reducir_columna(self):
		self.tableWidget.removeColumn(0)

	def reducir_fila(self):
		self.tableWidget.removeRow(0)

	def agregar_fila(self):
		self.tableWidget.insertRow(0)
		
	def imprimir(self):
		conjunto = []
		allRows = self.tableWidget.rowCount()
		for row in xrange(0,allRows):
			twi0 = self.tableWidget.item(row,0)
			conjunto.append(str(twi0.text()))
		
		print conjunto	

	def imprimir_combinatoria(self):

		
		numero_filas = self.tableWidget.rowCount()
		numero_columnas = self.tableWidget.columnCount()
		matriz = []
		for row in range(numero_filas):
		    matriz.append([])
		    for column in range(numero_columnas):
		    	celda = self.tableWidget.item(row,column)
		        if celda == None:
		        	pass
		        else:	
		        	matriz[row].append(str(celda.text()))
		
		elementos = matriz 
		combinaciones = []

		if 	self.tableWidget.rowCount() ==1:
			for x1 in elementos[0]:
				x1 = str(x1)
				set_data = x1
				combinaciones.append(set_data)


		elif self.tableWidget.rowCount() ==2:
			for x1 in elementos[0]:
				for x2 in elementos[1]:
					x1 = str(x1)
					x2 = str(x2)
					set_data = x1+','+x2
					combinaciones.append(set_data)
		
		elif self.tableWidget.rowCount() ==3:
			for x1 in elementos[0]:
				for x2 in elementos[1]:
					for x3 in elementos[2]:
						x1 = str(x1)
						x2 = str(x2)
						x3 = str(x3)
						set_data = x1+','+x2+','+x3
						combinaciones.append(set_data)

		elif self.tableWidget.rowCount() ==4:
			for x1 in elementos[0]:
				for x2 in elementos[1]:
					for x3 in elementos[2]:
						for x4 in elementos[3]:
							x1 = str(x1)
							x2 = str(x2)
							x3 = str(x3)
							x4 = str(x4)
							set_data = x1+','+x2+','+x3+','+x4
							combinaciones.append(set_data)

		elif  self.tableWidget.rowCount() ==5:
			for x1 in elementos[0]:
				for x2 in elementos[1]:
					for x3 in elementos[2]:
						for x4 in elementos[3]:
							for x5 in elementos[4]:

								x1 = str(x1)
								x2 = str(x2)
								x3 = str(x3)
								x4 = str(x4)
								x5 = str(x5)
								set_data = x1+ ','+x2+','+x3+','+x4+','+x5
								combinaciones.append(set_data)

		elif self.tableWidget.rowCount() ==6:
			for x1 in elementos[0]:
				for x2 in elementos[1]:
					for x3 in elementos[2]:
						for x4 in elementos[3]:
							for x5 in elementos[4]:
								for x6 in elementos[5]:

									x1 = str(x1)
									x2 = str(x2)
									x3 = str(x3)
									x4 = str(x4)
									x5 = str(x5)
									x6 = str(x6)
									set_data = x1+','+x2+','+x3+',' +x4+',' +x5+','+x6	
									combinaciones.append(set_data)	

		else:
			pass


		#=======================================================================================	
			return combinaciones 

		#=======================================================================================	
		#print combinaciones
		workbook = xls.Workbook('etiquetas.xlsx')
		worksheet = workbook.add_worksheet()
		for i in combinaciones:
			self.textEdit.append(i)
			worksheet.write('A1', 'tratamiento')
			worksheet.write('B1', 'codigo de barras')
			worksheet.write(str('A'+str(2+combinaciones.index(i))), i)
			
			funciones.createBarCodes(str("Temp/"+i))
			
			#funciones.conversor(str("Temp/"+i))
			#worksheet.write(str('B'+str(2+combinaciones.index(i))), i)
			#worksheet.insert_image(str('B'+str(2+combinaciones.index(i))), str(i+'.jpg'), {'x_scale': 0.5, 'y_scale': 0.5})




############################################################
		self.textEdit_2.append(str(len(combinaciones)))	

app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()