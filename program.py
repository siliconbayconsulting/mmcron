# importing modules 
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors 

class PdfGen:
	def __init__(self):
		self.fileName = 'static/sample.pdf'
		self.documentTitle = 'sample'
		self.title = 'Metamorphic'
		self.subTitle = 'Your personalized program!!'
		self.textLines = [ 
			'Here is your personalized program', 
			'be with metamorphic.', 
		] 
		self.image = 'static\image.jpg'

	def createPdf(self):
		# creating a pdf object 
		pdf = canvas.Canvas(self.fileName) 

		# setting the title of the document 
		pdf.setTitle(self.documentTitle) 

		# registering a external font in python 
		pdfmetrics.registerFont( 
			TTFont('abc', 'SakBunderan.ttf') 
		) 

		# creating the title by setting it's font d
		# and putting it on the canvas 
		pdf.setFont('abc', 36) 
		pdf.drawCentredString(300, 770, self.title) 

		# creating the subtitle by setting it's font, 
		# colour and putting it on the canvas 
		pdf.setFillColorRGB(0, 0, 255) 
		pdf.setFont("Courier-Bold", 24) 
		pdf.drawCentredString(290, 720, self.subTitle) 

		# drawing a line 
		pdf.line(30, 710, 550, 710) 

		# creating a multiline text using 
		# textline and for loop 
		text = pdf.beginText(40, 680) 
		text.setFont("Courier", 18) 
		text.setFillColor(colors.red) 
		for line in self.textLines: 
			text.textLine(line) 
		pdf.drawText(text) 

		# drawing a image at the 
		# specified (x.y) position 
		pdf.drawInlineImage(self.image, 130, 400) 

		# saving the pdf 
		pdf.save() 
