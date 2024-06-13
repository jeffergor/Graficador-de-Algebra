import tkinter as tk
from tkinter import messagebox
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def resolver_formula():
    try:
        formula = entry_formula.get()
        print(f"Fórmula ingresada: {formula}")
        expr = sp.sympify(formula)
        print(f"Expresión simbólica: {expr}")
        
        # Resolver la fórmula
        x = sp.symbols('x')
        solucion = sp.solve(expr, x)
        print(f"Solución: {solucion}")
        
        # Mostrar la solución
        resultado.set(f'Solución: {solucion}')
        
        # Graficar la fórmula
        fig, ax = plt.subplots()
        sp.plot(expr, (x, -10, 10), ax=ax, show=False)  # Ajustamos el rango de x para visualizar mejor la gráfica
        ax.set_title(f"Gráfica de {formula}")
        
        # Limpiar el canvas anterior
        for widget in frame_canvas.winfo_children():
            widget.destroy()
        
        # Crear un nuevo canvas para el gráfico
        canvas = FigureCanvasTkAgg(fig, master=frame_canvas)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        # Mensaje de depuración
        print("Gráfica generada correctamente")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        messagebox.showerror("Error", str(e))

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Álgebra Lineal")

# Crear y colocar los widgets
frame_formula = tk.Frame(root)
frame_formula.pack(pady=10)

label_formula = tk.Label(frame_formula, text="Introduce la fórmula:")
label_formula.pack(side=tk.LEFT)

entry_formula = tk.Entry(frame_formula, width=40)
entry_formula.pack(side=tk.LEFT)

button_resolver = tk.Button(root, text="Resolver y Graficar", command=resolver_formula)
button_resolver.pack(pady=10)

resultado = tk.StringVar()
label_resultado = tk.Label(root, textvariable=resultado)
label_resultado.pack(pady=10)

frame_canvas = tk.Frame(root)
frame_canvas.pack(pady=10)

# Iniciar el bucle principal de Tkinter
root.mainloop()
