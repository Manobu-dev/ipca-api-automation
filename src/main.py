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

def buscar_ipca_por_periodo(serie):
    dados = buscar_ipca()
    for item in dados:
        if item['serie'] == serie:
            return item

def main():
    dados = buscar_ipca()
    serie = dados[0]["resultados"][0]["series"][0]["serie"]
    serie = list(serie.items())
    serieAnoMes = serie[0][0]
    serierAno = serieAnoMes[0:4]
    serieMes = serieAnoMes[4:6]
    serievalor = serie[0][1]
    print(f"IPCA - {serierAno}/{serieMes}: {serievalor}%")

if __name__ == "__main__":
    main()