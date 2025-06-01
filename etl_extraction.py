import requests
import pandas as pd
import time

def extract_bee_data(limit=300):
    taxon_keys = [1334757, 1340042, 7541754, 1342048, 1340278, 1340556]     #["Apis", "Melipona", "Trigona", "Xylocopa", "Bombus", "Euglossa"]   
    url = 'https://api.gbif.org/v1/occurrence/search'
    offset = 0
    results_total = []

    # Para pegar dados com paginação com offset
    while offset < 3000:
    # Estabelecendo os parâmetros em formato de lista de tuplas para se adequar aos múltiplos taxonKey
        params = [("taxonKey", str(key)) for key in taxon_keys]
        params.append(("country", "BR"))
        params.append(("limit", str(limit)))
        params.append(("offset", str(offset)))

    #Requisição:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            dados = response.json()
            results = dados.get('results', [])
            results_total.extend(results)

            print(f"Página coletada: {offset} → {offset + len(results)}")
            
            if len(results) < limit:
                break   # final dos dados disponíveis
            
            offset += limit
            time.sleep(1)   # para evitar sobrecarga
        else:
            print(f"Erro: {response.status_code}")
            break
        
    return results_total

def transform_data(results_total):
    registros = []
    for item in results_total:
        registros.append({
            "Nome Científico": item.get('scientificName'),
            "Gênero": item.get('genus'),
            "Família": item.get('family'),
            "Data do Registro": item.get('eventDate'),
            "Estado": item.get('stateProvince'),
            "País": item.get('country'),
            "Id da Ocorrencia": item.get('occurrenceId')
            })
    return registros

if __name__ == '__main__':
    dados_brutos = extract_bee_data()
    dados_tratados = transform_data(dados_brutos)
    df = pd.DataFrame(dados_tratados)
    df.to_csv("dados_abelha_2.csv", index=False)

  
  

   