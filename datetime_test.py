from datetime import date, timedelta
import pandas as pd

def calcula_dias(date1,validade):
    #print("Insira a data de início de contagem dessa forma '2020-12-25':")
    date1 = date.fromisoformat(date1)
    flag = 1
    indice = 1
    df = pd.DataFrame({"Dia":[date1]})
#A partir daí, nossa tarefa é calcular a diferença de dias em que ele vai estudar
#e só imprimir as linhas com esses dias no dataframe.
# Definir fórmula para alterar timedelta:
#flag = n° de dias depois do primeiro estudo
#365 é o limite provisório de dias para o fim da contagem
    if flag == 1:
        date2 = date1 + timedelta(days = 1)#24h depois do estudo
        df.at[indice,"Dia"] = date2
        flag = 7
        topic_rows = 1#Quantas linhas são de fato, para que a coluna de assunto bata
        indice = indice + 1
    if flag == 7: # condição é a soma dos dias totais passados desde a primeira sessão
        date3 = date1 + timedelta(days = 7)#1 semana depois do estudo
        df.at[indice,"Dia"] = date3
        flag = 30
        indice = indice + 1
        topic_rows = topic_rows + 1
    if flag == 30:
        date4 = date1 + timedelta(days = 30)#1 mês depois do estudo
        df.at[indice,"Dia"] = date4
        indice = indice + 1
        flag = 60
        topic_rows = topic_rows + 1
    for flag in range(60,int(validade)):
        flag = flag + 30
        if flag % 30 == 0:
            date4 = date4 + timedelta(days =30)#intervalos de dias constantes
            df.at[indice,"Dia"] = date4
            indice = indice + 1
            topic_rows = topic_rows + 1
            
    df1 = df
    return df1,topic_rows
    #df.to_csv('Dias.csv', index = False)
    #return df.insert(loc = 0, column = "Data", value = df["Dia"])
    #yeah
