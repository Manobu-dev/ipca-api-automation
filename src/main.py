# src/main.py

import json
from pathlib import Path

import requests

URL = "https://servicodados.ibge.gov.br/api/v3/agregados/1737/periodos/-1/variaveis/63?localidades=N1[all]"
ARQUIVO_ULTIMO_IPCA = Path(__file__).resolve().parent.parent / "data" / "last_ipca.json"

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


def carregar_ultimo_ipca():
    if not ARQUIVO_ULTIMO_IPCA.exists():
        return None

    try:
        with ARQUIVO_ULTIMO_IPCA.open(encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        return None


def salvar_ultimo_ipca(periodo, valor):
    dados = {
        "periodo": periodo,
        "valor": valor,
    }

    ARQUIVO_ULTIMO_IPCA.parent.mkdir(parents=True, exist_ok=True)
    with ARQUIVO_ULTIMO_IPCA.open("w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

    return dados


def extrair_ipca_mais_recente(dados):
    serie_dict = dados[0]["resultados"][0]["series"][0]["serie"]
    serie_items = list(serie_dict.items())
    serie_Ano_Mes = serie_items[0][0]
    serie_Ano = serie_Ano_Mes[0:4]
    serie_Mes = serie_Ano_Mes[4:6]
    serie_valor = serie_items[0][1]
    return serie_Ano, serie_Mes, serie_valor, serie_Ano_Mes

def main():
    dados = buscar_ipca()
    ano, mes, valor, periodo = extrair_ipca_mais_recente(dados)
    salvar_ultimo_ipca(periodo, valor)
    print(f"IPCA - {ano}/{mes}: {valor}%")

if __name__ == "__main__":
    main()
