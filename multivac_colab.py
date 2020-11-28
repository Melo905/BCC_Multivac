from datetime import date, datetime, timedelta
from backports.datetime_fromisoformat import MonkeyPatch
MonkeyPatch.patch_fromisoformat()
import pandas as pd

#Funções que operam datas
def calcula_dias(date1,validade):
   while True:
    try:
      date1 = date.fromisoformat(date1)
      flag = 1
      indice = 1
      df = pd.DataFrame({"Dia":[date1]})
      if flag == 1: #flag = n° de dias depois do primeiro estudo
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
      for flag in range(60,int(validade),30):
          if flag % 30 == 0:
              date4 = date4 + timedelta(days =30)#intervalos de dias constantes (30 em 30 dias)
              df.at[indice,"Dia"] = str(date4)
              indice = indice + 1
              topic_rows = topic_rows + 1 
      df1 = df
      return df1,topic_rows    
      break
    except (ValueError,TypeError):
      print("Data apenas aceita no formato 'YYYY-MM-DD'!\n")
      date1 = input("Insira a data de início de contagem dessa forma '2020-12-30':")#função de data
      validade = int(input("Prazo de validade (em dias):"))#função de data   

def calcula_dias_dif(coluna,date1,validade):#mudar o número do atributo "Dias" com o acréscimo da posição da coluna
  while True:
    try:
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
      break
    except (ValueError,TypeError):
      print("Data apenas aceita no formato 'YYYY-MM-DD'!\n")
      date1 = input("Insira a data de início de contagem dessa forma '2020-12-30':")#função de data
      validade = int(input("Prazo de validade (em dias):"))#função de data

def the_seeker(arquivo):
  continuar = True
  pd.set_option("display.max_rows", None, "display.max_columns", None)# mostrar todas as colunas e linhas do dataframe
  df = pd.read_csv(arquivo)# procurar arquivo no formato .csv
  print(df)
  while continuar == True:
    try:
      seek_data = input("Procurar por data(ex.: 2020-11-19): ")
      #instruções para procurar na tabela
      i = 0
      rows, col = df.shape
      limite = int(col/2)
      for i in range(0,rows):
        n=1
        if n == 1:
          if df.at[i,'Dia'] == seek_data:
            col_id = df.columns.get_loc('Dia')
            print("\n"+df.columns[col_id+1],"-", df.at[i,'Dia'],"-", df.iat[i,col_id+1])          
          n = 2
        for n in range (2,limite+1,1):
          string = "Dia "+str(n)
          if df.at[i,string] == seek_data:
            col_id = df.columns.get_loc(string)
            print(df.columns[col_id+1],"-", df.at[i,string],"-", df.iat[i,col_id+1])
      choice = input("1) Pesquisar mais alguma data no mesmo arquivo.             2) Tela Inicial.\n")
      if choice == "2":
        return 5 #acabar com o while loop do menu principal, se não, ao encerrar essa funão, ele pede para inserir o nome do arquivo novamente
        continuar = False
    except ((ValueError,TypeError,KeyError)):
      print("Parece que essa data não existe na Tabela. Tente outra vez.")

def create_column_base(assunto,time_min,start_day,end_day):
    # Chamar função para criar as datas para a tabela:
    df1, topic_rows = calcula_dias(start_day, end_day)
    #criando coluna do assunto com os tempos em minutos:
    time_min = 0.3 * time_min # 30% do tempo de aprendizagem
    df2 = pd.DataFrame({assunto:["%.2f"%(time_min)+"min"]}) 
    x = 0
    indice = 1 #progressão das linhas preenchidas
    time_min = 0.30 * time_min
    for indice in range(1,topic_rows+1):
        #Fórmula (provisória):
        if indice >= 2:
          time_min = time_min * 0.7
        if time_min >= 5:
            df2.at[indice, assunto] = "%.2f"%(time_min)+" min" #inserção do tempo calculado na coluna e linha respectiva
        if time_min < 5:
            df2.at[indice, assunto] = "5.00 min"
        indice = indice + 1
    frames = [df1,df2]
    df = pd.concat(frames, axis = 1, ignore_index=False)
    df.rename(columns={"0": "Data", "1": assunto})
    return df

def create_and_app(coluna,df_current,assunto,time_min,start_day,end_day):
    # Chamar função para criar as datas para a tabela:
    df1, topic_rows = calcula_dias_dif(coluna, start_day, end_day)
    #criando coluna do assunto com os tempos em minutos:
    df2 = pd.DataFrame({assunto:["%.2f"%(time_min)+"min"]}) 
    x = 0
    indice = 1 #progressão das linhas preenchidas
    time_min = 0.30 * time_min
    for indice in range(1,topic_rows+1):
      #Fórmula (provisória):
      if indice >= 2:
        time_min = time_min * 0.7
      if time_min >= 5:
        df2.at[indice, assunto] = "%.2f"%(time_min)+" min" #inserção do tempo calculado na coluna e linha respectiva
      if time_min < 5:
        df2.at[indice, assunto] = "5.00 min"
      indice = indice + 1
    frames = [df1,df2]
    df = pd.concat(frames, axis = 1, ignore_index=False)
    df.rename(columns={"0": "Data", "1": assunto})
    df = pd.concat([df_current,df], axis = 1, ignore_index=False)
    return df
       
def new_file():#solicita info essenciais para criar uma coluna na tabela
     # flag -> contar os atributos colocados
  flag = 1
  continuar = True
  while continuar == True:
    # Info fornecida pelo usuário
    assunto = input("Assunto %d:" % flag)
    while True:
      try:
        time_min = float(input("Tempo de aprendizagem (em minutos):"))#em minutos]
        break
      except (ValueError,TypeError):
        print("Digite um valor numérico! E use '.' ao invés de ',' para decimais.")
    while True:
      try:
        start_day = input("Insira a data de início de contagem dessa forma '2020-12-30':")#função de data
        end_day = int(input("Prazo de validade (em dias):"))#função de data
        break
      except (ValueError,TypeError):
        print("Data apenas aceita no formato 'YYYY-MM-DD'.\nO prazo da contagem é em números inteiros de dias.")
    # Primeiro assunto cria a tabela (os posteriores são emendados à primeira)
    if flag == 1:
      retorno = create_column_base(assunto,time_min,start_day,end_day)
      coluna = 2
    # Para mais de um assunto
    if flag > 1:
      retorno = create_and_app(coluna,retorno,assunto,time_min,start_day,end_day)#"Create and append"
      coluna = coluna + 1
    while continuar == True: 
      mais = input("Adicionar outro assunto? S ou N\n")
      if mais == "S" or mais == "s":
        flag = flag + 1
        break
      elif mais == "N" or mais == "n":
        arquivo = input("Coloque um nome no seu arquivo(.csv, mas não precisa indicar a extensão).\nNada de colocar sinais como em \"][´~'\", porque pode até passar aqui, mas não será encontrado na pesquisa.\n")
        retorno.to_csv(arquivo, index=False)
        print("Seu arquivo está pronto. Olhe na pasta do programa!")
        print("Para pesquisar nele,vá na opção 2 e insira '%s' e uma data que você gostaria de saber se existem revisões." % arquivo)        
        continuar = False
      else:
        print("Digite 'S' ou 'N' para escolher!")
    
# Tela Inicial
def main():
  continuar = True
  count = 1
  print("*****************************  TABELA EBBINGHAUS  *************************")
  print("\nInsira os assuntos que você estuda e o programa vai agendar suas revisões.")
  while continuar == True:
    choice1 = input ("\n1)Novo arquivo      2)Consultar seu arquivo      3)Sair\n")
    if choice1 == "1":
        new_file()
    elif choice1 == "2":
      while True:
        if count == 5:
          break
        arquivo = input("Insira o nome do arquivo para a consulta: ")
        count = 1
        while True:
          try:
            count = the_seeker(arquivo)
            break
          except (FileNotFoundError,pd.errors.EmptyDataError):
            if count == 4 or count == 5:
              break
            arquivo = input("Arquivo não encontrado. Talvez seja erro de digitação. Tente novamente:\n")
            count = count + 1
            if count == 3:
              print("Arquivo não encontrado. Verifique se você digitou corretamente, se o arquivo está fora da pasta do programa,\nse é um arquivo CSV, ou se a existência dele não é só fruto da sua imaginação.")
              while True:
                choice = input("Deseja cancelar a pesquisa? S/N\n")
                if choice == "S" or choice == "s":
                  count = 5
                  break
                elif choice == "N" or choice == "n":
                  count = 4
                  break
                else:
                  print("'S' para 'Sim' e 'N' para 'Não'!")
    elif choice1 == "3":
      print("Programa terminado.")
      continuar = False
    else:
      print("Entrada incorreta. Digite o número correspondente à sua escolha!")

main()

    



