import tkinter as tk
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
        entrada1.grid(row=0, column=1, sticky="w")
        etiqueta2 = tk.Label(nueva, text="Institución de la banda: ", font=("Arial", 12))
        etiqueta2.grid(row=1, column=0, sticky="w", padx=10, pady=20)
        entrada2 = tk.Entry(nueva, font=("Arial", 12))
        entrada2.grid(row=1, column=1, sticky="w")
        etiqueta3 = tk.Label(nueva, text="Categoría de la banda (Primaria, Básico, Diversificado): ", font=("Arial", 12))
        etiqueta3.grid(row=2, column=0, sticky="w", padx=10, pady=20)
        entrada3 = tk.Entry(nueva, font=("Arial", 12))
        entrada3.grid(row=2, column=1, sticky="w")
        etiqueta_error = tk.Label(nueva, text="", font=("Arial", 12, "bold"), fg="red")
        etiqueta_error.grid(row=5, column=0, columnspan=2)
        def agregar_banda():
            nombre = entrada1.get().upper()
            institucion = entrada2.get().lower()
            categoria = entrada3.get().lower()

            if nombre.strip() == "":
                etiqueta_error.config(text="Error: El nombre no puede estar vacío")
                entrada1.delete(0, tk.END)
                entrada2.delete(0, tk.END)
                entrada3.delete(0, tk.END)
                return
            else:
                if nombre in bandas.keys():
                    etiqueta_error.config(text="Error: Esa banda ya está registrada")
                    entrada1.delete(0, tk.END)
                    entrada2.delete(0, tk.END)
                    entrada3.delete(0, tk.END)
                    return
            if institucion.strip() == "":
                etiqueta_error.config(text="Error: El nombre de institución no puede estar vacío")
                entrada1.delete(0, tk.END)
                entrada2.delete(0, tk.END)
                entrada3.delete(0, tk.END)
                return
            if categoria.strip() == "":
                etiqueta_error.config(text="Error: La categoría no puede estar vacía")
                entrada1.delete(0, tk.END)
                entrada2.delete(0, tk.END)
                entrada3.delete(0, tk.END)
                return

            bandas[nombre] = {
                "institucion": institucion,
                "categoria": categoria
            }

            print(f"Banda agregada: {nombre} -> {bandas[nombre]}")
            nueva.destroy()

        boton_agregar = tk.Button(nueva, text="Agregar Banda", font=("Arial", 12, "bold"), command=agregar_banda)
        boton_agregar.grid(row=3, column=0, columnspan=2, pady=20)
        boton_salir = tk.Button(nueva, text="Salir",font=("Arial", 12, "bold"),  command=nueva.destroy)
        boton_salir.grid(row=3, column=1, columnspan=2, pady=20)

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        nueva = tk.Toplevel(self.ventana)
        nueva.title("Registrar Evaluacion")
        nueva.geometry("800x600")

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