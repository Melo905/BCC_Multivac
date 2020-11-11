                                                            Programa BCC_Multivac 
                                                                           
Utiliza a teoria de Hermann Ebbinghaus para gerar um cronograma de estudo (não personalizado, apenas seguindo o modelo ideal por conta das nossas limitações) e organizá-lo num arquivo .csv para o aluno salvar no libreoffice.

O resultado vai depender do tempo da primeira sessão de estudo. A equação de Ebbinghaus prevê grosseiramente a retenção do assunto pelo tempo desde o primeiro contato. Nosso objetivo não é monitorar "porcentagens remanescentes do que foi aprendido". 

Vamos usar uma progressão geométrica para redução do tempo de revisões, e a função de calenário datetime() do python para organizar em datas de estudo. Não vai ser personalizado, no sentido de que não vai se adaptar às necessidades específicas dos estudantes (por conta das limitações de tempo, recursos e domínio do python), vai apenas seguir as condições ideais de estudos como solução para o esquecimento previsto pela equação de Ebbinghaus.

O usuário então vai colocar o nome dos tópicos que ele pretende estudar (podendo ser mais de um ao mesmo tempo), o tempo da sessão completa de estudo de cada assunto, a dificuldade de cada tema* (mais subjetivo, apenas servirá, inicialmente, como marcador de prioridade) e o período em semanas ou meses em que ele pretende manter o ritmo de revisões (para uma prova final ou alguma apresentação, por exemplo). A saída, como já falado acima, será uma tabela do LibreOffice com os tópicos como atributos (colunas) e os dias em cada linha com o respectivo tempo de sessão, em minutos. 

Mesmo com um escopo teórico mais rígido, o programa se propõe a auxiliar o estudante nas revisões, incentivando o desenvolvimento do hábito de revisar, para maior eficiência de aprendizado, pois a aplicação constante ameniza os efeitos do esquecimento com o tempo e, a longo prazo, evita que o estudante tenha de gastar mais horas para reaprender tudo. O método em si não é universal, mas pode servir para apresentar um nova perspectiva de otimização da aprendizagem. É só pensar em outros métodos de estudo, como o de Pomodoro, que, apesar de estar mais relacionado à divisão temporal das tarefas em pequenos espaços para o rendimento máximo, assim como o de Ebbinghaus, não se adapta a todos os perfis de usuário, mas carrega uma essência estratégica que pode ser adaptada quantitativamente ao indivíduo.



* 1- fácil; 2- certa familiaridade; 3- difícil.
------------------------------------------------------------------------------------------------------

# BCC_Multivac (Bibliotecas e esqueleto)
import pynput 
import pandas as pd
import math as mt


A) Receber os dados do usuário:
     - Duas opções:
        1) novo arquivo  2) modificar arquivo pré-existente
     - assunto;
     - tempo;
     - data;
     - dificuldade
         1) fácil, 2) certa familiaridade e 3) difícil
     - validade.

      
    
B) Resultados:
   - arquivo.csv (Novo ou adições ao arquivo armazenado na variável)

