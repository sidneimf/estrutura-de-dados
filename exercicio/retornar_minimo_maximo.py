"""
Verificação do código

>>> lista = _gerar_lista_teste()
>>> lista
[345, 1407, 60, 981, 1639, 1671, 60, 1074, 1698, 432, 776, 1494, 1332, 888, 205, 1042, 494, 398, 962, 1712, 931, 16, 1619, 326, 1513, 1927, 1898, 81, 206, 554]

>>> retornar_maior_menor(lista)
(1927, 16)
"""


def gerar_lista_aleatoria(quantidade,maximo):
    import random
    lista = []
    for i in range(quantidade):
        lista.append(int(random.random()*maximo))
    return lista

def _gerar_lista_teste():
    lista = [345, 1407, 60, 981, 1639, 1671, 60, 1074, 1698, 432, 776, 1494, 1332, 888, 205, 1042, 494, 398, 962, 1712, 931, 16, 1619, 326, 1513, 1927, 1898, 81, 206, 554]
    return lista

def retornar_maior_menor(lista):
    maior = menor = lista[0]
    for item in lista[1:]:
        if item < menor:
            menor = item

        if item > maior:
            maior = item

    return maior, menor


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    lista = gerar_lista_aleatoria(30, 2000)
    print(lista)
    maior, menor = retornar_maior_menor(lista)
    print (f'maior = {maior} e menor = {menor}')
