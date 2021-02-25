"""
    Verificação do código

    >>> lista = _gerar_lista_teste()

    >>> lista
    [345, 1407, 60, 981, 1639, 1671, 60, 1074, 1698, 432, 776, 1494, 1332, 888, 205, 1042, 494, 398, 962, 1712, 931, 16, 1619, 326, 1513, 1927, 1898, 81, 206, 554]

    >>> tamanho = len(lista)

    >>> maior = menor = lista[0]

    >>> retornar_maior_menor(lista, tamanho, maior, menor)
    (1927, 16)
"""


def gerar_lista_aleatoria(quantidade, maximo):
    import random
    lista = []
    for i in range(quantidade):
        lista.append(random.randint(0,maximo))
    return lista

def _gerar_lista_teste():
    lista = [345, 1407, 60, 981, 1639, 1671, 60, 1074, 1698, 432, 776, 1494, 1332, 888, 205, 1042, 494, 398, 962, 1712, 931, 16, 1619, 326, 1513, 1927, 1898, 81, 206, 554]
    return lista

def retornar_maior_menor(lista, tamanho, maior, menor):
    item = lista[tamanho - 1]
    if item < menor:
        menor = item

    if item > maior:
        maior = item

    tamanho -= 1

    if tamanho > -1:
        maior, menor = retornar_maior_menor(lista, tamanho, maior, menor)
    return (maior, menor)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    lista = gerar_lista_aleatoria(30, 2000)
    tamanho = len(lista)
    if tamanho > 0:
        maior = menor = lista[0]
        print(lista)
        maior, menor = retornar_maior_menor(lista,tamanho, maior, menor)
        print (f'maior = {maior} e menor = {menor}')
