import pandas as pd

def limpar_dados(path_csv):
    df = pd.read_csv(path_csv)

# Remove as colunas 100% vazias
    df = df.dropna(axis=1, how='all')

# Troca os valores 'Rs' na coluna Estado por 'Rio Grande do Sul'
    valores_Rs = df['Estado'] == 'Rs'
    df[valores_Rs]['Estado'] = 'Rio Grande do Sul'

# Elimina linhas com valores 'Misiones' na coluna 'Estado'
    df = df[df['Estado'] != 'Misiones']

# Descartar as horas e modificar o dtype para datetime
    df['Data do Registro'] = pd.to_datetime(df['Data do Registro'], errors='coerce', format='ISO8601').dt.date
    df['Data do Registro'] = pd.to_datetime(df['Data do Registro'], errors='coerce')

# Remove todos as linhas com valores NaN
    df = df.dropna()

# Salva em um novo arquivo csv
    df.to_csv('dados_abelha_limpos.csv', index=False)
    print('Dados salvos com sucesso em: dados_abelha_limpos.csv')

if __name__ == '__main__':
    limpar_dados('./dados_abelha.csv')
