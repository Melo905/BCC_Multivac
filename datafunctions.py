from datetime import date, timedelta
import pandas as pd
#Funções que operam datas
def calcula_dias(date1,validade):
    date1 = date.fromisoformat(date1)
    flag = 1
    indice = 1
    df = pd.DataFrame({"Dia":[date1]})
#A partir daí, calcular a diferença de dias em que o usuário vai estudar
#e só imprimir as linhas com esses dias no dataframe.
#flag = n° de dias depois do primeiro estudo
    if flag == 1:
        date2 = date1 + timedelta(days = 1)#24h depois do estudo
        df.at[indice,"Dia"] = str(date2)
        flag = 7
        topic_rows = 1#Quantas linhas são de fato, para que a coluna de assunto bata
        indice = indice + 1
    if flag == 7: # condição é a soma dos dias totais passados desde a primeira sessão
        date3 = date1 + timedelta(days = 7)#1 semana depois do estudo
        df.at[indice,"Dia"] = str(date3)
        flag = 30
        indice = indice + 1
        topic_rows = topic_rows + 1
    if flag == 30:
        date4 = date1 + timedelta(days = 30)#1 mês depois do estudo
        df.at[indice,"Dia"] = str(date4)
        indice = indice + 1
        flag = 60
        topic_rows = topic_rows + 1
    for flag in range(60,int(validade)):
        flag = flag + 30
        if flag % 30 == 0:
            date4 = date4 + timedelta(days =30)#intervalos de dias constantes (30 em 30 dias)
            df.at[indice,"Dia"] = str(date4)
            indice = indice + 1
            topic_rows = topic_rows + 1
            
    df1 = df
    return df1,topic_rows


#mudar o número do atributo "Dias.n"
#usando 'coluna'
def calcula_dias_dif(coluna,date1,validade):
    date1 = date.fromisoformat(date1)
    flag = 1
    indice = 1
    data = "Dia " + str(coluna)
    df = pd.DataFrame({data:[date1]})
    if flag == 1:
        date2 = date1 + timedelta(days = 1)
        df.at[indice,data] = date2
        flag = 7
        topic_rows = 1 
        indice = indice + 1
    if flag == 7: 
        date3 = date1 + timedelta(days = 7)
        df.at[indice,data] = date3
        flag = 30
        indice = indice + 1
        topic_rows = topic_rows + 1
    if flag == 30:
        date4 = date1 + timedelta(days = 30)
        df.at[indice,data] = date4
        indice = indice + 1
        flag = 60
        topic_rows = topic_rows + 1
    for flag in range(60,int(validade)):
        flag = flag + 30
        if flag % 30 == 0:
            date4 = date4 + timedelta(days =30)
            df.at[indice,data] = date4
            indice = indice + 1
            topic_rows = topic_rows + 1
            
    df1 = df
    coluna = coluna + 1
    return df1,topic_rows


def the_seeker(arquivo):
    pd.set_option("display.max_rows", None, "display.max_columns", None)# mostrar todas as colunas e linhas do dataframe
    df = pd.read_csv(arquivo)# procurar arquivo no formato .csv
    print(df)# O programa final não exibe antes da pesquisa
    seek_data = input("Procurar por data(ex.: 2020-11-19): ")
    date.fromisoformat(seek_data)
    print(df.query("Dia ==  %s" % seek_data))
    number = 1
    for number in range(1,99):
        string = "Dia " + str(number) 
        condition = string + " == %s"%seek_data
        print(condition)
        print(df.query(condition))
        number = number + 1
