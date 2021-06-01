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
                  "on_AccederUs_activate": self.on_EntrarBoton_clicked,
                  "on_AccederCo_activate": self.on_EntrarBoton_clicked,
                  "on_EntrarBoton_delete_event": Gtk.main_quit}

        builder.connect_signals(sinais)

        Acceder = builder.get_object("Acceder")
        Acceder.show_all()

        Datos = builder.get_object("Datos")
        Datos.show_all()
        Datos.hide()


        self.AccederUs = builder.get_object("AccederUs")
        self.AccederUsuario = builder.get_object("AccederUsuario")
        self.AccederCo = builder.get_object("AccederCo")
        self.Accederontraseña = builder.get_object("AccederContraseña")

    def on_EntrarBoton_clicked(self, boton):
        us = self.AccederUs.get_text()
        co = self.AccederCo.get_text()
        print(us, co)



if __name__ == "__main__":
    recudi()
    Gtk.main()