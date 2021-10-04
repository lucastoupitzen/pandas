#!/usr/local/bin/python3

import pandas as pd  # importa a bibloteca pandas


def analisa_nota(nota):
    resultado = 0
    if nota < 5.0:
        resultado = "Não"
    elif nota > 10:
        resultado = "Erro"
    else:
        resultado = "Sim"
    return resultado


def retorna_nomes():
    nome = str(input("Nome do aluno ou digite Sair para sair "))
    return nome


def retorna_notas():
    nota = float(input("Nota do aluno "))
    return nota


def corrige_nome(nome):
    while nome[0] == " ":
        nome = nome[1:]
    return nome


def controle(lista_nome, lista_notas, lista_passou):
    controle = pd.DataFrame(
        {"Nome": lista_nome,
            "Nota": lista_notas,
            "Passou": lista_passou
         }
    )
    return controle


def main():
    lista_nome = []  # parâmetros que serão listados nas linhas
    lista_notas = []
    lista_passou = []
    nome = 0  # controle de quando deve encerrar
    while nome != "Sair":
        nome = retorna_nomes()
        nome = corrige_nome(nome)
        if nome != "Sair":
            lista_nome.append(nome)
            nota = retorna_notas()
            lista_notas.append(nota)
            lista_passou.append(analisa_nota(nota))
    print(controle(lista_nome, lista_notas, lista_passou))


main()
