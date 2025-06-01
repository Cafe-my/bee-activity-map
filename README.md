# Mapa da Atividade de Abelhas no Brasil 🐝

Este projeto realiza um pipeline ETL para mapear ocorrências de abelhas no Brasil, usando a API pública do GBIF.

## Etapas

- **Extract**: Busca dados da API GBIF (espécie Apis) com filtros por país (Brasil).
- **Transform**: Limpeza com pandas — mantém apenas dados relevantes e padronizados.
- **Load**: Insere os dados tratados no PostgreSQL, permitindo visualizações futuras.

## Requisitos

- Python 3.10+
- Bibliotecas: requests, pandas, SQLAlchemy/psycopg2, dotenv
- PostgreSQL local ou em nuvem

## Futuras Extensões

- Painel em Streamlit

