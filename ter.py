import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class CustomButton(tk.Canvas):
    def __init__(self, parent, text, command=None, width=120, height=35, corner_radius=10, bg="#2196F3", fg="white"):
        super().__init__(parent, width=width, height=height, bg=parent["bg"], highlightthickness=0)
        self.command = command
        self.bg = bg
        self.text = text  # Guardamos el texto como atributo de la clase
        
        # Crear el botón redondeado
        self.create_rounded_button(width, height, corner_radius, text, bg, fg)
        
        # Vincular eventos
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)

    def create_rounded_button(self, width, height, corner_radius, text, bg, fg):
        # Crear forma redondeada
        self.create_rounded_rectangle(0, 0, width, height, corner_radius, fill=bg, outline="")
        
        # Agregar texto
        font = tkFont.Font(family="Arial", size=10)
        self.create_text(width/2, height/2, text=text, fill=fg, font=font)

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def on_enter(self, e):
        self.delete("all")
        self.create_rounded_button(self.winfo_width(), self.winfo_height(), 10, 
                                 self.text,  # Usamos el texto guardado
                                 "#1976D2", "white")

    def on_leave(self, e):
        self.delete("all")
        self.create_rounded_button(self.winfo_width(), self.winfo_height(), 10, 
                                 self.text,  # Usamos el texto guardado
                                 self.bg, "white")

    def on_click(self, e):
        if self.command:
            self.command()

class VentanaTkinter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación con Tkinter")
        self.geometry("400x480")
        self.configure(bg="#f0f0f0")  # Color de fondo

        # ─────────────────────── CREACIÓN DE WIDGETS ───────────────────────
        
        # Etiqueta
        tk.Label(self, text="Nombre:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)

        # Entrada de texto
        self.entrada = tk.Entry(self, width=30)
        self.entrada.pack(pady=5)

        # Botón redondeado personalizado
        CustomButton(self, text="Mostrar", command=self.mostrar_texto).pack(pady=5)

        # Área de texto
        self.texto = tk.Text(self, height=4, width=40)
        self.texto.pack(pady=5)

        # Casilla de verificación
        self.var_check = tk.BooleanVar()
        self.check = tk.Checkbutton(self, text="Aceptar términos", 
                                  variable=self.var_check, bg="#f0f0f0")
        self.check.pack(pady=5)

        # RadioButton
        self.var_radio = tk.StringVar(value="Opción 1")
        tk.Radiobutton(self, text="Opción 1", variable=self.var_radio, 
                      value="Opción 1", bg="#f0f0f0").pack()
        tk.Radiobutton(self, text="Opción 2", variable=self.var_radio, 
                      value="Opción 2", bg="#f0f0f0").pack()

        # Lista desplegable
        self.combo = ttk.Combobox(self, 
            values=["Python", "Java", "C++", "JavaScript", "PHP", "Ruby"])
        self.combo.pack(pady=5)
        self.combo.set("Selecciona un lenguaje")

        # ───────────────────── MINI FORMULARIO DE INICIO DE SESIÓN ─────────────────────

        tk.Label(self, text="Inicio de Sesión", 
                font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)
        tk.Label(self, text="Usuario:", bg="#f0f0f0").pack()
        self.usuario = tk.Entry(self, width=30)
        self.usuario.pack()

        tk.Label(self, text="Contraseña:", bg="#f0f0f0").pack()
        self.contraseña = tk.Entry(self, width=30, show="*")
        self.contraseña.pack()

        CustomButton(self, text="Iniciar Sesión", 
                    command=self.iniciar_sesion).pack(pady=10)

    def mostrar_texto(self):
        self.texto.insert(tk.END, f"Hola, {self.entrada.get()}!\n")

    def iniciar_sesion(self):
        usuario = self.usuario.get()
        contraseña = self.contraseña.get()
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")

if __name__ == "__main__":
    app = VentanaTkinter()
    app.mainloop()