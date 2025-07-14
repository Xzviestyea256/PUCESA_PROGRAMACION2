print("-------------")
print("Nombre: Paul Sanchez")
print("Fecha: 29 de junio, 2025")
print("Materia: Programación II")
print("Tema: Nodo Doble")

class NodoDoble:
    #Creación de datos necesarios de la calse para el funcionamiento del programa
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class HistorialNavegador:
    def __init__(self):
        self.actual = None

    def visitar_pagina(self, url):
        #Funcion que  muestra las pagina que se visita dentro del programa
        #Se asigna el valor de la pagina a la variable para que sea la primera en ser ingresada,
        #y se guarda en una lista todas las paginas visitadas
        nuevo = NodoDoble(url)
        if self.actual:
            nuevo.anterior = self.actual
            self.actual.siguiente = nuevo
        self.actual = nuevo
        print(f"Pagina visitada:", url)
        print("")
        
    def atras(self):
        #Función que retrocede las paginas visitadas en 1, mostrando la pagina anterior
        #a la pagina actual
        print("Retrocediendo una página")
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"Página actual: {self.actual.dato}")
        else:
            print("No hay páginas anteriores.")

        print("")

    def adelante(self):
        #Función que avanza las paginas visitadas en 1, mostrando la pagina siguiente
        #a la pagina actual
        print("Avanzando una página")
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"Página actual: {self.actual.dato}")
        else:
            print("No hay páginas siguientes.")
        print("")

    def mostrar_historial(self):
        #Hace un recorrido por todas los datos ingresados para mostrarlos de forma de historial
        #creando la variable "actual", para no tener conflictos con la lista princial de elementos    
        print("Historial completo:")
        actual = self.actual
        while actual and actual.anterior:
            actual = actual.anterior
        while actual:
            print(actual.dato, end = " <-> ")
            actual = actual.siguiente
        print("Null")
        print("")

    def pagina_actual(self):
        #Muestra la pagina que se encuentre almacenada en "self.actual", para mostrar la pagina 
        #en la que se encuentra
        if self.actual:
            return self.actual.dato
        else:
            return "No hay página actual."
    print("")

nav = HistorialNavegador()

nav.visitar_pagina("google.com")
nav.visitar_pagina("youtube.com")
nav.visitar_pagina("newgrounds.com")
nav.visitar_pagina("github.com")
nav.visitar_pagina("stackoverflow.com")
nav.visitar_pagina("lostmediawiki.com")
nav.visitar_pagina("khinsider.com")

nav.mostrar_historial()
nav.atras()
nav.adelante()
nav.adelante()

nav.mostrar_historial()
print("Página actual:", nav.pagina_actual()) 