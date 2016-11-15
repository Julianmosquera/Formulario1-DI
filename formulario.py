import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class formulario(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Formulario")
        self.set_border_width(4)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.paxina1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.paxina1.set_border_width(10)

        self.paxina1.add(Gtk.Label("NIF"))
        self.paxina1.add(Gtk.Label("Denominacion"))
        self.paxina1.add(Gtk.Label("Provincia"))
        self.paxina1.add(Gtk.Label("Finalidade"))
        check=Gtk.CheckButton("Publica")
        self.paxina1.add(check)
        

        self.paxina2=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        boton1=Gtk.Button("Anterior")
        boton2 = Gtk.Button("Siguiente")
        boton3= Gtk.Button("Modificar")
        
        self.paxina2.add(boton1)
        self.paxina2.add(boton2)
        self.paxina2.add(boton3)
        self.paxina1.add(self.paxina2)
        entry=Gtk.Entry()
        self.paxina1.add(entry)

        









        self.notebook.append_page(self.paxina1, Gtk.Label('Editar'))

        self.paxina3 = Gtk.Box()
        self.paxina3.set_border_width(10)
        self.paxina3.add(Gtk.Label("Visualizar"))
        self.notebook.append_page(self.paxina3, Gtk.Label("Visualizar"))



        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


aplicacion=formulario()
Gtk.main()
