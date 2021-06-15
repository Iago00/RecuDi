import gi
import conexionBD
from conexionBD import ConexionBD
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class recudi():
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file ("recudi.glade")

        sinais = {"on_EntrarBoton_clicked": self.on_EntrarBoton_clicked,

                  "on_ProdAñadir_clicked": self.on_ProdAñadir_clicked,
                  "on_ProdModificar_clicked": self.on_ProdModificar_clicked,
                  "on_ProdEliminar_clicked": self.on_ProdEliminar_clicked,
                  "on_ProdConsultar_clicked": self.on_ProdConsultar_clicked,


                  "on_ProvAñadir_clicked": self.on_ProvAñadir_clicked,
                  "on_ProvModificar_clicked": self.on_ProvModificar_clicked,
                  "on_ProvEliminar_clicked": self.on_ProvEliminar_clicked,
                  "on_ProvConsultar_clicked": self.on_ProvConsultar_clicked,


                  "on_SuperAñadir_clicked": self.on_SuperAñadir_clicked,
                  "on_SuperModificar_clicked": self.on_SuperModificar_clicked,
                  "on_SuperEliminar_clicked": self.on_SuperEliminar_clicked,
                  "on_SuperConsultar_clicked": self.on_SuperConsultar_clicked }



        builder.connect_signals(sinais)

        #Producto

        self.ProdId = builder.get_object("ProdId")
        self.ProdNo = builder.get_object("ProdNo")
        self.ProdCo = builder.get_object("ProdCo")
        self.ProdDe = builder.get_object("ProdDe")
        self.ProdPr = builder.get_object("ProdPr")
        self.ProdCa = builder.get_object("ProdCa")
        self.ProdPro = builder.get_object("ProdPro")
        self.ProductoTree = builder.get_object("ProductoTree")

        #self.selection = self.ProductoTree.get_selection()

        modelo_tabla = Gtk.ListStore(int, str, int, str, int, int, str)

        bD = ConexionBD("recu.dat")
        lispro = bD.consultaSenParametros("SELECT * FROM Producto")

        for ax in lispro:

            modelo_tabla.append(ax)

        #Proveedor

        self.ProvId = builder.get_object("ProvId")
        self.ProvNo = builder.get_object("ProvNo")
        self.ProvTe = builder.get_object("ProvTe")
        self.ProvCo = builder.get_object("ProvCo")
        self.ProvPa = builder.get_object("ProvPa")
        self.ProvDi = builder.get_object("ProvDi")
        self.ProvNu = builder.get_object("ProvNu")
        self.ProvCod = builder.get_object("ProvCod")
        self.ProvCi = builder.get_object("ProvCi")
        self.ProvDa = builder.get_object("ProvDa")
        self.ProveedorTree = builder.get_object("ProveedorTree")
        #self.selection = self.ProveedorTree.get_selection()
        modelo_tabla2 = Gtk.ListStore(int, str, int, str, str, str, int, int, int, int)

        bD = ConexionBD("recu.dat")
        lisprov = bD.consultaSenParametros("SELECT * FROM Proveedor")

        for ax in lisprov:
            modelo_tabla2.append(ax)


        #Supermercados

        self.SuperId = builder.get_object("SuperId")
        self.SuperNo = builder.get_object("SuperNo")
        self.SuperTe = builder.get_object("SuperTe")
        self.SuperPa = builder.get_object("SuperPa")
        self.SuperCo = builder.get_object("SuperCo")
        self.SuperDi = builder.get_object("SuperDi")
        self.SuperCod = builder.get_object("SuperCod")
        self.SuperCi = builder.get_object("SuperCi")
        self.SuperNu = builder.get_object("SuperNu")
        self.SupermercadosTree = builder.get_object("SupermercadosTree")
        #self.selection = self.SupermercadosTree.get_selection()
        modelo_tabla3 = Gtk.ListStore(int, str, int, str, str, str, int, int, int)

        bD = ConexionBD("recu.dat")
        lissuper = bD.consultaSenParametros("SELECT * FROM Supermercados")

        for ax in lissuper:
            modelo_tabla3.append(ax)


        # Producto
        treeProd = Gtk.TreeView(modelo_tabla)
        seleccion = treeProd.get_selection()
        seleccion.connect("changed", self.treevcli_selec_chan)



        for x, columnas in enumerate(["Identificador", "NombreProducto", "CodigoProducto", "Proveedor", "Precio", "Cantidad", "Descripcion"]):
            celda = Gtk.CellRendererText()
            columnacli = Gtk.TreeViewColumn(columnas, celda, text=x)
            celda.props.editable = True


            celda.connect("edited", self.celda_edit, x, modelo_tabla)


            self.ProductoTree.append_column(columnacli)

        self.ProductoTree.set_model(modelo_tabla)
        self.ProductoTree.set_reorderable(True)

        #Proveedor
        treeProv = Gtk.TreeView(modelo_tabla2)
        seleccion = treeProv.get_selection()
        seleccion.connect("changed", self.treevprov_selec_chan)


        for x, columnas in enumerate(["Identificador", "NombreProveedor", "Telefono", "CorreoElectronico", "Pais", "Direccion", "Numero", "CodigoPostal", "CIF", "DatosBancarios"]):
            celda = Gtk.CellRendererText()
            columnacli = Gtk.TreeViewColumn(columnas, celda, text=x)
            celda.props.editable = True


            celda.connect("edited", self.celda_edit, x, modelo_tabla2)


            self.ProveedorTree.append_column(columnacli)

        self.ProveedorTree.set_model(modelo_tabla2)
        self.ProveedorTree.set_reorderable(True)

        #Supermercados
        treeSuper = Gtk.TreeView(modelo_tabla3)
        seleccion = treeSuper.get_selection()
        seleccion.connect("changed", self.treevsuper_selec_chan)

        for x, columnas in enumerate(["Identificador", "NombreSupermercado", "Telefono", "CorreoElectronico", "Pais", "Direccion", "Numero", "CodigoPostal", "CIF"]):
            celda = Gtk.CellRendererText()
            columnacli = Gtk.TreeViewColumn(columnas, celda, text=x)
            celda.props.editable = True

            celda.connect("edited", self.celda_edit, x, modelo_tabla3)

            self.SupermercadosTree.append_column(columnacli)

        self.SupermercadosTree.set_model(modelo_tabla3)
        self.SupermercadosTree.set_reorderable(True)


        #34
        self.Acceder = builder.get_object("Acceder")
        self.Acceder.show_all()

        self.Datos = builder.get_object("Datos")
        self.Datos.hide()


        self.AccederUs = builder.get_object("AccederUs")
        self.AccederUsuario = builder.get_object("AccederUsuario")
        self.AccederCo = builder.get_object("AccederCo")
        self.Accederontraseña = builder.get_object("AccederContraseña")

    def celda_edit(self, celda, fila, texto, columna, modelo):
            modelo[fila][columna] = texto

    def celda_change(self, combo, fila, texto, modelo, columna):

        modelo[fila][columna] = texto

    def on_celda_edite(self, celda, fila, texto, columna, modelo):
        modelo[fila][columna] = texto

    #Producto
    def treevcli_selec_chan(self, selection):

        modelo, fila = selection.get_selected()
        if fila is not None:
            self.ProdId.set_text(str(modelo[fila][0]))
            self.ProdNo.set_text(modelo[fila][1])
            self.ProdCo.set_text(str(modelo[fila][2]))
            self.ProdDe.set_text(modelo[fila][3])
            self.ProdPr.set_text(str(modelo[fila][4]))
            self.ProdCa.set_text(str(modelo[fila][5]))
            self.ProdPro.set_text(modelo[fila][6])

    #Proveedor
    def treevprov_selec_chan(self, selection):

        modelo, fila = selection.get_selected()
        if fila is not None:
            self.ProvId.set_text(str(modelo[fila][0]))
            self.ProvNo.set_text(modelo[fila][1])
            self.ProvTe.set_text(str(modelo[fila][2]))
            self.ProvCo.set_text(modelo[fila][3])
            self.ProvPa.set_text(modelo[fila][4])
            self.ProvDi.set_text(modelo[fila][5])
            self.ProvNu.set_text(str(modelo[fila][6]))
            self.ProvCod.set_text(str(modelo[fila][7]))
            self.ProvCi.set_text(str(modelo[fila][8]))
            self.ProvDa.set_text(str(modelo[fila][9]))

    #Supermercados
    def treevsuper_selec_chan(self, selection):

        modelo, fila = selection.get_selected()
        if fila is not None:
            self.ProvId.set_text(str(modelo[fila][0]))
            self.ProvNo.set_text(modelo[fila][1])
            self.ProvTe.set_text(str(modelo[fila][2]))
            self.ProvCo.set_text(modelo[fila][3])
            self.ProvPa.set_text(modelo[fila][4])
            self.ProvDi.set_text(modelo[fila][5])
            self.ProvNu.set_text(str(modelo[fila][6]))
            self.ProvCod.set_text(str(modelo[fila][7]))
            self.ProvCi.set_text(str(modelo[fila][8]))
            self.ProvDa.set_text(str(modelo[fila][9]))


    def on_EntrarBoton_clicked(self, boton):
        us = self.AccederUs.get_text()
        co = self.AccederCo.get_text()
        print(us, co)
        self.Datos.show_all()
        self.Acceder.hide()

    def on_ProdConsultar_clicked(self, boton):
        bD = ConexionBD("recu.dat")
        identificador = self.ProdId.get_text()
        listaProducto = bD.consultaConParametros("SELECT * FROM Producto WHERE Identificador=?", int(identificador))
        for consulta in listaProducto:
            self.ProdNo.set_text(consulta[1])
            self.ProdCo.set_text(str(consulta[2]))
            self.ProdPr.set_text(consulta[3])
            self.ProdCa.set_text(str(consulta[4]))
            self.ProdPro.set_text(str(consulta[5]))

        self.ProdDe.set_text("consulta realizada")

    def on_ProdAñadir_clicked(self, boton):
        bD = ConexionBD("recu.dat")
        iden = self.ProdId.get_text()
        listaProducto = bD.consultaConParametros("SELECT * FROM Producto WHERE Identificador=?", iden)

        def is_emply(compo):
            if len(compo) == 0:
                return True
            return False

        listaP = list()

        if is_emply(listaProducto) == True:
            listaP.append(self.ProdId.get_text())
            listaP.append(self.ProdNo.get_text())
            listaP.append(self.ProdCo.get_text())
            listaP.append(self.ProdPr.get_text())
            listaP.append(self.ProdCa.get_text())
            listaP.append(self.ProdPro.get_text())

            bD.añadirProducto(listaP)
        else:

            print("Producto repetido")


    def on_ProdModificar_clicked(self, boton):
        bD = ConexionBD("recu.dat")
        identificador = self.ProdId.get_text()
        listaProducto = bD.consultaConParametros("SELECT * FROM Producto WHERE Identificador=?", identificador)

        def is_emply(x):
            if len(x) == 0:
                return True
            return False

        listaP = list()

        if is_emply(listaProducto) == False:
            listaP.append(self.ProdId.get_text())
            listaP.append(self.ProdNo.get_text())
            listaP.append(self.ProdCo.get_text())
            listaP.append(self.ProdPr.get_text())
            listaP.append(self.ProdCa.get_text())
            listaP.append(self.ProdPro.get_text())
            listaP.append(self.ProdDe.get_text())



            bD.modificarProducto(listaP)

    def on_ProdEliminar_clicked(self, boton):
        print("")



    def on_ProvConsultar_clicked(self, boton):
        bD = ConexionBD("recu.dat")
        identificador = self.ProvId.get_text()
        listaProveedor = bD.consultaConParametros("SELECT * FROM Proveedor WHERE Identificador=?", identificador)
        for consulta in listaProveedor:
            self.ProvNo.set_text(consulta[1])
            self.ProvTe.set_text(str(consulta[2]))
            self.ProvCo.set_text(consulta[3])
            self.ProvPa.set_text(consulta[4])
            self.ProvDi.set_text(consulta[5])
            self.ProvNu.set_text(str(consulta[6]))
            self.ProvCod.set_text(str(consulta[7]))
            self.ProvCi.set_text(str(consulta[8]))
            self.ProvDa.set_text(str(consulta[9]))

    def on_ProvAñadir_clicked(self, boton):
        bD = ConexionBD("recu.dat")
        identificador = self.ProvId.get_text()
        listaProveedor = bD.consultaConParametros("SELECT * FROM Proveedor WHERE Identificador=?", identificador)

        def is_emply(x):
            if len(x) == 0:
                return True
            return False

        listaPr = list()



        if is_emply(listaProveedor) == True:
            listaPr.append(self.ProvId.get_text())
            listaPr.append(self.ProvNo.get_text())
            listaPr.append(self.ProvTe.get_text())
            listaPr.append(self.ProvCo.get_text())
            listaPr.append(self.ProvPa.get_text())
            listaPr.append(self.ProvDi.get_text())
            listaPr.append(self.ProvNu.get_text())
            listaPr.append(self.ProvCod.get_text())
            listaPr.append(self.ProvCi.get_text())
            listaPr.append(self.ProvDa.get_text())

            bD.añadirProveedor(listaPr)

        else:

            print("Producto repetido")




    def on_ProvModificar_clicked(self, boton):
        bD = ConexionBD("recu.dat")
        identificador = self.ProdId.get_text()
        listaProveedor = bD.consultaConParametros("SELECT * FROM Producto WHERE Identificador=?", identificador)

        def is_emply(x):
            if len(x) == 0:
                return True
            return False

        listaPr = list()

        if is_emply(listaProveedor) == False:
            listaPr.append(self.ProvId.get_text())
            listaPr.append(self.ProvNo.get_text())
            listaPr.append(self.ProvTe.get_text())
            listaPr.append(self.ProvCo.get_text())
            listaPr.append(self.ProvPa.get_text())
            listaPr.append(self.ProvDi.get_text())
            listaPr.append(self.ProvNu.get_text())
            listaPr.append(self.ProvCod.get_text())
            listaPr.append(self.ProvCi.get_text())
            listaPr.append(self.ProvDa.get_text())

            bD.modificarProveedor(listaPr)

    def on_ProvEliminar_clicked(self, boton):
        print("")


    def on_SuperConsultar_clicked(self, boton):
            bD = ConexionBD("recu.dat")
            identificador = self.SuperId.get_text()
            listaSupermercados = bD.consultaConParametros("SELECT * FROM Supermercados WHERE Identificador=?", identificador)
            for consulta in listaSupermercados:
                print("consulta")
                self.SuperNo.set_text(consulta[1])
                self.SuperTe.set_text(str(consulta[2]))
                self.SuperPa.set_text(consulta[3])
                self.SuperCo.set_text(consulta[4])
                self.SuperDi.set_text(consulta[5])
                self.SuperCod.set_text(str(consulta[6]))
                self.SuperCi.set_text(str(consulta[7]))
                self.SuperNu.set_text(str(consulta[8]))

    def on_SuperAñadir_clicked(self, boton):
        bD = ConexionBD("recu.dat")
        identificador = self.SuperId.get_text()
        listaSupermercados = bD.consultaConParametros("SELECT * FROM Supermercados WHERE Identificador=?", identificador)

        def is_emply(x):
            if len(x) == 0:
                return True
            return False

        listaS = list()

        if is_emply(listaSupermercados) == True:
            listaS.append(self.SuperId.get_text())
            listaS.append(self.SuperNo.get_text())
            listaS.append(self.SuperTe.get_text())
            listaS.append(self.SuperPa.get_text())
            listaS.append(self.SuperCo.get_text())
            listaS.append(self.SuperDi.get_text())
            listaS.append(self.SuperCod.get_text())
            listaS.append(self.SuperCi.get_text())
            listaS.append(self.SuperNu.get_text())


            bD.añadirSupermercados(listaS)

        else:

            print("Producto repetido")

    def on_SuperModificar_clicked(self, boton):
        bD = ConexionBD("recu.dat")
        identificador = self.SuperId.get_text()
        listaSupermercados = bD.consultaConParametros("SELECT * FROM Supermercados WHERE Identificador=?", identificador)

        def is_emply(x):
            if len(x) == 0:
                return True
            return False

        listaS = list()

        if is_emply(listaSupermercados) == False:
            listaS.append(self.SuperId.get_text())
            listaS.append(self.SuperNo.get_text())
            listaS.append(self.SuperTe.get_text())
            listaS.append(self.SuperPa.get_text())
            listaS.append(self.SuperCo.get_text())
            listaS.append(self.SuperDi.get_text())
            listaS.append(self.SuperCod.get_text())
            listaS.append(self.SuperCi.get_text())
            listaS.append(self.SuperNu.get_text())

            bD.modificarSupermercados(listaS)

    def on_SuperEliminar_clicked(self, boton):
     print("")


if __name__ == "__main__":
    recudi()
    Gtk.main()