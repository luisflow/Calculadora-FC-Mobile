# Calculadora Compra y venta jugadores FC Mobile (coinfcm) 2.0 Modo Ventana por Luis Flow - https://github.com/luisflow/Calculadora-FC-Mobile

import webbrowser
import tkinter as tk
from tkinter import ttk
#from tkinter import font
from tkinter import messagebox


def calcular():
    try:
        preciocompra = float(entry_preciocompra.get())
        numjugadorescompra = int(entry_numjugadorescompra.get())
        precioventa = float(entry_precioventa.get())
        porcventa = ((10)/100)
        ganancia = ((precioventa - (precioventa * porcventa)) - (preciocompra * numjugadorescompra))
        
        resultado_compra = preciocompra * numjugadorescompra
        resultado_venta = precioventa - (precioventa * porcventa)
        
        label_resultado_compra.config(text=f"Precio total de compra: {resultado_compra:,.0f}")
        label_resultado_venta.config(text=f"Precio total de venta: {resultado_venta:,.0f}")
        
        if ganancia < 0:
            label_ganancia.config(text=f"Compra negativa: {ganancia:,.0f} ☹", fg="red")
            # Registrar la fuente personalizada
            #futuristic_font = font.Font(family="Helvetica", size=12, weight="bold")   
            #label_ganancia = tk.Label(root, text=f"Compra negativa: {ganancia:,.0f} ☹", 
            #              fg="red", 
            #              font=futuristic_font)
            #label_ganancia.grid(row=5, column=1, padx=10, pady=10) 
        else:
            label_ganancia.config(text=f"!!! COMPRALO, es ganancia de ${ganancia:,.0f} !!! ☺👍", fg="green")
            # Registrar la fuente personalizada
            #futuristic_font = font.Font(family="Helvetica", size=15, weight="bold")   
            # Crear la etiqueta con la fuente personalizada y emojis
            #label_ganancia = tk.Label(root, text=f"!!! COMPRALO, es ganancia de ${ganancia:,.0f} !!! ☺👍", 
            #              fg="green", 
            #              font=futuristic_font)
            #label_ganancia.pack(pady=20)
            #label_ganancia.grid(row=5, column=1, padx=10, pady=10)
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores válidos.")

def limpiar():
    entry_preciocompra.delete(0, tk.END)
    entry_numjugadorescompra.delete(0, tk.END)
    entry_precioventa.delete(0, tk.END)
    label_resultado_compra.config(text="")
    label_resultado_venta.config(text="")
    label_ganancia.config(text="")

def cerrar():
    root.destroy()
    
def repositorio():
    url = "https://github.com/luisflow/Calculadora-FC-Mobile"
    webbrowser.open(url)

    
# para que cuando se presione enter se mueva a la caja o boton siguiente
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Ganancia FC Mobile - Luis Flow")

# Etiquetas y cajas de texto
tk.Label(root, text="Precio de Compra:", anchor="w").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_preciocompra = tk.Entry(root)
entry_preciocompra.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Número de Jugadores:", anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_numjugadorescompra = tk.Entry(root)
entry_numjugadorescompra.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Precio de Venta:", anchor="w").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_precioventa = tk.Entry(root)
entry_precioventa.grid(row=2, column=1, padx=10, pady=5)

# Etiqueta publicitaria
tk.Label(root, text="Por Luis Flow Ver 1.0 (2024)", anchor="w").grid(row=6, column=0, padx=10, pady=5, sticky="w")

# Aplicar estilo al botón
style = ttk.Style(root)
style.configure("TButtonAzul.TButton", 
                foreground="blue", 
                font=("Helvetica", 10, "bold"),
                padding=5)
style.map("TButtonAzul.TButton", 
          background=[('active', '#0056b3'), ('!disabled', '#007BFF')])

style.configure("TButtonVerde.TButton", 
                foreground="green", 
                font=("Helvetica", 10, "bold"),
                padding=5)
style.map("TButtonVerde.TButton", 
          background=[('active', '#218838'), ('!disabled', '#28A745')])

style.configure("TButtonRojo.TButton", 
                foreground="red", 
                font=("Helvetica", 10, "bold"),
                padding=5)
style.map("TButtonRojo.TButton", 
          background=[('active', '#c82333'), ('!disabled', '#DC3545')])
          
# Botones
#tk.Button(root, text="Calcular", command=calcular).grid(row=3, column=0, padx=10, pady=10)
boton_calcular= ttk.Button(root, text="Calcular", command=calcular, style="TButtonVerde.TButton").grid(row=0, column=2, padx=10, pady=5)
boton_limpiar= ttk.Button(root, text="Limpiar", command=limpiar, style="TButtonVerde.TButton").grid(row=1, column=2, padx=10, pady=5)
#tk.Button(root, text="Repositorio", command=repositorio, style="TButton").grid(row=3, column=3, padx=10, pady=20)
boton_repositorio = ttk.Button(root, text="Repositorio", command=repositorio, style="TButtonAzul.TButton").grid(row=2, column=2, padx=10, pady=5)
boton_cerrar= ttk.Button(root, text="Cerrar", command=cerrar, style="TButtonRojo.TButton").grid(row=6, column=2, padx=10, pady=5)

# Etiquetas para mostrar los resultados
label_resultado_compra = tk.Label(root, text="")
label_resultado_compra.grid(row=3, column=0, columnspan=3, padx=10, pady=3)

label_resultado_venta = tk.Label(root, text="")
label_resultado_venta.grid(row=4, column=0, columnspan=3, padx=10, pady=3)

label_ganancia = tk.Label(root, text="")
label_ganancia.grid(row=5, column=0, columnspan=3, padx=10, pady=3)



# Iniciar el bucle principal de la ventana
root.mainloop()
