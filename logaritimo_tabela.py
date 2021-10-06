#!/usr/local/bin/python3


# def entrada_usuario():
#     # input do usuário com a base, logaritimando e as casas decimais do resultado
#     logaritimando = float(input("Qual é o logaritimando? "))
#     base = float(input("Qual é a base? "))
#     casas_decimais = int(input("Com quantas casas decimais você deseja? "))
#     return [logaritimando, base, casas_decimais]


def teste_expoente(base, logaritimando):
    # achar o menor expoente inteiro que mais se aproxima do expoente desejado
    memoria_anterior = 0  # guarda o valor do último inteiro testado
    memoria_prox = 0  # guarda o valor do inteiro testado no momento
    expoente = 0  # será o valor retornado
    pause = False
    while pause == False:
        memoria_prox = base**expoente
        if memoria_anterior <= logaritimando < memoria_prox:
            # testa se o logaritimando está entre os valores
            expoente -= 1  # expoente do inteiro anterior
            return expoente
            pause = True
        else:
            memoria_anterior = memoria_prox
            expoente += 1


def testa_decimais(base, logaritimando, expoente):
    decimais_estatico = 10**(-6)
    # realizará testes com decimais até a 7º casa
    exp = expoente + decimais_estatico  # valor que será retornado
    teste = 0
    while teste <= logaritimando:
        teste = base**(exp)
        exp += decimais_estatico
    return exp


def main(logaritimando, base, casas_decimais):
    if logaritimando > 0:
        expoente = teste_expoente(base, logaritimando)
        resultado = testa_decimais(base, logaritimando, expoente)
        return f"{resultado: .{casas_decimais}f}"
    else:
        return "Erro"


