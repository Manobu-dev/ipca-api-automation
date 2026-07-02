<div align="center">

# 📊 Automação de Consulta do IPCA

### Automatizando a consulta do Índice Nacional de Preços ao Consumidor Amplo (IPCA) através da API oficial do IBGE.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![REST API](https://img.shields.io/badge/REST_API-005571?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>

---

# 📖 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de automatizar a consulta do **Índice Nacional de Preços ao Consumidor Amplo (IPCA)** utilizando a **API oficial do IBGE**.

A aplicação realiza a comunicação com a API, interpreta os dados retornados em formato JSON e identifica automaticamente o índice mais recente disponível.

Além de atender a uma necessidade prática, o projeto foi utilizado para aprofundar conhecimentos em consumo de APIs REST, organização de código, tratamento de exceções e desenvolvimento de automações em Python.

---

# ✨ Funcionalidades

- ✅ Consulta automática da API oficial do IBGE
- ✅ Obtenção do índice mais recente do IPCA
- ✅ Processamento de respostas em JSON
- ✅ Tratamento de erros de requisição
- ✅ Estrutura organizada para futuras evoluções

---

# 🛠 Tecnologias

| Tecnologia | Utilização |
|------------|------------|
| Python | Desenvolvimento da aplicação |
| Requests | Consumo da API |
| JSON | Manipulação dos dados |
| Git | Controle de versão |

---

# 🏗 Estrutura do projeto

```text
📦 ipca-api-automation

├── src
│   ├── main.py
│   ├── services
│   ├── utils
│   └── config
│
├── requirements.txt
└── README.md
```

> A estrutura poderá evoluir conforme novas funcionalidades forem adicionadas.

---

# 🚀 Como executar

Clone o repositório

```bash
git clone https://github.com/Manobu-dev/ipca-api-automation.git
```

Entre na pasta

```bash
cd ipca-api-automation
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Execute a aplicação

```bash
python src/main.py
```

---

# 📸 Demonstração

Exemplo de saída:

```text
===========================
Consulta do IPCA
===========================

Período:
2025-12

Valor:
0,45%

Consulta realizada com sucesso.
```

*(Substitua por uma captura real da aplicação quando finalizar a primeira versão.)*

---

# 🛣 Roadmap

## ✔ Concluído

- Consulta à API do IBGE
- Processamento do JSON
- Organização inicial do projeto
- Tratamento básico de erros

## 🚧 Em desenvolvimento

- Histórico das consultas
- Registro em banco de dados
- Execução automática diária
- Logs da aplicação

## 🔮 Futuras melhorias

- Dashboard Web
- Docker
- GitHub Actions
- Testes automatizados
- Envio de notificações
- API própria para consulta

---

# 📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos importantes como:

- Consumo de APIs REST
- Manipulação de dados em JSON
- Organização de aplicações Python
- Tratamento de exceções
- Separação de responsabilidades
- Boas práticas de versionamento com Git

---

# 👨‍💻 Autor

**Bruno Manobu Kayano**

- GitHub: https://github.com/Manobu-dev
- LinkedIn: https://www.linkedin.com/in/brunomanobukayano

---

## ⭐ Se este projeto foi interessante para você, deixe uma estrela no repositório.
