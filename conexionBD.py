import sqlite3 as dbapi


class ConexionBD:
    """Clase para realizar a conexión a una base de datos SQlite.

    """

    def __init__(self,rutaBd):
        """Crea as propiedades e as inicializa

        :param rutaBd: Ruta onde se encontra o ficheiro da base de datos SQlite

        """
        self.rutaBd = rutaBd
        self.conexion = dbapi.connect("recu.dat")
        self.cursor = self.conexion.cursor()


    def conectaBD (self):
        """Método que crea a conexión da base de datos.

        Para realizar a conexión precisa da ruta onde está a base de datos que pásaselle no método __init__.

        """

        try:
            if self.conexion is None:
                if self.rutaBd is None:
                    print ("A ruta da base de datos é: None ")
                else:
                    self.conexion = dbapi.connect (self.rutaBd)
            else:
                print ("Base de datos conectada: " + self.conexion)

        except dbapi.StandardError as e:
            print ("Erro o facer a conexión a base de datos " + self.rutaBd + ": " + e)
        else:
            print ("Conexión de base de datos realizada")


    def creaCursor(self):
        """Método que crea o cursor da base de datos.

        Para realizar o cursor precísase previamente da execución do método conectaBD, que crea a conexión a base de
        datos na ruta onde está padada o método __init__.

        """

        try:
            if self.conexion is None:
                print ("Creando o cursor: É necesario realizar a conexión a base de datos previamente")


            else:
                if self.cursor is None:
                    self.cursor = self.conexion.cursor()
                else:
                    print ("O cursor xa esta inicializado: " + self.cursor)


        except dbapi.Error as e:
            print (e)
        else:
            print ("Cursor preparado")


    def consultaSenParametros (self, consultaSQL):
        """Retorna unha lista cos rexistros dunha consulta realizada sen pasarlle parámetros.

        :param consultaSQL. Código da consulta sql a executar
        :return listaConsulta

        """

        listaConsulta = list()
        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:
                    self.cursor.execute(consultaSQL)

                    for fila in self.cursor.fetchall():
                        listaConsulta.append (fila)

        except dbapi.DatabaseError as e:
            print("Erro facendo a consulta: " + str(e))
            return None
        else:
            print("Consulta executada")
            return listaConsulta

    def consultaConParametros(self, consultaSQL, *parametros):
        """Retorna unha lista cos rexistros dunha consulta realizada pasandolle os parámetros.

        A consulta ten que estar definida con '?' na clausula where de SQL.

        :param consultaSQL. Código da consulta sql a executar
        :param *parametros. Lista de parámetros para introducir na consulta
        :return listaConsulta

        """

        listaConsulta = list()
        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:
                    self.cursor.execute(consultaSQL, parametros)

                    for fila in self.cursor.fetchall():
                        listaConsulta.append(fila)

        except dbapi.DatabaseError as e:
            print("Erro facendo a consulta AQUI: " + str(e))
            return None
        else:
            print("Consulta executada")
            return listaConsulta


    def añadirProducto(self, y):

        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:

                    lista = y

                    self.cursor.execute("INSERT INTO Producto VALUES( '" + str(lista[0]) +
                                        "' , '" + lista[1] +
                                        "' , '" + str(lista[2]) +
                                        "' , " + lista[3] +
                                        " , " + str(lista[4]) +
                                        " , " + str(lista[5]) +
                                        " , '" + lista[6] +"'")

        except dbapi.DatabaseError as e:
            print("Erro facendo insert producto: " + str(e))
            return None
        else:
            print("Operacion executada")

            self.conexion.commit()

    def modificarProducto(self, y):
        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:

                    lista = y

                    identificador = lista[0]

                    self.cursor.execute(
                        "UPDATE Producto SET NombreProducto= '" + lista[1] + "',CodigoProducto=" + str(lista[2]) + ",Proveedor='" + lista[3] + "',Precio=" + str(lista[4]) + ",Cantidad=" + str(lista[5]) + ",Descripcion='" + lista[6] + "' WHERE Identificador=  '"+identificador + "'")




        except dbapi.DatabaseError as e:
            print("Erro facendo insert producto: " + str(e))
            return None
        else:
            print("Operacion executada")

            self.conexion.commit()

    def añadirProveedor(self, y):

        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:

                    lista = y

                    self.cursor.execute("INSERT INTO Proveedor VALUES( '" + lista[0] +
                                        "' , '" + lista[1] +
                                        "' , '" + str(lista[2]) +
                                        "' , " + lista[3] +
                                        " , " + lista[4] +
                                        " , " + lista[5] +
                                        "' , '" + str(lista[6]) +
                                        "' , '" + str(lista[7]) +
                                        "' , '" + str(lista[8]) +
                                        "' , '" + str(lista[9]) + ")")

        except dbapi.DatabaseError as e:
            print("Erro facendo insert Proveedor: " + str(e))
            return None
        else:
            print("Operacion executada")

            self.conexion.commit()

    def modificarProveedor(self, y):
        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:

                    lista = y

                    identificador = lista[0]

                    self.cursor.execute(
                        "UPDATE Proveedor SET NombreProveedor= '" + lista[1] + "',Telefono='" + str(lista[2]) + "',CorreoElectronico=" +
                            lista[3] + ",Pais=" + lista[4] + ",Direccion=" + lista[5] + "',Numero='" + str(lista[6]) + "',CodigoPostal='" + str(lista[7]) + "',CIF='" + str(lista[8]) + "',DatosBancarios='" + str(lista[9]) + " WHERE Identificador= '" + identificador + "'")




        except dbapi.DatabaseError as e:
            print("Erro facendo insert Proveedor: " + str(e))
            return None
        else:
            print("Operacion executada")

            self.conexion.commit()

    def añadirSupermercados(self, y):

        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:

                    lista = y

                    self.cursor.execute("INSERT INTO Supermercados VALUES( '" + lista[0] +
                                        "' , '" + lista[1] +
                                        "' , '" + str(lista[2]) +
                                        "' , " + lista[3] +
                                        " , " + lista[4] +
                                        "' , '" + lista[5] +
                                        "' , '" + str(lista[6]) +
                                        "' , '" + str(lista[7]) +
                                        "' , '" + str(lista[8]) + ")")

        except dbapi.DatabaseError as e:
            print("Erro facendo insert supermercados: " + str(e))
            return None
        else:
            print("Operacion executada")

            self.conexion.commit()


    def modificarSupermercados(self, y):
        try:
            if self.conexion is None:
                print("Creando consulta: É necesario realizar a conexión a base de datos previamente")
            else:
                if self.cursor is None:
                    print("Creando consulta: É necesario realizar a creación do cursor previamente")
                else:

                    lista = y

                    identificador = lista[0]

                    self.cursor.execute(
                        "UPDATE Supermercados SET NombreSupermercado= '" + lista[1] + "',Telefono='" + str(lista[2]) + "',CorreoElectronico=" +
                            lista[3] + ",Pais=" + lista[4] + ",Direccion=" + lista[5] + "',Numero='" + str(lista[6]) + "',CodigoPostal='" + str(lista[7]) + "',CIF='" + str(lista[8]) + "',DatosBancarios='" + str(lista[9]) + " WHERE Identificador= '" + identificador + "'")




        except dbapi.DatabaseError as e:
            print("Erro facendo insert Supermercados: " + str(e))
            return None
        else:
            print("Operacion executada")

            self.conexion.commit()



