#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Le facteur doit être un entier positif ou nul.")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # 🔹 Décrémenter n pour éviter la boucle infinie
    return result

# Vérification de la présence d'un argument
if len(sys.argv) < 2:
    print("Usage: python3 script.py <nombre_entier>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    f = factorial(number)
    print(f)
except ValueError as e:
    print(f"Erreur : {e}")
