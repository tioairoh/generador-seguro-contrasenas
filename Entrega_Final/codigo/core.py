# core.py - Logica del generador de contrasenas (sin interfaz grafica)

import secrets
import string
import math

MAYUS = string.ascii_uppercase
MINUS = string.ascii_lowercase
NUMEROS = string.digits
SIMBOLOS = string.punctuation

def generar(long, may, min_, num, sim):
    chars = ""
    req = []

    sets = [(may, MAYUS), (min_, MINUS), (num, NUMEROS), (sim, SIMBOLOS)]
    for activo, s in sets:
        if activo:
            chars += s
            req.append(secrets.choice(s))

    while len(req) < long:
        req.append(secrets.choice(chars))

    for i in range(len(req)-1, 0, -1):
        j = secrets.randbelow(i+1)
        req[i], req[j] = req[j], req[i]

    return "".join(req)

def calcular_entropia(contrasena):
    pool = 0
    if any(c.isupper() for c in contrasena):
        pool += 26
    if any(c.islower() for c in contrasena):
        pool += 26
    if any(c.isdigit() for c in contrasena):
        pool += 10
    if any(c in string.punctuation for c in contrasena):
        pool += 32
    if pool == 0:
        pool = 1
    bits = len(contrasena) * math.log2(pool)
    return bits

def calcular_fortaleza(bits):
    if bits >= 80:
        return "Muy fuerte", "#2e7d32"
    elif bits >= 60:
        return "Fuerte", "#388e3c"
    elif bits >= 36:
        return "Aceptable", "#f9a825"
    else:
        return "Debil", "#c62828"


