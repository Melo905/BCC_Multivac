#createcolumn()- função para criar colunas e linhas
#possibilitar uso de caracteres especiais
#prever erros do usuário
#intuitividade da operação
import pandas as pd
import calendar
#df = pd.DataFrame({"Data\\Assunto": [day1], assunto: [str(time_min)+"min"]})

x = 0
indice = 1 #progressão das linhas preenchidas
for x in range(0,100):
    if x == 0: #criação da tabela e da primeira(dia) e segunda(primeiro assunto) colunas
        assunto = "Efeito Fotoelétrico"#input()
        time_min = int("30")#float(input())
        day = int("2") #int(input())
        y = day
        validade = int("5")#int(input()) #dia em que deve acabar ou número de semanas/meses
        df = pd.DataFrame({"Data\\Assunto": [str(day)], assunto: [str(time_min)+"min"]})
    if x > 0:# preenchimento da nova coluna
        for y in range(day,validade): #day seria '3'
            #Fórmula (provisória):
            time_min = time_min * 0,7
            df.at[indice, assunto] = str(time_min) #inserção do tempo calculado na coluna e linha respectiva
            df.at[indice,"Data\\Assunto"] = str(day)
            indice = indice + 1
    day = int(day) + 1
    x = x + 1 #fim da iteração

print(df)


    
#acrescenta linha a uma coluna existente e coloca novo valor
#df.at[1, assunto] = time_min

# acrescenta colunas
#df.insert(loc = 1, column = "bcc", value = str(time_min)+"min")
#print(df)


#Passando para arquivo csv:
df.to_csv('Multivac.csv', index=False)  
