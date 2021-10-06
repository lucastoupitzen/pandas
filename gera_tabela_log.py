#!/usr/local/bin/python3

import pandas as pd
from log_tabela import logaritimo_tabela as log


def condição_base(base):
    if base > 0 and base != 1:
        return True


def main():

    primeiro_inteiro = float(input("Qual é o inteiro inicial da tabela? "))
    ultimo_inteiro = float(input('Qual é o inteiro final da tabela? '))
    controle_base = False
    while controle_base == False:
        base = float(input("Qual é a base? "))
        if condição_base(base):
            controle_base = True
        else:
            print("Valor da base fora da condição de existencência! A base deve ser um número positivo diferente de 1!")
    controle_cd = False
    while controle_cd == False:
        casas_decimais = int(
            input("Com quantas casas decimais você deseja (até 6 estão disponíveis)? "))
        if casas_decimais <= 0 or casas_decimais > 6:
            print("Erro na quantidade de casas decimais")
        else:
            controle_cd = True
    lista_inteiros = []
    lista_log = []
    for i in range(int(primeiro_inteiro), int(ultimo_inteiro)+1):
        lista_inteiros.append(i)
        lista_log.append(log.main(i, base, casas_decimais))

    tabela = pd.DataFrame(
        {
            "Número": lista_inteiros,
            "Logarítimo": lista_log,
        }
    )
    tabela = tabela[["Número", "Logarítimo"]]
    print(tabela)
    tabela.to_csv("tabela.log.csv")


main()
