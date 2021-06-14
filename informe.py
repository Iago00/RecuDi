import sqlite3 as dbapi
import os

from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A3
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas


estiloHoja = getSampleStyleSheet()
story = []


cabecera = estiloHoja['Heading4']
cabecera.pageBreakBefore=0
cabecera.keepWithNext=0
cabecera.backColor=colors.green

parrafo= Paragraph("RecuDi",cabecera)
story.append(parrafo)

cadena = " Productos "
estilo = estiloHoja['BodyText']
parrafo2 = Paragraph(cadena,estilo)
story.append(parrafo2)

story.append(Spacer(0,20))

doc = SimpleDocTemplate("Informe.pdf",pagesize = A3, showBoundary =1)



story.append(Spacer(0,20))



listaprod = []
listaprod.append(("Ident","NombreProd","CodigoProd","Prov","Precio","Cant","Descripcion"))
listapro = []
listapro.append(("Ident","NombreProv","Telefono","Correo","Pais","Direccion","Numero","CodPostal","CIF","Banco"))
listasuper = []
listasuper.append(("Ident","NombreSuper","Telefono","Correo","Pais","Direccion","Numero","CodPostal","CIF"))



try:

    conexion = dbapi.connect("recu.dat")

except dbapi.StandardError as e:

    print(e)
else:

    print("Base conectada")

try:

    cursor = conexion.cursor()
    cursor.execute("select * from Producto")
    for filaprod in cursor.fetchall():
        listaprod.append(filaprod)

    cursor.execute("select * from Proveedor")
    for filapro in cursor.fetchall():
        listapro.append(filapro)

    cursor.execute("select * from Supermercados")
    for filasuper in cursor.fetchall():
        listasuper.append(filasuper)


except dbapi.DatabaseError as e:

    print("Error en consulta Producto: "+ str(e))

else:
    print("Consulta realizada")

finally:
    cursor.close()
    conexion.close()

tablaprod= Table(listaprod)

tablaprod.setStyle([('TEXTCOLOR',(0,0),(-1,0),colors.chocolate)])
tablaprod.setStyle([('BACKGROUND',(0,1),(-1,-1),colors.fuchsia)])
tablaprod.setStyle([('INNERGIRD',(0,1),(-1,-1),0.25,colors.blueviolet)])
story.append(tablaprod)

story.append(Spacer(0,20))

cadena = " Proveedor"
estilo = estiloHoja['BodyText']
parrafo2 = Paragraph(cadena,estilo)
story.append(parrafo2)


story.append(Spacer(0,20))

tablapro = Table(listapro)

tablapro.setStyle([('TEXTCOLOR',(0,0),(-1,0),colors.chocolate)])
tablapro.setStyle([('BACKGROUND',(0,1),(-1,-1),colors.fuchsia)])
tablapro.setStyle([('INNERGIRD',(0,1),(-1,-1),0.25,colors.blueviolet)])
story.append(tablapro)


story.append(Spacer(0,20))

cadena = " Supermercados "
estilo = estiloHoja['BodyText']
parrafo2 = Paragraph(cadena,estilo)
story.append(parrafo2)

story.append(Spacer(0,20))

tablasuper = Table(listasuper)

tablasuper.setStyle([('TEXTCOLOR',(0,0),(-1,0),colors.chocolate)])
tablasuper.setStyle([('BACKGROUND',(0,1),(-1,-1),colors.fuchsia)])
tablasuper.setStyle([('INNERGIRD',(0,1),(-1,-1),0.25,colors.blueviolet)])
story.append(tablasuper)


doc.build(story)