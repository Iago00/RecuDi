import sqlite3 as dbapi

try:
    bbdd = dbapi.connect ("recu.dat")
    print (bbdd)


except dbapi.StandardError as e:
    print (e)
else:
    print ("Base de datos abierta")

try:
    cursor = bbdd.cursor ()
    print (cursor)

except dbapi.Error as e:
    print (e)
else:
    print ("Cursor preparado")

try:

   cursor.execute(""" CREATE TABLE Producto (
	"Identificador"	INTEGER PRIMARY KEY NOT NULL,
	"NombreProducto"	TEXT NOT NULL,
	"CodigoProducto"	INTEGER NOT NULL,
	"Proveedor"	TEXT NOT NULL,
	"Precio"	INTEGER NOT NULL,
	"Cantidad"	INTEGER NOT NULL,
	"Descripcion"	TEXT
   )
   """)

   cursor.execute("""insert into Producto
                        values (1, 'Arroz bomba',555,'Auchan',1,80,'Arroz bomba')""")
   cursor.execute("""insert into Producto
                         values (2, 'Empanada',482,'Hacendado',2,50,'Empanada')""")
   cursor.execute("""insert into Producto
                         values (3, 'Mejillones',359,'La Lata De Braulio',4,30,'Mejillones')""")
   bbdd.commit()

except dbapi.DatabaseError as e:
   print("Error insertando los datos en productos: " + str(e))

try:
   cursor.execute(""" CREATE TABLE Proveedor (
	"Identificador"	INTEGER PRIMARY KEY NOT NULL,
	"NombreProveedor"	TEXT NOT NULL,
	"Telefono"	INTEGER NOT NULL,
	"CorreoElectronico"	TEXT NOT NULL,
	"Pais"	TEXT NOT NULL,
	"Direccion"	TEXT NOT NULL,
	"Numero"	INTEGER NOT NULL,
	"CodigoPostal"	INTEGER NOT NULL,
	"CIF"	INTEGER NOT NULL,
	"DatosBancarios"	INTEGER NOT NULL
      )
      """)
   cursor.execute("""insert into Proveedor
                    values(1, 'Auchan',654425458,'ftj@gmail','Pontevedra','Calle Juan Carlos',69,56541,5489521,34488781)""")
   cursor.execute("""insert into Proveedor
                    values(2, 'Hacendado',624825428,'rbm@gmail','Barcelona','Avenida Rucula',25,19985,5488612,91547952)""")
   cursor.execute("""insert into Proveedor
                    values(3, 'La Lata De Braulio',689246578,'jaf@gmail','Portugal','Calle Central',10,38748,54892165,56547892014)""")
   bbdd.commit()
except dbapi.DatabaseError as e:
   print("Erro insertando os datos en proveedor: " + str(e))

   try:
       cursor.execute(""" CREATE TABLE Supermercados (
   	"Identificador"	INTEGER PRIMARY KEY NOT NULL,
   	"NombreSupermercado"	TEXT NOT NULL,
   	"Telefono"	INTEGER NOT NULL,
   	"CorreoElectronico"	TEXT NOT NULL,
   	"Pais"	TEXT NOT NULL,
   	"Direccion"	TEXT NOT NULL,
   	"Numero"	INTEGER NOT NULL,
   	"CodigoPostal"	INTEGER NOT NULL,
   	"CIF"	INTEGER NOT NULL
         )
         """)
       cursor.execute("""insert into Proveedor
                       values(1, 'Froiz',654425458,'hytt@gom','Galicia','Calle Roberto Carlos',14,55991,7689521)""")
       cursor.execute("""insert into Proveedor
                       values(2, 'Eroski',624825428,'hffw@gam','Galicia','Avenida da Fonte',40,90485,7688612)""")
       cursor.execute("""insert into Proveedor
                       values(3, 'Gadis',589246578,'kijhp@la','Galicia','Calle Bilbao',88,76548,76892165)""")
       bbdd.commit()
   except dbapi.DatabaseError as e:
       print("Error insertando los datos en Supermercados: " + str(e))

   try:
       cursor.execute("select * from Producto")
       # fetchone a seguinte tupla
       # fetchall devolta un obxecto iterable con todalas tuplas
       # fetcmany numero de tuplas pasado por parametro
       for fila in cursor.fetchall():
           # print (fila)
           print("Identificador: " + str(fila[0]))
           print("NombreProducto: " + fila[1])
           print("CodigoProducto: " + str(fila[2]))
           print("Proveedor: " + fila[3])
           print("Precio: " + str(fila[4]))
           print("Cantidad: " + str(fila[5]))
           print("Descripcion: " + fila[6])

   except dbapi.DatabaseError as e:
       print("Erro facendo a consulta: " + str(e))
   else:
       print("Consulta executada")
   NombreProducto= input("Introduce o nome")
   try:
       consulta = "select * from producto where NombreProducto= ?"
       print(consulta)
       cursor.execute(consulta, (NombreProducto,))
       for rexistro in cursor.fetchall():
           print(rexistro)
   except dbapi.DatabaseError as e:
       print("Error haciendo la consulta: " + str(e))
   else:
       print("Consulta ejecutada")
   bbdd.commit()

else:
    print ("Base de datos creada")

finally:
    cursor.close()
    bbdd.close()





