# interfaz.py - Ventana grafica del generador de contrasenas (tkinter)

import tkinter as tk
from tkinter import ttk, messagebox
from core import generar, calcular_entropia, calcular_fortaleza

class GeneradorApp:

    def __init__(self, root):
        self.root = root
        root.title("Generador Seguro de Contrasenas")
        root.configure(bg="#f0f4f8")
        root.resizable(False, False)
        w, h = 600, 420
        root.geometry(f"{w}x{h}+{(root.winfo_screenwidth()-w)//2}+{(root.winfo_screenheight()-h)//2}")

        main = ttk.Frame(root, padding=15)
        main.pack(fill="both", expand=True)

        ttk.Label(main, text="Generador Seguro de Contrasenas",
                  font=("Segoe UI", 16, "bold"), foreground="#1565c0",
                  background="#f0f4f8").pack(pady=(0, 10))

        frame = ttk.Frame(main, padding=15)
        frame.pack(fill="both", expand=True)

        flong = ttk.Frame(frame)
        flong.pack(fill="x", pady=5)
        ttk.Label(flong, text="Longitud (8-32):", font=("Segoe UI", 11)).pack(side="left")
        self.long_var = tk.StringVar(value="16")
        self.long_entry = ttk.Entry(flong, textvariable=self.long_var, width=4, font=("Segoe UI", 11))
        self.long_entry.pack(side="left", padx=(10, 5))
        self.long_slider = ttk.Scale(flong, from_=8, to=32, value=16, command=self._act_long, length=200)
        self.long_slider.pack(side="left", padx=5)

        ttk.Label(frame, text="Incluir:", font=("Segoe UI", 11)).pack(anchor="w", pady=(10, 5))
        ftipos = ttk.Frame(frame)
        ftipos.pack(fill="x")
        self.may = tk.BooleanVar(value=True)
        self.min = tk.BooleanVar(value=True)
        self.num = tk.BooleanVar(value=True)
        self.sim = tk.BooleanVar(value=False)
        ttk.Checkbutton(ftipos, text="Mayusculas (A-Z)", variable=self.may).pack(side="left", padx=5)
        ttk.Checkbutton(ftipos, text="Minusculas (a-z)", variable=self.min).pack(side="left", padx=5)
        ttk.Checkbutton(ftipos, text="Numeros (0-9)", variable=self.num).pack(side="left", padx=5)
        ttk.Checkbutton(ftipos, text="Simbolos (!@#...)", variable=self.sim).pack(side="left", padx=5)

        fbot = ttk.Frame(frame)
        fbot.pack(pady=10)
        self.btn_gen = ttk.Button(fbot, text="Generar Contrasena", command=self._generar)
        self.btn_gen.pack(side="left", padx=5)
        self.btn_otra = ttk.Button(fbot, text="Generar Otra", command=self._generar, state="disabled")
        self.btn_otra.pack(side="left", padx=5)
        self.root.bind("<Return>", lambda e: self._generar())

        self.res = ttk.LabelFrame(frame, text="Resultado", padding=10)
        self.res.pack(fill="x")

        fpass = ttk.Frame(self.res)
        fpass.pack(fill="x")
        ttk.Label(fpass, text="Contrasena:", font=("Segoe UI", 10, "bold")).pack(side="left")
        self.pw_var = tk.StringVar()
        ttk.Entry(fpass, textvariable=self.pw_var, font=("Consolas", 11), width=35).pack(side="left", padx=5)
        self.btn_cop = ttk.Button(fpass, text="Copiar", width=8, command=self._copiar, state="disabled")
        self.btn_cop.pack(side="left", padx=2)

        fentropia = ttk.Frame(self.res)
        fentropia.pack(fill="x", pady=(5, 0))
        self.entropia_var = tk.StringVar(value="Entropia: -- bits")
        ttk.Label(fentropia, textvariable=self.entropia_var, font=("Segoe UI", 10)).pack(side="left")
        self.fortaleza_var = tk.StringVar(value="Fortaleza: --")
        self.fortaleza_label = ttk.Label(fentropia, textvariable=self.fortaleza_var, font=("Segoe UI", 10, "bold"))
        self.fortaleza_label.pack(side="left", padx=(10, 0))

        self.barra = ttk.Progressbar(self.res, length=300, mode="determinate", value=0)
        self.barra.pack(fill="x", pady=(5, 0))

        self.long_entry.bind("<KeyRelease>", self._act_entry)

        self.estado = tk.StringVar()
        ttk.Label(main, textvariable=self.estado, font=("Segoe UI", 9),
                  foreground="#555", background="#f0f4f8").pack(pady=(5, 0))

    def _act_long(self, val):
        self.long_var.set(str(int(float(val))))

    def _act_entry(self, event):
        try:
            v = int(self.long_var.get())
            if 8 <= v <= 32:
                self.long_slider.set(v)
        except:
            pass

    def _generar(self):
        try:
            long = int(self.long_var.get())
        except:
            messagebox.showerror("Error", "La longitud debe ser un numero entero")
            return
        if long < 8 or long > 32:
            messagebox.showerror("Error", "La longitud debe estar entre 8 y 32")
            return
        if not (self.may.get() or self.min.get() or self.num.get() or self.sim.get()):
            messagebox.showerror("Error", "Selecciona al menos un tipo de caracter")
            return
        pw = generar(long, self.may.get(), self.min.get(), self.num.get(), self.sim.get())
        self.pw_var.set(pw)
        self.btn_cop.config(state="normal")
        self.btn_otra.config(state="normal")

        entropia = calcular_entropia(pw)
        nivel, color = calcular_fortaleza(entropia)
        self.entropia_var.set(f"Entropia: {entropia:.1f} bits")
        self.fortaleza_var.set(f"Fortaleza: {nivel}")
        self.fortaleza_label.configure(foreground=color)
        pct = min(entropia / 150 * 100, 100)
        self.barra["value"] = pct

        self.estado.set("Contrasena generada exitosamente")

    def _copiar(self):
        t = self.pw_var.get()
        if not t:
            return
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(t)
            self.estado.set("Copiada al portapapeles!")
        except tk.TclError:
            self.estado.set("Error al copiar al portapapeles")
