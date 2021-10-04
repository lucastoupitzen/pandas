#!/usr/local/bin/python3

import pandas as pd  # importa a bibloteca pandas


def analisa_nota(nota): # analisa o resultado das notas dos alunos e retorna se passou ou não
    resultado = 0
    if nota < 5.0:
        resultado = "Não"
    elif nota > 10:
        resultado = "Erro"
    else:
        resultado = "Sim"
    return resultado


def retorna_nomes(): # input do nome do aluno ou da chave de saída
    nome = str(input("Nome do aluno ou digite Sair para sair "))
    return nome


def retorna_notas(): # input da nota do aluno
    nota = float(input("Nota do aluno "))
    return nota


def corrige_nome(nome): # corrige espaços na frente do nome, viabilizando a chave de saída
    while nome[0] == " ":
        nome = nome[1:]
    return nome


def controle(lista_nome, lista_notas, lista_passou): # retorna o DataFrame da biblioteca pandas
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
    while nome != "Sair": # controla a chave de saída do código
        nome = retorna_nomes()
        nome = corrige_nome(nome)
        if nome != "Sair": # se for igual a Sair -> sai do laço
            lista_nome.append(nome)
            nota = retorna_notas()
            lista_notas.append(nota)
            lista_passou.append(analisa_nota(nota))
    print(controle(lista_nome, lista_notas, lista_passou))


main()
