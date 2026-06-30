# Generador Seguro de Contraseñas

**Proyecto Integrador:** El impacto de las nuevas tecnologias en la sociedad: desarrollo y proyeccion de soluciones informaticas

**Estudiante:** Cesar Paul Cango Medina  
**Carrera:** Ingenieria en Sistemas Informaticos  
**Anio lectivo:** 2026 / 2027  
**Fecha:** Junio 2026  

---

## Objetivo del sistema

Desarrollar una herramienta de generacion y analisis de contraseñas criptograficamente seguras que demuestre la aplicacion de estructuras logicas, buenas practicas de programacion y conciencia sobre seguridad informatica, como respuesta a una necesidad real en la sociedad digital actual.

---

## Funcionalidades del sistema

El programa cuenta con **3 modos de operacion** mediante pestanas:

### 1. Generar
Genera contraseñas aleatorias con parametros configurables:
- **Longitud**: 8 a 32 caracteres (slider + entrada manual sincronizados)
- **Tipos**: mayusculas, minusculas, numeros, simbolos (checkboxes)
- **Garantia**: al menos un caracter de cada tipo seleccionado
- **Seguridad**: secrets.choice() + Fisher-Yates shuffle
- **Visualizacion**: entropia en bits + barra de fortaleza proporcional

### 2. Passphrase
Genera frases memorables en espanol:
- 4 a 8 palabras seleccionadas de un diccionario de 130+ terminos
- Separadas por guiones (ej: "lago-perro-verde-canto")
- Entropia estimada: log2(diccionario) x cantidad de palabras
- Ideal para contraseñas faciles de recordar pero dificiles de adivinar

### 3. Analizador
Analiza cualquier contraseña ingresada por el usuario:
- Composicion (mayus, minus, numeros, simbolos, otros)
- Entropia en bits y nivel de fortaleza
- Deteccion de patrones debiles (caracteres repetidos, secuencias)
- Tiempo estimado de ruptura (basado en 10^9 guesses/s)
- Recomendaciones personalizadas de mejora

### Funcionalidades generales
- Copia al portapapeles con un solo clic (con manejo de errores)
- Atajo de teclado Enter para generar
- Validacion robusta de todas las entradas
- Sin dependencias externas (solo libreria estandar)

---

## Captura de pantalla

```
 ┌──────────────────────────────────────────────────┐
 │  Generador Seguro de Contraseñas                 │
 │  Cesar Paul Cango Medina - Ing. Sistemas         │
 │                                                  │
 │  ┌──────────┬────────────┬──────────┐            │
 │  │ Generar  │ Passphrase │ Analizar │            │
 │  └──────────┴────────────┴──────────┘            │
 │                                                  │
 │  Longitud (8-32): [16] ════●══════════════       │
 │                                                  │
 │  Incluir:                                        │
 │  [✓] Mayusculas [✓] Minusculas                   │
 │  [✓] Numeros    [ ] Simbolos                     │
 │                                                  │
 │    [ Generar Contraseña ] [ Generar Otra ]       │
 │                                                  │
 │  ─── Resultado ───                               │
 │  Contrasena: [kR7mP2xQw9nLvB3j] [Copiar]        │
 │  Entropia: 104.9 bits                            │
 │  Fortaleza: [████████████████░░] Muy fuerte      │
 │                                                  │
 │  Contrasena generada exitosamente                │
 └──────────────────────────────────────────────────┘
```

---

## Como ejecutarlo

### Requisitos
- Python 3.x (sin dependencias externas)

### Ejecucion
```bash
python main.py
```

---

## Estructura del codigo

```
main.py                    ← Punto de entrada
interfaz.py                ← Presentacion (GUI con 3 pestanas)
core.py                    ← Logica de negocio + datos

core.py
│
├── CAPA 3 — Datos y Constantes
│   ├── MAYUS, MINUS, NUMEROS, SIMBOLOS
│   └── PALABRAS (diccionario para passphrase, 130+ terminos)
│
├── CAPA 2 — Logica de Negocio
│   ├── generar()               → if/while/for + secrets.choice()
│   ├── generar_passphrase()    → secrets.sample() del diccionario
│   ├── analizar_contrasena()   → entropia, patrones, tiempo estimado
│   ├── calcular_entropia()     → formula H = L x log2(T)
│   └── calcular_fortaleza()    → clasifica segun umbrales
│
interfaz.py
│
└── CAPA 1 — Presentacion
    └── GeneradorApp (clase tkinter)
        ├── Pestana Generar    → slider, checkboxes, botones, barra
        ├── Pestana Passphrase → selector de cantidad, generacion
        ├── Pestana Analizar   → entrada de texto, analisis completo
        └── Metodos: _generar(), _copiar(), _generar_passphrase(),
                     _analizar(), _toggle_mostrar()
```

---

## Estructuras logicas implementadas

| Estructura | Donde se usa | Para que |
|---|---|---|
| `if / elif / else` | `calcular_fortaleza()` | Clasifica fortaleza segun entropia (36, 60, 80 bits) |
| `if` | `generar_contrasena()` | Arma el pool segun los conjuntos elegidos |
| `if` | `analizar_contrasena()` | Detecta patrones debiles en la contrasena |
| `while` | `generar_contrasena()` | Completa la longitud de la contrasena |
| `for` | `generar_contrasena()` | Algoritmo de shuffle Fisher-Yates |
| `for` | `analizar_contrasena()` | Conteo de caracteres por tipo y deteccion de patrones |
| `try / except` | Varios metodos | Captura errores de tipo, portapapeles, log2(0) |
| Eventos tkinter | `mainloop()` | Bucle principal de la interfaz grafica |
| Notebook | `GeneradorApp` | Pestanas para los 3 modos de operacion |

---

## Resultados de pruebas

### Distribucion de entropia (100 muestras, 16 char, todos los tipos)
- Nivel 4 (Muy fuerte): 100% de las muestras
- Entropia promedio: 104.9 bits
- Tiempo estimado de ruptura: miles de anos

### Comparacion por configuracion
| Configuracion | Entropia | Nivel |
|---|---|---|
| 8 char, solo mayusculas | 37.6 bits | Debil |
| 8 char, may+min+num | 47.6 bits | Aceptable |
| 8 char, todos los tipos | 52.4 bits | Aceptable |
| 12 char, todos los tipos | 78.7 bits | Fuerte |
| 16 char, todos los tipos | 104.9 bits | Muy fuerte |
| 20 char, todos los tipos | 131.1 bits | Muy fuerte |
| 32 char, todos los tipos | 209.7 bits | Muy fuerte |

### Deteccion de contraseñas debiles
| Contrasena | Entropia | Tiempo de ruptura |
|---|---|---|
| "123456" | 19.9 bits | Segundos |
| "password" | 37.6 bits | Minutos |
| "admin123" | 41.4 bits | Horas |
| "abcdef" | 28.2 bits | Minutos |
| "aaaaaa" | 28.2 bits | Minutos |

---

## Archivos del repositorio

```
Entrega_Final/
├── .gitignore
├── codigo/
│   ├── main.py                   # Punto de entrada
│   ├── interfaz.py               # GUI con 3 pestanas (tkinter)
│   ├── core.py                   # Logica de negocio
│   ├── requirements.txt          # Sin dependencias externas
│   └── README.md                 # Documentacion
│
├── diagramas/
│   ├── casos_uso.svg
│   ├── diagrama_arquitectura.svg
│   ├── diagrama_flujo_general.svg
│   ├── flujo_generar_contrasena.svg
│   ├── flujo_calcular_fortaleza.svg
│   ├── cronograma.md
│   ├── png_temp/                 # Diagramas adicionales (DrawIO)
│   └── ~$agramas_Proyecto.docx   # Respaldo temporal (documento original se perdio)
│
├── documento/
│   └── Documento_Proyecto_Integrador.docx
│
└── presentacion/
    └── Generador Seguro de Contrasenas.pptx
```

---

## Tecnologias

- **Python 3.x**
- **tkinter** — interfaz grafica (incluido en Python)
- **secrets** — aleatoriedad criptografica (CSPRNG del SO)
- **string** — conjuntos de caracteres (estandar)
- **math** — calculo de entropia (estandar)

---

## Relacion con los contenidos de la asignatura

| Unidad | Contenido aplicado |
|---|---|
| **Unidad 1** | Algoritmos, diagramas de flujo, diseno del sistema |
| **Unidad 2** | Estructuras condicionales (if/elif/else) y repetitivas (while/for) |
| **Unidad 3** | Funciones, modularizacion en 3 capas, alcance de variables |
| **Unidad 4** | Seguridad informatica, entropia de Shannon, modulo secrets |

---

## Analisis comparativo

| Caracteristica | Este Proyecto | LastPass | Bitwarden | random.org |
|---|---|---|---|---|
| Aleatoriedad | secrets CSPRNG | CSPRNG | CSPRNG | No documentado |
| Analisis de contrasenas | SI (entropia+patrones) | No | No | No |
| Passphrases | SI (espanol) | SI (ingles) | SI (ingles) | No |
| Codigo abierto | SI (Python puro) | No | Parcial | No |
| Entropia visible | SI (bits + barra) | Parcial | Parcial | No |

Este proyecto es el unico que integra generacion, analisis y educacion en una sola herramienta de codigo abierto.

---

## Conclusiones

1. La generacion de contrasenas con 16 caracteres usando los 4 tipos produce consistentemente mas de 100 bits de entropia (Nivel "Muy fuerte"), superando el minimo de 80 bits recomendado por NIST.

2. El modulo secrets de Python (CSPRNG) garantiza aleatoriedad impredecible, a diferencia del modulo random que genera secuencias deterministicas.

3. El analizador de contrasenas identifico correctamente patrones debiles en ejemplos como "123456" (19.9 bits, rompible en segundos) y "password" (37.6 bits, nivel debil).

4. El modo passphrase ofrece una alternativa valiosa para contrasenas memorables, aunque con un diccionario limitado (130 palabras) que se recomienda expandir.

5. La comparacion con LastPass, Bitwarden y random.org revelo que este proyecto es el unico que integra generacion, analisis y educacion en una plataforma de codigo abierto.

---

## Limitaciones identificadas

- El diccionario de passphrases (130+ palabras) es limitado. Un diccionario Diceware completo (7776 palabras) ofreceria 12.9 bits por palabra.
- El analisis de patrones no incluye deteccion de palabras de diccionario, fechas, o patrones de teclado (qwerty).
- La estimacion de tiempo de ruptura asume 10^9 guesses/s. Atacantes con GPUs especializadas superan 10^12 guesses/s.
- El programa no almacena ni gestiona contrasenas. Es exclusivamente un generador/analizador.
- La seguridad final depende del usuario: una contrasena segura almacenada en un archivo sin cifrar sigue siendo vulnerable.

---

## Reflexion sobre el impacto de la tecnologia

Las nuevas tecnologias han transformado todos los aspectos de la sociedad, desde la comunicacion hasta la seguridad digital. Si bien ofrecen beneficios enormes, tambien presentan desafios como la exposicion de datos personales y los ciberataques.

Proyectos como este generador de contrasenas buscan ser parte de la solucion, brindando a las personas herramientas sencillas pero efectivas para protegerse en el entorno digital. La informatica, bien aplicada, no solo resuelve problemas tecnicos sino que contribuye a construir una sociedad mas segura y consciente de su privacidad.
