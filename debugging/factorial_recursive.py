#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule le factoriel d'un entier positif ou nul de manière récursive.

    Paramètres :
    -----------
    n : int
        L'entier dont on souhaite calculer le factoriel. 
        Doit être supérieur ou égal à 0.

    Retour :
    -------
    int
        Le factoriel de l'entier n (n!), défini comme :
        - 0! = 1
        - n! = n * (n-1)! pour n > 0

    Exemple :
    --------
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
