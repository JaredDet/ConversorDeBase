import math

def baseNaBaseB(numero, baseN, baseB):
    numeroN = baseNaBase10(numero, baseN)
    return base10aBaseN(numeroN, baseB)

def base10aBaseN(numero, baseN):
    simbolos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstvwxyz"
    resultado = ""
    while numero != 0:
        resto = numero % baseN
        numero = int(numero / baseN)
        resultado += simbolos[resto]
    return resultado[:: -1]

def baseNaBase10(numero, baseN):
    resultado = 0
    simbolos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstvwxyz"
    for i in range(0, len(numero)):
        resultado += simbolos.index(numero[i]) * pow(baseN, len(numero) - (i + 1))
    return resultado

print(baseNaBaseB("255", 10, 2))
