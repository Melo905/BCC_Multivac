#bcc_Multivac (Bibliotecas e esqueleto)
import pandas as pd
from datetime_test import calcula_dias

# Todas as funções
def create_column_base(assunto,time_min,start_day,end_day):
    # Chamar função para criar as datas para a tabela:
    df1, topic_rows = calcula_dias(start_day, end_day)
    #criando coluna do assunto com os tempos em minutos:
    df2 = pd.DataFrame({assunto:["%.2f"%(time_min)+"min"]}) 
    x = 0
    indice = 1 #progressão das linhas preenchidas
    for indice in range(1,topic_rows+1):
        #Fórmula (provisória):
        time_min = time_min * 0.7
        if time_min > 1:
            df2.at[indice, assunto] = "%.2f"%(time_min)+" min" #inserção do tempo calculado na coluna e linha respectiva
        if time_min <=1:
            df2.at[indice, assunto] = "1.00 min"
        indice = indice + 1
    frames = [df1,df2]
    df = pd.concat(frames, axis = 1, ignore_index=False)
    df.rename(columns={"0": "Data", "1": assunto})
    return df


def create_and_app(df_current,assunto,time_min,start_day,end_day):
    # Chamar função para criar as datas para a tabela:
    df1, topic_rows = calcula_dias(start_day, end_day)
    #criando coluna do assunto com os tempos em minutos:
    df2 = pd.DataFrame({assunto:["%.2f"%(time_min)+"min"]}) 
    x = 0
    indice = 1 #progressão das linhas preenchidas
    for indice in range(1,topic_rows+1):
        #Fórmula (provisória):
        time_min = time_min * 0.7
        df2.at[indice, assunto] = "%.2f"%(time_min)+"min" #inserção do tempo calculado na coluna e linha respectiva
        indice = indice + 1
    frames = [df1,df2]
    df = pd.concat(frames, axis = 1, ignore_index=False)
    df.rename(columns={"0": "Data", "1": assunto})
    df = pd.concat([df_current,df], axis = 1, ignore_index=False)
    return df
    

def new_file():#solicita info essenciais para criar uma coluna na tabela
     # flag -> contar os atributos colocados(limite de 10)
    for flag in range(1,10):
        # Info fornecida pelo usuário
        assunto = input("Assunto %d:" % flag)
        time_min = float(input("Tempo de aprendizagem(min):"))#em minutos
        start_day = input("Insira a data de início de contagem dessa forma '2020-12-25':")#função de data
        end_day = input("Prazo de validade(em dias):")#função de data

        # Primeiro assunto cria a tabela (os posteriores são emendados à primeira)
        if flag == 1:
            retorno = create_column_base(assunto,time_min,start_day,end_day)
            
        # Para mais de um assunto
        if flag > 1 and flag <=10:
            retorno = create_and_app(retorno,assunto,time_min,start_day,end_day)#"Create and append"

        if flag == 10:
            retorno.to_csv('Multivac.csv', index=False)
        #Pergunta se vai continuar a iteração
        mais = input("Adicionar outro assunto? S ou N\n")
        if mais == "S" or mais == "s":
            flag = flag + 1
        if mais == "N" or mais == "n":
            flag = 11
            retorno.to_csv('Multivac.csv', index=False)
            print("Seu arquivo está pronto. Olhe na pasta do programa!")

    # Ao final das iterações, salvar a tabela        
    print(df)
    df.to_csv('Multivac.csv', index=False)
        #else:
            #print("Nao entendi. \"S\" para \"Sim\" ou \"N\" para \"Não\".")#Colocar condição para retornar à pergunta
    
    
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
    print("Programa terminado.")

    



