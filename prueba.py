def ej2():
    print("Jugando a los dados")

    '''
    Un dado común tiene 6 caras, 6 resultados posibles
    1 - 2 - 3 - 4 - 5 - 6

    Utilice la función "lista_aleatoria" para generar
    5 tiros de dados (una lista de 5 valores con resultados posibles
    de un dado)
    ejemplo, se tiraron 5 dados y los resultados de lista aleatoria
    se deben parecer a:
    [1, 2, 3, 2, 5]
    Cada valor representa el valor que sacó cada uno de los 5 dados

    1)
    Utilice la función "ordenar" para ordenar la lista
    de números generados.
    Imprimir en pantalla la lista ordenada
    '''
    numeros = fabian.lista_aleatoria(inicio=1, fin=6, cantidad=5)
    print(numeros)
    print('el resultado del primer intento es:',fabian.ordenar(numeros=numeros)