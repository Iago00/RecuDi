import gi
import conexionBD
from conexionBD import ConexionBD
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class recudi():
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file ("recudi.glade")

        sinais = {"on_btnRecudi_clicked": self.on_btnRecudi_clicked,
                  "on_txtRecudi_activate": self.on_btnRecudi_clicked,
                  "on_winRecudi_delete_event": Gtk.main_quit}

        builder.connect_signals(sinais)

        Acceder = builder.get_object("Acceder")
        Acceder.show_all()

        Datos = builder.get_object("Datos")
        Datos.show_all()


        self.txtRecudi = builder.get_object("txtRecudi")
        self.lblRecudi = builder.get_object("lblRecudi")

    def on_btnRecudi_clicked(self, boton):
        nome = self.txtRecudi.get_text()
        print(nome)


if __name__ == "__main__":
    recudi()
    Gtk.main()