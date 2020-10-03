#!/usr/bin/env python
'''
Funciones [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import random


def imprimir_nombre(nombre, apellido):
    
    print('nombre completo: {} {}'.format(nombre, apellido))
    pass

    # En este lugar debe colocar el "print" e imprimir
    # en pantalla el nombre y apellido que vienen por parámetro
    # print(.....)

    



def promedio(numeros):
    # Alumno:
    # 1) calcule el promedio
    # 2) use "return" para retornar ese valor
    # Cuando termine de implementar está función borrar "pass"


    cantidad_numeros = len(numeros)
    sumatoria_numeros = sum(numeros)

    if numeros == []:
      print('no tiene notas para realizar el promedio,la lista esta vacia')

    else:
        promedio = sumatoria_numeros / cantidad_numeros
        print('el promedio {} es: {}'.format(numeros, round(promedio, 2)))
        return promedio

    


def ej1():
    print('Mi primera funcion')
    # Realice una función llamada "imprimir_nombre"
    # la cual reciba dos parámetros, el nombre y el apellido
    # Esa función ya se encuentra a medio armar al principio de este archivo.
    # Debe cumpletar la función para que se imprima en pantalla su nombre y apellido
    # Debe invocar a la función como:
    imprimir_nombre('Fabian', 'Gamboa')


    # Reemplazar por su nombre y apellido los textos


def ej2():
    # Ejercicios con funciones del sistema
    

    '''
    Realice una funcion llamada "promedio" la cual
    reciba como parámetro una lista de números y calcule
    el promedio de ella como:
    promedio = sumatoria_numeros / cantidad_numeros

    Resuelva la sumatoria y la cantidad con las herramientas
    que desee, recomendamos usar las funciones disponibles
    de Python para ello o en tal caso realizar un bucle.
    Puede utilizar la función "sum" y la función "len"
    sum --> obtener la sumatoria de números
    len --> obtener la cantidad de números
    promedio = sumatoria_numeros / cantidad_numeros

    La función debe retornar (return) el promedio calculado
    La función debe contemplar si se le pasa una lista vacia
    (es decir, de "0" elementos)

    Utilice esa función para calcular el promedio y luego
    imprima en pantalla el resultado
   
    '''
    # La función ya se encuentra definida arriba de todo en el archivo,
    # busque al princpio de todo "def promedio"
    # Ya la función fue preparada para que usted le pase "numeros"
    # como parámetro, falta que calcule el promedio y retorne el valor
    # resultante.

    # Llamar a la función en este lugar y capturar el valor del retorno
    # promedio_re

    # Luego imprimir en pantalla el valor resultante, tal que:

    numeros = [2, 4, 6, 8, 10, 12]
    promedio_resul = promedio(numeros)

    print('\n\nlista de numeros: {}'.format(numeros))


    if promedio_resul is None:
        print('\nno se pudo calcular promedio, la lista esta vacia')
        print ('tiene 0 elementos. \n\n')

    else:
        print('\n el promedio de los numeros es: {} \n\n' .format(promedio_resul))



    







def ej3():
    # Ejercicios de listas y métodos
    numeros = [2, 4, 6, 8, 10, 12]

    '''
    Generar una una nueva funcion que se llame "ordenar",
    que utilizaremos para odernar la lista de numeros.
    Dentro de la función puede ordenar la lista
    usando bucles o las funciones nativas de Python (sort)

    Aproveche el ejemplo de "promedio" para crear una función
    similar, la debe crear y escribir abajo de ella.

    '''

    # Luego de crear la función invocarla en este lugar:
    # lista_ordenada = ordenar(numeros)
    # Imprimir en pantalla "lista_ordenada" que tendrá
    # los valores retornado por la función ordenar
    
    if numeros == []:
        print('\n\n La lista esta vacia. ==> {}\n' .format(numeros))

    else:
        lista_ordenada = ordenar(numeros)

    print('\n\n la lista de numeros es: {}') .format(numeros)
    print('\n\n la lista de numeros ordenada de menor a mayor es: {}\n' .format(lista_ordenada))



def ej4():
    # Ejercicios con modulos del sistema
    inicio = 0
    fin = 10
    cantidad = 5

    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    numero = random.randrange(inicio, fin+1)
    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html
    # Ante cualquier duda preguntar en el campus!

    '''
    Realice una funcion llamada "lista_aleatoria" la cual
    reciba como parámetro el rango de aceptación de la lista
    "inicio y fin" y la cantidad de elementos que deseamos que
    contenga la lista, es decir, la cantidad de elementos random a generar.

    --> def lista_aleatoria (inicio, fin, cantidad)

    Para ello dentro de la función deberá realizar un bucle que repita "cantidad"
    veces esta operacion:
    numero = random.randrange(inicio, fin+1)

    Cada valor generado lo debe guardar en una lista, recuerde:
    1) Iniciar y crear esa lista vacia.
    2) Para agregar nuevos elementos en la lista utiliza "append"

    Finalmente dicha función debe retornar la lista de elementos random generados.
    '''

    # Invocar lista_aleatoria
    mi_lista_aleatorio = lista_aleatoria(inicio, fin, cantidad)
    print('\n la lista aleatoria de numeros dentro del rango [{}, {} ] es :{}\n\n' .format(inicio, fin +1 , mi_lista_aleatorio)

 

def ej5():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "contar",
    que cuenta la cantidad de veces que un elemento pasado
    por parámetro se repite en la lista.
    Para saber cuantas veces se repiten el elemento pasado
    en la lista pueden usar bucles o el método nativo de list
    "count"

    '''

    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)

    lista_numeros = lista_aleatoria(inicio,fin,cantidad numeros)
    print('\n\n la lista aleatoria es: {}\n' .format(lista_numeros))

    numero_repetido = 3
    cantidad_veces = contar(lista_numeros, numero_repetido)

    if cantidad_veces == 0:
        cantidad_repeticiones = cantidad_veces

    else:
        cantidad_repeticiones = cantidad_veces -1

    print('la cantidad de veces que aparece el numero {} es: {}'.format(numero_repetido, cantidad_veces))
    print('la cantidad de veces que repite el numero {} es: {}\n\n'.formar(numero_repetido, cantidad_repeticiones))
    

    


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
