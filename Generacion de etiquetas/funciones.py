from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from wand.image import Image
#from pdf_a_jpg import convert
import os

def createBarCodes(barcode_value):
    """
    Crea codigo de barra a partir de un texto y genera la etiqueta requerida.
    barcode128
    """
    etiqueta = barcode_value
    barcode128 = code128.Code128(str(etiqueta.strip('Temp/')), barHeight=19*mm,barWidth = 0.9, stop=1)
    c = canvas.Canvas(str(barcode_value), pagesize=(barcode128.minWidth(),29*mm))
    x = 3 * mm
    y = 3 * mm
    barcode128.drawOn(c, x, y)
    c.setFont("Helvetica", 8)
    c.setStrokeColorRGB(0,0,0)
    c.rect(1*mm,2*mm,barcode128.minWidth() - 2*mm,29*mm, fill=0)
    c.drawString(3*mm, 22*mm, str(etiqueta.strip('Temp/')))
    c.save()



def conversor(file):
	#file = str(file)+'.pdf'
	file = str(file)
	with Image(filename = file, resolution = 600) as img:
		salida = file.strip(' ')
		img.save(filename= str(file.strip(' .pdf')+ ".jpg"))
		#img.save(filename= str(file.strip(' .pdf')))
os.system("mkdir Temp")
