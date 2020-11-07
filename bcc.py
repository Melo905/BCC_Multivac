#bcc_Multivac (Bibliotecas e esqueleto)
import pynput 
import pandas as pd
import math as mt
import numpy as np

# Todas as funções
def create_column():
    print("Coluna nova")

def new_file():#solicita info essenciais para criar uma coluna na tabela
    flag = 0
    for x in range(0,1):
        print("Novo arquivo")
        input("Assunto %d:" % flag)# usar uma flag para contar os atributos
        level = input("Dificuldade da matéria:\n1)facil   2)familiarizado   3)dificil\n")
        t0 = float(input("Tempo da sessao:"))#em minutos (conversão de horas para minutos)
        day = input("Dia dessa sessão(min):")#função de data
        valid = input("Prazo de validade:")#função de data
        create_column()
        mais = input("Adicionar outro assunto? S ou N")
        if mais == "S" or if mais == "s"
            x = 0
        if mais == "N" or if mais == "n"
            x = 1
        else:
            print("Nao entendi. \"S\" para \"Sim\" ou \"N\" para \"Não\".")#Colocar condição para retornar à pergunta
    
    
def mod_file():
    print("Localizar arquivo")


# Mainframe
print("*****************************  TABELA EBBINGHAUS  *************************")
print("\nInsira os assuntos que você estuda e o programa vai agendar suas revisoes.")
choice1 = input ("\n1)Novo arquivo      2)Modificar seu arquivo      3)Sair\n")
if choice1 == "1":
    new_file()
if choice1 == "2":
    mod_file()
if choice1 == "3":
    print("bye bye")

    



