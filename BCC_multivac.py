#BCC_Multivac.py
import pandas as pd
from datafunctions import calcula_dias, calcula_dias_dif, the_seeker

def create_column_base(assunto,time_min,start_day,end_day):
    # Chamar função para criar as datas para a tabela:
    df1, topic_rows = calcula_dias(start_day, end_day)
    #criando coluna do assunto com os tempos em minutos:
    df2 = pd.DataFrame({assunto:["%.2f"%(time_min)+"min"]}) 
    x = 0
    indice = 1 #progressão das linhas preenchidas
    time_min = 0.3 * time_min
    for indice in range(1,topic_rows+1):
        #Fórmula (provisória):
        time_min = time_min * 0.7
        if time_min > 1:
            df2.at[indice, assunto] = "%.2f"%(time_min)+" min" #inserção do tempo calculado na coluna e linha respectiva
        if time_min <=1:
            df2.at[indice, assunto] = "5.00 min"
        indice = indice + 1
    frames = [df1,df2]
    df = pd.concat(frames, axis = 1, ignore_index=False)
    df.rename(columns={"0": "Data", "1": assunto})
    return df

def create_and_app(coluna,df_current,assunto,time_min,start_day,end_day):
    # Chamar função para criar as datas para a tabela:
    df1, topic_rows = calcula_dias_dif(coluna,start_day, end_day)
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
     # flag -> contar os atributos colocados(limite de 100)
    for flag in range(1,100):
        # Info fornecida pelo usuário
        assunto = input("Assunto %d:" % flag)
        time_min = float(input("Tempo de aprendizagem(min):"))#em minutos
        start_day = input("Insira a data de início de contagem dessa forma '2020-12-25':")#função de data
        end_day = input("Prazo de validade(em dias):")#função de data

        # Primeiro assunto cria a tabela (os posteriores são emendados à primeira)
        if flag == 1:
            retorno = create_column_base(assunto,time_min,start_day,end_day)
            coluna = 1
        # Para mais de um assunto
        if flag > 1 and flag <=10:
            retorno = create_and_app(coluna,retorno,assunto,time_min,start_day,end_day)#"Create and append"
            coluna = coluna + 1# numero n ("Dia.n")
        if flag == 100:
            arquivo = input("Coloque um nome no seu arquivo(.csv):\n")
            retorno.to_csv(arquivo, index=False)
            print("Seu arquivo está pronto. Olhe na pasta do programa!")
        #Pergunta se vai continuar a iteração
        mais = input("Adicionar outro assunto? S ou N\n")
        if mais == "S" or mais == "s":
            flag = flag + 1
        if mais == "N" or mais == "n":
            flag = 11
            arquivo = input("Coloque um nome no seu arquivo(.csv):\n")
            retorno.to_csv(arquivo, index=False)
            print("Seu arquivo está pronto. Olhe na pasta do programa!")
            main()
    
def search_file():
    arquivo = input("Insira o nome do arquivo para a consulta: ")
    the_seeker(arquivo)

# Tela Inicial
def main():
    print("*****************************  TABELA EBBINGHAUS  *************************")
    print("\nInsira os assuntos que você estuda e o programa vai agendar suas revisoes.")
    choice1 = input ("\n1)Novo arquivo      2)Consultar seu arquivo      3)Sair\n")
    if choice1 == "1":
        new_file()
    if choice1 == "2":
        search_file()
    if choice1 == "3":
        print("Programa terminado.")

main()

    



