"""
Created on Sat Sep  7 11:43:02 2024

@author: sofia
"""
from math import sqrt

def exercicio1(vetor: tuple) -> float:
    """
    Calcula a norma de um vetor representado como uma tupla de números.

    A função verifica se o vetor fornecido é uma tupla e se todos os elementos 
    são números (int ou float). Caso contrário, levanta exceções apropriadas.
    Em seguida, calcula a soma dos quadrados dos elementos do vetor e 
    retorna a raiz quadrada dessa soma, que é a norma do vetor.

    Parameters
    ----------
    vetor : tuple
        Tupla contendo números (int ou float) representando o vetor.

    Raises
    ------
    TypeError
        Se o argumento não for uma tupla.
    ValueError
        Se a tupla contiver elementos que não sejam números.

    Returns
    -------
    norma : float
        Norma do vetor.

    """
    count = 0
    if not isinstance(vetor, tuple):
        raise TypeError("Somente tuplas por aqui")
    for i in vetor:
        if not isinstance(i, int) and not isinstance(i, float):
            raise ValueError("Números em seu vetor, por favor")
    for i in vetor:
        count += i**2
     
    norma = sqrt(count)
    
    return norma

def exercicio2(ponto1: tuple, ponto2: tuple) -> tuple:
    """
    Recebe as coordenadas de dois pontos distintos e retorna os coeficientes da reta que é definida por eles.

    Parameters
    ----------
    ponto1 : tuple(int, int)|(float, float)
        Coordenadas cartesianas do primeiro ponto.
    ponto2 : tuple(int, int)|(float, float)
        Coordenadas cartesianas do segundo ponto.

    Raises
    ------
    TypeError
        Quando os pontos não são dados em tuplas.
    ValueError
        Quando os pontos não tem duas coordenadas.
        Quando os pontos não tem coordenadas numéricas.
    KeyError
        Quando os pontos são iguais.
    ZeroDivisionError
        Quando a reta é vertical

    Returns
    -------
    m : int|float
        Coeficiente angular da reta.
    n : int|float
        Coeficiente linear da reta.

    """
    if not isinstance(ponto1, tuple) or not isinstance(ponto2, tuple):
        raise TypeError("Os pontos devem ser tuplas!")
    if len(ponto1) != 2 or len(ponto2) != 2:
        raise ValueError("Os pontos devem ter duas coordenadas!")
    for coord1 in ponto1:
        if not isinstance(coord1, int) and not isinstance(coord1, float):
            raise ValueError("Os pontos devem ter duas coordenadas númericas!")
    for coord2 in ponto2:
        if not isinstance(coord2, int) and not isinstance(coord2, float):
            raise ValueError("Os pontos devem ter duas coordenadas númericas!")
    if ponto1 == ponto2:
        raise KeyError("Uma reta só pode ser dada a partir de dois pontos diferentes contidos nela.")
    If ponto1[0] == ponto2[0]:
        raise ZeroDivisionError("Essa reta é vertical, o coeficiente angular não existe.")
    
    x, y = ponto1
    a, b = ponto2
        
    m = (y-b)/(x-a)
    n = y - m * x
    
    return (m, n)