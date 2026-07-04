# src/main.py

import requests

URL = "https://servicodados.ibge.gov.br/api/v3/agregados/1737/periodos/-1/variaveis/63?localidades=N1[all]"

def buscar_ipca():
    # 1. fazer a requisição
    response = requests.get(URL, timeout=10)

    # 2. verificar se a resposta deu certo
    if response.status_code != 200:
        raise Exception(f"Erro na requisição: {response.status_code}")
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise Exception(f"Erro na requisição: {e}") 
    
    # 3. retornar response.json()
    return response.json()


def extrair_ipca_mais_recente(dados):
    serie_dict = dados[0]["resultados"][0]["series"][0]["serie"]
    serie_items = list(serie_dict.items())
    serie_Ano_Mes = serie_items[0][0]
    serie_Ano = serie_Ano_Mes[0:4]
    serie_Mes = serie_Ano_Mes[4:6]
    serie_valor = serie_items[0][1]
    return serie_Ano, serie_Mes, serie_valor

def main():
    dados = buscar_ipca()
    ano, mes, valor = extrair_ipca_mais_recente(dados)
    print(f"IPCA - {ano}/{mes}: {valor}%")

if __name__ == "__main__":
    main()