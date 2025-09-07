import tkinter as tk
from tkinter import messagebox, ttk
bandas = {}
class Participante:
    def __init__(self, institucion):
        self.institucion = institucion

    def mostrar_info(self):
        return f"NOMBRE DE INSTITUCIÓN: {self.institucion}"
class BandaEscolar(Participante):
    def __init__(self, institucion,categoria,ritmo, uniformidad, coreograf, alineacion, puntualidad,total):
        super().__init__(institucion)
        self.categoria = categoria
        self.ritmo = ritmo
        self.uniformidad = uniformidad
        self.coreograf = coreograf
        self.alineacion = alineacion
        self.puntualidad = puntualidad
        self.total = total

    def mostrar_info(self):
        return f"NOMBRE DE INSTITUCIÓN: {self.institucion} | Categoria: {self.categoria} | Ritmo: {self.ritmo} | Uniformidad: {self.uniformidad} | Coreografía: {self.coreograf} | Alineación: {self.alineacion} | Puntualidad: {self.puntualidad} | Total: {self.total}"
    def agregar_banda(self,nombre, banda):
        bandas[nombre] = banda
        for clave, datos in bandas.items():
            print(clave, datos.mostrar_info())
    def agregar_puntaje(self,nombre, ritmo, uniformidad, coreograf, alineacion, puntualidad,total):
        bandas[nombre].ritmo = ritmo
        bandas[nombre].uniformidad = uniformidad
        bandas[nombre].coreograf = coreograf
        bandas[nombre].alineacion = alineacion
        bandas[nombre].puntualidad = puntualidad
        bandas[nombre].total = total
        for clave, datos in bandas.items():
            print(clave, datos.mostrar_info())
class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("1024x720")
        self.ventana.resizable(False, False)

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
                messagebox.showerror("Error", "El nombre no puede estar vacío",parent=nueva) #Para todas mis validaciones busqué como implementar los mensajes de error en una ventana desplegable
                entrada1.delete(0, tk.END) # Este comentario complementa el de arriba, busqué como hacer que el messagebox no sobrepusiera la ventana principal
                entrada2.delete(0, tk.END)
                entrada3.delete(0, tk.END)
                return
            else:
                if nombre in bandas.keys():
                    messagebox.showerror("Error", "Esa banda ya está registrada",parent=nueva)
                    entrada1.delete(0, tk.END)
                    entrada2.delete(0, tk.END)
                    entrada3.delete(0, tk.END)
                    return
            if institucion.strip() == "":
                messagebox.showerror("Error", "El nombre de institución no puede estar vacío",parent=nueva)
                entrada1.delete(0, tk.END)
                entrada2.delete(0, tk.END)
                entrada3.delete(0, tk.END)
                return
            if categoria.strip() == "":
                messagebox.showerror("Error", "La categoría no puede estar vacía",parent=nueva)
                entrada1.delete(0, tk.END)
                entrada2.delete(0, tk.END)
                entrada3.delete(0, tk.END)
                return

            band = BandaEscolar(institucion,categoria,ritmo=None,uniformidad=None,coreograf=None,alineacion=None,puntualidad=None,total=None)
            band.agregar_banda(nombre,band)
            messagebox.showinfo("EXITO", "Se ha guardado la información!",parent=nueva) #Esto muestra el mensaje de confirmación de que se ha agregado la información
            nueva.destroy()

        boton_agregar = tk.Button(nueva, text="Agregar Banda", font=("Arial", 12, "bold"), command=agregar_banda)
        boton_agregar.grid(row=3, column=0, columnspan=2, pady=20)
        boton_salir = tk.Button(nueva, text="Salir",font=("Arial", 12, "bold"),  command=nueva.destroy)
        boton_salir.grid(row=3, column=1, columnspan=2, pady=20)
        nueva.bind("<Return>", agregar_banda) #Investigué que con esto puedo hacer que con el enter se ejecute lo mismo que con el boton agregar :D

    def registrar_evaluacion(self):
        if bandas:
            print("Se abrió la ventana: Registrar Evaluación")
            nueva = tk.Toplevel(self.ventana)
            nueva.title("Registrar Evaluacion")
            nueva.geometry("800x600")
            nueva.resizable(False, False)
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
            etiqueta6.grid(row=5, column=0, sticky="w", padx=10, pady=20)
            entrada6 = tk.Entry(nueva, font=("Arial", 12))
            entrada6.grid(row=5, column=1, sticky="w")

            def acreditar_punteo():
                try:
                    suma = 0
                    b = 0
                    nombre = entrada1.get().upper().strip()
                    ritmo = int(entrada2.get())
                    uniformidad = int(entrada3.get())
                    coreograf = int(entrada4.get())
                    alineacion = int(entrada5.get())
                    puntualidad = int(entrada6.get())
                    if nombre == "":
                        messagebox.showerror("Error", "El nombre no puede estar vacío", parent=nueva)
                        entrada1.delete(0, tk.END)
                        entrada2.delete(0, tk.END)
                        entrada3.delete(0, tk.END)
                        entrada4.delete(0, tk.END)
                        entrada5.delete(0, tk.END)
                        entrada6.delete(0, tk.END)
                        return
                    else:
                        if nombre in bandas.keys():
                            if 0 <= ritmo <= 2:
                                suma += ritmo
                                b += 1
                            if 0 <= uniformidad <= 2:
                                suma += uniformidad
                                b += 1
                            if 0 <= coreograf <= 2:
                                suma += coreograf
                                b += 1
                            if 0 <= alineacion <= 2:
                                suma += alineacion
                                b += 1
                            if 0 <= puntualidad <= 2:
                                suma += puntualidad
                                b += 1
                            if b == 5:
                                band = BandaEscolar(bandas[nombre].institucion,bandas[nombre].categoria,ritmo, uniformidad, coreograf, alineacion, puntualidad,suma)
                                band.agregar_puntaje(nombre, ritmo, uniformidad, coreograf, alineacion, puntualidad,suma)
                                messagebox.showinfo("EXITO", "Se ha acreditado la puntuación a la banda", parent=nueva)
                                entrada1.delete(0, tk.END)
                                entrada2.delete(0, tk.END)
                                entrada3.delete(0, tk.END)
                                entrada4.delete(0, tk.END)
                                entrada5.delete(0, tk.END)
                                entrada6.delete(0, tk.END)
                                nueva.destroy()
                            else:
                                messagebox.showerror("Error", "Algún dato no es correcto, reintene", parent=nueva)
                                entrada1.delete(0, tk.END)
                                entrada2.delete(0, tk.END)
                                entrada3.delete(0, tk.END)
                                entrada4.delete(0, tk.END)
                                entrada5.delete(0, tk.END)
                                entrada6.delete(0, tk.END)
                                entrada1.focus()

                        else:
                            messagebox.showerror("Error", "La banda no está registrada", parent=nueva)
                            entrada1.delete(0, tk.END)
                            entrada2.delete(0, tk.END)
                            entrada3.delete(0, tk.END)
                            entrada4.delete(0, tk.END)
                            entrada5.delete(0, tk.END)
                            entrada6.delete(0, tk.END)
                            entrada1.focus()
                            return
                except Exception as ex:
                    messagebox.showerror("ERROR CATASTROFICO!", ex, parent=nueva)
                    entrada1.delete(0, tk.END)
                    entrada2.delete(0, tk.END)
                    entrada3.delete(0, tk.END)
                    entrada4.delete(0, tk.END)
                    entrada5.delete(0, tk.END)
                    entrada6.delete(0, tk.END)
                    entrada1.focus()
                    return

            boton_agregar = tk.Button(nueva, text="Agregar Punteo", font=("Arial", 12, "bold"),command=acreditar_punteo)
            boton_agregar.grid(row=6, column=0, columnspan=2, pady=20)
            boton_salir = tk.Button(nueva, text="Salir", font=("Arial", 12, "bold"), command=nueva.destroy)
            boton_salir.grid(row=6, column=2, columnspan=2, pady=20)
            nueva.bind("<Return>", acreditar_punteo)
        else:
            messagebox.showwarning("Advertencia!","No hay bandas registradas")

    def listar_bandas(self):
        if not bandas:
            messagebox.showwarning("Advertencia!", "No hay bandas registradas", parent=self.ventana)
            return

        nueva = tk.Toplevel(self.ventana)
        nueva.title("Listado de Bandas")
        nueva.geometry("1500x500")
        nueva.resizable(False, False)

        columnas = ("Nombre", "Institución", "Categoría", "Total")
        tree = ttk.Treeview(nueva, columns=columnas, show="headings")#Busqué como mostrarlo por lista
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=280, anchor="center")

        for nombre, datos in bandas.items():
            tree.insert("", tk.END, values=(nombre, datos.institucion, datos.categoria,datos.total))

    def ver_ranking(self):
        if not bandas:
            messagebox.showinfo("Información", "No hay bandas registradas", parent=self.ventana)
            return

        nueva = tk.Toplevel(self.ventana)
        nueva.title("Ranking Final")
        nueva.geometry("1500x500")
        nueva.resizable(False, False)

        columnas = ("Nombre", "Institución","Categoria","Total")
        tree = ttk.Treeview(nueva, columns=columnas, show="headings")
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=280, anchor="center")

        # Ordenar por puntaje total de mayor a menor
        ranking = sorted(bandas.items(), key=lambda item: item[1].total if item[1].total is not None else 0,
                         reverse=True)
        for nombre, datos in ranking:
            tree.insert("", tk.END, values=(nombre, datos.institucion, datos.total if datos.total is not None else 0))


if __name__ == "__main__":
    ConcursoBandasApp()