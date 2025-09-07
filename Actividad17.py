import tkinter as tk
from tkinter import messagebox
bandas = {}
class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("1024x720")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify= "center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        print("Se abrió la ventana: Inscribir Banda")
        nueva = tk.Toplevel(self.ventana)
        nueva.title("Inscribir Banda")
        nueva.geometry("800x600")
        etiqueta1 = tk.Label(nueva, text="Nombre de la banda: ", font=("Arial", 12))
        etiqueta1.grid(row=0, column=0, sticky="w", padx=10, pady=20)
        entrada1 = tk.Entry(nueva, font=("Arial", 12))
        entrada1.focus() #Este también investigué que con este hago que de una vez esté en el primer campo listo para escribir y no tenga que darle click a cada campo
        entrada1.grid(row=0, column=1, sticky="w")
        etiqueta2 = tk.Label(nueva, text="Institución de la banda: ", font=("Arial", 12))
        etiqueta2.grid(row=1, column=0, sticky="w", padx=10, pady=20)
        entrada2 = tk.Entry(nueva, font=("Arial", 12))
        entrada2.grid(row=1, column=1, sticky="w")
        etiqueta3 = tk.Label(nueva, text="Categoría de la banda (Primaria, Básico, Diversificado): ", font=("Arial", 12))
        etiqueta3.grid(row=2, column=0, sticky="w", padx=10, pady=20)
        entrada3 = tk.Entry(nueva, font=("Arial", 12))
        entrada3.grid(row=2, column=1, sticky="w")
        def agregar_banda(event=None):
            nombre = entrada1.get().upper()
            institucion = entrada2.get().lower()
            categoria = entrada3.get().lower()

            if nombre.strip() == "":
                messagebox.showerror("Error", "El nombre no puede estar vacío") #Para todas mis validaciones busqué como implementar los mensajes de error en una ventana desplegable
                entrada1.delete(0, tk.END)
                entrada2.delete(0, tk.END)
                entrada3.delete(0, tk.END)
                return
            else:
                if nombre in bandas.keys():
                    messagebox.showerror("Error", "Esa banda ya está registrada")
                    entrada1.delete(0, tk.END)
                    entrada2.delete(0, tk.END)
                    entrada3.delete(0, tk.END)
                    return
            if institucion.strip() == "":
                messagebox.showerror("Error", "El nombre de institución no puede estar vacío")
                entrada1.delete(0, tk.END)
                entrada2.delete(0, tk.END)
                entrada3.delete(0, tk.END)
                return
            if categoria.strip() == "":
                messagebox.showerror("Error", "La categoría no puede estar vacía")
                entrada1.delete(0, tk.END)
                entrada2.delete(0, tk.END)
                entrada3.delete(0, tk.END)
                return

            bandas[nombre] = {
                "institucion": institucion,
                "categoria": categoria,
                "punteo": {}
            }

            nueva.destroy()

        boton_agregar = tk.Button(nueva, text="Agregar Banda", font=("Arial", 12, "bold"), command=agregar_banda)
        boton_agregar.grid(row=3, column=0, columnspan=2, pady=20)
        boton_salir = tk.Button(nueva, text="Salir",font=("Arial", 12, "bold"),  command=nueva.destroy)
        boton_salir.grid(row=3, column=1, columnspan=2, pady=20)
        nueva.bind("<Return>", agregar_banda) #Investigué que con esto puedo hacer que con el enter se ejecute lo mismo que con el boton agregar :D

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        nueva = tk.Toplevel(self.ventana)
        nueva.title("Registrar Evaluacion")
        nueva.geometry("800x600")
        etiqueta1 = tk.Label(nueva, text="Nombre de la banda: ", font=("Arial", 12))
        etiqueta1.grid(row=0, column=0, sticky="w", padx=10, pady=20)
        entrada1 = tk.Entry(nueva, font=("Arial", 12))
        entrada1.focus()
        entrada1.grid(row=0, column=1, sticky="w")
        etiqueta2 = tk.Label(nueva, text="Punteo de Ritmo (0-2): ", font=("Arial", 12))
        etiqueta2.grid(row=1, column=0, sticky="w", padx=10, pady=20)
        entrada2 = tk.Entry(nueva, font=("Arial", 12))
        entrada2.grid(row=1, column=1, sticky="w")
        etiqueta3 = tk.Label(nueva, text="Punteo de Uniformidad (0-2): ", font=("Arial", 12))
        etiqueta3.grid(row=2, column=0, sticky="w", padx=10, pady=20)
        entrada3 = tk.Entry(nueva, font=("Arial", 12))
        entrada3.grid(row=2, column=1, sticky="w")
        etiqueta4 = tk.Label(nueva, text="Punteo de Coreografía (0-2): ", font=("Arial", 12))
        etiqueta4.grid(row=3, column=0, sticky="w", padx=10, pady=20)
        entrada4 = tk.Entry(nueva, font=("Arial", 12))
        entrada4.grid(row=3, column=1, sticky="w")
        etiqueta5 = tk.Label(nueva, text="Punteo de Alineación (0-2): ", font=("Arial", 12))
        etiqueta5.grid(row=4, column=0, sticky="w", padx=10, pady=20)
        entrada5 = tk.Entry(nueva, font=("Arial", 12))
        entrada5.grid(row=4, column=1, sticky="w")
        etiqueta6 = tk.Label(nueva, text="Punteo de Puntualidad (0-2): ", font=("Arial", 12))
        etiqueta6.grid(row=4, column=0, sticky="w", padx=10, pady=20)
        entrada6 = tk.Entry(nueva, font=("Arial", 12))
        entrada6.grid(row=4, column=1, sticky="w")


        boton_agregar = tk.Button(nueva, text="Agregar Punteo", font=("Arial", 12, "bold"))
        boton_agregar.grid(row=6, column=0, columnspan=2, pady=20)
        boton_salir = tk.Button(nueva, text="Salir", font=("Arial", 12, "bold"), command=nueva.destroy)
        boton_salir.grid(row=6, column=2, columnspan=2, pady=20)
        #nueva.bind("<Return>", agregar_punteos)

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        nueva = tk.Toplevel(self.ventana)
        nueva.title("Registrar Evaluacion")
        nueva.geometry("800x600")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        nueva = tk.Toplevel(self.ventana)
        nueva.title("Registrar Evaluacion")
        nueva.geometry("800x600")


if __name__ == "__main__":
    ConcursoBandasApp()