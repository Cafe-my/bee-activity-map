import pandas as pd

df = pd.read_csv('./dados_abelha.csv')



# Corrigir a escrita da data de registro e modificar o dtype para datetime
# Eliminar linha com elementos nulos (2 no Estado)
#Eliminar 1 registro com Estado == Misiones
# trocar os valores 'Rs' na coluna Estado por 'Rio Grande do Sul'
# apagar coluna vazia ID de ocorrencia
#UTILIZAR O ARQUIVO 2 DDE DADOS ABELHA
print(df.info())