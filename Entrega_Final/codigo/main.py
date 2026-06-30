# main.py - Punto de entrada del programa

import tkinter as tk              # Biblioteca para crear la ventana
from interfaz import GeneradorApp # Importa la clase con la interfaz grafica

if __name__ == "__main__":        # Solo se ejecuta si corres este archivo directamente
    root = tk.Tk()                # Crea la ventana principal
    GeneradorApp(root)            # Crea la interfaz dentro de la ventana
    root.mainloop()               # Mantiene la ventana abierta esperando clicks
