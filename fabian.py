'''
funciones para ejercicio
---------------------------
Autor: fabian gamboa


Descripcion:
Programa creado para incorporar en el ej 1 de ejercicios practicas
'''
import random


numeros = list()

def promedio ():
    # calcula el promedio

    if numeros == []:
        return None

    else:

        promedio = sum(numeros) / len(numeros)
        return promedio

def ordenar ():
    # devuelta lista numeros en forma ordenada de mayor a menor, utilizando metodo sort

    numeros.sort(reverse=True)  
    return numeros


def lista_aleatoria(inicio,fin,cantidad):
    '''esta funcion arroja numeros aleatorios dependiendo de la cantidad que ingrese el usuario'''
    Mlista_aleatoria = []

    for numero in range(cantidad):
        numero = random.randrange(inicio,fin+1) 
        Mlista_aleatoria.append(numero)

        return Mlista_aleatoria


def contar(lista_numeros, numero):
    #permite contar numeros

   cant_numeros = lista_numeros.count(numeros)
   return cant_numeros





